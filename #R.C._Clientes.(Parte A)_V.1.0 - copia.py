#Reserva de cine
import time

#Creamos un diccionario vacío
Clientes = {

}

def CrearUser_Menú ():   #Creamos la funcion para crear usuarios
    Rut_Cliente = "" #Variable simpre para que funcione el if que sigue
    
    if Rut_Cliente not in Clientes: #Condicional para filtrar si el rut esta registrado o no
        print()  # De aquí para abajo es una secuencia que pide un ingreso de datos que se van guardando
        print("|==== Creación de cliente ====|")
        print("Rut: ")
        Rut_Cliente = input(":").upper()
        if Rut_Cliente in Clientes:
            return print("Rut ya registrado")
        print("Nombre: ")
        Nombre = str(input(":")).upper()
        print("Mail")
        Mail = str(input(":")).upper()
        Mail in Clientes
        print("Teléfono: ")
        Télefono = str(input(":"))
        print("Vigencia: ")
        print("S para cliente vigente y N para cliente no vigente")
        Vigencia = str(input(":")).upper()

    
    Clientes [Rut_Cliente] = {          #Así se irán guardando los datos, asociandose deacuerdo al rut.
        "Nombre": Nombre,
        "Mail": Mail,
        "Télefono": Télefono,
        "Vigencia": Vigencia
    }
    

def Menú_Clientes_PA():
    opc = 0           #Variables para las opciones siguientes.
    opc2 = 0
    while True:     #Bucle infinito, más abajo se especifica con que condición se sale del bucle.
        print()
        print("<|==-- Alta y consulta de clientes --==|>")
        print("1)Crear cliente\n2)Lista de clientes\n3)Salir")
        print("Seleccione una opción")
        opc = int(input(":"))
        if opc == 1:              #Se ejecuta la función para crear usuario.
            CrearUser_Menú()
        elif opc == 2:            # Se libera una lista de los datos de cada cliente asociado al rut, y se recorre con un for.
             for Rut, Datos in Clientes.items():
                 print("|==Clientes registrados==|")
                 print(f"Rut: {Rut} | Datos: {Datos} ")


        elif opc == 3:
            print("Cerrando gestión de clientes")    #Opción con la cual se sale del bucle y del menú
            print("...")
            time.sleep(1)                             #Simple decoración para crear un retraso simulando un menú normal
            break    #break para quebrar el codigo y terminarlo

Menú_Clientes_PA()

