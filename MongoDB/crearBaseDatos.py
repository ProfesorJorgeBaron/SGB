from Conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

baseDatos = cliente["mi_primera_base_datos"]

coleccion = baseDatos["mi_primera_coleccion"]

documento = {'nombre':'Jorge','apellido':'Baron'}

insercion = coleccion.insert_one(documento)

print(insercion)
