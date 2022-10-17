# <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" width="30px"> PyCripto

O projeto disponibiliza para o usuário duas formas de criptografia diferentes, **cifra de Vigenère** e o método **RSA**.  
<br>

## 📒 Sumário

 * [Template](#-template)
    * [template/index.html](#%EF%B8%8F-templateindexhtml)
    * [template/_home.html](#%EF%B8%8F-template_homehtml)
    * [template/_rsa.py](#%EF%B8%8F-template_rsapy)
 * [Cifra de Vigenère](#-cifra-de-vigenère)
    * [Construção da tabula recta](#-construção-da-tabula-recta)
    * [Encriptação e decriptação de Virgenère](#-encriptação-e-decriptação-de-virgenère)
 * [Método RSA](#-escolha-das-primeiras-chaves-privadas)
    * [Escolha das primeiras chaves privadas](#-método-rsa)
    * [Definindo as chaves públicas](#-definindo-as-chaves-públicas)
    * [Definindo a terceira chave privada](#-definindo-a-terceira-chave-privada)
    * [Encriptação](#-encriptação)
    * [Decriptação](#-decriptação)

---
<br>

# 💻 Template

O arquivo *app.py* é a raiz do projeto, responsável por dar início a aplicação, utilizando a biblioteca *flask* para rodar aplicação em uma página html.
<br><br>

## 🖱️ template/index.html

É o template base da aplicação. Contém a barra de navegação e o seu main será substituído por outros templates que serão chamados com os decoradores. 
<br><br>

## 🖱️ template/_home.html

Apresenta, no main da aplicação, uma mensagem de boas-vindas. 
<br><br>

## 🖱️ template/_rsa.py

Irá utilizar os decoradores `rsa/criptografar`  e `rsa/descriptografar`  para criptografar e descriptografar um texto digitado pelo usuário.
<br><br>

# 🔐 Cifra de Vigenère
Irá utilizar uma serie de deslocamentos alfabéticos, baseado em única chave. Trata-se, portanto, de um método de criptografia de chave simétrica.
<br><br>

## 🔑 Construção da tabula recta

Um arquivo csv (_file_vigerene.csv_ no programa) contem todos os caracteres possíveis.

A função _table_vigerene()_ irá construir uma tabela e utilizar esses caracteres como cabeçalhos de linhas e colunas. Os valores da tabela serão os mesmos caracteres, mas o vetor de _B_ será o vetor de _A_, com a alteração de que a primeira posição de _A_ passa a ser a última posição de _B_. 
Veja o exemplo abaixo:
   <div align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Vigen%C3%A8re_square.svg/800px-Vigen%C3%A8re_square.svg.png" alt="exemplo de uma tabula recta" width="300px" height="300px">
   </div>
<br><br>

## 🔑 Encriptação e decriptação de Virgenère
A função _vigerene_encrypt()_ irá repetir a palavra chave até que ela possua o mesmo tamanho do texto que será criptografado. Cada letra da palavra chave irá servir como índice de linha para cada letra do texto que a ser criptografado, e que também será o índice de coluna.

# 🔐 Método RSA

Utiliza um conjunto de chaves assimétricas, sendo duas chaves públicas e três chaves privadas. O código das funções utilizadas neste método está no arquivo *_rsa.py* na pasta raiz do projeto. 
<br><br>

## 🔑 Escolha das primeiras chaves privadas

A encriptação começa a partir da escola de duas chaves privadas, arbitraria, mas precisam ser necessariamente dois números primos. Quanto maior o algarismo, mas difícil se torna a decriptação. 

No código chamaremos essas duas chaves de: 

```python
key_one = 883     # 1ª Chave privada
key_two = 997     # 2ª Chave privada
```
<br><br>

## 🔑 Definindo as chaves públicas

A primeira chave pública é dada pelo produto das chaves privadas. No código:

```python
product_of_keys = key_one * key_two     # Mais conhecido como 1ª Chave pública
```

A segunda chave pública também é arbitrária, mas precisa obedecer às seguintes regras:

- 1 < *segunda chave pública < φ(n)*
- m.d.c( *φ(n), segunda chave pública) = 1*
- *segunda chave pública) =* número primo

A função *public_key()* será responsável por retornar uma lista com as duas chaves públicas de acordo com a regras acima. 
<br><br>

## 🔑 Definindo a terceira chave privada

A terceira chave privada será o inverso multiplicativo modular da segunda chave pública. No código, a function responsável por retornar esse valor será *private_key()*
<br><br>

## 🔑 Encriptação

A formula da encriptação é *'x' = ('Número da letra ** '2ª Chave pública') % '1ª Chave pública’* e será dada pela function *criptografar()*
<br><br>

## 🔑 Decriptação

A fórmula da decriptação é *'x' = ('Número criptografado ** '3ª chave privada') % '1ª Chave pública’* e será dada pela function *descriptografar()*
<br><br>
