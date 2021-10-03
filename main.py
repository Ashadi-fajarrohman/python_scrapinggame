import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def popular_games():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/93.0.4577.82 Safari/537.36'}
    url = 'https://www.epicgames.com/store/en-US/collection/most-popular'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    popular_games = soup.findAll('div', attrs={'class': 'css-lrwy1y'})
    return render_template('index.html', popular_games=popular_games)


if __name__ == '__main__':
    app.run(debug=True)
