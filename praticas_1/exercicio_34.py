def termometro():
    user = int(input('Digite a temperatura da Carne: '))
    if user <= 0:
        print('Temperatura Inválida!')
    elif user <= 47:
        print('Cozinhar Mais!')
    elif user == 48:
        print('Selada!')
    elif user == 54:
        print('Ao ponto Para o Mal!')
    elif user == 60:
        print('Ao Ponto!')
    elif user == 65:
        print('Ao Ponto Para o Bem!')
    elif user == 71:
        print('Bem Passada!')
    elif user > 71:
        print('Passou do Ponto!')


print(termometro())
