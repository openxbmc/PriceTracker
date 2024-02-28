import requests
import mysql.connector
from flask import Flask, render_template

# 数据库配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "btc_prices"
}

# 创建Flask应用
app = Flask(__name__)

# 获取BTC价格
def get_btc_price(source):
    if source == "coingecko":
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data["bitcoin"]["usd"]
    elif source == "coinmarketcap":
        url = "https://api.coinmarketcap.com/v2/ticker/1/"
        response = requests.get(url)
        data = response.json()
        return data["data"]["quote"]["USD"]["price"]

# 将价格存储到数据库
def store_price(price):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO prices (timestamp, price) VALUES (NOW(), %s)", (price,))
    connection.commit()
    cursor.close()
    connection.close()

# 显示价格的网页
@app.route("/")
def index():
    price = get_btc_price("coingecko")
    store_price(price)
    return render_template("index.html", price=price)

# 运行Flask应用
if __name__ == "__main__":
    app.run(debug=True)
