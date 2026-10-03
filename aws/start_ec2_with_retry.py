import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")

def start_instance(instance_id):
    response = None
    for attempt in range(3):
        try:
            response = ec2.start_instances(InstanceIds=[instance_id])
            print("Instance started")
            break
        
        except ClientError as error:
            print(f"Attempt {attempt + 1} failed:", error)
            if attempt == 2:
                break
            
    return response

start_instance("i-00a3a9be0249a5tg4")