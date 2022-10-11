# <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" width="30px"> PyCripto

O projeto disponibiliza para o usuário duas formas de criptografia diferentes, **cifra de Cesar** e o método **RSA**. 

## 📒 Sumário

 * [Template](#💻-Template)
    * [template/index.html](##🖱️-template/index.html)
    * [template/_home.html](##🖱️-template/_home.html)
    * [template/_rsa.py](##🖱️-template/_rsa.py)
 * [Método RSA](#🔐-Método-RSA)
    * [Escolha das primeiras chaves privadas](##🔑-Escolha-das-primeiras-chaves-privadas)
    * [Definindo as chaves públicas](##🔑-Definindo-as-chaves-públicas)
    * [Definindo a terceira chave privada](##🔑-Definindo-a-terceira-chave-privada)
    * [Encriptação](##🔑-Encriptação)
    * [Decriptação](##🔑-Decriptação)
# 💻 Template

O arquivo *app.py* é a raiz do projeto, responsável por dar início a aplicação, utilizando a biblioteca *flask* para rodar aplicação em uma página html.

## 🖱️ template/index.html

É o template base da aplicação. Contém a barra de navegação e o seu main será substituído por outros templates que serão chamados com os decoradores. 

## 🖱️ template/_home.html

Apresenta, no main da aplicação, uma mensagem de boas vindas. 

## 🖱️ template/_rsa.py

Irá utilizar os decoradores `rsa/criptografar`  e `rsa/descriptografar`  para criptografar e descriptografar um texto digitado pelo usuário.

# 🔐 Método RSA

Utiliza um conjunto de chaves assimétricas, sendo duas chaves públicas e três chaves privadas. O código das funções utilizadas neste método estão no arquivo *_rsa.py* na pasta raiz do projeto. 

## 🔑 Escolha das primeiras chaves privadas

A encriptação começa a partir da escola de duas chaves privadas, arbitraria, mas precisam ser necessariamente dois números primos. Quanto maior o algarismo, mas difícil se torna a decriptação. 

No código chamaremos essa duas chaves de: 

```python
key_one = 883     # 1ª Chave privada
key_two = 997     # 2ª Chave privada
```

## 🔑 Definindo as chaves públicas

A primeira chave pública é dada pelo produto das chaves privadas. No código:

```python
product_of_keys = key_one * key_two     # Mais conhecido como 1ª Chave pública
```

A segunda chave pública também é arbitrária, mas precisa obedecer as seguintes regras:

- 1 < *segunda chave pública < φ(n)*
- m.d.c( *φ(n), segunda chave pública) = 1*
- *segunda chave pública) =* número primo

A função *public_key()* será responsável por retornar uma lista com as duas chaves públicas de acordo com a regras acima. 

## 🔑 Definindo a terceira chave privada

A terceira chave privada será o inverso multiplicativo modular da segunda chave pública. No código, a function responsável por retornar esse valor será *private_key()*

## 🔑 Encriptação

A formula da encriptação é *'x' = ('Número da letra ** '2ª Chave pública') % '1ª Chave pública’* e será dada pela function *criptografar()*

## 🔑 Decriptação

A fórmula da decriptação é *'x' = ('Número criptografado ** '3ª chave privada') % '1ª Chave pública’* e será dada pela function *descriptografar()*