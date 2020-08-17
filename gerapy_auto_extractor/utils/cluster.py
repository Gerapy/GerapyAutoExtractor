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


def cluster_dict(data: dict, threshold=0.8):
    """
    cluster dict, convert id key to cluster id key
    :param threshold:
    :param data:
    :return:
    """
    ids = data.keys()
    clusters_map = cluster(ids, threshold)
    result = defaultdict(list)
    for k, v in data.items():
        if isinstance(v, list):
            for i in v:
                result[clusters_map[k]].append(i)
        else:
            result[clusters_map[k]].append(v)
    return dict(result)


if __name__ == '__main__':
    data = {
        '/html/body/div[@class="main"]/div[1]/ul': ['child1', 'child2', 'child3'],
        '/html/body/div[@class="main"]/div[2]/ul': ['child4', 'child5', 'child6'],
        '/html/body/div[@class="main"]/div[3]/ul': ['child7', 'child8', 'child9'],
        '/html/body/header/div[1]': ['child10', 'child11', 'child12'],
        '/html/body/header/div[2]': ['child13', 'child14', 'child15'],
    }
    print(cluster_dict(data, threshold=0.7))
