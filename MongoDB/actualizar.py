
from Conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]


for l in librosColeccion.find({"precio":14.5}):
  print(l)
  
miquery = { "precio": 14.5 }
nuevosValores = { "$set": { "precio": 10.99 } }

resultado = librosColeccion.update_one(miquery, nuevosValores)

print(resultado.modified_count, "documentos actualizados.")

#Mostramos si los libros han cambiado de precio
for l in librosColeccion.find({"precio":10.99}):
  print(l)
  
  
miquery = { "titulo": "1984" }
nuevosValores = { "$set": { "titulo": "Reina Roja" } }

resultado = librosColeccion.update_many(miquery, nuevosValores)

print(resultado.modified_count, "documentos actualizados.")