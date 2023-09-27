precoetiqueta = float(input("Digite o preço normal de etiqueta do produto: "))
condicaopagamento = int(input("Escolha a condição de pagamento (1, 2, 3 ou 4): "))

valorapagar = 0.0

if condicaopagamento == 1:
    valorapagar = precoetiqueta - (precoetiqueta * 0.10)
elif condicaopagamento == 2:
    valorapagar = precoetiqueta - (precoetiqueta * 0.15)
elif condicaopagamento == 3:
    valorapagar = precoetiqueta
elif condicaopagamento == 4:
    valorapagar = precoetiqueta + (precoetiqueta * 0.10)
else:
    print("Condição de pagamento inválida. Por favor, escolha entre 1, 2, 3 ou 4.")

if condicaopagamento in (1, 2, 3, 4):
    print(f"O valor a ser pago é: R${valorapagar:.2f}")
