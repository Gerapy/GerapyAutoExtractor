from collections import defaultdict

from numpy import mean

from gerapy_auto_extractor.utils.element import similarity_with_siblings
from gerapy_auto_extractor.utils.preprocess import preprocess4list
from gerapy_auto_extractor.extractors.base import BaseExtractor
from gerapy_auto_extractor.utils.element import descendants_of_body, alias, number_of_descendants, parent
from gerapy_auto_extractor.schemas.element import Element


class ListExtractor(BaseExtractor):
    """
    extract list from index page
    """
    
    def process(self, element: Element):
        """
        extract content from html
        :param element:
        :return:
        """
        # preprocess
        preprocess4list(element)
        
        # start to evaluate every child element
        # element_infos = []
        descendants_tree = defaultdict(list)
        descendants = descendants_of_body(element)
        
        for descendant in descendants:
            descendant.similarity_with_siblings = similarity_with_siblings(descendant)
            descendant.number_of_descendants = number_of_descendants(descendant)
            descendant.parent_id = hash(parent(descendant))
            # collect tree
            descendants_tree[descendant.parent_id].append(descendant)
        
        # get max similarity_with_siblings
        similarity_with_siblings_max = 0
        similarity_with_siblings_max_parent_id = None
        for id, children in descendants_tree.items():
            similarity_with_siblings_list = []
            for child in children:
                similarity_with_siblings_list.append(child.similarity_with_siblings)
            similarity_with_siblings_mean = mean(similarity_with_siblings_list)
            if similarity_with_siblings_mean > similarity_with_siblings_max:
                similarity_with_siblings_max = similarity_with_siblings_mean
                similarity_with_siblings_max_parent_id = id
        print('similarity_with_siblings_max', similarity_with_siblings_max)
        print('similarity_with_siblings_max_parent_id', similarity_with_siblings_max_parent_id)
        
        # print child
        for child in descendants_tree[similarity_with_siblings_max_parent_id]:
            print('similarity_with_siblings', child.similarity_with_siblings)
            print('number_of_descendants', child.number_of_descendants)
            print('child', child.similarity_with_siblings)
            print('alias', child.alias)
        
        
        #
        

list_extractor = ListExtractor()


def extract_list(html):
    """
    extract list from index html
    :return:
    """
    return list_extractor.extract(html)
