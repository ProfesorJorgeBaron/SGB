from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

uri =  'mongodb+srv://'+usuario+':'+password+'@'+cluster+'.teycm.mongodb.net/?retryWrites=true&w=majority&appName='+cluster

cliente = MongoClient(uri,maxPoolSize=50)

baseDatos = cliente["mi_primera_base_datos"]

coleccion = baseDatos["mi_primera_coleccion"]

documento = { "nombre": "Jorge", "apellido": "Baron" }

inserccion = coleccion.insert_one(documento)

print(inserccion)