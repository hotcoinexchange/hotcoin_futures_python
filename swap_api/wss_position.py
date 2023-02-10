import websocket
import ssl
import gzip
import time
import datetime
import json
import base64
import hashlib
import hmac
import urllib
import urllib.parse
import urllib.request
import requests
from datetime import datetime

ACCESS_KEY = "xxx"
SECRET_KEY = "yyy"
WSS_HOST = 'wss-ct.hotcoin.fit'
WSS_URL = 'wss://' + WSS_HOST


def get_utc_str():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
def api_SignIn():
    method = 'wss'
    params_to_sign = {'AccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': get_utc_str()}
    paramsPrefix = {"host": 'api.ws.contract.hotcoin.top', 'method': method, 'uri': '/wss'}
    params_to_sign['Signature'] = paramsSign(params_to_sign, paramsPrefix, SECRET_KEY).decode(encoding='UTF-8')
    ws.send('{"event": "signin","params": {"apiKey": "' + ACCESS_KEY + '","timestamp": "' + params_to_sign['Timestamp'] + '","signature": "' + params_to_sign['Signature'] + '"}}')

def paramsSign(params, paramsPrefix, accessSecret):
    host = paramsPrefix['host']
    method = paramsPrefix['method'].upper()
    uri = paramsPrefix['uri']
    tempParams = urllib.parse.urlencode(sorted(params.items(), key=lambda d: d[0], reverse=False))
    payload = '\n'.join([method, host, uri, tempParams]).encode(encoding='UTF-8')
    accessSecret = accessSecret.encode(encoding='UTF-8')
    return base64.b64encode(hmac.new(accessSecret, payload, digestmod=hashlib.sha256).digest())

# When the server has data updates, it actively pushes the data
def on_message(ws, message):  
    print(message)

# When the program reports an error, will be triggered on_error event
def on_error(ws, error):
    print(error)

# Trigger the close event after the program is closed
def on_close(ws):
    print("Connection closed ……")

# On will be triggered after connecting to the on_open event
def on_open(ws):
    api_SignIn()
    ws.send('{"event":"subscribe","params":{"biz":"perpetual","type":"position","zip":false,"serialize":false}}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WSS_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()