"""__author__=余婷"""
import json

URL = '../files/'


def read_text_file(file_name):
    """
    读普通文本文件
    :param file_name: 文件名
    :return: 文件中的内容
    """
    try:
        with open(URL+file_name, 'r', encoding='utf-8') as f:
            return f.read()

    except FileNotFoundError:
        return ''


def read_json_file(file_name):
    """
    读json文件中的内容(json文件是文件内容是json数据的文件)
    :param file_name: 文件名
    :return: json数据对应的python数据
    """
    try:
        with open(URL+file_name, 'r', encoding='utf-8') as f:
            return json.loads(f.read())

    except FileNotFoundError:
        return None


def write_json_file(file_name, data):
    """
    将数据写入json文件中
    :param file_name: 文件名
    :param data: 需要写入文件中的数据
    :return: 是否写入成功
    """
    try:
        with open(URL+file_name, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
        return True
    except:
        return False

