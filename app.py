from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/deneyim')
def deneyim():
    return render_template('deneyim.html')

@app.route('/yetenekler')
def yetenekler():
    return render_template('yetenekler.html')

@app.route('/liderlik')
def liderlik():
    return render_template('liderlik.html')

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/referanslar')
def referanslar():
    return render_template('referanslar.html')

  # Doğru Yazım Şekli:
@app.route('/referanslar')
def referanslar():
    return render_template('referanslar.html')  # <- 1 Tab/4 boşluk içeride