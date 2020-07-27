import boto3
import sys

region='us-east-1'
access_key='AKIAICK4YLZXHUDZF2NQ'
secret_key='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'
instances='i-00b21d3fd6196a070'

ec2 = boto3.client('ec2',region_name=region,
	aws_access_key_id=access_key,
	aws_secret_access_key=secret_key)

def startec2():
    ec2.start_instances(InstanceIds=instances)

startec2()
