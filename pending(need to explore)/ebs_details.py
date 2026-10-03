import boto3
import json

ec2 = boto3.client("ec2")
cloudtrail = boto3.client("cloudtrail")

# 1. Use the specific Volume ID you want to investigate
volume_id = "vol-0a56100a65c44f28c"

print("Starting CloudTrail event lookup...")

response1 = cloudtrail.lookup_events(
    LookupAttributes=[
        {
            "AttributeKey": "ResourceName",
            "AttributeValue": volume_id
        }
    ],
    # Crucial DevOps addition: Ignore read-only checks to find the creation event
    # ReadOnly=False, 
    MaxResults=50
)

print("Events found count:", len(response1["Events"]))

for event in response1["Events"]:

    # 2. Add an explicit check to look for the volume creation event name
    if event["EventName"] == "CreateVolume":

        print(
            "Event:",
            event["EventName"]
        )

        print(
            "Time:",
            event["EventTime"]
        )

        print(
            "Username:",
            event["Username"]
        )

        details = json.loads(
            event["CloudTrailEvent"]
        )

        identity = details.get(
            "userIdentity",
            {}
        )

        print(
            "Identity ARN:",
            identity.get("arn")
        )

print("Script execution finished.")
