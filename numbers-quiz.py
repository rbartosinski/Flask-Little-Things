import random
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def kalkulator():
    if request.method == "POST":
        liczba_1 = int(request.form["liczba_1"])
        if liczba_1 > n:
            return 'Za duża' + form
        elif liczba_1 < n:
            return 'Za mała' + form
        else:
            return 'Udało się'
    else:
        return form

form = """
        <form action="/" method="POST">
            <label>Spróbuj zgadnąć liczbę!
                <input type="text" name="liczba_1">
            </label>
            <label>
                <input type="submit" value="Sprawdź..."></input >
            </label>
        </form>"""
n = random.randint(0, 10)

app.run(debug=True)