import boto3

client = boto3.client('dynamodb')
print(client.list_tables())