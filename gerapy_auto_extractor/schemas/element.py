from lxml.html import HtmlElement


class Element(HtmlElement):
    id: int = None
    alias: str = None
    tag_name: str = None
    element: HtmlElement = None
    parent_id: int = None
    number_of_char: int = None
    number_of_linked_char: int = None
    number_of_tag: int = None
    number_of_linked_tag: int = None
    number_of_p_tag: int = None
    number_of_punctuation: int = None
    number_of_children: int = None
    number_of_descendants: int = None
    density_of_punctuation: int = None
    density_of_text: float = None
    density_score: float = None
    similarity_with_siblings: float = None
