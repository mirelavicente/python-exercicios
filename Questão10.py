peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "Peso normal"
elif 25 <= imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"

print(f"O IMC é {imc:.2f} e a condição é: {condicao}")
