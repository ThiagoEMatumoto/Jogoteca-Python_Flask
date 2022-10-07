from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista = ['Valorant', 'League of Legends', 'Overwatch 2', 'Fortnite']
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
