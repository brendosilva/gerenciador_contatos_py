import agenda

while True:
    print("---AGENDA TELEFONICA---")
    print("1 - Adicionar contato")
    print("2 - Visualizar contatos")
    print("3 - editar contato ")
    print("4 - marcar/desmarca contato favorito")
    print("5 - Visualizar contatos favoritos")
    print("6 - Remover contato")
    print("7 - Para sair")

    resposta = input("Digite a opção desejada: ")

    if (resposta == "1"):
        print ("Ok vamos adicionar novo contato")
        nome =  input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")        
        favorito = input("Deseja incluir na lista de favoritos [sim/não] ")  

        resultado = agenda.adicionar(nome, telefone, email, favorito )
        print(resultado)
    
    elif (resposta == "2"):
        agenda.visualizar()

    elif (resposta == "3"):
        print("Ok vamos editar um contato: ")
        indice = input("Qual contato deseja alterar, coloque o indice: ")
        novo_nome = input("Digite novo nome: ")
        novo_email = input("Digite novo email: ")
        novo_telefone = input("Digite novo telefone: ")
        agenda.editar(indice, novo_nome, novo_telefone, novo_email)
    
    elif (resposta == "4"):
        print("--- marcar/desmarca contato favorito ---")
        agenda.visualizar()
        indice = input("Digite o indice do contato: ")
        agenda.favorito(indice)
        
    
    elif (resposta == "5"):
        agenda.visualizar_contatos_favoritos()
    
    elif (resposta == "6"):
        indice = input("Digite o indice do contato a ser removido: ")
        agenda.revomer(indice)
        
    elif (resposta == "7"):
        break


