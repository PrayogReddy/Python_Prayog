from datetime import datetime, timedelta, timezone
import boto3

Region = "us-east-1"
ec2_client = boto3.client("ec2", region_name=Region)
cloudwatch = boto3.client("cloudwatch", region_name=Region)
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=1)

response = ec2_client.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}])

running_instances = []
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        running_instances.append(instance)

if not running_instances:
    print("No EC2 instances found running.")
    exit()

unique_types = list(set(inst["InstanceType"] for inst in running_instances))
specs_response = ec2_client.describe_instance_types(InstanceTypes=unique_types)
type_catalog = {
    spec["InstanceType"]: {
        "vcpus": spec["VCpuInfo"]["DefaultVCpus"],
        "ram_gb": spec["MemoryInfo"]["SizeInMiB"] / 1024
    }
    for spec in specs_response.get("InstanceTypes", [])
}

for inst in running_instances:
    inst_id = inst["InstanceId"]
    inst_type = inst["InstanceType"]    
    
    hardware = type_catalog.get(inst_type, {"vcpus": "N/A", "ram_gb": "N/A"})
    
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

    print(f"Instance ID   : {inst_id}")
    print(f"Type Profile  : {inst_type}")
    print(f"Hardware Specs: {hardware['vcpus']} vCPUs | {hardware['ram_gb']:.1f} GiB RAM")
    print(f"Avg CPU (1hr) : {cpu_str}")
    print("-" * 60)
