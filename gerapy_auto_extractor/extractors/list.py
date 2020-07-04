import re

from numpy import mean
from collections import defaultdict

from gerapy_auto_extractor.utils.cluster import cluster_dict
from gerapy_auto_extractor.utils.element import similarity_with_siblings, number_of_linked_tag, linked_descendants, \
    text, siblings
from gerapy_auto_extractor.utils.preprocess import preprocess4list
from gerapy_auto_extractor.extractors.base import BaseExtractor
from gerapy_auto_extractor.utils.element import descendants_of_body, number_of_siblings, number_of_descendants, parent
from gerapy_auto_extractor.schemas.element import Element

LIST_MIN_NUMBER = 5
LIST_MIN_LENGTH = 8
LIST_MAX_LENGTH = 35
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
        clusters = cluster_dict(descendants_tree)
        
        # choose best cluster using score
        clusters_score = defaultdict(dict)
        clusters_score_arg_max = 0
        clusters_score_max = -1
        for cluster_id, cluster in clusters.items():
            clusters_score[cluster_id]['avg_similarity_with_siblings'] = mean(
                [element.similarity_with_siblings for element in cluster])
            # TODO: add more quota to select best cluster
            clusters_score[cluster_id]['clusters_score'] = clusters_score[cluster_id]['avg_similarity_with_siblings']
            if clusters_score[cluster_id]['clusters_score'] > clusters_score_max:
                clusters_score_max = clusters_score[cluster_id]['clusters_score']
                clusters_score_arg_max = cluster_id
        print(clusters_score)
        best_cluster = clusters[clusters_score_arg_max]
        
        # extract link from clusters
        result = []
        for element in best_cluster:
            descendants = element.linked_descendants
            for descendant in descendants:
                descendant_text = text(descendant)
                if not descendant_text or len(
                        descendant_text) < self.min_length:
                    continue
                href = descendant.attrib.get('href')
                if not href:
                    continue
                result.append({
                    'title': descendant_text,
                    'href': href
                })
        return result


list_extractor = ListExtractor()


def extract_list(html):
    """
    extract list from index html
    :return:
    """
    return list_extractor.extract(html)
