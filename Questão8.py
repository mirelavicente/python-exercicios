# Solicite três valores inteiros diferentes ao usuário
a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
c = int(input("Digite o terceiro valor inteiro: "))

# Verifique se os valores são diferentes
if a != b != c != a:
    # Encontre o valor máximo
    max_value = max(a, b, c)
    # Encontre o valor mínimo
    min_value = min(a, b, c)
    # Calcule o valor do meio
    middle_value = (a + b + c) - max_value - min_value

    # Imprima os valores em ordem decrescente
    print("Valores em ordem decrescente:", max_value, middle_value, min_value)
else:
    print("Os valores inseridos não são diferentes.")