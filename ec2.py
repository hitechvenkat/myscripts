import boto3

region_name = 'us-east-2'
aws_access_key_id = 'AKIAJMCAY57CKWCUWZJQ'
aws_secret_access_key = '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'

client = boto3.client('ec2')
myec2 = client.describe_instances()
for listec2 in myec2['Reservations']:
	for listinsid in listec2['Instances']:
		print(listinsid['InstanceId'])
		
stopec2 = client.stop_instances(
    InstanceIds=[listinsid['InstanceId']])