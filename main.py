from lxml.html import fromstring

from gerapy_auto_extractor.extractors import extract
from gerapy_auto_extractor.schemas.element import Element
from gerapy_auto_extractor.extractors.list import extract_list
import json

html = open('samples/list/sample1.html', encoding='utf-8').read()

# with open('result.html', 'w', encoding='utf-8') as f:
#     f.write(etree.tostring(element, pretty_print=True, encoding="utf-8", method='html').decode('utf-8'))

# print(json.dumps(extract(html), indent=2, ensure_ascii=False, default=str))
# element = fromstring(html=html)
#
le = extract_list(html)
#
# for element in element.iterchildren():
#     print(element)
#     element.__class__ = Element
#
#     #element.dist = 1
#
#     print(element.tag)
#     print(element.attrib)
#
#
#     print(type(element))
#     print(isinstance(element, Element))
#     print(element.id)
#
#     if element.tag == 'head':
#         element.id = 'dsdsdsdsdds'
#     print(element.id, element.attrib)
