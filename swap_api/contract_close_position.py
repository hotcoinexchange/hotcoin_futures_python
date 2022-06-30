import base_util

"""
市价全平
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    params = {
    }
    contract_code = 'btcusd'
    side = 'long'
    uri = f'/api/v1/perpetual/products/{contract_code}/{side}/closePosition'
    response = base_util.post(ACCESS_KEY, SECRET_KEY, HOST, uri, params, params)
    print(response)
