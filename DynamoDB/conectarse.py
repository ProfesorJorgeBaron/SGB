import boto3
from dotenv import load_dotenv
import os

load_dotenv()

client = boto3.client(
    'dynamodb',
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    aws_session_token=os.getenv("SESSION_TOKEN"),
    region_name=os.getenv("REGION")
)

print(client.list_tables())