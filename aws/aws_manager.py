import boto3
from botocore.exceptions import ClientError

class AWSAccountManager:
    """
    A professional class to handle common AWS administrative operations
    across S3, EC2, and IAM services.
    """
    def __init__(self, region_name="us-east-1"):
        """
        The constructor. Every time you create an instance of this class,
        it automatically authenticates and builds connections for 'self'.
        """
        print(f"Initializing AWS Connections for region: {region_name}...")
        
        # We attach the AWS clients to 'self' so every other method can reuse them
        self.region = region_name
        self.s3 = boto3.resource('s3')
        self.ec2 = boto3.resource('ec2', region_name=self.region)
        self.iam = boto3.resource('iam')

    def list_s3_buckets(self):
        """Uses self's S3 connection to find buckets"""
        print("\n--- S3 Buckets ---")
        for bucket in self.s3.buckets.all():
            print(f"Bucket: {bucket.name}")

    def list_ec2_instances(self):
        """Uses self's EC2 connection to find instances in this region"""
        print(f"\n--- EC2 Instances ({self.region}) ---")
        for instance in self.ec2.instances.all():
            print(f"Instance ID: {instance.id} | State: {instance.state['Name']}")

    def list_iam_users(self):
        """Uses self's IAM connection to find users"""
        print("\n--- IAM Users ---")
        for user in self.iam.users.all():
            print(f"User: {user.name}")


# --- HOW TO USE THIS CLASS ---
if __name__ == "__main__":
    try:
        print("testing")
        # 1. Create the manager object (This fires __init__ automatically)
        aws_admin = AWSAccountManager(region_name="us-east-1")
        
        # 2. Call the individual actions using our new object
        aws_admin.list_s3_buckets()
        aws_admin.list_iam_users()
        aws_admin.list_ec2_instances()

    except ClientError as e:
        print(f"AWS Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
