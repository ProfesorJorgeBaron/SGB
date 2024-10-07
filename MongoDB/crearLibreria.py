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
libros = [
    { "titulo": "Cien Años de Soledad", "paginas": 417, "precio": 19.99,"disponible": True },
    { "titulo": "1984", "paginas": 328, "precio": 14.50, "disponible": False },
    { "titulo": "Don Quijote de la Mancha", "paginas": 1072, "precio": 24.99, "disponible": True },
    { "titulo": "El Principito", "paginas": 96, "precio": 7.99, "disponible": False }
]

libros_creados = librosColeccion.insert_many(libros)
print(libros_creados.inserted_ids)