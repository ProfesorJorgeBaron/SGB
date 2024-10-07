from Conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

print("Listado de libros con expresion AND")

libros= librosColeccion.find({ "$and" : [ 
                                                      { "paginas" : {"$lt": 400 }}, 
                                                      { "precio" : { "$gt":7} }
                                                    ]
                                            }
                                            )

for l in libros:
    print(l)

print("Listado de libros con expresión OR")

libros= librosColeccion.find({ "$or" : [ 
                                                      { "paginas" : {"$lt": 400 }}, 
                                                      { "precio" : { "$gt":7} }
                                                    ]
                                            }
                                            )

for l in libros:
    print(l)

print("Listado de libros filtrados con NOR")
libros= librosColeccion.find({ "$nor" : [ 
                                                      { "paginas" : {"$lt": 400 }}, 
                                                      { "precio" : { "$gt":7} }
                                                    ]
                                            }
                                            )

for l in libros:
    print(l)
  
    print("Listado de libros filtrados con NOT")
    libros= librosColeccion.find({"paginas" :  { "$not" : {"$lt": 400 }}})

for l in libros:
    print(l)
  