import boto3

ec2 = boto3.client("ec2")
counts = {}
paginator = ec2.get_paginator("describe_instances")

for page in paginator.paginate():
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            state = instance["State"]["Name"]
            counts[state] = counts.get(state, 0) + 1

print(counts)
