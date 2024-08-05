dicionario={}

def adicionar_contato(nome,telefone,email):
    dicionario[nome]={'telefone':telefone,
                      'email':email}
    print(dicionario)

nome=input('digite o nome do contato: ')
telefone=str(input('digite o numero de telefone: '))
email=str(input('digite o endereço de email: '))
adicionar_contato(nome,telefone,email)