# Solicite o preço normal de etiqueta e a condição de pagamento
preco_etiqueta = float(input("Digite o preço normal de etiqueta do produto: "))
condicao_pagamento = int(input("Escolha a condição de pagamento (1, 2, 3 ou 4): "))

# Inicialize a variável que armazenará o valor a ser pago
valor_a_pagar = 0.0

# Verifique a condição de pagamento e calcule o valor apropriado
if condicao_pagamento == 1:
    valor_a_pagar = preco_etiqueta - (preco_etiqueta * 0.10)
elif condicao_pagamento == 2:
    valor_a_pagar = preco_etiqueta - (preco_etiqueta * 0.15)
elif condicao_pagamento == 3:
    valor_a_pagar = preco_etiqueta
elif condicao_pagamento == 4:
    valor_a_pagar = preco_etiqueta + (preco_etiqueta * 0.10)
else:
    print("Condição de pagamento inválida. Por favor, escolha entre 1, 2, 3 ou 4.")

# Imprima o valor a ser pago
if condicao_pagamento in (1, 2, 3, 4):
    print(f"O valor a ser pago é: R${valor_a_pagar:.2f}")