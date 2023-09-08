from cod_generator import generar

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}
libroAgregado = {}

#Función que genera un nuevo diccionario para la lista
def nuevo_libro():
    codigoNuevo = generar()
    while True:
        cantEjemplares = int(input("Cuantos ejemplares desea agregar?"))
        if cantEjemplares < 0:
            print("Cantidad inválida, ingrese un número positivo.")
        else:
            break
    while True:
        cantPrestados = int(input("Cuantos ejemplares fueron prestados?"))
        if cantPrestados < 0:
            print("Cantidad inválida, ingrese un número positivo.")
        else:
            break
    nuevoTitulo = str(input("Ingrese el nombre del libro"))
    nuevoAutor = str(input("Ingrese el nombre del autor"))
    libroAgregado = {'cod': codigoNuevo, 'cant_ej_ad': cantEjemplares, 'cant_ej_pr': cantPrestados, "titulo": nuevoTitulo, "autor": nuevoAutor}
    print("Datos del libro nuevo:")
    print("Codigo:", libroAgregado['cod'])
    print("Titulo:", libroAgregado['titulo'])
    print("Autor:", libroAgregado['autor'])
    print("Cantidad de ejemplares adquiridos:", libroAgregado['cant_ej_ad'])
    print("Cantidad de ejemplares prestados:", libroAgregado['cant_ej_pr'])
    return libroAgregado
