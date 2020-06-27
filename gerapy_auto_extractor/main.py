from lxml import etree

from gerapy_auto_extractor.extractors.content import extract_content
from gerapy_auto_extractor.extractors.content import ContentExtractor
from gerapy_auto_extractor.utils.element import html2element
from gerapy_auto_extractor.utils.preprocess import preprocess4content

html = open('./sample.html', encoding='utf-8').read()
# date = extract_datetime(html)
# print('date', date)

#
# content = extract_content(html)
# print('content', content)
#
# ce = ContentExtractor()
# elements = ce.extract(html)

element = html2element(html)
preprocess4content(element)
with open('result.html', 'w', encoding='utf-8') as f:
    f.write(etree.tostring(element, pretty_print=True, encoding="utf-8", method='html').decode('utf-8'))


extract_content(html)