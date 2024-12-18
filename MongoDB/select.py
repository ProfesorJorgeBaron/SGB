from Conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

#Obtenemos el primero libro que encontremos
libro = librosColeccion.find_one()
print(libro)
print("\n")

#Obtenermos varios libros
libros = librosColeccion.find()
for l in libros:
  print(l)
  print("\n")

#Obtenemos libros pero no el campo id
libros2 = librosColeccion.find({},{ "_id": 0, "titulo": 1, "paginas": 1, "precio":1,"disponible":1 })
for l in libros2:
  print(l)
  print("\n")
  
libros3 = librosColeccion.find({},{"paginas": 0,"precio":0})
for l in libros3:
  print(l)
  print("\n")

#Si mezclamos 1 y 0, sólo podemos poner 0 en un campo
cliente.close()