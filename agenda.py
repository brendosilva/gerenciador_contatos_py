contatos = []
favoritos = []



def adicionar (nome, telefone,email, favorito):

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    
    if (favorito.lower() == "sim"):
        contato["favorito"] = True
        print("Salvo como favorito")
        favoritos.append(contato)

    contatos.append(contato)
    return f"Contato {nome} foi salvo com sucesso"


def editar(indice, novo_nome, novo_telefone, novo_email):
    novo_indice = int(indice) - 1
    if (novo_indice >= 0 and novo_indice < len(contatos)):
        contatos[novo_indice]["nome"] = novo_nome
        contatos[novo_indice]["telefone"] = novo_telefone
        contatos[novo_indice]["email"] = novo_email
    else:
        print("indice contato invalido")

    
    contato_encontrado = []
    for indice, contato in enumerate(contatos,start=1):
        if (indice == novo_indice):
            contato_encontrado = contato

    for indice, favorito in enumerate(favoritos,start=1):
        if (indice == novo_indice):
            favorito = contato_encontrado    
    return 
            


def revomer (indice):
    novo_indice = int(indice) - 1
    removido = contatos.pop(novo_indice)
    
    for indice, favorito in enumerate(favoritos):
        if (indice == novo_indice):
            favoritos.remove(favorito)
    
    print(f"Contato: {removido['nome']}  removido com sucesso!")
    return 

def visualizar ():
    print("--- EXIBINDO SEUS CONTATOS ---")
    for indice, contato in enumerate(contatos, start=1):
        favorito_status = " ♥ " if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]

        print(f"{indice}. [{favorito_status}] - {nome} - {telefone} - {email}")
    return

def favorito (indice):    
    novo_indice = int(indice) - 1

    contato_encontrado = []
    for indice, contato in enumerate(contatos):
        if (indice == novo_indice):
            contato_encontrado = contato


    if (contatos[novo_indice]["favorito"] == False):
        contatos[novo_indice]["favorito"] = True    
        
        if (contato_encontrado["favorito"] == True) :
            favoritos.append(contato_encontrado)
            print("Contato favoritado com sucesso")

    elif (contato_encontrado["favorito"] == True):
        contatos[novo_indice]["favorito"] = False 
        
        if (contato_encontrado["favorito"] == False) :
            favoritos.remove(contato_encontrado)
            print("Contato removido dos favoritos com sucesso")


def visualizar_contatos_favoritos():
    print("--- EXIBINDO SEUS CONTATOS FAVORITOS ---")
    for indice, favorito in enumerate(favoritos, start=1):
        nome = favorito["nome"]
        telefone = favorito["telefone"]
        email = favorito["email"]
        print(f"{indice}. {nome} -  {telefone} - {email}")