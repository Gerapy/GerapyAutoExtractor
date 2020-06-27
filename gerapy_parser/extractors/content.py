import re
import numpy as np
from lxml.html import etree, HtmlElement
from html import unescape

from gerapy_parser.utils.preprocess import preprocess4content
from gne.utils import iter_node, pad_host_for_images, config, get_high_weight_keyword_pattern
from gerapy_parser.extractors.base import BaseExtractor
from gerapy_parser.utils.element import children, children_of_body, fill_element_info
from gerapy_parser.schemas.element import ElementInfo


class ContentExtractor(BaseExtractor):
    def __init__(self, content_tag='p'):
        """

        :param content_tag: 正文内容在哪个标签里面
        """
        self.content_tag = content_tag
        self.node_info = {}
        self.high_weight_keyword_pattern = get_high_weight_keyword_pattern()
        self.punctuation = set('''！，。？、；：“”‘’《》%（）,.?:;'"!%()''')  # 常见的中英文标点符号
    
    def process(self, element: HtmlElement):
        """
        extract content from html
        :param element:
        :return:
        """
        # preprocess
        preprocess4content(element)
        
        with open('result.html', 'w', encoding='utf-8') as f:
            
        
            f.write(etree.tostring(element, pretty_print=True, encoding="utf-8", method='html').decode('utf-8'))
        # start to evaluate every child element
        element_infos = []
        child_elements = children_of_body(element)
        print('child', child_elements)
        for child_element in child_elements:
            print('child', child_element)
            # new element info
            element_info = ElementInfo()
            element_info.element = child_element
            element_info = fill_element_info(element_info)
            element_infos.append(element_info)
        
        density_of_text = [element_info.density_of_text for element_info in element_infos]
        density_of_text_std = np.std(density_of_text, ddof=1)
        
        # get score
        for element_info in element_infos:
            score = np.log(density_of_text_std) * \
                    element_info.density_of_text * \
                    np.log10(element_info.number_of_p_tag + 2) * \
                    np.log(element_info.density_of_punctuation)
            element_info.density_score = score
            
            print('element_info', element_info)
        
        element_infos = sorted(element_infos, key=lambda x: x.density_score, reverse=True)
        print('len', element_infos)
        
        count = 0
        for element_info in element_infos:
            print('element_info', element_info)
            print('element_info', ''.join(element_info.element.xpath('//text()')))
            print('=======')
            count += 1
            if count > 5:
                break


content_extractor = ContentExtractor()


def extract_content(html):
    """
    extract content from detail html
    :return:
    """
    return content_extractor.extract(html)
