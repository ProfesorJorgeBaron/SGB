from Conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

miquery = { "titulo": "Cien Años de Soledad" }

resultado = librosColeccion.delete_one(miquery)

print(resultado.deleted_count, " documento eliminado.")

myquery = { "titulo": {"$regex": "^E"} }

resultado = librosColeccion.delete_many(myquery)

print(resultado.deleted_count, " documentos eliminados.")