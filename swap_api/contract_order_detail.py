import json

import base_util

"""
订单详情
"""

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
HOST = "https://api-ct.hotcoin.fit"

if __name__ == '__main__':
    params = {
        'orderId': 138434463977680
    }
    contract_code = 'bchusdt'
    uri = f'/api/v1/perpetual/products/{contract_code}/orderDetail'
    response = base_util.get(ACCESS_KEY, SECRET_KEY, HOST, uri, params)
    print(json.dumps(response))
