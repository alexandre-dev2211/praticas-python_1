# Calculando Dias Trabalhados:

f_ponto = int(input("Informe A Quanitdade de Dias de Trabalho: "))

bruto = f_ponto * 30.00

irpf = bruto * 8 / 100

liquido = bruto - irpf

print("O Valor Bruto da Folha é: R$ ", bruto)

print("O Valor de IRPF Retido na Fonte é: R$ ", irpf)

print("O Valor Líquido a Ser Creditado é: R$ ", liquido)
