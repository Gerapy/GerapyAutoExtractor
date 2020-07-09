from lxml.html import fromstring
from loguru import logger
from lxml.html import etree
from gerapy_auto_extractor.schemas.element import Element


class BaseExtractor(object):
    """
    Base Extractor which provide common methods
    """
    
    kwargs = None
    
    def to_string(self, element: Element, limit: int = None):
        """
        convert element to string
        :param element:
        :param limit:
        :return:
        """
        result = etree.tostring(element, pretty_print=True, encoding="utf-8", method='html').decode('utf-8')
        if limit:
            return result[:limit]
        return result
    
    def process(self, element: Element):
        """
        process method that you should implement
        :param element:
        :return:
        """
        logger.error('You must implement process method in your extractor.')
        raise NotImplementedError
    
    def extract(self, html, **kwargs):
        """
        base extract method, firstly, it will convert html to WebElement, then it call
        process method that child class implements
        :param html:
        :return:
        """
        self.kwargs = kwargs
        element = fromstring(html=html)
        element.__class__ = Element
        return self.process(element)
