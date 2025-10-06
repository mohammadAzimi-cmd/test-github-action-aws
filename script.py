import boto3

# Create an EC2 resource object (replace 'your-region' with your AWS region)
ec2 = boto3.resource('ec2', region_name='us-west-1')

# Iterate through all instances
for instance in ec2.instances.all():
    print(f"Instance ID: {instance.id}")
    print(f"Instance Type: {instance.instance_type}")
    print(f"State: {instance.state['Name']}")
    print(f"Public IP: {instance.public_ip_address}")
    # You can access other attributes like tags, launch time, etc.
    for tag in instance.tags or []:  # Handle cases where instances might not have tags
        if tag['Key'] == 'Name':
            print(f"Name: {tag['Value']}")
    print("-" * 20)

# To filter instances (e.g., by state)
for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
    print(f"Running Instance ID: {instance.id}")
    print(f"Running Instance Type: {instance.instance_type}")
    print("-" * 20)