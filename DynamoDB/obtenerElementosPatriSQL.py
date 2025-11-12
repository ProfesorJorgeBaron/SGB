from conectarse import * 

dynamodb = conectarseDynamoDBCliente()


consulta = """
SELECT *
FROM "ejemplo_tabla_libros"
WHERE genero = 'Policíaca' AND precio > 15
"""

respuesta = dynamodb.execute_statement(Statement=consulta)

libros = respuesta['Items']
for libro in libros:
    print(libros)