import re

from numpy import mean
from collections import defaultdict

from gerapy_auto_extractor.utils.cluster import cluster_dict
from gerapy_auto_extractor.utils.element import similarity_with_siblings, number_of_linked_tag, linked_descendants
from gerapy_auto_extractor.utils.preprocess import preprocess4list
from gerapy_auto_extractor.extractors.base import BaseExtractor
from gerapy_auto_extractor.utils.element import descendants_of_body, number_of_siblings, number_of_descendants, parent
from gerapy_auto_extractor.schemas.element import Element

LIST_MIN_NUMBER = 5
LIST_MIN_LENGTH = 10
LIST_MAX_LENGTH = 30
SIMILARITY_THRESHOLD = 0.8


class ListExtractor(BaseExtractor):
    """
    extract list from index page
    """
    
    def __init__(self, min_number=LIST_MIN_NUMBER, min_length=LIST_MIN_LENGTH, max_length=LIST_MAX_LENGTH,
                 similarity_threshold=SIMILARITY_THRESHOLD):
        """
        init list extractor
        """
        super(ListExtractor, self).__init__()
        self.min_number = min_number
        self.min_length = min_length
        self.max_length = max_length
        self.similarity_threshold = similarity_threshold
    
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
            # descendant.id = hash(descendant)
            descendant.number_of_siblings = number_of_siblings(descendant)
            # if one element does not have enough siblings, this is not a child of candidate element
            if descendant.number_of_siblings + 1 < self.min_number:
                continue
            
            if descendant.linked_descendants_group_text_min_length > self.max_length:
                continue
            
            if descendant.linked_descendants_group_text_max_length < self.min_length:
                continue
            
            descendant.similarity_with_siblings = similarity_with_siblings(descendant)
            if descendant.similarity_with_siblings < self.similarity_threshold:
                continue
            descendants_tree[descendant.parent_selector].append(descendant)
        
        descendants_tree = dict(descendants_tree)
        
        # cut tree, remove parent block
        selectors = sorted(list(descendants_tree.keys()))
        last_selector = None
        for selector in selectors[::-1]:
            # if later selector
            if last_selector and selector and last_selector.startswith(selector):
                del descendants_tree[selector]
            last_selector = selector
        
        print(selectors)
        print(len(list(descendants_tree.keys())))
        exit()
        
        clusters = cluster_dict(descendants_tree)
        
        print('clusters', clusters)
        exit()
        clusters_score = defaultdict(dict)
        for cluster_id, cluster in clusters.items():
            clusters_score[cluster_id]['avg_similarity_with_siblings'] = mean(
                [element.similarity_with_siblings for element in cluster])
        
        print(clusters_score)
        
        exit()
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
            print('string', child.string)
            print('tag path', child.tag_path)
            print('linked_descendants', child.linked_descendants)
            print('linked_descendants', child.linked_descendants_group)
            print('linked_descendants', child.linked_descendants_group_text_min_length)
            print('linked_descendants', child.linked_descendants_group_text_max_length)
        #


list_extractor = ListExtractor()


def extract_list(html):
    """
    extract list from index html
    :return:
    """
    return list_extractor.extract(html)
