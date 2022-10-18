from _files import table_vigenere, alfabet_of_vigenere

table = table_vigenere()

def vigenere_encrypt(text:str, key_word:str) -> str:
    '''
    Distribui para cada letra do texto uma letra da palavra chave. Depois, na linha cujo o índice corresponde ao resultado da busca e coluna, que  sera a letra a ser criptografada, encontra o resultado correspondente.
    '''

    encrypted_text = ''
    index_key_word = 0

    if key_word == '':
        return 'Desculpe, mas não consigo critpgrafar isso 😿'

    for letter_text in text:
        encrypted_text += table[key_word[index_key_word]][letter_text]

        # Desoloca a letra da chave
        index_key_word =+ 1 
        if index_key_word == len(key_word):
            index_key_word = 0
    
    return encrypted_text

def vigenere_decrypt(text:str, key_word:str) -> str:
    '''
    Processo inverso ao da função 'vigenere_encrypt'.
    '''

    # Desloca a posiçao/letra da chave a medida que a decriptaçao avança
    count_key_letter = 0 

    # Recebe o texto descriptografado
    decrypt_text = ''

    # Recebe ocabechalho da tabela de vigenere
    characters = alfabet_of_vigenere()

    try:
        for letter_in_text in text: 
            for char in characters:
                if letter_in_text == table[key_word[count_key_letter]][char]:
                    decrypt_text += char

                    # Desoloca a letra da chave
                    count_key_letter =+ 1 
                    if count_key_letter == len(key_word):
                        count_key_letter = 0

                    break
    except:
        decrypt_text = 'Desculpe, mas não consegui descriptografar isso 😿'

    return decrypt_text