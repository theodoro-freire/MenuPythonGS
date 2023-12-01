# Lista para armazenar cadastros
cadastros = []

# Explicação sobre nossa equipe e solução.
def exibir_equipe_e_solucao():
    print("\nEquipe:\n Gustavo Rocha Caxias - RM: 553310 \n Matheus Tenreiro Rodrigues - RM: 553734 \n Theodoro Freire de Lima - RM: 552903\n")
    print("\nSolução:\n Apresentamos uma solução inovadora de monitoramento de saúde, simplificando o processo para os usuários. Ao inserirem informações vitais, como batimentos cardíacos e pressão arterial, nosso sistema oferece recomendações instantâneas para consultas e exames. Focamos na prevenção, identificando precocemente problemas de saúde, o que não apenas melhora as chances de tratamento eficaz, mas também reduz os custos associados a intervenções médicas complexas. Nossa abordagem eficiente e preventiva se traduz em economia de dinheiro a longo prazo, promovendo uma vida saudável de forma acessível. Estamos comprometidos em simplificar e fortalecer a jornada de cuidados com a saúde.")
    input("\nPressione Enter para voltar ao menu principal.")

# Menu secundário de cadastro
def cadastrar_atualizar_excluir_ver(cadastros, nome, idade, email, senha):
    while True:
        print("\nMenu de Cadastro:")
        print("1. Cadastrar")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Ver Cadastro")
        print("0. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("\nDigite seu nome: ")
            idade = input("\nDigite sua idade: ")
            email = input("\nDigite seu email: ")
            senha = input("\nDigite sua senha: ")
            cadastrar(cadastros, nome, idade, email, senha)
        elif opcao == "2":
            atualizar(cadastros)
        elif opcao == "3":
            excluir(cadastros)
        elif opcao == "4":
            ver_cadastro(cadastros)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar(cadastros, nome, idade, email, senha):
    # Adiciona as informações à lista de cadastros
    cadastros.append({"nome": nome, "idade": idade, "email": email, "senha": senha})
    print("Cadastro realizado com sucesso!")

def atualizar(cadastros):
    print("\nAtualização de Cadastro:")
    email_atualizar = input("\nDigite o email do cadastro a ser atualizado (ou digite 0 para sair): ")

    if email_atualizar == "0":
        return

    # Procura o cadastro na lista e atualiza as informações
    for cadastro in cadastros:
        if cadastro["email"] == email_atualizar:
            cadastro["idade"] = input("Digite a nova idade: ")
            cadastro["senha"] = input("Digite a nova senha: ")
            print("Cadastro atualizado com sucesso!")
            return  # Adiciona um return para sair da função após a atualização

    # Se o email não for encontrado
    print("Cadastro não encontrado.")

def excluir(cadastros):
    print("\nExclusão de Cadastro:")
    email_excluir = input("Digite o email do cadastro a ser excluído (ou digite 0 para sair): ")

    if email_excluir == "0":
        return

    # Remove o cadastro da lista
    for cadastro in cadastros:
        if cadastro["email"] == email_excluir:
            cadastros.remove(cadastro)
            print("Cadastro excluído com sucesso!")
            return  # Adiciona um return para sair da função após a exclusão

    # Se o email não for encontrado
    print("Cadastro não encontrado.")

def ver_cadastro(cadastros):
    print("\nConsulta de Cadastro:")
    email_consulta = input("Digite o email do cadastro a ser consultado (ou digite 0 para sair): ")

    if email_consulta == "0":
        return

    # Exibe as informações do cadastro
    for cadastro in cadastros:
        if cadastro["email"] == email_consulta:
            print(f"Nome: {cadastro['nome']}, Idade: {cadastro['idade']}, Email: {cadastro['email']}")
            return  # Adiciona um return para sair da função após a consulta

    # Se o email não for encontrado
    print("\nCadastro não encontrado.")

def verificar_dados(batimentos, saturacao, freq_respiratoria, pressao):
    print("\nResultado:")

    if batimentos > 100:
        print("\nBatimentos altos! Risco de taquicardia.")
    elif batimentos < 50:
        print("\nBatimentos baixos! Risco de bradicardia.")

    if saturacao < 90:
        print("\nSaturação baixa! Possível falta de oxigênio.")

    if freq_respiratoria < 12:
        print("\nFrequência respiratória baixa! Risco de bradipneia.")
    elif freq_respiratoria > 20:
        print("\nFrequência respiratória alta! Risco de taquipneia.")

    if pressao > 140:
        print("\nPressão alta!")
    elif pressao < 90:
        print("\nPressão baixa!")

    if 50 <= batimentos <= 100 and saturacao >= 90 and 12 <= freq_respiratoria <= 20 and 90 <= pressao <= 140:
        print("\nTudo está bem!")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Equipe e nossa solução")
        print("2. Cadastro")
        print("3. Avaliar saúde")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_equipe_e_solucao()
        elif opcao == "2":
            nome = input("\nDigite seu nome: ")
            idade = input("\nDigite sua idade: ")
            email = input("\nDigite seu email: ")
            senha = input("\nDigite sua senha: ")
            cadastrar(cadastros, nome, idade, email, senha)
            cadastrar_atualizar_excluir_ver(cadastros, nome, idade, email, senha)
        elif opcao == "3":
            batimentos = int(input("\nDigite os batimentos por minuto: "))
            saturacao = int(input("\nDigite a saturação: "))
            freq_respiratoria = int(input("\nDigite a frequência respiratória: "))
            pressao = int(input("\nDigite a pressão: "))
            verificar_dados(batimentos, saturacao, freq_respiratoria, pressao)
        elif opcao == "0":
            print("\nObrigado por usar o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
