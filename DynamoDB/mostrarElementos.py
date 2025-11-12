def mostrarElementosTabla(tabla):

    respuesta = tabla.scan()

    elementos = respuesta['Items']

    # Mostrar todos los elementos
    for elemento in elementos:
        print(elemento)