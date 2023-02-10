import base64
import hashlib
import hmac
import urllib
import urllib.parse
import urllib.request
import requests
# from Script.Hktest_HeYue_OlderCode.Conf.Post_Data import contractCode
from datetime import datetime

ACCESS_KEY = "xxx"
SECRET_KEY = "yyy"
API_HOST = 'api-ct.hotcoin.fit'
API_RUL = 'https://' + API_HOST 

def paramsSign(params, paramsPrefix, accessSecret):
    host = "api.hotcoin.top"
    method = paramsPrefix['method'].upper()
    uri = paramsPrefix['uri']
    tempParams = urllib.parse.urlencode(sorted(params.items(), key=lambda d: d[0], reverse=False))
    payload = '\n'.join([method, host, uri, tempParams]).encode(encoding='UTF-8')
    accessSecret = accessSecret.encode(encoding='UTF-8')
    return base64.b64encode(hmac.new(accessSecret, payload, digestmod=hashlib.sha256).digest())


def http_post_request(url, params, data, timeout=10):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url, params=params, headers=headers, data=data, timeout=timeout)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()


def get_utc_str():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'


def api_key_post(params, data, API_URI, timeout=10):
    method = 'POST'

    params_to_sign = {'AccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': get_utc_str()}
    host_name = urllib.parse.urlparse(API_RUL).hostname
    host_name = host_name.lower()
    paramsPrefix = {"host": host_name, 'method': method, 'uri': API_URI}
    params_to_sign.update(params)
    params_to_sign['Signature'] = paramsSign(params_to_sign, paramsPrefix, SECRET_KEY).decode(encoding='UTF-8')
    url = 'https://api-ct.hotcoin.fit' + API_URI
    print(url)
    return http_post_request(url, params_to_sign, data, timeout)

#   下单
def order_send(datasend, contractCode, timeout=10):
    params = {
    }
    data = datasend
    API_RUI = '/api/v1/perpetual/products/' + contractCode + 'order'
    return api_key_post(params, data, API_RUI, timeout)


if __name__ == "__main__":
    dict_data = {
        'type': "11",  # 10 限价或条件单 11 市价
        'side': "open_long",  # open_long 开多 open_short 开空 close_long 平多 close_short 平空
        'price': "",
        'amount': "1",
        'beMaker': "0",
        'tag': "1",
    }

    datasend = str(dict_data)
    contractCode = "bchusdt/"
    res_data = order_send(datasend, contractCode, timeout=10)
    print(res_data)
