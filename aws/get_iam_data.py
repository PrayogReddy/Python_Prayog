import boto3

res = boto3.resource('iam')

print("IAM Users:")

for user in res.users.all():
    # print(dir(user))
    print(f"User: {user.name} | ARN: {user.arn}")