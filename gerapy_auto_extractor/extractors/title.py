from gerapy_auto_extractor.extractors.base import BaseExtractor
from lxml.html import HtmlElement
from gerapy_auto_extractor.patterns.title import METAS
from gerapy_auto_extractor.utils.lcs import lcs_of_2


class TitleExtractor(BaseExtractor):
    """
    Title Extractor which extract title of page
    """
    
    def extract_by_meta(self, element: HtmlElement) -> str:
        """
        extract according to meta
        :param element:
        :return: str
        """
        for xpath in METAS:
            title = element.xpath(xpath)
            if title:
                return ''.join(title)
    
    def extract_by_title(self, element: HtmlElement):
        """
        get title from <title> tag
        :param element:
        :return:
        """
        return ''.join(element.xpath('//title//text()')).strip()
    
    def extract_by_h(self, element: HtmlElement):
        """
        extract by h tag, priority h1, h2, h3
        :param elemeent:
        :return:
        """
        for xpath in ['//h1', '//h2', '//h3']:
            children = element.xpath(xpath)
            if not children:
                continue
            child = children[0]
            texts = child.xpath('./text()')
            if texts and len(texts):
                return texts[0].strip()
    
    def process(self, element: HtmlElement):
        """
        extract title from element
        :param element:
        :return:
        """
        title_extracted_by_meta = self.extract_by_meta(element)
        title_extracted_by_h = self.extract_by_h(element)
        title_extracted_by_title = self.extract_by_title(element)
        
        if title_extracted_by_meta:
            return title_extracted_by_meta
        
        if title_extracted_by_title and title_extracted_by_h:
            return lcs_of_2(title_extracted_by_title, title_extracted_by_h)
        
        if title_extracted_by_title:
            return title_extracted_by_title
        
        return title_extracted_by_h


title_extractor = TitleExtractor()


def extract_title(html):
    """
    extract title from html
    :param html:
    :return:
    """
    result = title_extractor.extract(html)
    return result
