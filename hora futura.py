horaActual = int(input("Introdusca la hora actual : "))
numeroHoras =int(input("Ingrese la cantidad de horas : "))
proximaHora = (horaActual + numeroHoras ) % 24
print("en " , numeroHoras ,"horas el reloj marcara las : ",proximaHora  )