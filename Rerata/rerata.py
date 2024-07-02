from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hitung-rerata.html', n=None, data=None, hasil=None)

@app.route('/proses', methods=['POST'])
def proses():
    n = int(request.form['n'])
    data = [float(request.form[f'data{i}']) for i in range(1, n + 1)]
    rerata = sum(data) / n
    hasil = {'data': data, 'rerata': rerata}

    return render_template('hitung-rerata.html', n=n, data=data, hasil=hasil)

if __name__ == '__main__':
    app.run()
