import boto3

region_name = 'us-east-2'
aws_access_key_id = 'AKIAJFB73E5C5NH65ZFQ'
aws_secret_access_key = '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'

client = boto3.client('ec2')
myec2 = client.describe_instances()
for listec2 in myec2['Reservations']:
	for listinsid in listec2['Instances']:
		print(listinsid['InstanceId'])
