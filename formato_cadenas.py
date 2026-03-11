
#Variable para escribir la palabra en tipo cadena.
word = str(input('Write your desired word: '))

#Funcion para contar las letras de la palabra y luego concatenarlas en el print.
def calculate_lenght(word):
    word_lenght = len(word)
    print(f'{word} has {word_lenght} letters')

#LLama la funcion
calculate_lenght(word)

