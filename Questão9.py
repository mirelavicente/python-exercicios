# Solicite a altura e o sexo da pessoa
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

# Verifique o sexo e calcule o peso ideal de acordo com a fórmula correspondente
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de {altura} metros é {peso_ideal:.2f} kg.")
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de {altura} metros é {peso_ideal:.2f} kg.")
else:
    print("Sexo não reconhecido. Por favor, digite 'M' para masculino ou 'F' para feminino.")