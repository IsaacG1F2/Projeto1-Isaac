print("Digite a sua idade abaixo:")
idade = int(input("(>)"))
if idade <= 10 and idade > 0:
    print("Você é uma criança!")
elif idade > 10 and idade < 18:
    print("Você é um adolescente!")
elif idade > 18 and idade < 60:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")
    