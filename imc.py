peso = float (input("Introduce tu peso"))
altura = float (input ("Introduce tu altura"))

imc = peso/(altura*altura)



if imc<18.5 :
    print("Bajo peso")

else if imc<25:
    print("Normal")

    else:
        print("Obeso")