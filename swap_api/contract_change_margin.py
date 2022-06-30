import base_util

"""
调整保证金
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    contract_code = 'ltcusdt'
    side = 'long'
    params = {
        'side': side,
        'margin': -1
    }
    uri = f'/api/v1/perpetual/position/{contract_code}/change-margin'
    response = base_util.post(ACCESS_KEY, SECRET_KEY, HOST, uri, params, params)
    print(response)
