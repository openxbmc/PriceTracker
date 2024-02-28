## 实时获取BTC价格并导出到MySQL数据库和网页显示

此代码使用Python和`requests`库从Coingecko或Coinmarketcap获取实时BTC价格，并将其存储到MySQL数据库中。然后，使用Flask框架创建一个简单的网页来显示价格数据。

**环境要求**

* Python 3
* pip
* MySQL数据库
* Flask

**运行方法**

1. 克隆此仓库
2. 安装依赖项：`pip install -r requirements.txt`
3. 创建并启动MySQL数据库
4. 修改`db_config`中的数据库配置
5. 运行代码：`python python.py`

**访问网页**

在浏览器中打开 `http://localhost:5000` 即可看到BTC价格。

**注意**

* 此代码仅供学习参考，请勿用于商业用途。
* Coingecko和Coinmarketcap的API可能会随时更改，请注意更新代码。

https://www.coingecko.com/
https://coinmarketcap.com/
