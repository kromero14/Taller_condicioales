# input
salario_emp=int(input("digite el salario de el empleado: "))
deudas=input("El empleado tiene deudas: si,no:")

#Processing

if salario_emp >=945200:
    if deudas=="no":
        rta=" APROBADO "
    else:
        rta=" RECHAZADO "
else:
    rta="RECHAZADO"

# output
print("su prestamo ha sido " + rta)