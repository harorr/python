
word = str(input('Escriba la palabra que desea: '))

def calcular_longitud(word):
    word_lenght = len(word)
    print(f'{word} tiene {word_lenght} letras')

calcular_longitud(word)