import boto3
from dotenv import load_dotenv
import os
load_dotenv()

def conectarseDynamoDBCliente():
    session = boto3.session.Session( 
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    aws_session_token=os.getenv("SESSION_TOKEN"),
    region_name=os.getenv("REGION"))

    dynamodb = session.client('dynamodb')
    
    return dynamodb


def conectarseDynamoDBResource():
    session = boto3.session.Session( 
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    aws_session_token=os.getenv("SESSION_TOKEN"),
    region_name=os.getenv("REGION"))

    dynamodb = session.resource('dynamodb')
    
    return dynamodb