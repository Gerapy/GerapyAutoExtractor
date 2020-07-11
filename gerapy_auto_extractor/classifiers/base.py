from lxml.html import fromstring
from gerapy_auto_extractor.schemas.element import Element


class BaseClassifier(object):
    
    def process(self, element: Element):
        """
        you must implement this method in child class
        :param element:
        :return:
        """
        raise NotImplementedError
    
    def classify(self, html, **kwargs):
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
