import boto3
from datetime import datetime, timedelta, timezone

logs = boto3.client("logs", region_name="us-east-1")

log_group = "/ec2/logs"
log_stream = "i-0160ecfd7d13807d0"

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=6)

response = logs.filter_log_events(
    logGroupName=log_group,
    logStreamNames=[log_stream],
    startTime=int(start_time.timestamp() * 1000),
    endTime=int(end_time.timestamp() * 1000),
    filterPattern='"ERROR:"'
    # filterPattern='%ERROR:|INFO:|WARNING: %'
)

print("ERROR logs:", len(response["events"]))

for event in response["events"]:
    print(event["message"])