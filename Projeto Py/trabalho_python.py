variavel = '222'
endereço = ("Resultado da busca: ")
dic = {}
nome_das_chaves = {}
while variavel != '0':
    print ("0-Sair")
    print ("1-Fazer um dicionario")
    print ("2-Nome das chaves: ")
    print ("3-Procurar dicionario por chave: ")
    print ("4-imprimir dicionario(s)")
    variavel = input("Escolha uma opção: ")
    if variavel == "0":
        print("Saindo")
    elif variavel == "1":
     nome_das_chaves = input("Nome do seu dicionario: ")
     Mac = input("Digite seu endereço Mac: ")
     Nome = input("Digite o nome do dispositivo movel: ")
     Data = input("Digite a data: ")
     Hora = input("Digite a hora: ")
     Latitude = input("Digite a latitude: ")
     Longitude = input("Digite a longitude: ")
    elif variavel == "2":
       print (nome_das_chaves)
    elif variavel =="4":
     nome_das_chaves
     print (nome_das_chaves)
    else:
       print("Essa opção não esta disponivel")
