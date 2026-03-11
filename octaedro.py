
#Importar librerias
import math

#Definir la variable para que acepte input de enteros
edge_lenght = int(input())

#Definir la funcion para calcular area y volumen, luego los redondea a dos decimales y los separa con un espacio
def octahedron_area_vol(edge_lenght):
    area = 2 * math.sqrt(3) * math.pow(edge_lenght, 2)
    volume = 1/3 * math.sqrt(2) * math.pow(edge_lenght, 3)
    print(round(area, 2), round(volume, 2), sep = " ")

#Llama la funcion
octahedron_area_vol(edge_lenght)
    





