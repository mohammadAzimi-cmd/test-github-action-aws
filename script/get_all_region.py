from http.client import responses

import boto3


ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_regions(AllRegions=True)


regions = [region['RegionName'] for region in response['Regions']]
print(regions)



