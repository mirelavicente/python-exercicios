altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

if sexo.upper() == "M":
    pesoideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de {altura} metros é {pesoideal:.2f} kg.")
elif sexo.upper() == "F":
    pesoideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de {altura} metros é {pesoideal:.2f} kg.")
else:
    print("Sexo não reconhecido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
