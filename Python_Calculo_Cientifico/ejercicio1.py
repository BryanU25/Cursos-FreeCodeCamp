eh=input("Ingresa Horas De Trabajo: ")
ep=input("Ingresa Pago Por Horas: ")
fh=float(eh)
fp=float(ep)

if fh>40.0:
    print("Tiempo extra")
    Salario=fp*fh
    Salario_Ex=(fh-40.0)*(fp*0.5)
    Salario_Fi=Salario+Salario_Ex
else:
    print("Tiempo regular")
    Salario_Fi=fp*fh
print("Se debe pagar: ",Salario_Fi)
