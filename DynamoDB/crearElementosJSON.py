from conectarse import * 
from mostrarElementos import mostrarElementosTabla
from decimal import Decimal

dynamodb = conectarseDynamoDBResource()

tabla = dynamodb.Table(os.getenv("TABLA"))

libros = [
    {
        'autor': 'Agatha Christie',
        'anyo_publicacion': "1934",
        'titulo': 'Muerte en el Nilo',
        'calificaciones': [Decimal('4.5'), Decimal('5'), Decimal('4')],
        'capitulos': ['capitulo1', 'capitulo2', 'capitulo3'],
        'editorial': {'ciudad': 'Londres', 'nombre': 'Collins Crime Club', 'pais': 'Reino Unido'},
        'fecha_creacion': None,
        'genero': 'Policíaca',
        'Libro': b'',
        'parrafos': [b''],
        'precio': 12,
        'temas': ['misterio', 'asesinato', 'investigación']
    },
    {
        'autor': 'Arthur Conan Doyle',
        'anyo_publicacion': "1892",
        'titulo': 'Estudio en escarlata',
        'calificaciones': [Decimal('4.5'), Decimal('5'), Decimal('4')],
        'capitulos': ['capitulo1', 'capitulo2', 'capitulo3'],
        'editorial': {'ciudad': 'Londres', 'nombre': 'Ward, Lock & Co', 'pais': 'Reino Unido'},
        'fecha_creacion': None,
        'genero': 'Policíaca',
        'Libro': b'',
        'parrafos': [b''],
        'precio': 15,
        'temas': ['detective', 'misterio', 'crimen']
    },
    {
        'autor': 'Raymond Chandler',
        'anyo_publicacion': "1939",
        'titulo': 'El sueño eterno',
        'calificaciones': [Decimal('4.5'), Decimal('5'), Decimal('4')],
        'capitulos': ['capitulo1', 'capitulo2', 'capitulo3'],
        'editorial': {'ciudad': 'Nueva York', 'nombre': 'Alfred A. Knopf', 'pais': 'EE.UU.'},
        'fecha_creacion': None,
        'genero': 'Policíaca',
        'Libro': b'',
        'parrafos': [b''],
        'precio': 18,
        'temas': ['private eye', 'misterio', 'crimen']
    },
    {
        'autor': 'Dashiell Hammett',
        'anyo_publicacion': "1930",
        'titulo': 'Cosecha roja',
        'calificaciones': [Decimal('4.5'), Decimal('5'), Decimal('4')],
        'capitulos': ['capitulo1', 'capitulo2', 'capitulo3'],
        'editorial': {'ciudad': 'Nueva York', 'nombre': 'Alfred A. Knopf', 'pais': 'EE.UU.'},
        'fecha_creacion': None,
        'genero': 'Policíaca',
        'Libro': b'',
        'parrafos': [b''],
        'precio': 10,
        'temas': ['crimen', 'misterio', 'investigación']
    },
    {
        'autor': 'Patricia Highsmith',
        'anyo_publicacion': "1950",
        'titulo': 'Extraños en un tren',
        'calificaciones': [Decimal('4.5'), Decimal('5'), Decimal('4')],
        'capitulos': ['capitulo1', 'capitulo2', 'capitulo3'],
        'editorial': {'ciudad': 'Nueva York', 'nombre': 'Alfred A. Knopf', 'pais': 'EE.UU.'},
        'fecha_creacion': None,
        'genero': 'Policíaca',
        'Libro': b'',
        'parrafos': [b''],
        'precio': 15,
        'temas': ['misterio', 'asesinato', 'psicología']
    }
]

for libro in libros:
    tabla.put_item(Item=libro)
    
mostrarElementosTabla(tabla)
