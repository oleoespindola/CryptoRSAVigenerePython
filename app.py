import html
from flask import Flask, render_template, request

from _rsa import criptografar, descriptografar, public_key, private_key

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def home() -> 'html':
    '''Retorna um template que diz ao usuário o objetivo da aplicação'''
    return render_template('_home.html')

# ========================================================================================

@app.route('/rsa')
def rsa() -> 'html':
    '''Retorna um template para que o usuário teste o modelo de criptografia RSA'''
    return render_template('_rsa.html', text='')



@app.route('/rsa/criptografar', methods=['GET', 'POST'])
def rsa_criptografar() -> 'html':
    '''Criptografa o texto fornecido pelo usuário'''

    keys = public_key()
    text = str(request.form.get('letters'))

    text_resul = criptografar(text=str(text), key_one=keys[0], key_two=keys[1])

    return render_template('_rsa.html', c_text=text_resul)

@app.route('/rsa/descriptografar', methods=['GET', 'POST'])
def rsa_descriptografar() -> 'html':
    '''Criptografa o texto fornecido pelo usuário'''

    keys = public_key()
    text = str(request.form.get('numbers'))

    text_resul = descriptografar(text=text, key_one=keys[0])

    return render_template('_rsa.html', d_text=text_resul)


app.run(debug=True)