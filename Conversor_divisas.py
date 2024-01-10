#def CLP(): #peso chileno

#def ARS(): #peso argentino

#def USD(): #dolar estadounidense

#def EUR(): #euro

#def TRY(): # Lira turca

#def GBP(): #Libra esterlina

control = True

while control:

    print('bienvenido a su conversor de divisas\n'  
          '1.CLP (Peso Chileno)\n'
          '2.ARS (Peso Argentino)\n'
          '3.USD (Dolar Estadounidense)\n'
          '4.EUR (Euro)\n'
          '5.TRY (Lira Turca)\n'
          '6.GBP (Libra Esterlina)\n'
          )
    div_inicial = int(input('escoja por favor el numero de su divisa inicial: '))
    div_final = int(input('escoja por favor el numero de su divisa a convertir: '))
    monto = int(input('Cuanto dinero quiere cambiar?----->'))


    control = False
