from gerapy_auto_extractor.extractors.content import extract_content
from gerapy_auto_extractor.extractors.title import extract_title
from gerapy_auto_extractor.extractors.datetime import extract_datetime
from gerapy_auto_extractor.extractors.list import extract_list


def extract_detail(html):
    """
    extract detail information
    :param html:
    :return:
    """
    return {
        'title': extract_title(html),
        'datetime': extract_datetime(html),
        'content': extract_content(html)
    }
