import boto3
from datetime import datetime, timedelta, timezone

logs = boto3.client(
    "logs",
    region_name="us-east-1"
)

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=12)

paginator = logs.get_paginator(
    "describe_log_groups"
)

for page in paginator.paginate():
    for group in page["logGroups"]:
        log_group = group["logGroupName"]
        response = logs.filter_log_events(
            logGroupName=log_group,
            startTime=int(
                start_time.timestamp() * 1000
            ),
            endTime=int(
                end_time.timestamp() * 1000
            ),
            filterPattern="ERROR"
        )

        for event in response["events"]:
            print(
                f"[{log_group}] "
                f"{event['message'].strip()}"
            )
print("No error logs found.")