from flask import redirect, url_for, render_template
from flask_restful import Resource
from . import app,api,db
from .models import ticker_list,price_history
from binance.client import Client
import yfinance as yf

api_key = 'bh7COkdr7z81fUAFv2fSnuZLXWQZk3XThDiEUVOgXEIwHrq8bOakz2b9C79gik4M'
secret_key = 'UmxOoeJNcrwHwlM0StkYBwwUXrOxNO9tZ9JT1tEdBt09diWN3WArPOn5k8kurlVX'
client = Client(api_key, secret_key)
client.API_URL = 'https://testnet.binance.vision/api'

@app.route('/')
def index():
    post = ticker_list.query.all()
    history = price_history.query.all()
    return render_template("home.html", title="Finance APİ", content=post,history=history)

@app.route('/<ticker>')
def input(ticker):
    ticker_new = ticker_list(ticker=ticker)
    db.session.add(ticker_new)
    db.session.commit()
    candles = client.get_klines(symbol = ticker, interval='5m', limit=13)
    tickerid = ticker_list.query.filter_by(ticker=ticker).first()
    tickerid = tickerid.id
    for i in range(len(candles)):
        price = price_history(price=candles[i][4],history=candles[i][0],ticker_id=tickerid)
        db.session.add(price)
        db.session.commit()
    return redirect(url_for('index'))

class ortalama(Resource):
    def get(self):
        ticker = ticker_list.query.filter_by(ticker = 'ETHBTC')
        post = price_history.query.filter_by(ticker_id=ticker[0].id).all()[::-1]
        total = 0
        for i in range(0,13):
            total += post[i].price
        total /=13
        return {'Son-60-Ortalama':total}

class son15dk(Resource):
    def get(self):
        ticker = ticker_list.query.filter_by(ticker='ETHBTC').all()
        post = price_history.query.filter_by(ticker_id=ticker[0].id).all()[::-1]
        content = {
        }
        for i in range(0,3):
            content[post[i].history] = post[i].price
        return content

api.add_resource(ortalama, "/ortalama")
api.add_resource(son15dk, "/son15dk")