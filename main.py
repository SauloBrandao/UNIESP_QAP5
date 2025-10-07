import imc

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o sua altura: "))

resultado = imc.imc(peso, altura)

print(f"Seu imc é: {resultado}")