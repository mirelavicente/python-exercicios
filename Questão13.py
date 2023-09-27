def calcular_imposto_de_renda(salario):
    if salario <= 1903.98:
        imposto_renda = 0
    elif salario <= 2826.65:
        imposto_renda = salario * 0.075 - 142.8
    elif salario <= 3751.05:
        imposto_renda = salario * 0.15 - 354.8
    elif salario <= 4664.68:
        imposto_renda = salario * 0.225 - 636.13
    else:
        imposto_renda = salario * 0.275 - 869.36
    
    return imposto_renda

salario = float(input("Digite o valor do salário: "))
imposto = calcular_imposto_de_renda(salario)

print(f"O imposto de renda a ser pago é R${imposto:.2f}")
print('Salário líquido após dedução do Imposto de Renda:', salario - imposto)