numeroidentificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
mediaexercicios = float(input("Digite a média dos exercícios: "))

mediaaproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + mediaexercicios) / 7

if mediaaproveitamento >= 90:
    conceito = "A"
elif 75 <= mediaaproveitamento < 90:
    conceito = "B"
elif 60 <= mediaaproveitamento < 75:
    conceito = "C"
elif 40 <= mediaaproveitamento < 60:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Número de Identificação: {numeroidentificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos Exercícios: {media_exercicios}")
print(f"Média de Aproveitamento: {media_aproveitamento:.2f}")
print(f"Conceito: {conceito}")
print(f"Resultado: {resultado}")
