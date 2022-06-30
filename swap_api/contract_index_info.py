import base_util

"""
指数价成分信息
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    params = {
    }
    contract_code = 'btcusdt'
    uri = f'/api/v1/perpetual/public/{contract_code}/indexInfo'
    response = base_util.get(ACCESS_KEY, SECRET_KEY, HOST, uri, params)
    print(response)
