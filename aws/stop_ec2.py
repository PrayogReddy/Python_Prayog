import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

instance_id = "i-0160ecfd7d13807d0"

response = ec2.stop_instances(
    InstanceIds=[instance_id]
)

print(response)