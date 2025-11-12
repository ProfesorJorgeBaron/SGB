from conectarse import * 
from boto3.dynamodb.conditions import Key

dynamodb = conectarseDynamoDBResource()

tabla = dynamodb.Table(os.getenv("TABLA"))
respuesta = tabla.query(
    KeyConditionExpression=Key('autor').eq('Agatha Christie'),
    IndexName='PrecioIndex',              # Nombre del LSI
    ScanIndexForward=True                 # True = ascendente, False = descendente
)

libros = respuesta['Items']
for libro in libros:
    print(libros)
    
respuesta = tabla.query(
    IndexName='GeneroTituloIndex',        # Nombre del GSI
    KeyConditionExpression=Key('genero').eq("Policíaca")
)

libros = respuesta['Items']
for libro in libros:
    print(libros)