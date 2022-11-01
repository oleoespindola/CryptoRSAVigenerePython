def table_rsa() -> list:
    '''
        Retorna a lista de caracteres da table ASCII
    '''

    table_ascii = list()

    with open('file_rsa.csv') as alfabet:
        for line in alfabet:
            line = line.replace('\n', '')
            table_ascii.append(line)            

    return table_ascii

# ==============================================
def table_vigenere() -> dict:
    '''
    Retorna a table de vigenere usando um arquivo que possui apenas uma linha - vetor - de caracteres pré-definidos que poderão ser utilizados na criptografia do texto. 
    '''
    # Variável que irá recbe o alfabeto pré definido no arquivo 'file_virginiere.csv' e utilizada com índice da linhas e colunas da table.
    alfabet = None
    size_alfabet = 0

    # Variável que irá recerber o alfabeto deslocado para cada linha da table.
    displaced_alfabet =  list()

    # Variável que irá recever a table de vigenere. 
    table = dict()

    # Abre o arquivo, remove os parágrados, depois atribui a variável alfabet.
    with open('file_vigenere.csv') as characters:
        for line in characters:
            for char in line:
                char = char.replace('[' , '')
            alfabet = line.split(';')

    # Contaa o tamanho da lista 'alfabet'
    size_alfabet = len(alfabet)

    # 'displaced_alfabet' recebe o alfabeto e irá deslocar as posições, inserindo uma casa no começo e removendo a casa no final, no loop abaixo. 
    displaced_alfabet = list(alfabet)        

    for letter_lin in alfabet:

        # Linhas da table
        table[letter_lin] = dict()

        # Colunas da tablecls
        for index in range(size_alfabet):
            table[letter_lin][alfabet[index]] = displaced_alfabet[index]
        
        # Insere a última letra do alfabeto deslocado na primeira posição
        displaced_alfabet.append(displaced_alfabet[0])
        # Remove a última posição do alfabeto descolado
        displaced_alfabet.pop(0)

    return table

def alfabet_of_vigenere() -> list:
    '''
    Retorna uma lista com os caracteres do cabeçalho da tabela de vigenere
    '''

    with open('file_vigenere.csv') as characters:
        for line in characters:
            for char in line:
                char = char.replace('[', '')
            line = line.split(';')
            return list(line)
