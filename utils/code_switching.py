import requests
import random
import json
from hashlib import md5

def code_switching(appid, appkey, from_lang, to_lang, query):
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    salt = random.randint(32768, 65536)
    sign = md5((appid + query + str(salt) + appkey).encode('utf-8')).hexdigest()
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()['trans_result']
    # result = json.dumps(result, indent=4, ensure_ascii=False)
    result = [result[0]['src'], result[0]['dst']]
    return result

def start_switching():
    pass
