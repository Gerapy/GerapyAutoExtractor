import numpy as np
import pandas as pd
from lxml.html import HtmlElement
from collections import defaultdict
from gerapy_auto_extractor.utils.element_info import similarity_with_siblings
from gerapy_auto_extractor.utils.preprocess import preprocess4list
from gerapy_auto_extractor.extractors.base import BaseExtractor
from gerapy_auto_extractor.utils.element import descendants_of_body, alias, number_of_descendants, parent
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
        element_infos_tree = defaultdict(list)
        descendants = descendants_of_body(element)
        
        for descendant in descendants:
            # new element info
            element_info = ElementInfo()
            element_info.element = descendant
            
            element_info.similarity_with_siblings = similarity_with_siblings(element_info)
            element_info.number_of_descendants = number_of_descendants(element_info.element)
            element_info.parent_id = hash(parent(element_info.element))
            print('similarity_with_siblings', element_info.similarity_with_siblings)
            print('number_of_descendants', element_info.number_of_descendants)
            print('alias', element_info.alias)
            print('parent_id', element_info.parent_id)
            print('=' * 20)
            element_infos.append(element_info)
            # collect tree
            element_infos_tree[element_info.parent_id].append(element_info)


list_extractor = ListExtractor()


def extract_list(html):
    """
    extract list from index html
    :return:
    """
    return list_extractor.extract(html)
