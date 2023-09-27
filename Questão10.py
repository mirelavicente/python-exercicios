# Solicite o peso em quilogramas e a altura em metros
peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

# Calcule o IMC
imc = peso / (altura ** 2)

# Determine a condição de peso com base no IMC
if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "Peso normal"
elif 25 <= imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"

# Imprima a condição de peso
print(f"O IMC é {imc:.2f} e a condição é: {condicao}")