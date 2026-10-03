import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")
paginator = ec2.get_paginator("describe_instances")
instances_found = False

for page in paginator.paginate():
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            instances_found = True
            
            print("Instance ID :", instance["InstanceId"])
            print("Type        :", instance["InstanceType"])
            print("State       :", instance["State"]["Name"])
            print("Private IP  :", instance.get("PrivateIpAddress"))
            print("Public IP   :", instance.get("PublicIpAddress"))
            print("Launch Time :", instance["LaunchTime"])
            print("-" * 50)

if not instances_found:
    print(f"No EC2 instances found in region {ec2.meta.region_name}")
