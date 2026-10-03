from datetime import datetime, timedelta, timezone
import boto3

# 1. Initialize our AWS clients
REGION = "us-east-1"
ec2_client = boto3.client("ec2", region_name=REGION)
cloudwatch = boto3.client("cloudwatch", region_name=REGION)

# 2. Time boundaries for tracking CloudWatch usage (last 1 hour)
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=1)

print("Scanning for running EC2 instances and fetching profiles...\n")

# 3. Pull only instances whose lifecycle state is actively 'running'
instances_response = ec2_client.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)

# Parse the structural layout into a clean flat list
running_instances = [
    inst for res in instances_response.get("Reservations", []) for inst in res.get("Instances", [])
]

if not running_instances:
    print("No active running EC2 instances found.")
    exit()

# 4. Gather the full hardware catalog profiles (vCPU and Memory specs) for these types
unique_types = list(set(inst["InstanceType"] for inst in running_instances))
specs_response = ec2_client.describe_instance_types(InstanceTypes=unique_types)
type_catalog = {
    spec["InstanceType"]: {
        "vcpus": spec["VCpuInfo"]["DefaultVCpus"],
        "ram_gb": spec["MemoryInfo"]["SizeInMiB"] / 1024  # Convert MiB capacity to GiB
    }
    for spec in specs_response.get("InstanceTypes", [])
}

# 5. Process and map the aggregated details for each target server
for inst in running_instances:
    inst_id = inst["InstanceId"]
    inst_type = inst["InstanceType"]
    
    # Grab capacity profile from our local catalog dictionary
    hardware = type_catalog.get(inst_type, {"vcpus": "N/A", "ram_gb": "N/A"})
    
    # Fetch real-time CloudWatch metrics for this specific ID loop
    metric = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[{"Name": "InstanceId", "Value": inst_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"]
    )
    
    datapoints = metric.get("Datapoints", [])
    if datapoints:
        avg_cpu = sum(d["Average"] for d in datapoints) / len(datapoints)
        cpu_str = f"{avg_cpu:.2f}%"
    else:
        cpu_str = "No recent data"

    # Display the final scannable breakdown
    print(f"Instance ID   : {inst_id}")
    print(f"Type Profile  : {inst_type}")
    print(f"Hardware Specs: {hardware['vcpus']} vCPUs | {hardware['ram_gb']:.1f} GiB RAM")
    print(f"Avg CPU (1hr) : {cpu_str}")
    print(f"Real-time RAM : Requires internal CloudWatch Agent configuration")
    print("-" * 60)
