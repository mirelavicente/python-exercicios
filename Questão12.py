# Solicite o número de identificação, as notas e a média dos exercícios
numero_identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

# Calcule a média de aproveitamento
media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

# Determine o conceito com base na média de aproveitamento
if media_aproveitamento >= 90:
    conceito = "A"
elif 75 <= media_aproveitamento < 90:
    conceito = "B"
elif 60 <= media_aproveitamento < 75:
    conceito = "C"
elif 40 <= media_aproveitamento < 60:
    conceito = "D"
else:
    conceito = "E"

# Determinar se o aluno está aprovado ou reprovado
if conceito in ["A", "B", "C"]:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# Imprimir os resultados
print(f"Número de Identificação: {numero_identificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos Exercícios: {media_exercicios}")
print(f"Média de Aproveitamento: {media_aproveitamento:.2f}")
print(f"Conceito: {conceito}")
print(f"Resultado: {resultado}")