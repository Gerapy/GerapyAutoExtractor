from gerapy_auto_extractor.classifiers.list import probability_of_list


def probability_of_detail(html, **kwargs):
    """
    get probability of detail page
    :param html:
    :param kwargs: other kwargs
    :return:
    """
    return 1 - probability_of_list(html, **kwargs)


def is_detail(html, threshold=0.5, **kwargs):
    """
    judge if this page is detail page
    :param html: source of html
    :param threshold:
    :param kwargs:
    :return:
    """
    _probability_of_detail = probability_of_detail(html, **kwargs)
    if _probability_of_detail > threshold:
        return True
    return False
