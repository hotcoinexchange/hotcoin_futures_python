import base_util

"""
获取合约K线
kLineType：1-最新价 2-标记价 3-指数价
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    params = {
        'kline': '1min',
        'since': 0,
        'size': 1000,
        'klineType': 3
    }
    contract_code = 'btcusdt'
    uri = f'/api/v1/perpetual/public/{contract_code}/candles'
    response = base_util.get(ACCESS_KEY, SECRET_KEY, HOST, uri, params)
    print(response)
