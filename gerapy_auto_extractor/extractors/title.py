from gerapy_auto_extractor.extractors.base import BaseExtractor
from lxml.html import HtmlElement
from gerapy_auto_extractor.patterns.title import METAS
from gerapy_auto_extractor.utils.lcs import lcs_of_2
from gerapy_auto_extractor.utils.similarity import similarity2


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
    
    def extract_by_hs(self, element: HtmlElement):
        """
        get title from all h1-h3 tag
        :param element:
        :return:
        """
        hs = element.xpath('//h1//text()|//h2//text()|//h3//text()')
        return hs or []
    
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
        title_extracted_by_hs = self.extract_by_hs(element)
        title_extracted_by_title = self.extract_by_title(element)
        
        # split logic to add more
        if title_extracted_by_meta:
            return title_extracted_by_meta
        
        # get most similar h
        title_extracted_by_hs = sorted(title_extracted_by_hs,
                                       key=lambda x: similarity2(x, title_extracted_by_title),
                                       reverse=True)
        if title_extracted_by_hs:
            return lcs_of_2(title_extracted_by_hs[0], title_extracted_by_title)
        
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
