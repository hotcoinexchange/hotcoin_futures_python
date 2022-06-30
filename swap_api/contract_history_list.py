import json

import base_util

"""
合约历史委托
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    params = {
    }
    contract_code = 'bchusdt'
    uri = f'/api/v1/perpetual/products/{contract_code}/history-list'
    response = base_util.get(ACCESS_KEY, SECRET_KEY, HOST, uri, params)
    print(json.dumps(response))
