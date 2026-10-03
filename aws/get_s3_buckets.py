import boto3

try:
    s3_client = boto3.client("s3")
    res = s3_client.list_buckets()
    print(f"{'Bucket name':<40} | {'Creation date'}")
    print("-" * 70)

    for bucket in res['Buckets']:
        name = bucket['Name']
        creation_date = bucket['CreationDate']
        print(f"{name:<40} | {creation_date}")

except Exception as e:
    print(f"No buckets were found. Error: {e}")