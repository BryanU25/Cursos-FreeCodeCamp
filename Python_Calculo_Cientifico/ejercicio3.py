def pago(horas,pago_h):
    print ("Se ingreso: ",horas," Horas y $",pago_h," por horas")
    if fh>40.0:
        print("Tiempo extra")
        Salario=fp*fh
        Salario_Ex=(fh-40.0)*(fp*0.5)
        Salario_Fi=Salario+Salario_Ex
    else:
        print("Tiempo regular")
        Salario_Fi=fp*fh
    print ("Retornando... ",Salario_Fi)
    return Salario_Fi


eh=input("Ingresa Horas De Trabajo: ")
ep=input("Ingresa Pago Por Horas: ")
try:
    fh=float(eh)
    fp=float(ep)
except:
    print ("Error, ingresa una entrada numerica")
    quit()

Pago=pago(fh,fp)
print("Se debe pagar: ",Pago)