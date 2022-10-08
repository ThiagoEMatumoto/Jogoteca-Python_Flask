from mimetypes import init
from flask import Flask, render_template

app = Flask(__name__)

class jogo:
    def __init__(self, nome, empresa, console):
        self.nome = nome
        self.empresa = empresa
        self.console = console

@app.route('/inicio')
def ola():
    valorant = jogo(nome='Valorant', empresa='Riot', console='Pc' )
    league_of_legends = jogo(nome="League of Legends", empresa='Riot', console='Pc')
    overwath2 = jogo(nome='Overwatch 2', empresa='Blizzard', console='Pc')
    fortnite = jogo(nome='Fortnite', empresa='EpicGames', console='Multiplataforma')
    
    
    lista = [valorant, league_of_legends, overwath2, fortnite]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
