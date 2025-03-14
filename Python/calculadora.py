# Função para realizar as operações
def calcular(operacao, num1, num2):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: divisão por zero!"
        return num1 / num2
    else:
        return "Operação inválida!"

# Menu de opções
print("Escolha a operação:")
print("+ para soma")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")

# Entrada do usuário
operacao = input("Digite a operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe o resultado
resultado = calcular(operacao, num1, num2)
print(f"Resultado: {resultado}")
