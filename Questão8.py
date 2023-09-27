a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
c = int(input("Digite o terceiro valor inteiro: "))

if a != b != c != a:
    max_value = max(a, b, c)
    min_value = min(a, b, c)
    middle_value = (a + b + c) - max_value - min_value
    
    print("Valores em ordem decrescente:", max_value, middle_value, min_value)
else:
    print("Os valores inseridos não são diferentes.")
