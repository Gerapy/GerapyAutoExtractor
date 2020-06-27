from lxml.html import fromstring, HtmlElement

class BaseExtractor(object):
    
    def __init__(self):
        pass
    
    
    
    
    
    def process(self, element):
        raise NotImplementedError
    
    
    
    def extract(self, html):
        element = fromstring(html=html)
        print('element', element)
        return self.process(element)
        
    
    