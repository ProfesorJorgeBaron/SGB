from conectarse import * 

dynamodb = conectarseDynamoDBResource()

tabla = dynamodb.Table(os.getenv("TABLA"))

respuesta = tabla.get_item(
        Key={
            'autor': 'García Márquez',
            'anyo_publicacion': "1967"
        },
        ProjectionExpression="titulo, autor"
)

libro = respuesta['Item']
print(libro)
