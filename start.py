from os import times
import re
import random
from hashlib import md5
import requests
import time

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


appid = ''
appkey = ''
from_lang = ''
to_lang = ''

with open('./use.storage', 'r', encoding='utf=8') as f:
    lines = f.readlines()
    for line in lines:
        label = line.split(':')[0]
        value = line.split(':')[1].strip()
        exec('{} = \'{}\''.format(label, value))

new_lines = []


with open('test/test.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        sentence_list = list(filter(lambda sentence: sentence != '', re.split('<.*?>|[^\u4e00-\u9fa5]+', line.replace('$$', '').replace('\n', ''))))
        if len(sentence_list) != 0:
            for sentence in sentence_list:
                time.sleep(1)
                switching_result = code_switching(appid, appkey, from_lang, to_lang, sentence)
                line = line.replace(switching_result[0], switching_result[1])
        new_lines.append(line)

with open('test/test_turn.md', 'a', encoding='utf-8') as f:
    for new_line in new_lines:
        f.write(new_line)