nome = input("Digite o nome da pessoa: ")
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")

estadocivil = input("Digite o estado civil da pessoa (SOLTEIRO, CASADO, DIVORCIADO, VIÚVO): ")

if sexo.upper() == "F" and estadocivil.upper() == "CASADA":
    tempo_casada = input("Digite o tempo de casamento em anos: ")
    print(f"{nome} é uma mulher casada há {tempo_casada} anos.")
else:
    print(f"{nome} não atende aos critérios de sexo feminino e estado civil casada.")