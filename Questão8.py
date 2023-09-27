a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
c = int(input("Digite o terceiro valor inteiro: "))

if a != b != c != a:
    maxvalue = max(a, b, c)
    minvalue = min(a, b, c)
    middlevalue = (a + b + c) - maxvalue - minvalue
    
    print("Valores em ordem decrescente:", maxvalue, middlevalue, minvalue)
else:
    print("Os valores inseridos não são diferentes.")
