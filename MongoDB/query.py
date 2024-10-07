from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

uri =  'mongodb+srv://'+usuario+':'+password+'@'+cluster+'.teycm.mongodb.net/?retryWrites=true&w=majority&appName='+cluster

cliente = MongoClient(uri,maxPoolSize=50)

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

miquery = { "precio": 19.99 }

libros = librosColeccion.find(miquery)

for l in libros:
  print(l)
  
miquery = { "precio":  { "$gt": 19 } }

libros = librosColeccion.find(miquery)

for l in libros:
  print(l)

miquery = { "titulo":  { "$regex": "^D" } }

libros = librosColeccion.find(miquery)

for l in libros:
  print(l) 
