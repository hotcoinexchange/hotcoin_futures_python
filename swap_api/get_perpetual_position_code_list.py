import base64
import hashlib
import hmac
import urllib
import urllib.parse
import urllib.request
from datetime import datetime

import requests

ACCESS_KEY = "您的Access Key"
SECRET_KEY = "您的Secret Key"
API_HOST = 'api-ct.hotcoin.fit'
API_RUL = 'https://' + API_HOST  # + API_TICKER_URI


def params_sign(params, params_prefix, access_secret):
    host = "perpetual.hotcoinex.io"
    method = params_prefix['method'].upper()
    uri = params_prefix['uri']
    api_params = urllib.parse.urlencode(sorted(params.items(), key=lambda d: d[0], reverse=False))
    payload = '\n'.join([method, host, uri, api_params]).encode(encoding='UTF-8')
    access_secret = access_secret.encode(encoding='UTF-8')
    return base64.b64encode(hmac.new(accessSecret, payload, digestmod=hashlib.sha256).digest())


def http_post_request(url, params, timeout=10):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url=url, params=params, headers=headers, timeout=timeout)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()


def get_utc_str():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'


def api_key_get(params, api_uri, timeout=10):
    method = 'GET'

    params_to_sign = {'AccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': get_utc_str()}
    host_name = urllib.parse.urlparse(API_RUL).hostname
    host_name = host_name.lower()
    params_prefix = {"host": host_name, 'method': method, 'uri': api_uri}
    params_to_sign.update(params)
    params_to_sign['Signature'] = params_sign(params_to_sign, params_prefix, SECRET_KEY).decode(encoding='UTF-8')
    url = "https://test-perpetual.hotcx.com" + api_uri
    print(url)
    # 更换       域名
    return http_post_request(url, params_to_sign, timeout)


#   仓位列表
def get_list(timeout=10):
    params = {}
    api_uri = '/api/v1/perpetual/position/BTCUSDT/list'
    return api_key_get(params, api_uri, timeout)


if __name__ == "__main__":
    res_data = get_list(timeout=10)
    print(res_data)
