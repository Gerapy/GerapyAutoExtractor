from lxml.html import HtmlElement, etree

from gerapy_auto_extractor.schemas.element import Element
from gerapy_auto_extractor.utils.element import children, remove_element, remove_children

CONTENT_EXTRACTOR_USELESS_TAGS = ['meta', 'style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg',
                                  'path',
                                  'symbol', 'img', 'footer', 'header']
CONTENT_EXTRACTOR_STRIP_TAGS = ['span', 'blockquote']
CONTENT_EXTRACTOR_NOISE_XPATHS = [
    '//div[contains(@class, "comment")]',
    '//div[contains(@class, "advertisement")]',
    '//div[contains(@class, "advert")]',
    '//div[contains(@style, "display: none")]',
]


def preprocess4content_extractor(element: HtmlElement):
    """
    preprocess element for content extraction
    :param element:
    :return:
    """
    # remove tag and its content
    etree.strip_elements(element, *CONTENT_EXTRACTOR_USELESS_TAGS)
    # only move tag pair
    etree.strip_tags(element, *CONTENT_EXTRACTOR_STRIP_TAGS)
    
    remove_children(element, CONTENT_EXTRACTOR_NOISE_XPATHS)
    
    for child in children(element):
        
        # merge text in span or strong to parent p tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')
            
            if not (child.text and child.text.strip()):
                remove_element(child)
        
        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'


LIST_EXTRACTOR_USELESS_TAGS = CONTENT_EXTRACTOR_USELESS_TAGS
LIST_EXTRACTOR_STRIP_TAGS = CONTENT_EXTRACTOR_STRIP_TAGS
LIST_EXTRACTOR_NOISE_XPATHS = CONTENT_EXTRACTOR_NOISE_XPATHS


def preprocess4list_extractor(element: Element):
    """
    preprocess element for list extraction
    :param element:
    :return:
    """
    # remove tag and its content
    etree.strip_elements(element, *CONTENT_EXTRACTOR_USELESS_TAGS)
    # only move tag pair
    etree.strip_tags(element, *CONTENT_EXTRACTOR_STRIP_TAGS)
    
    remove_children(element, CONTENT_EXTRACTOR_NOISE_XPATHS)
    
    for child in children(element):
        
        # merge text in span or strong to parent p tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')
            
            if not (child.text and child.text.strip()):
                remove_element(child)
        
        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'


LIST_CLASSIFIER_USELESS_TAGS = ['style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg', 'path',
                                'symbol', 'footer', 'header']
LIST_CLASSIFIER_STRIP_TAGS = ['span', 'blockquote']
LIST_CLASSIFIER_NOISE_XPATHS = [
    '//div[contains(@class, "comment")]',
    '//div[contains(@class, "advertisement")]',
    '//div[contains(@class, "advert")]',
    '//div[contains(@style, "display: none")]',
]


def preprocess4list_classifier(element: HtmlElement):
    """
    preprocess element for list classifier
    :param element:
    :return:
    """
    # remove tag and its content
    etree.strip_elements(element, *LIST_CLASSIFIER_USELESS_TAGS)
    # only move tag pair
    etree.strip_tags(element, *LIST_CLASSIFIER_STRIP_TAGS)
    
    remove_children(element, LIST_CLASSIFIER_NOISE_XPATHS)
    
    for child in children(element):
        
        # merge text in span or strong to parent p tag
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')
            
            if not (child.text and child.text.strip()):
                remove_element(child)
        
        # if a div tag does not contain any sub node, it could be converted to p node.
        if child.tag.lower() == 'div' and not child.getchildren():
            child.tag = 'p'
