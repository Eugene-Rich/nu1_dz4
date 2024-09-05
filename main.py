import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)

    print(data)
    datv = data['Date']
    valutes = list(data['Valute'].values())
    return valutes, datv


app = Flask(__name__)


def create_html(valutes, datv):
    text = '<h1>Курс валют на ' + datv + '</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes, datv = get_valutes_list()
    html = create_html(valutes, datv)
    return html


if __name__ == "__main__":
    app.run()