nota1 = int(input("Ingrese la nota del primer certamen: "))
nota2 = int(input("Ingrese la nota del segundo certamen: "))
laboratorio = float(input("Ingrese la nota del laboratorio: "))
promedioRamo = (nota1 + nota2)/2
notaFinal = (60 - (promedioRamo * 0.7)) /  0.3
print("Nececita " , notaFinal,"en la nota del tercer certamen.")
