from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def tabela():
    if request.method == "POST":
        n = int(request.form["licz"])
        return """
    <table>
      <tr>
        <th>2 do potęgi n</th>
        <td>{}</td>
      </tr>
      <tr>
        <th>n do potęgi n</th>
        <td>{}</td>
      </tr>
      <tr>
        <th>n silnia</th>
        <td>{}</td>
      </tr>
    </table>""".format((a ** n), (n ** n), silnia(n))
    else:
        return form

form = """
        <form action="/" method="POST">
            <label>Podaj liczbę natrualną n:
                <input type="text" name="licz">
            </label>
            <label>
                <input type="submit" value="Przejdź dalej"></input >
            </label>
        </form>"""

a = 2
def silnia(s):
    silnia = 1
    if s in (0,1):
        return 1
    else:
        for i in range(2,s+1):
            silnia = silnia*i
        return silnia

app.run(debug=True)