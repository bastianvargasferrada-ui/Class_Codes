#Reserva de cine
import time

#Creamos una lista vacía
Clientes = {

}

def CrearUser_Menú ():   #Creamos la funcion para crear usuarios
    Rut_Cliente = "" #Variable simpre para que funcione el if que sigue
    
    if Rut_Cliente not in Clientes: #Condicional para filtrar si el rut esta registrado o no
        print()  # De aquí para abajo es una secuencia que pide un ingreso de datos que se van guardando
        print("|==== Creación de cliente ====|")
        print("Rut: ")
        Rut_Cliente = input(":")
        if Rut_Cliente in Clientes:
            return print("Rut ya registrado")
        print("Nombre: ")
        Nombre = str(input(":"))
        print("Mail")
        Mail = str(input(":"))
        print("Teléfono: ")
        Télefono = int(input(":"))
        print("Vigencia: ")
        Vigencia = str(input(":"))

    
    Clientes [Rut_Cliente] = {
        "Nombre": Nombre,
        "Mail": Mail,
        "Télefono": Télefono,
        "Vigencia": Vigencia
    }
    

def Menú_Principal():
    opc = 0
    opc2 = 0
    while True:
        print()
        print("<|==-- Gestión de clientes --==|>")
        print("1)Crear cliente\n2)Lista de clientes\n3)Modificar/Eliminar Cliente\n4)Salir")
        print("Seleccione una opción")
        opc = int(input(":"))
        if opc == 1:
            CrearUser_Menú()
        elif opc == 2:
             for Rut, Datos in Clientes.items():
                 print(f"Rut: {Rut} | Datos: {Datos} ")
        elif opc ==3:
            print("Seleccione una opcion")
            print("1)Modificar cliente\n2)Eliminar cliente")
            opc2 = int(input(":"))
            if opc2 == 1:
                print("|== Modificación de cliente ==|")
                print("Ingrese el rut del cliente: ")
                Found_rut = input(":")
                print(Clientes[Found_rut])
                opc2 = ("¿Que dato desea modificar?")
            elif opc2 == 2:
                print("|== Eliminar cliente ==|")
                print("Ingrese el rut del cliente: ")
                Found_rut = input(":")
                print(Clientes[Found_rut])


        elif opc == 4:
            print("Cerrando gestión de clientes")
            print("...")
            time.sleep(1)
            break    

Menú_Principal()

