import csv
import os.path

def main():
    CAMPOS = ["Legajo", "Apellido", "Nombre"]
    eleccion = int(input("Elija una opcion: \n 1-Cargar Legajos\n 2-Estado de Gastos\n 3- salir\n"))
    if eleccion == 1:
        cargar(CAMPOS)
    elif eleccion == 2:
        registro_viaticos()
    elif eleccion == 3:
        exit()
    else:
        print("Esa opcion no existe. Por favor, elegir entre las opciones dadas")
    main()

def cargar(encabezados):
    guardar = 's'
    lista_usuarios = []
    lista_usuarios.append(encabezados)
    while guardar == 's':
        usuario = {}
        for encabezado in encabezados:
            dato = input(f"Ingrese {encabezado} del usuario: ")
            if encabezado == encabezados[0]:
                try:
                    int(dato)     
                except:
                    print("Los legajos deben ser numeros enteros")
                    dato = input(f"Ingrese {encabezado} del usuario: ")

            usuario[encabezado] = dato
        guardar = input("Quiere seguir agregando usuarios? s/n ")
        lista_usuarios.append(usuario)
    try:
        archivo1 = input("ingrese el nombre del archivo para guardar los usuarios (sin la extension): ") + ".csv"
        if os.path.isfile(archivo1):
            opcion = input("Ese archivo ya existe, desea 1-agregar legajos o 2-sobreescribirlo? ") 
            while opcion == "1" or opcion == "2":
                if opcion == "1":
                    with open(archivo1, 'a', newline='') as f:
                        usuarios_csv = csv.writer(f)
                        usuarios_csv.writerows(lista_usuarios)
                        return
                elif opcion == "2":    
                    with open(archivo1, 'w', newline='') as f:
                        usuarios_csv = csv.writer(f)
                        usuarios_csv.writerows(lista_usuarios)
                        return 
            print("Opcion no disponible")
            opcion = input("Ese archivo ya existe, desea 1-agregar legajos o 2-sobreescribirlo? ")
        else:
            with open(archivo1, 'w', newline='') as f:
                usuarios_csv = csv.writer(f)
                usuarios_csv.writerows(lista_usuarios) 

    except IOError:
        print("Hubo un problema con el archivo")

def registro_viaticos():
    try:
        archivo_1 = input("ingrese el nombre del archivo de legajos (sin la extension): ") + ".csv"
        archivo_2 = input("ingrese el nombre del archivo de los viaticos: ") + ".csv"
        if os.path.isfile(archivo_1) and os.path.isfile(archivo_2) == True:
            with open(archivo_1, 'r', newline='') as file1, open(archivo_2, 'r', newline='') as file2:
                    legajos_csv = csv.reader(file1)
                    viaticos_csv = csv.reader(file2)
                    next(legajos_csv, None)
                    next(viaticos_csv, None)
                    
                    dato = int(input(f"Ingrese el numero de legajo: "))
                    for viatico in viaticos_csv:
                        presup = 5000
                        cont = 0
                        if int(viatico[0]) == dato:
                            cont += int(viatico[1])
                        for legajo in legajos_csv:
                            if int(legajo[0]) == dato:
                                if cont > presup:
                                    print(f"Legajo {dato} : {legajo[2]} {legajo[1]}, gastó ${cont} y se ha pasado del presupuesto por ${cont-presup}")
                                else:
                                    print(f"Legajo {dato} : {legajo[2]} {legajo[1]}, gastó ${presup-cont}")

    except IOError:
        print("Hubo problemas con los archivos")
    
main()