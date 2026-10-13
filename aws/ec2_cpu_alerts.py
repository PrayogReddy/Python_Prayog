import json
import boto3
import urllib.request

secrets_client = boto3.client("secretsmanager")
secret_name = "slack_webhook_ec2-alert"

def get_webhook_url():
    response = secrets_client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])
    return secret["webhook_url"]

def lambda_handler(event, context):
    webhook_url = get_webhook_url()

    for record in event.get("Records", []):
        msg = json.loads(record["Sns"]["Message"])
        
        payload = {
            "text": (
                f"EC2 High CPU Alert\n"
                f"*Alarm:* {msg.get('AlarmName')}\n"
                f"*State:* {msg.get('NewStateValue')}\n"
                f"*Reason:* {msg.get('NewStateReason')}"
            )
        }

        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        urllib.request.urlopen(req)

    return {"statusCode": 200}