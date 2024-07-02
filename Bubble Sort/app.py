from flask import Flask, render_template, request

app = Flask(__name__)

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    n = None
    data = []
    data_before_sort = None
    hasil = None
    error_message = None

    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            data = [int(request.form[f'data{i}']) for i in range(1, n + 1)]
            data_before_sort = data.copy()
            hasil = bubble_sort(data)
        except (KeyError, ValueError):
            error_message = 'Masukkan data yang valid (bilangan bulat)'

    return render_template('bubble-sort.html', n=n, data=data, data_before_sort=data_before_sort, hasil=hasil, error_message=error_message)

if __name__ == '__main__':
    app.run()
