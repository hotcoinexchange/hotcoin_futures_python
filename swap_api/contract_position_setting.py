import base_util

"""
设置自动追加保证金
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    params = {
        'value': 1
    }
    contract_code = 'bchusdt'
    uri = f'/api/v1/perpetual/position/{contract_code}/setting'
    response = base_util.post(ACCESS_KEY, SECRET_KEY, HOST, uri, params, params)
    print(response)
