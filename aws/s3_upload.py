import boto3

s3 = boto3.client("s3")

s3.upload_file(
    "C:\\Users\\prayo\\Python\\Python_Prayog\\aws_costs.csv",
    "prayog-demo-bucket-vscode",
    "upload_aws_costs.csv"
)
print("Upload completed successfully.")