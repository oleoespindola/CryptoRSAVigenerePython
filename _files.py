def tabela_ascii() -> set:
    '''
        Retorna a lista de caracteres da tabela ASCII
    '''

    tabela_ascii = []

    with open('ascii.csv') as linhas:
        for i in linhas:
            tabela_ascii.append(i)

    return tabela_ascii

