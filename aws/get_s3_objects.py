import boto3

s3 = boto3.client("s3")
bucket_name = "prayog-demo-bucket-vscode"
paginator = s3.get_paginator("list_objects_v2")

for page in paginator.paginate(Bucket=bucket_name):
    for obj in page.get("Contents", []):

        print(
            obj["Key"], "|" ,
            obj["Size"], "|" ,
            obj["LastModified"]
        )