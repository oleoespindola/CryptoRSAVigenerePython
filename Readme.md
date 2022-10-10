# PyCripto

O projeto disponibiliza para o usuário duas formas de criptografia diferentes, **cifra de Cesar** e o método **RSA**. 

## Método RSA

Utiliza um conjunto de chaves assimétricas, sendo duas chaves públicas e três chaves privadas. O código das funções utilizadas neste método estão no arquivo *_rsa.py* na pasta raiz do projeto. 

### 🔑 Escolha das primeiras chaves privadas

A encriptação começa a partir da escola de duas chaves privadas, arbitraria, mas precisam ser necessariamente dois números primos. Quanto maior o algarismo, mas difícil se torna a decriptação. 

No código chamaremos essa duas chaves de: 

```python
key_one = 883     # 1ª Chave privada
key_two = 997     # 2ª Chave privada
```

### 🔑 Definindo as chaves públicas

A primeira chave pública é dada pelo produto das chaves privadas. No código:

```python
product_of_keys = key_one * key_two     # Mais conhecido como 1ª Chave pública
```

A segunda chave pública também é arbitrária, mas precisa obedecer as seguintes regras:

**1ª Regra:** 1 < *segunda chave pública < φ(n)*

**2ª Regra:** m.d.c( *φ(n), segunda chave pública) = 1*

3**ª Regra:** *segunda chave pública) =* número primo