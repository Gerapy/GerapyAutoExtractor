from gerapy_auto_extractor.utils import *

from lxml import etree
from gerapy_auto_extractor.extractors.content import extract_content
from gerapy_auto_extractor.extractors.title import extract_title
from gerapy_auto_extractor.extractors.datetime import extract_datetime
from gerapy_auto_extractor.utils.element import html2element

html = open('sample.html', encoding='utf-8').read()
element = html2element(html)


def test_content():
    content = extract_content(html)
    print(f'content: {content}')
    assert content is not None


def test_title():
    title = extract_title(html)
    print(f'title: {title}')
    assert title is not None


def test_datetime():
    datetime = extract_datetime(html)
    print(f'datetime: {datetime}')
    assert datetime is not None
