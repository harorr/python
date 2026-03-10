
from math import sin, cos

#Define la funcion, halla la diferencia entre sen y cos
def sin_cos(angle):
    print(sin(angle) - cos(angle))

#Lee la entrada (el angulo en radianes como valor flotante)
angle = float(input())

#Llama la funciona para calcular e imprimir el resultado
sin_cos(angle)