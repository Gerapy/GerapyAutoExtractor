import json


def jsonify(data):
    """
    format the output data
    :param data:
    :return:
    """
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)


def content(file_path, encoding='utf-8'):
    """
    get content of html file
    :param encoding: file encoding
    :param file_path:
    :return:
    """
    with open(file_path, encoding=encoding) as f:
        return f.read()