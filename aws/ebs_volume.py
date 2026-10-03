import boto3

ec2 = boto3.client("ec2")
response = ec2.describe_volumes()

for volume in response["Volumes"]:
    # print(dir(volume))
    # print(volume.keys())
    print("Volume ID:", volume["VolumeId"])
    print("Size:", volume["Size"], "GiB")
    print("Type:", volume["VolumeType"])
    print("State:", volume["State"])
    print("AZ:", volume["AvailabilityZone"])

    for attachment in volume.get("Attachments", []):
        print("Attached Instance:", attachment["InstanceId"])
        print("-" * 50)