import aws_manager

res = aws_manager.AWSAccountManager("us-east-1")
res.list_s3_buckets()