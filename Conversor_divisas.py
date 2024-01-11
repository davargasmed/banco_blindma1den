"""def CLP():# peso chileno 0.0011 usd
    cambioUSD = monto * 0.0011

def ARS(): # peso argentino = 0.0012 usd
    cambioUSD = monto * 0.0012
def USD(): # dolar estadounidense = 1 usd
    cambioUSD = monto * 1
def EUR(): # euro = 1.09 usd
    cambioUSD = monto * 1.09
def TRY(): # Lira turca = 0.033 usd
    cambioUSD = monto * 0.033
def GBP(): # Libra esterlina = 1.27 usd
    cambioUSD = monto * 1.27
"""



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
