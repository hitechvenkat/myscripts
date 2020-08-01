import boto3

listec2 = boto3.client('ec2',region_name='us-east-2',
	aws_access_key_id='AKIAJFB73E5C5NH65ZFQ',
	aws_secret_access_key='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')

output = listec2.describe_instances()
for printid in output['Reservations']:
    for printid2 in printid['Instances']:
        for printid3 in printid2['Tags']:
            print((printid2['InstanceId']),
                  (printid2['InstanceType']),
                  (printid2['LaunchTime']),
                  (printid2['State']['Name']),
                  (printid3['Value']))
