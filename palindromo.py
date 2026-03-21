
palindromo = str(input("Escribe una palabra: ")).replace(" ", "",)

print(palindromo)

if palindromo[:] == palindromo[::-1]: 
    print("La palabra que ingresaste es un palindromo.")
else: print("Esta palabra no es un palindromo")


txt = " Hello World "
x = txt.strip()
print(x)