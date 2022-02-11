palabra=input("Ingrese una palabra: ")
Index=len(palabra)-1
nuevapalabra=""
while Index>=0:
    nuevapalabra=nuevapalabra+palabra[Index]
    Index=Index-1

if palabra == nuevapalabra:
   print ("SI ES PALINDROMO")
else:
   print("NO ES PALINDROMO")
