import numpy as np
import pandas as pd
from lxml.html import HtmlElement
from gerapy_auto_extractor.utils.preprocess import preprocess4list
from gerapy_auto_extractor.extractors.base import BaseExtractor
from gerapy_auto_extractor.utils.element import children_of_body, fill_element_info
from gerapy_auto_extractor.schemas.element import ElementInfo


class ListExtractor(BaseExtractor):
    """
    extract list from index page
    """
    
    def process(self, element: HtmlElement):
        """
        extract content from html
        :param element:
        :return:
        """
        # preprocess
        preprocess4list(element)
        
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
        result = []
        
        for element_info in element_infos:
            result.append({
                'html': self.to_string(element_info.element, 100),
                'density_score': element_info.density_score,
                'density_of_text': element_info.density_of_text,
                'number_of_char': element_info.number_of_char,
                'number_of_linked_char': element_info.number_of_linked_char,
                'number_of_tag': element_info.number_of_tag,
                'number_of_linked_tag': element_info.number_of_linked_tag,
                'number_of_p_tag': element_info.number_of_p_tag,
                'number_of_punctuation': element_info.number_of_punctuation,
                'density_of_punctuation': element_info.density_of_punctuation,
            })
        df = pd.DataFrame(result)
        df.to_csv('result.csv')
        df.to_excel('result.xlsx')


list_extractor = ListExtractor()


def extract_list(html):
    """
    extract list from index html
    :return:
    """
    return list_extractor.extract(html)
