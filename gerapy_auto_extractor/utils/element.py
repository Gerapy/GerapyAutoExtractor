import re
import numpy as np
from os.path import exists
from types import ModuleType
from collections import defaultdict
from loguru import logger
from lxml.html import fromstring, HtmlElement
from gerapy_auto_extractor.schemas.element import Element
from gerapy_auto_extractor.utils.similarity import similarity

PUNCTUATION = set('''！，。？、；：“”‘’《》%（）<>{}「」【】*～`,.?:;'"!%()''')


def remove_element(element: Element):
    """
    remove child element from parent
    :param element:
    :return:
    """
    if element is None:
        return
    p = element.getparent()
    if p is not None:
        p.remove(element)


def remove_children(element: Element, xpaths):
    """
    remove children from element
    :param element:
    :param xpaths:
    :return:
    """
    if element is None:
        return
    if not xpaths:
        return
    for xpath in xpaths:
        nodes = element.xpath(xpath)
        for node in nodes:
            remove_element(node)
    return element


def html2element(html: str):
    """
    convert html to HtmlElement
    :param html:
    :return:
    """
    if not html:
        return None
    element = fromstring(html)
    element.__class__ = Element
    return element


def file2element(file_path):
    """
    convert file to element
    :param file_path:
    :return:
    """
    if not exists(file_path):
        return
    with open(file_path, encoding='utf-8') as f:
        return html2element(f.read())


def selector(element: Element):
    """
    get id using recursive function.
    for example result: html/body/div/div/ul/li
    :param element:
    :return:
    """
    if element is None:
        return ''
    p = parent(element)
    if p is not None:
        return selector(p) + '>' + alias(element)
    return element.alias


def path_raw(element: Element):
    """
    get tag path using recursive function, only contains raw tag
    for example result: html/body/div/div/ul/li
    :param element:
    :return:
    """
    if element is None:
        return ''
    p = parent(element)
    if p is not None:
        return path_raw(p) + '/' + element.tag
    return element.tag


def path(element: Element):
    """
    get tag path using recursive function.
    for example result: html/body/div/div/ul/li
    :param element:
    :return:
    """
    if element is None:
        return ''
    result = path_raw(element)
    # get nth-child
    nth = len(list(element.itersiblings(preceding=True))) + 1
    result += f':nth-child({nth})'
    return result


def a_descendants(element: Element):
    """
    get
    :param element:
    :return:
    """
    if element is None:
        return []
    descendants = []
    for descendant in element.xpath('.//a'):
        descendant.__class__ = Element
        descendants.append(descendant)
    return descendants


def a_descendants_group(element: Element):
    """
    get linked descendants group
    :param element:
    :return:
    """
    result = defaultdict(list)
    for linked_descendant in element.a_descendants:
        p = linked_descendant.path_raw
        result[p].append(linked_descendant)
    return result


def parent(element: Element):
    """
    get parent of element
    :param element:
    :return:
    """
    if element is None:
        return None
    parent = element.getparent()
    if isinstance(parent, ModuleType):
        parent.__class__ = Element
    return parent


def children(element: Element, including=False):
    """
    get children
    :param element:
    :param including:
    :return:
    """
    if element is None:
        return []
    if including:
        yield element
    for child in element.iterchildren():
        if isinstance(child, HtmlElement):
            child.__class__ = Element
            yield child


def siblings(element: Element, including=False):
    """
    get siblings of element
    :param element:
    :param including: include current element or not
    :return:
    """
    if element is None:
        return []
    if including:
        yield element
    for sibling in element.itersiblings(preceding=True):
        if isinstance(sibling, HtmlElement):
            sibling.__class__ = Element
            yield sibling
    for sibling in element.itersiblings(preceding=False):
        if isinstance(sibling, HtmlElement):
            sibling.__class__ = Element
            yield sibling


def descendants(element: Element, including=False):
    """
    get descendants clement of specific element
    :param element: parent element
    :param including: including current element or not
    :return:
    """
    if element is None:
        return []
    if including:
        yield element
    for descendant in element.iterdescendants():
        if isinstance(descendant, HtmlElement):
            descendant.__class__ = Element
            yield descendant


def alias(element: Element):
    """
    get alias of element, concat tag and attribs
    :param element:
    :return:
    """
    if element is None:
        return ''
    tag = element.tag
    # skip nth-child
    if tag in ['html', 'body']:
        return tag
    attribs = [tag]
    for k, v in element.attrib.items():
        k, v = re.sub(r'\s*', '', k), re.sub(r'\s*', '', v)
        attribs.append(f'[{k}="{v}"]' if v else f'[{k}]')
    result = ''.join(attribs)
    # get nth-child
    nth = len(list(element.itersiblings(preceding=True))) + 1
    result += f':nth-child({nth})'
    return result


def children_of_head(element: Element):
    """
    get children element of body element
    :param element:
    :return:
    """
    if element is None:
        return []
    body_xpath = '//head'
    body_element = element.xpath(body_xpath)
    if body_element:
        body_element.__class__ = Element
        return descendants(body_element, True)
    return []


def descendants_of_body(element: Element):
    """
    get descendants element of body element
    :param element:
    :return:
    """
    if element is None:
        return []
    body_xpath = '//body'
    elements = element.xpath(body_xpath)
    if elements:
        elements[0].__class__ = Element
        return list(descendants(elements[0], True))
    return []


def text(element: Element):
    """
    get text of element
    :param element:
    :return:
    """
    if element is None:
        return 0
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    return text


def number_of_char(element: Element):
    """
    get number of char, for example, result of `<a href="#">hello</a>world` = 10
    :param element:
    :return: length
    """
    if element is None:
        return 0
    return len(text(element))


def number_of_a_char(element: Element):
    """
    get number of linked char, for example, result of `<a href="#">hello</a>world` = 5
    :param element:
    :return: length
    """
    if element is None:
        return 0
    text = ''.join(element.xpath('.//a//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    return len(text)


def number_of_a_char_log10(element: Element):
    """
    get number of linked char, to log10
    :param element:
    :return: length
    """
    if element is None:
        return 0
    return np.log10(number_of_a_char(element) + 1)


def number_of_p_children(element: Element):
    """
    get number of p tags in children
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(element.xpath('./p'))


def number_of_p_descendants(element: Element):
    """
    get number of p tags in descendants
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(element.xpath('.//p'))


def number_of_p_descendants_log10(element: Element):
    """
    get number of p tags, to log10
    :param element:
    :return:
    """
    if element is None:
        return 0
    return np.log10(number_of_p_descendants(element))


def number_of_a_descendants(element: Element):
    """
    get number of a tags in this element
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(element.xpath('.//a'))


def number_of_punctuation(element: Element):
    """
    get number of punctuation of text in this element
    :param element:
    :return:
    """
    if element is None:
        return 0
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    punctuations = [c for c in text if c in PUNCTUATION]
    return len(punctuations)


def number_of_descendants(element: Element):
    """
    get number of descendants
    :param element:
    :return:
    """
    if element is None:
        return 0
    # return len(element.xpath('.//*'))
    return len(list(descendants(element, including=False)))


def number_of_siblings(element: Element):
    """
    get number of siblings
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(list(siblings(element, including=False)))


def number_of_clusters(element: Element, tags=None):
    """
    get number of clusters
    :param element:
    :return:
    """
    from gerapy_auto_extractor.extractors.list import LIST_MIN_NUMBER, LIST_MAX_LENGTH, LIST_MIN_LENGTH, \
        SIMILARITY_THRESHOLD
    if element is None:
        return 0
    if tags and not isinstance(tags, (list, tuple)):
        logger.error('you must pass tags arg as list or tuple')
    descendants_tree = defaultdict(list)
    descendants = descendants_of_body(element)
    for descendant in descendants:
        # if one element does not have enough siblings, it can not become a child of candidate element
        if descendant.number_of_siblings + 1 < LIST_MIN_NUMBER:
            continue
        # if min length is larger than specified max length, it can not become a child of candidate element
        if descendant.a_descendants_group_text_min_length > LIST_MAX_LENGTH:
            continue
        # if max length is smaller than specified min length, it can not become a child of candidate element
        if descendant.a_descendants_group_text_max_length < LIST_MIN_LENGTH:
            continue
        # descendant element must have same siblings which their similarity should not below similarity_threshold
        if descendant.similarity_with_siblings < SIMILARITY_THRESHOLD:
            continue
        # filter tag
        if tags and descendant.tag not in tags:
            continue
        descendants_tree[descendant.parent_selector].append(descendant)
    return len(descendants_tree)


def number_of_children(element: Element):
    """
    get number of children
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(list(children(element)))


def density_of_text(element: Element):
    """
    get density of text, using:
               number_of_char - number_of_a_char
    result = ------------------------------------------
               number_of_descendants - number_of_a_descendants
    :return:
    """
    # if denominator is 0, just return 0
    if element.number_of_descendants - element.number_of_a_descendants == 0:
        return 0
    return (element.number_of_char - element.number_of_a_char) / \
           (element.number_of_descendants - element.number_of_a_descendants)


def density_of_punctuation(element: Element):
    """
    get density of punctuation, using
                number_of_char - number_of_linked_char
    result = -----------------------------------------
                 number_of_punctuation + 1
    :param element:
    :return:
    """
    result = (element.number_of_char - element.number_of_a_char) / \
             (element.number_of_punctuation + 1)
    # result should not be zero
    return result or 1


def similarity_with_element(element1: Element, element2: Element):
    """
    get similarity between two elements
    :param element1:
    :param element2:
    :return:
    """
    alias1 = element1.alias
    alias2 = element2.alias
    # TODO: use better metrics to compare the two elements
    return similarity(alias1, alias2)


def similarity_with_siblings(element: Element):
    """
    get similarity with siblings
    :param element:
    :return:
    """
    scores = []
    for sibling in siblings(element):
        # TODO: maybe compare all children not only alias
        scores.append(similarity_with_element(element, sibling))
    if not scores:
        return 0
    return np.mean(scores)
