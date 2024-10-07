from Conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

print("Listado de libros ordeandos titulo Ascendente")

librosOrdenadosPorTitulo = librosColeccion.find().sort("titulo")

for l in librosOrdenadosPorTitulo:
    print(l)

print("Listado de libros ordeandos por precio descendente")

librosOrdenadosPorPrecioDescendente = librosColeccion.find().sort("precio",-1)

for l in librosOrdenadosPorPrecioDescendente:
    print(l)

print("Listado de libros filtrados por precio y ordenados por número de Páginas")

librosFiltradoPorPrecioyOrdenadosPorPaginas = librosColeccion.find({ "precio":  { "$lt": 20 } }).sort("paginas")

for l in librosFiltradoPorPrecioyOrdenadosPorPaginas:
    print(l)
  
