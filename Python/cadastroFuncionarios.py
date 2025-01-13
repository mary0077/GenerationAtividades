# Exemplos de entradas para testes:

# funcionarios = [
# {"nome": "Alice", "idade": 30, "cargo": "Desenvolvedor", "salario": 3500},
# {"nome": "Bob", "idade": 40, "cargo": "Gerente", "salario": 5500},
# {"nome": "Carlos", "idade": 25, "cargo": "Desenvolvedor", "salario": 3200},
# ]


# Lista de funcionários
funcionarios = []

# Função para cadastrar um novo funcionário
def cadastrar_funcionario(nome, idade, cargo, salario):
    funcionario = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "salario": salario
    }
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso!")

# Função para exibir todos os funcionários
def listar_funcionarios():
    if funcionarios:
        for f in funcionarios:
            print(f"Nome: {f['nome']}, Idade: {f['idade']}, Cargo: {f['cargo']}, Salário: {f['salario']}")
    else:
        print("Nenhum funcionário cadastrado.")

# Função para calcular o salário médio
def salario_medio():
    if funcionarios:
        total_salarios = sum(f['salario'] for f in funcionarios)
        return total_salarios / len(funcionarios)
    return 0

# Função para filtrar funcionários por cargo
def filtrar_por_cargo(cargo):
    funcionarios_filtrados = [f for f in funcionarios if f['cargo'].lower() == cargo.lower()]
    if funcionarios_filtrados:
        for f in funcionarios_filtrados:
            print(f"Nome: {f['nome']}, Cargo: {f['cargo']}, Salário: {f['salario']}")
    else:
        print(f"Nenhum funcionário encontrado com o cargo {cargo}.")

# Função para remover um funcionário pelo nome
def remover_funcionario(nome):
    global funcionarios
    funcionarios = [f for f in funcionarios if f['nome'].lower() != nome.lower()]
    print(f"Funcionário {nome} removido com sucesso!")

# Exemplo de uso:
cadastrar_funcionario("Alice", 30, "Desenvolvedor", 3500)
cadastrar_funcionario("Bob", 40, "Gerente", 5500)
cadastrar_funcionario("Carlos", 25, "Desenvolvedor", 3200)

listar_funcionarios()
print(f"Salário médio: {salario_medio()}")

print("\nFiltrar por cargo 'Desenvolvedor':")
filtrar_por_cargo("Desenvolvedor")

remover_funcionario("Carlos")
listar_funcionarios()

