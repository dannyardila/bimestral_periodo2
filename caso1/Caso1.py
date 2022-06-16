print("--------------------------------")
print("------ NOTAS ESTUDIANTES -------")
print("--------------------------------")

#Entrada
cod = int(input("Digite el código del estudiante: "))
if cod!=0:
         nota1 = float(input("Digite la nota del parcial no. 1:"))
         nota2 = float(input("Digite la nota del parcial no. 2:"))
         nota3 = float(input("Digite la nota del parcial no. 3:"))
         nota4 = float(input("Digite la nota del parcial no. 4:"))
         nota5 = float(input("Digite la nota del parcial no. 5:"))

else:
     print("Fin de los datos de entrada")

#Procesamiento

reprobados = 0

while cod != 0:
    nota_final = (nota1 + nota2 + nota3 + nota4 + nota5)/(5)
    print("El estudiante de código " + str(cod) + " obtuvo una nota definitiva de " + str(nota_final))
    cod=0


if nota_final <3:
    reprobados=reprobados+1


# Entrada

cod = int(input("Digite el código del estudiante: "))
if cod!=0:
         nota1 = float(input("Digite la nota del parcial no. 1:"))
         nota2 = float(input("Digite la nota del parcial no. 2:"))
         nota3 = float(input("Digite la nota del parcial no. 3:"))
         nota4 = float(input("Digite la nota del parcial no. 4:"))
         nota5 = float(input("Digite la nota del parcial no. 5:"))

while cod != 0:
     nota_final = (nota1 + nota2 + nota3 + nota4 + nota5)/ (5)
     print("El estudiante de código " + str(cod) + " obtuvo una nota definitiva de " + str(nota_final))
     cod=0


if nota_final <3:
    reprobados=reprobados+1


#Salida

print("Cantidad de estudiantes que reprobaron la materia: " + str(reprobados))
print("Eso era...") 
print("Fin de los datos de entrada")