import boto3

s3 = boto3.client("s3")

s3.download_file(
    "prayog-demo-bucket-vscode",
    "upload_aws_costs.csv",
    "C:\\Users\\prayo\\Python\\Python_Prayog\\aws_costs.csv"
)
print("Download completed successfully.")