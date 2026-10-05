nombre = input("¿Cual es tu nombre?")
edad = int (input("¿Cuántos años tienes?"))
nacionalidad = input ("¿Eres español? (si/no): ")

if edad > 18 and nacionalidad == "si":  
    print("Hola", nombre, "puedes votar")

else:
    print("Lo siento", nombre, "no puedes votar")

print("Gracias por usar el programa")

