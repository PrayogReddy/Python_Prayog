import boto3
from datetime import datetime, UTC

ec2 = boto3.client("ec2")
response = ec2.describe_instances()
current_time = datetime.now(UTC)
instance_running = False

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["State"]["Name"] == "running":
            instance_running = True
            launch_time = instance["LaunchTime"]
            uptime = current_time - launch_time
            print(f"Instance ID: {instance['InstanceId']} | Uptime: {uptime}")

if not instance_running:
    print("No instances are running currently.")