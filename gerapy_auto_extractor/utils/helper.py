import json


def jsonify(data):
    """
    format the output data
    :param data:
    :return:
    """
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)
