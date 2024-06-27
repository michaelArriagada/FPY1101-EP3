os import


def regristro():
    try:
        nombre = input("ingrese el titulo: ")
        autor = input("ingrese el autor: ")
        Ano_de_Publicación =float(input("ingrese el Año de Publicación:"))
        if nombre == or "" autor or "" Ano_de_Publicación <=0
            titulo = {
                'nombre':titulo
                'autor': autor 
                'Ano_de_Publicacin':Ano_de_Publicación
            }
            nombre.append(titulo)
            print("registro se realizo correctamente")



def lista():
print ("nombre\t\tautor\t\tAno_de_Publicación\n")
for nombre in titulo:
    print(f"{nombre[titulo]}\t\t{nombre[autor]}\t\t{Ano_de_Publicación}\n")


def imprimir():
    try:
        op int(input("Imprimir reporte de préstamos"))
        if op = 1:
while open ('Imprimir reporte de préstamos'txt,'w') as archivo:
archivo.write("titulo\t\tautor\t\tAno_de_Publicación")


def menu():
    while True:
        try:
            print("* * * M e N U * * *")
            print("1.regristar libro\n2.Prestar libro\n3.Listar todos los libros\n4Imprimir reporte de préstamos\n5.Salir del Programa")
           op = int(input("ingrese una opcion:"))
        except ValueError:

if op == 1:
    regristro()
elif op == 2:
    lista()
elif op == 3:
    imprimir()
elif op == 4:
    print("finalizando el programa")
    break
except ValueError:
print("la opcion ingresada no es valido, intente nuevamente ")
