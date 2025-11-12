from conectarse import * 
from mostrarElementos import mostrarElementosTabla

dynamodb = conectarseDynamoDBResource()

tabla = dynamodb.Table(os.getenv("TABLA"))

libros = [
    {'autor': 'Mary Shelley', 'anyo_publicacion': '1818', 'titulo': 'Frankenstein', 'genero': 'Horror'},
    {'autor': 'Bram Stoker', 'anyo_publicacion': '1897', 'titulo': 'Drácula', 'genero': 'Horror'},
    {'autor': 'Mark Twain', 'anyo_publicacion': '1884', 'titulo': 'Las aventuras de Huckleberry Finn', 'genero': 'Aventura'},
    {'autor': 'Charles Dickens', 'anyo_publicacion': '1859', 'titulo': 'Historia de dos ciudades', 'genero': 'Clásico'},
    {'autor': 'Victor Hugo', 'anyo_publicacion': '1862', 'titulo': 'Los miserables', 'genero': 'Clásico'}
]

for libro in libros:
    tabla.put_item(
        Item={
            'autor': libro['autor'],
            'anyo_publicacion': libro['anyo_publicacion']
        }
    )
    
mostrarElementosTabla(tabla)
