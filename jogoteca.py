from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'criptografado'


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario_mestre = Usuario('teste', 'teste', 'teste')
thiago = Usuario('Thiago', 'Thiago', '1234')

usuarios = {usuario_mestre.nickname: usuario_mestre,
            thiago.nickname: thiago}


class Jogo:
    def __init__(self, nome, empresa, console):
        self.nome = nome
        self.empresa = empresa
        self.console = console


valorant = Jogo(nome='Valorant', empresa='Riot', console='Pc')
league_of_legends = Jogo(nome="League of Legends", empresa='Riot', console='Pc')
overwath2 = Jogo(nome='Overwatch 2', empresa='Blizzard', console='Pc')
fortnite = Jogo(nome='Fortnite', empresa='EpicGames', console='Multiplataforma')

lista = [valorant, league_of_legends, overwath2, fortnite]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo_jogo')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo_jogo')))
    else:
        return render_template('novo_jogo.html', titulo='Cadastro de jogos')


@app.route('/criar_jogo', methods=['POST', ])
def criar_jogo():
    nome = request.form['nome']
    empresa = request.form['empresa']
    console = request.form['console']
    new_jogo = Jogo(nome, empresa, console)
    lista.append(new_jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima_pagina = request.args.get('proxima')
    return render_template('login.html', proxima=proxima_pagina)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
        session['usuario_logado'] = None
        flash('Logout realizado com sucesso!')
        return redirect(url_for('index'))


app.run(debug=True)
