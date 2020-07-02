from gerapy_auto_extractor.schemas.element import ElementInfo
from gerapy_auto_extractor.utils.element import number_of_char, number_of_linked_char, number_of_tag, \
    number_of_linked_tag, number_of_p_tag, number_of_punctuation, siblings, alias
from gerapy_auto_extractor.utils.similarity import similarity
from numpy import mean


def density_of_text(element_info: ElementInfo):
    """
    get density of text, using:
               number_of_char - number_of_linked_char
    result = ------------------------------------------
               number_of_tags - number_of_linked_tags
    :param element_info:
    :return:
    """
    if element_info.number_of_char is None:
        element_info.number_of_char = number_of_char(element_info.element)
    
    if element_info.number_of_linked_char is None:
        element_info.number_of_linked_char = number_of_linked_char(element_info.element)
    
    if element_info.number_of_tag is None:
        element_info.number_of_tag = number_of_tag(element_info.element)
    
    if element_info.number_of_linked_tag is None:
        element_info.number_of_linked_tag = number_of_linked_tag(element_info.element)
    
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
    if element_info.number_of_char is None:
        element_info.number_of_char = number_of_char(element_info.element)
    
    if element_info.number_of_linked_char is None:
        element_info.number_of_linked_char = number_of_linked_char(element_info.element)
    
    if element_info.number_of_punctuation is None:
        element_info.number_of_punctuation = number_of_punctuation(element_info.element)
    
    result = (element_info.number_of_char - element_info.number_of_linked_char) / \
             (element_info.number_of_punctuation + 1)
    # result should not be zero
    return result or 1


def similarity_with_siblings(element_info: ElementInfo):
    """
    get similarity with siblings
    :param element:
    :return:
    """
    element = element_info.element
    if not element_info.alias:
        element_info.alias = alias(element)
    scores = []
    for sibling in siblings(element):
        sibling_alias = alias(sibling)
        scores.append(similarity(element_info.alias, sibling_alias))
    if not scores:
        return 0
    return mean(scores)


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
    return element_info
