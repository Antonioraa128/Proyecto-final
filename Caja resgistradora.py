#Funcion que imprime el menu completo, se utiliza a lo largo de todo el programa
def mmenu(Menu, MenuN, conta, X):
    conta = 0
    while X >conta:
        print ("Costo del paquete "+str(conta+1)+" "+str(MenuN[conta])+" : "+str(Menu[conta])+"$")
        conta = conta + 1
#Listas que utilizaremos en el programa
Menu = [] 
MenuN = []
Opciones = ['1) Dar de alta el menú entero', '2) Dar datos de alta', '3) Dar datos de baja', '4) Consultar datos', '5) Cambiar dato', '6) Caja registradora', '7) Volver al menú inicial de cliente o empleado', "8) Cerrar programa (los datos de MENU se reinician al volver a iniciarlo)"]
AP = 0; conta = 0; total = 0; MI = 0; count = 0
while MI == 0:
    print ("""        ---------------------------------------------------------------------------
  ------Hola bienvenido a Fiesta Chicken ¿Es Empleado o Cliente?------------
        --------------------------------------------------------------------------
        1) Empleado""")
        #Print condicional por si es la primera vez que aparece, porque el menú no está registrado todavía
    if count == 0:
        print ("""        2) Cliente (El menú debe registrarse primero, llame a un empleado)
        --------------------------------------------------------------------------""")
    else:
        print ("""        2) Cliente
        --------------------------------------------------------------------------""")
    usuario = input("        Introduzca el número de la opción que sea : ")
    AP = 0
    if usuario == "1":
        #Validación de usuario con la contraseña de ejemplo 1234
        contraseña = input("Introduzca su contraseña de usuario : ")
        if contraseña == "1234":
            while AP == 0:
                AP=0
                if count == 0:
                    #Print condicional nuevamente por si es la primera vez que aparece, porque el menú no está registrado todavía
                    print  ("""--------------------------------------------------------------------------
---------------------- Bienvenido de nuevo socio :) ----------------------
--------------------------------------------------------------------------
---------- ANTES DE UTILIZAR CUALQUIER OTRA OPCIÓN DEBE HACER LA 1 --------""")
                print ("""--------------------------------------------------------------------------
-----------------------MENÚ DE OPCIONES EMPLEADOS-------------------------
--------------------------------------------------------------------------""")
                count = 1
                while count < 9:
                    print (Opciones[count-1])
                    count = count+1
                print ("--------------------------------------------------------------------------")
                op = int(input('¿Qué opción desea realizar? : '))
                if op == 1:
                    #proceso de creación del menu, con una lista y append
                    count = 1
                    X = int(input ("Ingrese el tamaño del menú : "))
                    while count < X +1:
                        nom = (input("Introduzca el nombre del producto o combo "+str(count)+" del menú : "))
                        co = float (input ("Ingrese el costo de "+str(nom)+" :"))
                        Menu.append(co)
                        MenuN.append(nom) 
                        count = count +1
                if op == 2:
                    #Integración de un nuevo producto al menu con la lista ya creada y append
                    print ("Menu actual: ")
                    mmenu(Menu, MenuN, conta, X)
                    OpAN = input("¿Que opcion del menu desea agregar?, Introduzca el nombre que le corresponda : ")
                    OpA = float (input("Introduzca el precio de "+str(OpAN)+" : "))
                    X = X+1
                    Menu.append(OpA)
                    MenuN.append(OpAN)
                    print ("Menu actualizado")
                    mmenu(Menu, MenuN, conta, X)
                if op ==3:
                    #Eliminación de un producto del menú sin lista y remove
                    contador3 = 0
                    mmenu(Menu, MenuN, conta, X)
                    OpE = int(input("¿Que opcion del menu desea eliminar?, Introduzca el número que le corresponda : "))
                    if OpE == X:
                        X = X-1
                    else:
                        Menu.remove(Menu[OpE-1])
                        MenuN.remove(MenuN[OpE-1])
                        X =X-1
                    print  ("Menu actualizado")
                    mmenu(Menu, MenuN, conta, X)
                if op ==4:
                    #Opción de consultar los datos actuales del menú
                    mmenu(Menu, MenuN, conta, X)
                if op == 5:
                    #Edición de datos de precio de algún producto del menú con lista
                    contador5=1
                    while contador5==1:
                        mmenu(Menu, MenuN, conta, X)
                        editar = int(input("Introduce el número del costo del menú a editar : "))
                        NuevoP = float(input("introduzca el nuevo precio : "))
                        Menu[editar-1]= NuevoP
                        print ("El costo actualizado de "+str(MenuN[editar-1])+" es "+str(Menu[editar-1]))
                        t5 = int(input("¿Desea cambiar algo más?, Escriba 1 para continuar o 0 para finalizar "))
                        contador5 = t5
                if op ==6:
                    #Función de caja registradora, donde se suma el total de lo que se indique y pide pago para dar el cambio
                    contador6 = "no"
                    while contador6 == "no"or contador6 == "No":
                        mmenu(Menu, MenuN, conta, X)
                        compra = int(input("introduzca el número del paquete seleccionado para comprar : "))
                        total = total + Menu[compra-1]
                        contador6 = input("¿Es todo? escriba (Si) si es todo o (No) para continuar : ")
                    print ("El total es ",total)
                    pago = int(input("¿Con cuánto se va a pagar? : "))
                    print ("El cambio es de ",pago-total," $ ")
                    total = 0
                if op == 7:
                    #Condicional para volver al menú anterior de usuarios
                    AP = 1
                if op ==8:
                    #Condicional para terminar con el programa, esta opción solo se le permite a los empleados
                    print ("Apagando el sistema, hasta la próxima...")
                    MI= 1
                    AP = 1
        else:
            #Print en caso de contraseña incorrecta
            print ("contraseña incorrecta, reiniciando...")
    elif usuario =="2":
        #Opción de cliente, en donde puede realizar su orden y/o regresar al menú de usuario con condicional
        while AP == 0:
                    contador6 = "no"
                    PO = int(input("¿Pedir una nueva orden? introduzca (0) para volver al menu anterior o (1) para seguir : "))
                    if PO == 1:
                     print  (""""               ---------------------------------------------------------
    -- Bienvenido a Fiesta Chicken nuestro menú de hoy es: --
    ---------------------------------------------------------""")
                     while contador6 == "no" or contador6 == "No":
                        mmenu(Menu, MenuN, conta, X)
                        compra = int(input("introduzca el número del paquete seleccionado para comprar : "))
                        total = total + Menu[compra-1]
                        contador6 = input("¿Es todo? escriba (Si) si es todo o (No) para continuar : ")
                     print ("El total es ",total)
                     pago = int(input("¿Con cuánto se va a pagar? : "))
                     print ("El cambio es de ",pago-total," $ ")
                     total = 0
                    elif PO == 0:
                        AP = 1
