import os
import sys
import time

sys.path.append(os.getcwd())

from utils.code_switching import code_switching, start_html_to_md, start_switching
from utils.parsing_md import get_sentence_list, get_md_str

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

md_file_path = 'test/test.md'
query_list = get_sentence_list(md_file_path)

md_file_read_result = get_md_str(md_file_path)


for query in query_list:
    time.sleep(1)
    alternative_sentence = code_switching(appid, appkey, from_lang, to_lang, query)
    md_file_read_result = start_switching(md_file_read_result, alternative_sentence)

result = start_html_to_md(md_file_read_result)

with open('./test/test_turn.md', 'w', encoding='utf-8') as f:
    f.write(result)
