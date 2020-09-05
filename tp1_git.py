# Para tributar un determinado impuesto se debe ser mayor de 16 años 
# y tener unos ingresos iguales o superiores a $ 90000 mensuales. 
# El numero que pagará sera un 10% de sus ingresos, pero si la persona es mayor de 40 años, pagara un 5%
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
# y muestre por pantalla si el usuario tiene que tributar o no. De tener que pagar calcular y mostrar el monto.


cliente=0
ingresos=0
edad=0
impuesto=0

print("Bienvenido al sistema tributario Rosarino")

cliente=int(input("Para consultar si ustede debe tributar o no, presione cualquier numero mayor a 0"))
while cliente>0:
    edad=int(input("Ingrese su edad"))
    ingresos=float(input("Ingrese sus ingresos mensuales"))
    if edad>16:
        if edad<40:
            impuesto= ingresos*10/100
            print ("Usted debe pagar de impuesto a los ingresos: $ ",impuesto)
        else:
            impuesto= ingresos*5/100
            print ("Usted debe pagar de impuesto a los ingresos: $ ",impuesto)