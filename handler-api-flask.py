from re import L
import requests

url = 'http://localhost:5000/alumno'

while True:
    print(
        """
        \nAdministracion remota
=======================================================
        1. Agregar alumno
        2. Modificar datos de un alumno
        3. Listar alumnos
        4. Eliminar un alumno
        5. Salir
        """
    )

    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        nombre = input("Nombre: ")
        cursos = input('Cursos: ')
        datos = {
            'nombre':nombre,
            'cursos':cursos
        }
        r = requests.post(url, json=datos)
        print('Codigo de respuesta: ', r.status_code)
        print('Respuesta: ', r.json())

    elif opcion == '2':
        id_alumno = int(input("ID: "))
        datos = {
            'id':id_alumno,
            'nombre':None,
            'cursos':None
        }
        cambiar = input('¿Desea cambiar el nombre (y/N)?: ')

        if cambiar.casefold() == 'y':
            datos['nombre'] = input('Nuevo nombre: ')

        cambiar = input('¿Desea cambiar los cursos (y/N)?: ')
        if cambiar.lower == 'y':
            datos['cursos'] = input('Nuevo curso: ')
        r = requests.put(url, json=datos)
        print('Codigo de respuesta: ', r.status_code)
        print('Respuesta: ', r.json())

    elif opcion == '3':
        r = requests.get(url)
        if r.status_code == 200:
            alumnos = r.json()['alumnos']
            if not alumnos:
                print('No hay alumnos')
            else:
                for alumno in alumnos:
                    print(alumno)
        else:
            print("No se pudo descargar la lista de alumnos")
            print('Codigo de respuesta', r.status_code)
    
    elif opcion == '4':
        id_alumno = int(input("ID: "))
        datos = {
            'id':id_alumno,
        }
        r = requests.delete(url, json=datos)
        print("Alumno eliminado")
        print('Codigo de respuesta', r.status_code)

    elif opcion == '5':
        break

    else:
        print('Equivocado')
