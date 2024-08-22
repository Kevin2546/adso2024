#Pedir 3 numeros e indicar cual de ellos es el valor del medio
print ("Aqui podras calcular el valor de el medio ingrese tres digitos ")
digt1= int(input("Ingrese el primer digito "))
digt2= int(input("Ingrese el segundo digito "))
digt3= int(input("Ingrese el tercer digito "))

if digt1 != digt2 != digt3:
    if digt1 > digt2 > digt3: 
        print (f'el numero de el medio es {digt1}')
    if digt1 < digt2 < digt3:
        print (f'El numero de el medio es {digt2}')
    if digt1 < digt2 > digt3:
        print (f'El numero de el medio es {digt1}')
    if digt1 > digt2 > digt3:
        print(f'el numero de el medio es {digt2}')

else:
    print("Los digitos ingresados no son diferentes porfavor hagalo nuevamente ") 