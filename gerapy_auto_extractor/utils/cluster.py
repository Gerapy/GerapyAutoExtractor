from gerapy_auto_extractor.utils.similarity import similarity
from collections import defaultdict


def cluster(items, threshold=0.9):
    """
    cluster names
    :param items:
    :param threshold:
    :return: cluster map, for example {"foo": 0, "bar": 1}
    """
    number = -1
    clusters_map = {}
    clusters = []
    for name in items:
        for c in clusters:
            if all(similarity(name, w) > threshold for w in c):
                c.append(name)
                clusters_map[name] = number
                break
        else:
            number += 1
            clusters.append([name])
            clusters_map[name] = number
    return clusters_map


def cluster_dict(data: dict):
    """
    cluster dict, convert id key to cluster id key
    :param data:
    :return:
    """
    ids = data.keys()
    clusters_map = cluster(ids)
    result = defaultdict(list)
    for k, v in data.items():
        if isinstance(v, list):
            for i in v:
                result[clusters_map[k]].append(i)
        else:
            result[clusters_map[k]].append(v)
    return dict(result)
