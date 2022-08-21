def processar_resposta(resposta,nome):
    if resposta == '1':
        print("{},O russo Yuri Gagarin (1934-1968) foi a primeira pessoa a viajar para o espaço, o que aconteceu em 12 de abril de 1961.".format(nome))
    elif resposta == '2':
        print("{},O Monte Everest tem 8.848 metros de altitude e localiza-se no Nepal, um país asiático que faz fronteira com a China e com a Índia.".format(nome))
    elif resposta == '3':
        print("{},O corpo humano tem 206 ossos: 22 na cabeça, 1 no pescoço, 6 no ouvido, 44 no tórax, 7 no abdômen, 62 nos membros inferiores e 64 nos membros inferiores.".format(nome))
    elif resposta == '4':
        print("{},Chove muito em Belém, porque a cidade é quente e muita úmida. A chuva costuma cair todos os dias quase à mesma hora depois do horário mais quente. Assim, é comum as pessoas combinarem coisas pensando na chuva (Você vai antes ou depois da chuva?).".format(nome))
    elif resposta == '5':
        print("{},Mais pesado é essa barra que é gostar de você <3".format(nome))
    else:
        print('Digite apenas 1,2,3,4 ou 5')
        return True
    
    continua = input("Você deseja continuar? s/n \n")
    if continua == "s" or continua == "S":
        return True
    elif continua == "n" or continua == "N":
        return False
    
    else:
        while(continua != "s" or continua != "S" or continua != "n" or continua !="N"):
            
            continua = input("Você deseja continuar? s/n \n")
            if continua == "s" or continua == "S":
                return True 
            elif continua == "n" or continua == "N":
                return False


def start():
    var = True
    # Apresentar o chatbot
    print("Olá seja bem vindo ao meu botcurioso!")
    # Pedir o nome
    nome = input("Digite seu nome: ")
    # Oferecer o menu de opções
    while(var != False):
        resposta = input("""O que gostaria de saber hoje?
[1] - Quem foi a primeira pessoa a viajar no Espaço?
[2] - Qual a montanha mais alta do mundo? 
[3] - Quantos ossos temos no nosso corpo?
[4] - Que cidade brasileira é conhecida por chover todos os dias quase à mesma hora?
[5] - O que é mais pesado: 1 quilo de algodão ou 1 quilo de ferro?
""")

    # Processar a resposta enviada

        var = processar_resposta(resposta,nome)




if __name__== '__main__':
    start()