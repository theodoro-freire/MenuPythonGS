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
