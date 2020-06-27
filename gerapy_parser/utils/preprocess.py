from lxml.html import HtmlElement, etree

from gerapy_parser.utils.element import children

USELESS_TAG = ['meta', 'style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg', 'path']


def preprocess4content(element: HtmlElement):
    """
    preprocess element for content extraction
    :param element:
    :return:
    """
    etree.strip_elements(element, *USELESS_TAG)
    print('---------')
    for child in children(element):
        
        # merge text in span or strong to parent p tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')
        
        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'
        
        if child.tag.lower() == 'span' and not child.getchildren():
            child.tag = 'p'
        