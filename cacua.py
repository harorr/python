import math
def calculo_octaedro ():
    try:
        borde = int( input( "digite el valor del lado del octaedro: ") )
        area = calcularAreaOctaedro(borde)
        volumen = calcularVolumenOctaedro(borde)
        print(round(area, 2), " ", round(volumen, 2))
    except ValueError:
        print("dígite un número entero por favor")

def calcularAreaOctaedro (borde):
    return 2 * math.sqrt(3) * math.pow(borde, 2)

def calcularVolumenOctaedro (borde):
    return 1/3 * math.sqrt(2) * math.pow(borde, 3)

calculo_octaedro()