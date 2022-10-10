from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'criptografado'


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


@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo_jogo')
def novo_jogo():
    return render_template('novo_jogo.html', titulo='Cadastro de jogos')


@app.route('/criar_jogo', methods=['POST', ])
def criar_jogo():
    nome = request.form['nome']
    empresa = request.form['empresa']
    console = request.form['console']
    new_jogo = Jogo(nome, empresa, console)
    lista.append(new_jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'teste' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect('/')


app.run(debug=True)
