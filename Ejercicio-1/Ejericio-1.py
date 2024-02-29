# Programa que lea las coordenadas cartesianas (x, y) de un punto en el plano y calcule el cuadrante al cual pertenece el punto.

# input

X = int(input("ingrese la coordenada X: "))
Y = int(input("ingrese la coordenada Y: "))

# Proccessing
if X == 0:
    if Y == 0:
        print("la coordenada" ,(X,Y),"esta en el origen")
    else:
        print("la coordenada" ,(X,Y),"esta en el eje Y")
elif Y == 0:
    print("la coordenada" ,(X,Y),"esta en el eje X") 
elif X > 0:
    if Y > 0:
     print("la coordenada" ,(X,Y),"esta en el cuadrante 1")
    else:
     print("la coordenada" ,(X,Y), "esta en el cuadrante 4")
elif Y < 0:
    print("la coordenada" ,(X,Y),"esta en el cuadrante 3")
else:
    print("la coordenada" ,(X,Y),"esta en el cuadrante 2")


    



