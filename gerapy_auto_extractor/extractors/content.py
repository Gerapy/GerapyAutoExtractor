import numpy as np
from lxml.html import HtmlElement
from gerapy_auto_extractor.utils.preprocess import preprocess4content
from gerapy_auto_extractor.extractors.base import BaseExtractor
from gerapy_auto_extractor.utils.element import children_of_body, fill_element_info
from gerapy_auto_extractor.schemas.element import ElementInfo


class ContentExtractor(BaseExtractor):
    """
    extract content from detail page
    """
    
    def process(self, element: HtmlElement):
        """
        extract content from html
        :param element:
        :return:
        """
        # preprocess
        preprocess4content(element)
        
        # start to evaluate every child element
        element_infos = []
        child_elements = children_of_body(element)
        for child_element in child_elements:
            # new element info
            element_info = ElementInfo()
            element_info.element = child_element
            element_info = fill_element_info(element_info)
            element_infos.append(element_info)
        
        # get std of density_of_text among all elements
        density_of_text = [element_info.density_of_text for element_info in element_infos]
        density_of_text_std = np.std(density_of_text, ddof=1)
        
        # get density_score of every element
        for element_info in element_infos:
            score = np.log(density_of_text_std) * \
                    element_info.density_of_text * \
                    np.log10(element_info.number_of_p_tag + 2) * \
                    np.log(element_info.density_of_punctuation)
            element_info.density_score = score
        
        # sort element info by density_score
        element_infos = sorted(element_infos, key=lambda x: x.density_score, reverse=True)
        element_info_first = element_infos[0] if element_infos else None
        if not element_info_first:
            return None
        text = '\n'.join(element_info_first.element.xpath('.//p//text()'))
        return text


content_extractor = ContentExtractor()


def extract_content(html):
    """
    extract content from detail html
    :return:
    """
    return content_extractor.extract(html)
