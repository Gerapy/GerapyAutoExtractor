from gerapy_auto_extractor.extractors.content import extract_content
from gerapy_auto_extractor.extractors.title import extract_title
from gerapy_auto_extractor.extractors.datetime import extract_datetime


def extract(html):
    """
    extract all information
    :param html:
    :return:
    """
    return {
        'title': extract_title(html),
        'datetime': extract_datetime(html),
        'content': extract_content(html)
    }
