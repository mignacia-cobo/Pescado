import csv
canchas = ["Club de Tenis Mantagua", "Club de Tenis Las Salinas","Club de Tenis La Ligua", "Club de Tenis Quilpué", "Club de Tenis La Calera"]
valor_cancha = [10000, 12000, 14000, 16000, 18000]
horarios = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
reservas =[]

def reservar_cancha():
    while True:
        #Seleccionar cancha
        while True:
            print("Canchas de tenis para reservar")
            for x in range(len(canchas)):
                print(f"{x+1}- {canchas[x]}")
            op = validar_int()
            if op >0 and op <6:
                print(f"Ha seleccionado la cancha {canchas[op-1]}")
                cancha = canchas[op-1]
                #asignar valor a la chancha de la lista valor_cancha
                valor = valor_cancha[op-1]
                break
            else:
                print("Debe seleccionar una cancha entre 1 y 5")
                
        #Seleccionar fecha
        print("Ingrese la fecha: ")
        fecha = validar_string()
        print(f"Ha seleccionado la fecha {fecha}")
        
        #Seleccionar horario
        while True:
            print("Horarios para reservar")
            for x in range(len(horarios)):
                print(f"{x+1}. {horarios[x]}")
            op = validar_int()
            if op >0 and op <10:
                print(f"Ha seleccionado el horario {horarios[op-1]}")
                hora = horarios[op-1]
                break
            else:
                print("Debe seleccionar una cancha entre 1 y 9")
        reserva = validar_reserva(cancha,fecha,hora)
        if reserva == True:
            print("Horario no disponible")
            continue
        else:

            #Ingresar nombre
            print("Ingrese su nombre: ")
            nombre = validar_string()

            #Ingresar contacto
            print("Ingrese su número de contacto: ")
            contacto = validar_int()
            
            #Solicitar si tiene código de descuento
            while True:
                print("Posee código de descuento S/N: ")
                op = validar_string()
                if op.upper() =='S':
                    print("Ingrese el código de descuento: ")
                    codigo = validar_string()
                    descuento = validar_descuento(codigo)
                    break
                elif op.upper() =='N':
                    descuento=0
                    print("No se aplica descuento")
                    break
                else:
                    print("Opción incorrecta")
                
            print(f"{nombre.upper()}, SU RESERVA: \n Cancha: {cancha}\n Fecha: {fecha}\n Hora: {hora}\n Valor: {valor}\n Descuento: {descuento*valor}\n Total: {valor-(descuento*valor)}\nSe ha realizado exitosamente")

            #Generar una lista con la cancha, la fecha, hora, nombre, contacto y valor.
            reserva =[cancha,fecha, hora, nombre, contacto, valor]
            #Se agrega la reserva realizada a la lista de las reservas
            reservas.append(reserva)

            #Preguntar si quiere realizar otra reserva o salir del programa
            while True:
                print("Desea realizar otra reserva S/N")
                op = validar_string()
                if op.upper() == 'S':
                    print()
                    break
                elif op.upper() == 'N':
                    exit()
                else:
                    print("Opción Incorrecta")
            break

def validar_reserva(cancha,fecha,hora):
    #mostrar las reservas para esa cancha en esa fecha y hora que se reciben por argumento
    flag = False
    for i in range(len(reservas)):

        if reservas[i][0]== cancha and reservas[i][1] == fecha and reservas[i][2]==hora:
            print(f"Horario reservado para el día {fecha} la cancha {cancha}")
            flag= True
            
    if flag ==True:
        return True
    else:
        return False
    

    
def validar_descuento(codigo):
    des=0
    while True:
        if codigo.upper() == "TENIS2024":
            print("Código correcto")
            des = 0.1
            break
        else:
            print("código incorrecto\nS- Reingresar código\nN- Continuar sin descuento")
            op = validar_string()
            if op.upper() =='S':
                print(f"Ingrese el código: ")
                codigo=validar_string()
                continue
            elif op.upper() =='N':
                des=0
                break
            else:
                print("Opción incorrecta")
    return des

def consultar_disponibilidad():
    horas_reservadas = []
    print("CONSULTAR DISPONIBILIDAD")
    #Seleccionar cancha para consultar la disponibilidad
    while True:
        print("Canchas de tenis para reservar")
        for x in range(len(canchas)):
            print(f"{x+1}- {canchas[x]}")
        op = validar_int()
        if op >0 and op <6:
            print(f"Ha seleccionado la cancha {canchas[op-1]}")
            cancha = canchas[op-1]
            break
        else: 
            print("Debe seleccionar una cancha entre 1 y 5")
    #Seleccionar una fecha para consultar la disponibilidad
    print("Ingrese la fecha: ")
    fecha = validar_string()
    print(f"Ha seleccionado la fecha {fecha}")
    #mostrar las reservas para esa cancha en esa fecha ingresada
    estado=''
    flag = False
    print(f"Reservas para la cancha: {cancha}")
    print(f"Fecha: {fecha}")
    for reserva in reservas:
        if reserva[0]== cancha and reserva[1] == fecha:
            horas_reservadas.append(reserva[2])
            flag=True
        
    if flag==True:
        for hora in horarios:
            if hora in horas_reservadas:
                estado = 'RESERVADO'
            else:
                estado= 'DISPONIBLE'
            print(f"{hora} - {estado}")
    else:
        print(f"no existen reservas para la cancha: {cancha} en la fecha: {fecha}")

def administrar_reservas():
    def ver_reservas():
        print("Ingrese el nombre: ")
        nombre= validar_string()
        reservas_nombre=[reserva for reserva in reservas if reserva[3].lower()==nombre.lower()]
        for f in range(len(reservas_nombre)):
            print(f"Reserva {f+1}")
            print(f"Cancha: {reservas_nombre[f][0]}")
            print(f"Fecha: {reservas_nombre[f][1]}")
            print(f"Hora: {reservas_nombre[f][2]}")
            print(f"Valor: {reservas_nombre[f][5]}")
            print()
            #for c in range(len(reservas_nombre[f])):
                #print(f"{reservas_nombre[f][c]} - ", end='')
            #print()

    def cancelar_reserva():
        print("Ingrese el nombre: ")
        nombre = validar_string()
        print("Ingrese la fecha: ")
        fecha = validar_string()
        print("Ingrese la hora")
        hora = validar_string()
        flag=False
        for f in range(len(reservas)):
            if reservas[f][1]== fecha and reservas[f][2]==hora and reservas[f][3]==nombre:
                print("confirmar cancelar la reserva S/N")
                op = validar_string()
                if op.upper() == 'S':
                    flag=True
                    i=f
                elif op.upper()== 'N':
                    print(f"{nombre}, su reserva no se ha cancelado")
                    flag=None
                else:
                    print("Opción Inválida")
                    flag=False
        if flag==True:
            reservas.pop(i)
            print (f"{nombre}, su reserva fue cancelada")
        elif flag==False:
            print("Reserva no encontrada")

    def modificar_reserva():
        print("Ingrese el nombre: ")
        nombre = validar_string()
        print("Ingrese la fecha: ")
        fecha = validar_string()
        print("Ingrese la hora")
        hora = validar_string()
        flag=False
        for f in range(len(reservas)):
            if reservas[f][1]== fecha and reservas[f][2]==hora and reservas[f][3]==nombre:
                print("confirmar modificar la reserva S/N")
                op = validar_string()
                if op.upper() == 'S':
                    flag=True
                    i=f
                elif op.upper()== 'N':
                    print(f"{nombre}, su reserva no se ha modificado")
                    flag=None
                else:
                    print("Opción Inválida")
                    flag=False
        if flag==True:
            #Seleccionar cancha
            while True:
                print("Canchas de tenis para reservar")
                for x in range(len(canchas)):
                    print(f"{x+1}- {canchas[x]}")
                op = validar_int()
                if op >0 and op <6:
                    print(f"Ha seleccionado la cancha {canchas[op-1]}")
                    cancha = canchas[op-1]
                    #asignar valor a la chancha de la lista valor_cancha
                    valor = valor_cancha[op-1]
                    break
                else:
                    print("Debe seleccionar una cancha entre 1 y 5")
                    
            #Seleccionar fecha
            print("Ingrese la fecha: ")
            fecha = validar_string()
            print(f"Ha seleccionado la fecha {fecha}")
            
            #Seleccionar horario
            while True:
                print("Horarios para reservar")
                for x in range(len(horarios)):
                    print(f"{x+1}. {horarios[x]}")
                op = validar_int()
                if op >0 and op <10:
                    print(f"Ha seleccionado el horario {horarios[op-1]}")
                    hora = horarios[op-1]
                    break
                else:
                    print("Debe seleccionar una cancha entre 1 y 9")
            reservas[i][0]= cancha
            reservas[i][1]= fecha
            reservas[i][2]= hora
            print (f"{nombre}, su reserva fue modificada con exito")

        elif flag==False:
            print("Reserva no encontrada")

    while True:
        print("ADMINISTRAR RESERVAS")
        print("1- Ver reservas por nombre")
        print("2- Cancelar reserva")
        print("3- Modificar reserva")
        print("4- Salir")
        op = validar_int()
        if op ==1:
            ver_reservas()
        elif op ==2:
            cancelar_reserva()
        elif op ==3:
            modificar_reserva()
        elif op ==4:
            break
        else:
            print("Opción incorrecta")

    print()

def validar_int():
    while True:
        try:
            num=int(input())
        except ValueError:
            print("Ingrese solo números")
        else: 
            break
    return num


def validar_string():
    while True:
        cadena = input()
        if cadena.strip(): #strip() devuelve el string sin espacios, para validar que contenga algun caracter
            return cadena
        else:
            print("El campo no debe estar vacío")

#función para leer el archivo csv y almacenar las reservas en la lista de reservas
def carga_inicial():
    with open('reservas_inicial.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            reservas.append(fila)
    print("Archivo procesado exitosamente")

#Función para crear archivo txt con las reservas
def crear_archivo():
    with open('reservas.txt', 'w')as archivo:
        i=0
        for reserva in reservas:
            
            if i==0:
                archivo.write("RESERVAS REGISTRADAS\n----------------------------------")

                i=i+1
            else:
                archivo.write(f"""
DETALLE DE LA RESERVA {i}
Nombre: {reserva[3]}
Cancha: {reserva[0]}
Fecha: {reserva[1]}
Hora: {reserva[2]}
Valor: {reserva[5]}
---------------------------------------
                    """)
                i=i+1

#Función para el menú principal
def menu():
    while True:
        try:
            print("----------MENÚ---------")
            print("1- Reservar Cancha")
            print("2- Consultar Disponibilidad")
            print("3- Administrar Reservas")
            print("4- Cargar Reservas")
            print("5- Guardar Reservar")
            print("6- Salir")

            op = int(input("Ingrese opción: "))
            
            if op == 1:
                reservar_cancha()
            elif op == 2:
                consultar_disponibilidad()
            elif op == 3:
                administrar_reservas()
            elif op == 4:
                carga_inicial()
            elif op == 5:
                crear_archivo()
            elif op == 6:
                print("CHAO")
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("La opción debe ser un número")

menu()