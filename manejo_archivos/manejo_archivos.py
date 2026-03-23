
# open(nombre, modo)

# R (read) Lectura
# W (write) Escritura
# X (Crea archivo nuevo)

try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
