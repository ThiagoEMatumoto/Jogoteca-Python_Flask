from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class jogo:
    def __init__(self, nome, empresa, console):
        self.nome = nome
        self.empresa = empresa
        self.console = console


valorant = jogo(nome='Valorant', empresa='Riot', console='Pc')
league_of_legends = jogo(nome="League of Legends", empresa='Riot', console='Pc')
overwath2 = jogo(nome='Overwatch 2', empresa='Blizzard', console='Pc')
fortnite = jogo(nome='Fortnite', empresa='EpicGames', console='Multiplataforma')

lista = [valorant, league_of_legends, overwath2, fortnite]


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
    new_jogo = jogo(nome, empresa, console)
    lista.append(new_jogo)
    return redirect('/')


app.run(debug=True)
