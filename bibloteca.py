import libro as l
# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    salirDelRegistro = 1
    while salirDelRegistro == 1:
        add_book = l.nuevo_libro()
        libros.append(add_book)
        nuevoIngreso = int(input("Desea ingresar un nuevo libro? 1. Si / 2. No"))
        if nuevoIngreso == 2:
            break   
    #completar
    return None

def eliminar_ejemplar_libro():
    codigoEliminar = (input("Ingrese el codigo del libro que desea eliminar"))
    
    #completar
    return None

def prestar_ejemplar_libro():
    buscar_codigo = input("Ingrese el codigo del libro a consultar:")
    libro_encontrado = False
    while libro_encontrado == False:
        for libro in libros:
            if buscar_codigo == libro.get('cod'):
                libro_encontrado = True
                if libro['cant_ej_ad'] > 0:
                    print("Libro encontrado:")
                    print(libro['titulo'])
                    print(libro['autor'])
                    print("Ejemplares disponibles:", libro['cant_ej_ad'])
                    while True:
                        nuevo_prestamo = int(input("Ingrese la cantidad de ejemplares a prestar:"))
                        if nuevo_prestamo > libro['cant_ej_ad']:
                            print("No hay suficiente stock, ingrese una nueva cantidad.")
                        else:
                            libro['cant_ej_pr'] += nuevo_prestamo
                            libro['cant_ej_ad'] -= nuevo_prestamo
                            print("Préstamo confirmado.")
                            print("Ejemplares disponibles restantes:", libro['cant_ej_ad'])
                            break
                   
                else:
                    print("No hay ejemplares disponibles.")
                    break
        break
    if buscar_codigo != libro.get('cod'):
            print("Error: No existe el codigo ingresado.")
    return None

def devolver_ejemplar_libro():
    buscar_codigo = input("Ingrese el codigo del libro a consultar:")
    while True:
        for libro in libros:
            if buscar_codigo == libro.get('cod'):
                print("Libro encontrado:")
                print("Título:", libro['titulo'])
                print("Autor", libro['autor'])
                print("Ejemplares prestados", libro['cant_ej_pr'])
                if libro['cant_ej_pr'] > 0:
                    while True:
                        devolucion = int(input("Cuantos ejemplares desea devolver?"))
                        if devolucion > libro['cant_ej_pr']:
                            print("Error: cantidad inválida.")
                        else:
                            libro['cant_ej_pr'] -= devolucion
                            libro['cant_ej_ad'] += devolucion
                            print("Devolución confirmada.")
                            print("Cantidad de ejemplares prestados actual:", libro['cant_ej_pr'])
                            break
                else:
                    print("No hay ejemplares prestados.")
                    break
        break
    if buscar_codigo != libro.get('cod'):
            print("Error: No existe el codigo ingresado.")
                    
                
    return None

def mostrar_libros():
    for libro in libros:
        print("-------------------------------------------")
        print("Codigo:", libro['cod'])
        print("Titulo:", libro['titulo'])
        print("Autor:", libro['autor'])
        print("Cantidad de ejemplares adquiridos:", libro['cant_ej_ad'])
        print("Cantidad de ejemplares prestados:", libro['cant_ej_pr'])    
    return None