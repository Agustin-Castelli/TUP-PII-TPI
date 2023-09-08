import libro as l
# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

#Función para ver un listado de los libros prestados
def ejemplares_prestados():
    sin_prestados = True
    print("Listado de libros prestados:")
    print("-----------------------------------")
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            print("Título:", libro['titulo'])
            print("Autor:", libro['autor'])
            print("Ejemplares prestados:", libro['cant_ej_pr'])
            print("-----------------------------------")
            sin_prestados = False
    if sin_prestados == True:
        print("No hay libros prestados.")
    return None

#Función para registrar un libro nuevo y agregarlo a la lista
def registrar_nuevo_libro():
    while True:
        add_book = l.nuevo_libro()
        libros.append(add_book)
        while True:
            nuevoIngreso = int(input("Desea ingresar un nuevo libro? 1. Si / 2. No"))
            if nuevoIngreso == 1 or nuevoIngreso == 2:
                break   
            else:
                print("Opción inválida.")
        if nuevoIngreso == 2:
            break
            
    return None

#Función para eliminar un ejemplar de la lista
def eliminar_ejemplar_libro():
    buscar_codigo = (input("Ingrese el codigo del libro que desea eliminar"))
    while True:
        for libro in libros:
            if buscar_codigo == libro.get('cod'):
                print("Libro encontrado:")
                print("Título:", libro['titulo'])
                print("Autor:", libro['autor'])
                print("Ejemplares disponibles:", libro['cant_ej_ad'])
                while True:
                    cant_eliminar = int(input("Cuántos ejemplares desea eliminar?"))
                    if cant_eliminar < 0 or cant_eliminar > libro['cant_ej_ad']:
                        print("Cantidad invalida")
                    else:
                        break
                libro['cant_ej_ad'] -= cant_eliminar
                print("Cantidad de ejemplares actualizada.")
                print("Título:", libro['titulo'])
                print("Autor:", libro['autor'])
                print("Ejemplares disponibles: ", libro['cant_ej_ad'])
        break
    if buscar_codigo != libro.get('cod'):
            print("Error: No existe el codigo ingresado.")
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
                        if nuevo_prestamo < 0 or nuevo_prestamo > libro['cant_ej_ad']:
                            print("Error: Cantidad inválida.")
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

#Función para devolver un ejemplar prestado a la lista
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
                        if devolucion < 0 or devolucion > libro['cant_ej_pr']:
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

#Función para mostrar los libros de la lista (no solicitada) 
#def mostrar_libros(): 
    #for libro in libros:
        #print("-----------------------------------")
        #print("Codigo:", libro['cod'])
        #print("Titulo:", libro['titulo'])
        #print("Autor:", libro['autor'])
        #print("Cantidad de ejemplares adquiridos:", libro['cant_ej_ad'])
        #print("Cantidad de ejemplares prestados:", libro['cant_ej_pr'])    
    #return None
