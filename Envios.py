"""Cree un sistema de envío en línea con las siguientes características:

1. El sistema tiene un inicio de sesión que se bloquea después del tercer intento fallido.
2. Mostrar un menú que permite: Enviar un paquete, salir del sistema.
3. Para enviar un paquete, se requieren los datos del remitente y del destinatario.
4. El sistema asigna un número de paquete aleatorio a cada paquete enviado.
5. El sistema calcula el precio de envío. $2 por kg.
6. El usuario debe ingresar el peso total de su paquete y el sistema debe mostrar el monto a pagar.
7. El sistema debería preguntar si el usuario desea realizar otra operación. Si la respuesta es sí,
   debería volver al menú principal. Si es no, debería cerrar el sistema."""

users = {
    'david22': 'miclave',
    'carlos53' : 'suclave'}

def login():
    for i in range(3):
        usuario = input('ingrese su usuario: ')
        password = input('ingrese su contraseña: ')
        if usuario in users and password == users[usuario]:
            print('accediste correctamente')
            return True
            break
        elif i<2:
            print('usuario o contraseña incorrecto ingrese de nuevo.')
        else:
            print("ingresaste mal tu usuario o contraseña en 3 oportunidades, el programa se cerrara.")
            return False

def cliente():
    remitente = dict()
    destinatario = dict()
    print('Por favor llene el siguiente formulario:')
    remitente['nombre'] = input('ingrese el nombre del remitente--->')
    remitente['telefono'] = int(input('Ingrese el numero de telefono del remitente--->'))
    remitente['direccion'] = input('Ingrese la direccion del remitente--->')
    print(f'los datos del remitente son:\n'
          f'Nombre---> {remitente['nombre']}\n'
          f'Telefono---> {remitente['telefono']}\n'
          f'Direccion---> {remitente['direccion']}\n')

def menu():
    print('****Bienvenido a nuestra empresa de envios****\n'
          '****Que desea hacer?****\n'
          '1. Enviar paquete\n'
          '2. Salir\n')
    opcion = int(input('Escriba el numero de la opcion que quiere realizar:'))
    if opcion == 1:
        cliente()
    else:
        print('gracias esperamos que vuelva pronto')

login()
menu()
