from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

uri = 'mongodb+srv://'+usuario+':'+password+'@'+cluster+'.teycm.mongodb.net/?retryWrites=true&w=majority&appName='+cluster

cliente = MongoClient(uri,maxPoolSize=50)

try:
    cliente.admin.command('ping')
    print("NOS CONECTAMOS CORRECTAMENTE")
except Exception as e:
    print(e)