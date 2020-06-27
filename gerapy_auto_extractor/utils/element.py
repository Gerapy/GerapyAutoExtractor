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
    parent = element.getparent()
    if parent is not None:
        parent.remove(element)


def remove_children(element: HtmlElement, xpaths=None):
    """
    remove children from element
    :param element:
    :param xpaths:
    :return:
    """
    if not xpaths:
        return
    for xpath in xpaths:
        nodes = element.xpath(xpath)
        for node in nodes:
            remove_element(node)
    return element


def html2element(html: str) -> HtmlElement:
    """
    convert html to HtmlElement
    :param html:
    :return:
    """
    element = fromstring(html)
    return element


def children(element: HtmlElement):
    """
    get children clement of specific element
    :param element: parent element
    :return:
    """
    yield element
    for child_element in element:
        if isinstance(child_element, HtmlElement):
            yield from children(child_element)


def children_of_head(element: HtmlElement):
    """
    get children element of body element
    :param element:
    :return:
    """
    body_xpath = '//head'
    body_element = element.xpath(body_xpath)
    if body_element:
        return children(body_element)
    return []


def children_of_body(element: HtmlElement):
    """
    get children element of body element
    :param element:
    :return:
    """
    body_xpath = '//body'
    elements = element.xpath(body_xpath)
    if elements:
        return children(elements[0])
    return []


def number_of_char(element: HtmlElement):
    """
    get number of char, for example, result of `<a href="#">hello</a>world` = 10
    :param element:
    :return: length
    """
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    return len(text)


def number_of_linked_char(element: HtmlElement):
    """
    get number of linked char, for example, result of `<a href="#">hello</a>world` = 5
    :param element:
    :return: length
    """
    text = ''.join(element.xpath('.//a//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    return len(text)


def number_of_tag(element: HtmlElement):
    """
    get number of all tags in this element
    :param element:
    :return:
    """
    return len(element.xpath('.//*'))


def number_of_p_tag(element: HtmlElement):
    """
    get number of p tags
    :param element:
    :return:
    """
    return len(element.xpath('.//p'))


def number_of_linked_tag(element: HtmlElement):
    """
    get number of a tags in this element
    :param element:
    :return:
    """
    return len(element.xpath('.//a'))


def density_of_text(element_info: ElementInfo):
    """
    get density of text, using:
               number_of_char - number_of_linked_char
    result = ------------------------------------------
               number_of_tags - number_of_linked_tags
    :param element_info:
    :return:
    """
    # if denominator is 0, just return 0
    if element_info.number_of_tag - element_info.number_of_linked_tag == 0:
        return 0
    return (element_info.number_of_char - element_info.number_of_linked_char) / \
           (element_info.number_of_tag - element_info.number_of_linked_tag)


def density_of_punctuation(element_info: ElementInfo):
    """
    get density of punctuation, using
                number_of_char - number_of_linked_char
    result = -----------------------------------------
                 number_of_punctuation + 1
    :param element_info:
    :return:
    """
    result = (element_info.number_of_char - element_info.number_of_linked_char) / \
             (element_info.number_of_punctuation + 1)
    # result should not be zero
    return result or 1


def number_of_punctuation(element: HtmlElement):
    """
    get number of punctuation of text in this element
    :param element:
    :return:
    """
    text = ''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    punctuations = [c for c in text if c in PUNCTUATION]
    return len(punctuations)


def fill_element_info(element_info: ElementInfo):
    """
    calculate info of this element, for example, number of char
    :param element_info:
    :return:
    """
    element = element_info.element
    
    # fill id
    element_info.id = hash(element)
    element_info.tag_name = element.tag
    
    # fill number_of_char
    element_info.number_of_char = number_of_char(element)
    element_info.number_of_linked_char = number_of_linked_char(element)
    element_info.number_of_tag = number_of_tag(element)
    element_info.number_of_linked_tag = number_of_linked_tag(element)
    element_info.number_of_p_tag = number_of_p_tag(element)
    element_info.number_of_punctuation = number_of_punctuation(element)
    
    # fill density
    element_info.density_of_text = density_of_text(element_info)
    element_info.density_of_punctuation = density_of_punctuation(element_info)
    
    print('element fffff', element_info)
    print('=' * 20)
    return element_info


if __name__ == '__main__':
    t = html2element('<a>dsdsjfkjsd年底红啊，但是军事基地分，是打发时间《第三方的身份》水电费水电费舒服的</a>')
    print(number_of_punctuation(t))
