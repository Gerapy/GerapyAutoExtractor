import distance


def similarity1(s1, s2):
    """
    get similarity of two strings
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or not s2:
        return 0
    edit_distance = distance.levenshtein(s1, s2)
    similarity_score = 1 - edit_distance / (len(s1) + len(s2))
    return similarity_score


def similarity2(s1, s2):
    """
    get similarity of two strings
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or not s2:
        return 0
    s1_set = set(list(s1))
    s2_set = set(list(s2))
    intersection = s1_set.intersection(s2_set)
    union = s1_set.intersection(s2_set)
    return len(intersection) / len(union)


def similarity(s1, s2):
    """
    get similarity of two strings
    :param s1:
    :param s2:
    :return:
    """
    return similarity2(s1, s2)


if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'world'
    print(similarity(s1, s2))
