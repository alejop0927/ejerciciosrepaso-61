
def cambio_temperatura(F):
   C=(F-32)*5/9
   return C

F = float(input("ingrese grados fahrenheit"))
C=cambio_temperatura(F)

print("el cambio de temperatura es "+str(C))

