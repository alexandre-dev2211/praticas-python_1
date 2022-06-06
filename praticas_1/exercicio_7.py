alt = float(input('Digite Sua Altura: '))
peso = float(input('Digite Seu Peso: '))


def imc_calc():
    imc = peso / (alt * alt)
    print('Seu IMC é igual á: ', imc)

    if imc < 18.5:
        print('Desnutrição')
    elif imc >= 18.5 < 24.9:
        print('Peso Normal')
    elif imc >= 25.0 < 29.0:
        print('Sobrepeso')
    elif imc >= 30.0 < 39.9:
        print('Obesidade')
    elif imc >= 40.0:
        print('Obesidade Mórbida')


imc_calc()
