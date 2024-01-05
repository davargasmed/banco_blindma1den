banco = {'david22': ['miclave', 2000] ,
         'liss97' : ['suclave' , 2000]
         }
c = 3


def depositar(): #funcion para hacer depositos a la cuenta
    deposito = int(input('Cuanto dinero va a depositar?\n$'))
    banco[user][1] = banco[user][1] + deposito
    print('su nuevo saldo es: $',banco[user][1])

def retirar():#funcion para retirar dinero de la cuenta
    retiro = int(input('Cuanto dinero quiere retirar?\n$'))
    if retiro > banco[user][1]:
        print('fondos insuficientes')
    else:
        banco[user][1] = banco[user][1]-retiro
        print('su nuevo saldo es: ',banco[user][1])

def ver_saldo():#funcion para ver el saldo en la cuenta
    print('su saldo es: ', banco[user][1])

def transferir():#funcion para transferir dinero a otra cuenta
    print('a que cuenta quiere transferir dinero?')


for i in range(c):
    user = input('ingrese su usuario: ')


    if user in banco:
        password = input('ingrese su contraseña: ')


        if password in banco[user]:
            print ('***Ingreso correctamente***')
            print('Su saldo es: ', banco[user][1])
            print('*****************************************************************')
            print('¿Qué deseas hacer?:\n'
            '1.Depositar\n'
            '2.Retirar\n'
            '3.Ver saldo\n'
            '4.Transferir\n'
            '5.Nada')

            opcion = int(input('Digita el numero de la opcion: '))
            if opcion == 1:
                depositar()
            if opcion == 2:
                retirar()
            if opcion == 3:
                ver_saldo()
            if opcion == 4:
                transferir()
            if opcion == 5:
                print('Gracias por usar nuestros servicios, hasta pronto.')
            break

        else:
            fallo = 2
            fallo = fallo - i
            print('usuario o contraseña incorrecto, intentos restantes:', fallo)
    else:
        fallo = 2
        fallo = fallo-i
        print('usuario o contraseña incorrecto, intentos restantes:',fallo)

#ponemos un comentario para probar