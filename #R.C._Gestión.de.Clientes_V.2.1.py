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
        print("Teléfono: ")
        Télefono = str(input(":"))
        print("Vigencia: ")
        Vigencia = str(input(":")).upper()

    
    Clientes [Rut_Cliente] = {          #Así se irán guardando los datos.
        "Nombre": Nombre,
        "Mail": Mail,
        "Télefono": Télefono,
        "Vigencia": Vigencia
    }
    

def Menú_Gestión_de_clientes():
    opc = 0           #Variables para las opciones siguientes.
    opc2 = 0
    while True:     #Bucle infinito, más abajo se especifica con que condición se sale del bucle.
        print()
        print("<|==-- Gestión de clientes --==|>")
        print("1)Crear cliente\n2)Lista de clientes\n3)Modificar/Eliminar Cliente\n4)Salir")
        print("Seleccione una opción")
        opc = int(input(":"))
        if opc == 1:              #Se ejecuta la función para crear usuario.
            CrearUser_Menú()
        elif opc == 2:            # Se libera una lista de los datos de cada cliente asociado al rut, y se recorre con un for.
             for Rut, Datos in Clientes.items():
                 print(f"Rut: {Rut} | Datos: {Datos} ")
        elif opc ==3:             #Opción para modificar o eliminar un cliente, falta la parte para eliminar solamente.
            print()
            print("Menú")               
            print("Seleccione una opcion")
            print("1)Modificar cliente\n2)Eliminar cliente")        
            opc2 = int(input(":"))
            if opc2 == 1:
                print("|== Modificación de cliente ==|")              
                print("Ingrese el rut del cliente: ")         #Se buscará mediante el rut
                Found_rut = input(":")                        #Por eso definimos que la variable que debe ingresar debe ser el rut a buscar
                if  Found_rut in Clientes:               #Con for se recorrerá el diccionario hasta encontrar el rut ingresado
                    print(Clientes[Found_rut])
                    opc2 = input("¿Que dato desea modificar? (Nombre, Mail, Teléfono, Vigencia): ")    #Se le pide al usuario que ingrese una de las #opciones para definir cual desea cambiar
                    
                    if opc2 in ["Nombre", "Mail", "Telefono", "Vigencia"]:        #Condicion para que revise que la opción registrada anteriormente sea valida                     
                        print()
                        print("Agregue el nuevo valor que desea darle: ") # se le pide al usuario que ingrese el nuevo valor de la opción elegida
                        Nuevo_valor = input(":")
                        Clientes[Found_rut][opc2] = Nuevo_valor          #Se le asocia el nuevo valor segun el rut y se el dato seleccionado
                        print("Datos modificados con éxito")
                        print(Clientes[Found_rut])
                    else:
                        print("Opción no valida, no se realizaron cambios")
                else:
                    print("Rut no asociado a ningún cliente")
            
            elif opc2 == 2:
                print("|== Eliminar cliente ==|")
                print("Ingrese el rut del cliente: ")
                Found_rut = input(":")
                if Found_rut not in Clientes:
                    print("No existe un cliente con ese rut")
                    return
                else:
                    print(Clientes[Found_rut])




        elif opc == 4:
            print("Cerrando gestión de clientes")    #Opción con la cual se sale del bucle y del menú
            print("...")
            time.sleep(1)                             #Simple decoración para crear un retraso simulando un menú normal
            break    #break para quebrar el codigo y terminarlo

Menú_Gestión_de_clientes()

