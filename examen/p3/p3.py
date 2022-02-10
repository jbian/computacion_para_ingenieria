# Dado el archivo estudiantes.txt y notas.txt unir en un solo archivo llamado primer_parcial.txt que contendra los nombre seguido de su nota
notas = open('notas.txt', 'r+')
alumnos = open('estudiantes.txt', 'r+')
salida = open('primer_parcial.txt', 'w+')

lineasNotas = notas.readlines()

for nota in lineasNotas:
    estudiante=alumnos.readline()
    salida.write(nota +' '+ estudiante)

alumnos.close()
notas.close()
salida.close()