# Filtrando Funcionários:

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']

t_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']

t_noite = ['Pedro', 'Sophia', 'Bruno']

habilitados = ['Marcos', 'Alice', 'Bruno', 'Melissa']

def filtro():
    filter_1 = set(habilitados).intersection(t_noite)
    filter_2 = set(habilitados).intersection(t_dia)
    filter_3 = set(funcionarios).difference(habilitados)
    print('Funcionários Habilitados Que Trabalham a Noite: ', filter_1)
    print('Funcionários Habilitados Que Trabalham de Dia: ', filter_2)
    print('Funcionários Não-Habilitados: ', filter_3)


filtro()

