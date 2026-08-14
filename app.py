from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projeler')
def projeler():
    return render_template('projeler.html')

@app.route('/deneyim')
def deneyim():
    return render_template('deneyim.html')

@app.route('/yetenekler')
def yetenekler():
    return render_template('yetenekler.html')

@app.route('/liderlik')
def liderlik():
    return render_template('liderlik.html')

@app.route('/referanslar')
def referanslar():
    return render_template('referanslar.html')

if __name__ == '__main__':
    app.run(debug=True)