import boto3
from dotenv import load_dotenv
import os

load_dotenv()

session = boto3.session.Session( 
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    aws_session_token=os.getenv("SESSION_TOKEN"),
    region_name=os.getenv("REGION"))


client = session.client('dynamodb')

print(client.list_tables())