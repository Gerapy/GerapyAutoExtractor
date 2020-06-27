from lxml.html import fromstring
from loguru import logger
from lxml.html import HtmlElement


class BaseExtractor(object):
    """
    Base Extractor which provide common methods
    """
    def process(self, element: HtmlElement):
        """
        process method that you should implement
        :param element:
        :return:
        """
        logger.error('You must implement process method in your extractor.')
        raise NotImplementedError
    
    def extract(self, html):
        """
        base extract method, firstly, it will convert html to WebElement, then it call
        process method that child class implements
        :param html:
        :return:
        """
        element = fromstring(html=html)
        return self.process(element)
