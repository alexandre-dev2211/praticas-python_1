def calculadora_pintura():
    alt = int(input('Digite a Altura da Parede: '))
    comp = int(input('Digite o Comprimento da Parede: '))
    tinta = int(input('Digite o Rendimento da Tinta: '))

    area = alt * comp
    print('Essa é a Area A Ser Pintada: ', area)

    rend = area / tinta
    print('A Quantidade de Latas de Tinta Necessária é: ', rend)


calculadora_pintura()