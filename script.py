import boto3

cloudformation = boto3.resource('cloudformation', region_name='us-east-1')
stack = cloudformation.Stack('mamad-test')

with open('cloudFormationVPC.yaml', 'r') as f:
    template_body = f.read()


try:
    response = cloudformation.create_stack(
        StackName=stack_name,
        TemplateBody=template_body
        # Capabilities=['CAPABILITY_IAM'] # Includ
    )
    print(f"CloudFormation stack '{stack_name}' creation initiated.")
    print(f"Stack ID: {response['StackId']}")
except Exception as e:
    print(f"Error creating CloudFormation stack: {e}")