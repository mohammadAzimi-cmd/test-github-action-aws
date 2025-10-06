import boto3

cf_client = boto3.client('cloudformation', region_name='us-east-1')

stack_name = 'mamad-test'

with open('cloudFormationVPC.yaml', 'r') as f:
    template_body = f.read()

try:
    response = cf_client.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Capabilities=['CAPABILITY_NAMED_IAM']  # if needed
    )
    print(f"🚀 CloudFormation stack '{stack_name}' creation initiated.")
    print(f"Stack ID: {response['StackId']}")
except Exception as e:
    print(f"❌ Error creating CloudFormation stack: {e}")
