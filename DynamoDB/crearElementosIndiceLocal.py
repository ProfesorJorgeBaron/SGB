from conectarse import * 
from mostrarElementos import mostrarElementosTabla

dynamodb = conectarseDynamoDBResource()

tabla = dynamodb.Table(os.getenv("TABLA"))

libros = [
    {'autor': 'Ernest Hemingway', 'anyo_publicacion': '1926', 'titulo': 'El viejo y el mar', 'precio': 10},
    {'autor': 'F. Scott Fitzgerald', 'anyo_publicacion': '1925', 'titulo': 'El gran Gatsby', 'precio': 12},
    {'autor': 'J.R.R. Tolkien', 'anyo_publicacion': '1954', 'titulo': 'El señor de los anillos', 'precio': 20},
    {'autor': 'Leo Tolstoy', 'anyo_publicacion': '1869', 'titulo': 'Guerra y paz', 'precio': 25},
    {'autor': 'Herman Melville', 'anyo_publicacion': '1851', 'titulo': 'Moby Dick', 'precio': 15}
]

for libro in libros:
    tabla.put_item(
        Item={
            'autor': libro['autor'],
            'anyo_publicacion': libro['anyo_publicacion']
        }
    )
    
mostrarElementosTabla(tabla)
