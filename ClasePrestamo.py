from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

loans = []

form_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Préstamo</title>
</head>
<body>
    <h1>Registro de Préstamo</h1>
    <form action="{{ url_for('register_loan') }}" method="post">
        <label for="borrower">Nombre del Prestatario:</label>
        <input type="text" id="borrower" name="borrower" required><br><br>

        <label for="amount">Monto del Préstamo:</label>
        <input type="number" id="amount" name="amount" required><br><br>

        <label for="date">Fecha del Préstamo:</label>
        <input type="date" id="date" name="date" required><br><br>

        <input type="submit" value="Registrar Préstamo">
    </form>

    <h2>Préstamos Registrados</h2>
    <ul>
    {% for loan in loans %}
        <li>{{ loan['borrower'] }} - {{ loan['amount'] }} - {{ loan['date'] }}</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(form_template, loans=loans)

@app.route('/register', methods=['POST'])
def register_loan():
    borrower = request.form['borrower']
    amount = request.form['amount']
    date = request.form['date']

    loans.append({
        'borrower': borrower,
        'amount': amount,
        'date': date
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)