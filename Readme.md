# <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" width="30px"> PyCripto

O objetivo deste projeto é mostrar ao usuário duas apicações de criptografia diferentes: **cifra de Vigenère** e o método **RSA**.  
<br>

## 📒 Sumário

 * [Template](#1---template)
    * [template/index.html](#11-templateindexhtml)
    * [template/_home.html](#12-template_homehtml)
    
 * [Cifra de Vigenère](#2---cifra-de-vigenère)
    * [Construção da tabula recta](#21-construção-da-tabula-recta)
    * [Encriptação e decriptação de Virgenère](#21-construção-da-tabula-recta)

 * [Método RSA](#3--método-rsa)
    * [Escolha das primeiras chaves privadas](#31-escolha-das-primeiras-chaves-privadas)
    * [Definindo as chaves públicas](#32-definindo-as-chaves-públicas)
    * [Definindo a terceira chave privada](#33-definindo-a-terceira-chave-privada)
    * [Encriptação](#34-encriptação)
    * [Decriptação](#35-decriptação)

---
<br>

## 1 - Template

   O arquivo *app.py* é a raiz do projeto, responsável por dar início a aplicação, utilizando a biblioteca *flask* para rodar aplicação em uma página html.
<br><br>

### 1.1 template/index.html

   É o template base da aplicação. Contém a _nav_ e _footer_ do projeto. Seu main será sibstituído pelos decodores. 
<br><br>

### 1.2 template/_home.html

   Apresenta no main da aplicação, uma mensagem de boas-vindas e um texo que explica o objetivo do projeto e como ele irá funcionar. 
<br><br>

--

## 2. - Cifra de Vigenère

   Irá utilizar uma serie de deslocamentos alfabéticos (assim como na Cifra de César) baseado em única chave, tratando-se, portanto, de um método de criptografia de chave simétrica.
   
   Neste projeto, o método de Viginére ira aceitar apenas letras (maiúsculas ou minúsculas). Não será possível utilizar números ou caracteres expeciais. 
   A desencriptação sempre irá retornar o texto em caixa alta.
<br><br>

### 2.1 Construção da tabula recta

Um arquivo csv (_file_vigenere.csv_ no programa) contem todos os caracteres possíveis.

A função _table_vigenere()_ irá construir uma tabela e utilizar esses caracteres como cabeçalhos de linhas e colunas. Os valores da tabela serão os mesmos caracteres, mas o vetor de _B_ será o vetor de _A_, com a alteração de que a primeira posição de _A_ passa a ser a última posição de _B_. 
Veja o exemplo abaixo:
   <div align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Vigen%C3%A8re_square.svg/800px-Vigen%C3%A8re_square.svg.png" alt="exemplo de uma tabula recta" width="300px" height="300px">
   </div>
<br><br>

### 2.2 Encriptação e decriptação de Virgenère

   A função _vigenere_encrypt()_ irá repetir a palavra chave até que ela possua o mesmo tamanho do texto que será criptografado. Cada letra da palavra chave servirá como índice de linha para cada letra do texto que a ser criptografado, as letras do texo a ser criptografa serão os índeces de coluna.
<br><br>

## 3- Método RSA

   Utiliza um conjunto de chaves assimétricas, sendo duas chaves públicas e três chaves privadas. O código das funções utilizadas neste método está no arquivo *_rsa.py* na pasta raiz do projeto. Trata-se de criptografia de chaves assimétricas com inúmeras possibilidades de combinações diferentes, logo, seu processamento é mais lento que o método anterior. 
<br><br>

### 3.1 Escolha das primeiras chaves privadas

   A encriptação começa a partir da escola de duas chaves privadas, arbitrarias, mas precisam ser necessariamente dois números primos. Quanto maior o algarismo, mas difícil se torna a decriptação. 

No código chamaremos essas duas chaves de: 

```python
key_one = 883     # 1ª Chave privada
key_two = 997     # 2ª Chave privada
```
<br><br>

### 3.2 Definindo as chaves públicas

   A primeira chave pública é dada pelo produto das chaves privadas. No código:

```python
product_of_keys = key_one * key_two     # Mais conhecido como 1ª Chave pública
```

   A segunda chave pública também é arbitrária, mas precisa obedecer às seguintes regras:

   - 1 < *segunda chave pública < φ(n)*
   - m.d.c( *φ(n), segunda chave pública) = 1*
   - *segunda chave pública =* número primo

   A função *public_key()* será responsável por retornar uma lista com as duas chaves públicas de acordo com a regras acima. 
<br><br>

### 3.3 Definindo a terceira chave privada

A terceira chave privada será o inverso multiplicativo modular da segunda chave pública. No código, a function responsável por retornar esse valor será *private_key()*
<br><br>

### 3.4 Encriptação

A formula da encriptação é *'x' = ('Número da letra ** '2ª Chave pública') % '1ª Chave pública’* e será dada pela function *criptografar()*
<br><br>

### 3.5 Decriptação

A fórmula da decriptação é *'x' = ('Número criptografado ** '3ª chave privada') % '1ª Chave pública’* e será dada pela function *descriptografar()*
<br><br>
