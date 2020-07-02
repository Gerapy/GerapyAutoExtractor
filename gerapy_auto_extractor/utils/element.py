from lxml.html import fromstring, HtmlElement
from gerapy_auto_extractor.schemas.element import ElementInfo
import re

PUNCTUATION = set('''！，。？、；：“”‘’《》%（）<>{}「」【】*～`,.?:;'"!%()''')


def remove_element(element: HtmlElement):
    """
    remove child element from parent
    :param element:
    :return:
    """
    if element is None:
        return
    parent = element.getparent()
    if parent is not None:
        parent.remove(element)


def remove_children(element: HtmlElement, xpaths):
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
    return element


def parent(element: HtmlElement):
    """
    get parent of element
    :param element:
    :return:
    """
    if element is None:
        return None
    return element.getparent()


def children(element: HtmlElement, including=False):
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
            yield child


def siblings(element: HtmlElement, including=False):
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
    for sibling in element.itersiblings():
        if isinstance(sibling, HtmlElement):
            yield sibling


def descendants(element: HtmlElement, including=False):
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
            yield descendant


def alias(element: HtmlElement):
    """
    get alias of element, concat tag and attribs
    :param element:
    :return:
    """
    if element is None:
        return ''
    tag = element.tag
    attribs = [tag]
    for k, v in element.attrib.items():
        k, v = re.sub(r'\s*', '', k), re.sub(r'\s*', '', v)
        attribs.append(f'{k}={v}')
    return '#'.join(attribs)


def children_of_head(element: HtmlElement):
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
        return descendants(body_element, True)
    return []


def descendants_of_body(element: HtmlElement):
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
        return descendants(elements[0], True)
    return []


def number_of_char(element: HtmlElement):
    """
    get number of char, for example, result of `<a href="#">hello</a>world` = 10
    :param element:
    :return: length
    """
    if element is None:
        return 0
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    return len(text)


def number_of_linked_char(element: HtmlElement):
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


def number_of_tag(element: HtmlElement):
    """
    get number of all tags in this element
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(element.xpath('.//*'))


def number_of_p_tag(element: HtmlElement):
    """
    get number of p tags
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(element.xpath('.//p'))


def number_of_linked_tag(element: HtmlElement):
    """
    get number of a tags in this element
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(element.xpath('.//a'))


def number_of_punctuation(element: HtmlElement):
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


def number_of_descendants(element: HtmlElement):
    """
    get number of descendants
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(list(descendants(element, including=False)))


def number_of_children(element: HtmlElement):
    """
    get number of children
    :param element:
    :return:
    """
    if element is None:
        return 0
    return len(list(children(element)))
