from conectarse import * 
from mostrarElementos import mostrarElementosTabla

dynamodb = conectarseDynamoDBResource()

tabla = dynamodb.Table(os.getenv("TABLA"))

libros = [
    {'autor': 'García Márquez', 'anyo_publicacion': '1967', 'titulo': 'Cien años de soledad'},
    {'autor': 'Isabel Allende', 'anyo_publicacion': '1982', 'titulo': 'La casa de los espíritus'},
    {'autor': 'J.K. Rowling', 'anyo_publicacion': '1997', 'titulo': 'Harry Potter y la piedra filosofal'},
    {'autor': 'George Orwell', 'anyo_publicacion': '1949', 'titulo': '1984'},
    {'autor': 'Jane Austen', 'anyo_publicacion': '1813', 'titulo': 'Orgullo y prejuicio'}
]

for libro in libros:
    tabla.put_item(
        Item={
            'autor': libro['autor'],
            'anyo_publicacion': libro['anyo_publicacion'],
            'titulo': libro['titulo'],
        }
    )
    
mostrarElementosTabla(tabla)
