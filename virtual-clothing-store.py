import time
#Menu#
#FUNÇAO---------------------------------------
def Abrir_Loja(Item):
    print("👕​-----LOJA DE ROUPAS------​🛒​")
    print("Observe o estoque da loja, mas infelismente, nao sera possivel comprar")
    time.sleep(1)
    print("​👖​calça jeans: 200R$")
    time.sleep(1)
    print("2 ​👚​Camisas Simples: 50R$")
    time.sleep(1)
    print("​🧢​Boné azul: 30R$")
    time.sleep(1)
    print("​👟​Tenis nike: 120R$")
    Fechar = input("Aperte 1 para voltar ao menu: ")
    if Fechar == ("1"):
        return
#FUNÇAO---------------------------------------
Rodar = True
while Rodar:   
        
    print("1- Para Abrir a loja")
    print("2- Para Fechar o sistema")
    Escolha = input("Selecione: ")  
    if Escolha == "1":
        print("​​⌛​abrindo, aguarde....")
        time.sleep(4)
        Abrir_Loja(Escolha)
    else:
        print("​​⌛​fechando....")
        time.sleep(4)
        print("​​​✅​Sistema fechado Com sucesso!")
        
        break
