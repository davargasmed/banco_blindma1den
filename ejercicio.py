horas =int(input('introduzca las horas:'))
tarifa = int(input('introduzca la tarifa por hora:'))
salario = 0
if horas > 40:
    extra = horas-40
    ntarifa = tarifa*1.5
    salario = (40*tarifa)+(extra*ntarifa)
    print(f'su salario es {salario}')
else:
    salario = horas * tarifa
    print(f'su salario es {salario}')