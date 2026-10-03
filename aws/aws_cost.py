import boto3

ce = boto3.client("ce")

response = ce.get_cost_and_usage(
    TimePeriod={"Start": "2026-09-01","End": "2026-10-01"},
    Granularity="MONTHLY",
    Metrics=["UnblendedCost"],
    GroupBy=[{"Type": "DIMENSION","Key": "SERVICE"}]
)

for result in response["ResultsByTime"]:
    for group in result["Groups"]:
        service = group["Keys"][0]
        amount = group["Metrics"]["UnblendedCost"]["Amount"]
        unit = group["Metrics"]["UnblendedCost"]["Unit"]

        print(service,amount,unit)