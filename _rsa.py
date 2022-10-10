from _files import tabela_ascii

# Tabela de caracteres possíveis
tabela_ascii = tabela_ascii()
for i in range(len(tabela_ascii)):
    tabela_ascii[i] = tabela_ascii[i].replace('\n', '')

# CHAVES PRIVADAS ARBITRÁRIAS
# *Constituídas de dois números primos.
key_one = 883     # 1ª Chave privada
key_two = 997     # 2ª Chave privada

def public_key() -> set:
    '''
        Função que irá gerar as duas cahves públicas.
        =============================================
        I  - A primeira chave é o produto das duas chaves privadas arbitrárias.
        II - A Segunda chave também é um número arbitrário x, tal que x seja um número inteiro, maior que um, menor que φ('product_of_keys') e o máximo divisor comum entre x e φ('product_of_keys') seja um.
    '''
    # Produto das chaves.
    product_of_keys = key_one * key_two     # Mais conhecido como 1ª Chave pública

    # Função totiene de 'product_of_keys' cujo a eepresentação matemática  é φ('product_of_keys') dada pela variável 'function_of_product'.
    function_of_product = (key_one - 1) * (key_two - 1)

    # Variável que irá guardar todos os números primos maiores que um e menores que 'function_of_product'.
    mdc_of_function = []
    for i in range(1, function_of_product):
        if (function_of_product % i) == 0:
            mdc_of_function.append(i)

    # Variável para guardar todas as possíveis chaves públicas.
    mdc_public_key = []
    # Conta a quantidade de possíveis chaves.
    quantity_of_number = 0
    # Resultado do teste de validade da chave.
    valid_key = False

    # De dois até 'function_of_product'...
    for x in range(2 , function_of_product):
        # Armazena todos os números primos menos que 'x', possíveis chaves publicas.
        for y in range(1 , x + 1):
            if (x % y) == 0:
                mdc_public_key.append(y)
        
        # Para cada possível chave pública, verifica se o único número em comum com o conjunto de números primos menores que a 'function_of_product' é um.
        for number_mdc_fn in mdc_public_key:
            for function_number in mdc_of_function:
                if number_mdc_fn == function_number:
                    quantity_of_number += 1 
                    if number_mdc_fn == 1:
                        valid_key = True
        
        # Se a proposição acima é verdadeira retorna a chave pública. Do contrário zera as variáveis e vai para o próximo algarismo do laço.
        if  (quantity_of_number == 1) and (valid_key == True): 
            return list([product_of_keys, mdc_public_key[1]])    # Retorna a primeira chave junto com a segunda, que acabou ser localizada 

        else:
            mdc_public_key = []
            quantity_of_number = 0
            valid_key = False

def private_key() -> set:
    '''
        Função que localiza a terceira chave privada.
        =============================================
        A terceira chave privada é dada pelo inverso modular da segunda chave pública mod(φ('product_of_keys'))
    '''
    # Função totiene de 'product_of_keys' cujo a eepresentação matemática  é φ('product_of_keys') dada pela variável 'function_of_product'.
    function_of_keys = (key_one -1) * (key_two - 1)
    keys = public_key() # Segunda chave pública


    for i in range(1, function_of_keys):
        if(((keys[1] % function_of_keys)*(i % function_of_keys)) % function_of_keys == 1):
            return i

def criptografar(text:str, key_one:int, key_two:int) -> set:
    '''
        Criptografa o texto por caractere.
        =============================================
        Fórmula da criptografia: 'x' = ('Número da letra ** '2ª Chave pública') % '1ª Chave pública '.

    '''
    tabela_ascii
    resultado = list()

    for letter in text:
        for i in range(len(tabela_ascii)):
            if str(letter) == str(tabela_ascii[i]):
                x = (i ** key_two) % key_one
                resultado.append(x)

    return resultado

def descriptografar(text:str, key_one:int) -> set:
    '''
        DesCriptografa o texto por números inteiros na lista.
        =============================================
        Fórmula da criptografia: 'x' = ('Número criptografado ** '3ª chave privada') % '1ª Chave pública'.
    '''
    tabela_ascii
    key_three = private_key()

    text  = text.replace('[' ,'')
    text  = text.replace(']' ,'')
    text  = text.replace(',' ,'')
    index_ascii = [int(number) for number in text.split()]
    
    text_resul = ''

    for i in index_ascii:
        i = (i ** key_three) % key_one
        text_resul = str(text_resul) + str(tabela_ascii[i])

    return text_resul