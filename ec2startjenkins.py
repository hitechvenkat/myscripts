import boto3
import sys

region='us-east-2'
access_key='AKIAJFB73E5C5NH65ZFQ'
secret_key='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'
instances='i-009fd4e100940e97f'

ec2 = boto3.client('ec2',region_name=region,
	aws_access_key_id=access_key,
	aws_secret_access_key=secret_key)

def startec2():
    ec2.start_instances(InstanceIds=instances)

startec2()
