import os
import sys
import time

sys.path.append(os.getcwd())

from utils.code_switching import code_switching
from utils.parsing_md import get_sentence_list, get_md_str

appid = ''
appkey = ''
from_lang = ''
to_lang = ''

with open('./user.storage', 'r', encoding='utf=8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        label = line.split(':')[0]
        value = line.split(':')[1].strip()
        exec('{} = \'{}\''.format(label, value))

md_file_path = 'test/test.md'
query_list = get_sentence_list(md_file_path)

md_file_read_result = get_md_str(md_file_path)
print(md_file_read_result)

for query in query_list:
    time.sleep(1)
    alternative_sentence = code_switching(appid, appkey, from_lang, to_lang, query)
    print(alternative_sentence)

