import re
import mistletoe


def read_md_file(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as fin:
        md_file_read_result = mistletoe.markdown(fin)
        return md_file_read_result


def get_sentence_list(md_file_path):
    md_file_read_result = read_md_file(md_file_path)
    sentence_list = list(filter(lambda sentence: sentence != '', re.split('<.*?>|[^\u4e00-\u9fa5]+', md_file_read_result.replace('$$', '').replace('\n', ''))))
    return sentence_list


def get_md_str(md_file_path):
    md_file_read_result = read_md_file(md_file_path)
    return md_file_read_result

