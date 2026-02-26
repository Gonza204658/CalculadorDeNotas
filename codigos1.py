#Calculador de notas

notas = []
print("Ingresa tus notas una por una. Escribe 0 cuando hayas terminado.")

while True:
    try:
        entrada = float(input("Ingresa tu nota: "))
        
        if entrada == 0:
            break
        
        notas.append(entrada)
    except ValueError:
        print("Por favor, ingresa solo números válidos.")

if notas:
    promedio = sum(notas) / len(notas)
    print("\nNotas ingresadas:", notas)
    print(f"Promedio: {round(promedio,2)}")
else:
    print("No ingresaste ninguna nota.")