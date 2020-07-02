from lxml.html import HtmlElement
from pydantic import BaseModel


class ElementInfo(BaseModel):
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
    
    class Config:
        arbitrary_types_allowed = True


class Element(HtmlElement):
    dist = None
    
    @classmethod
    def from_parent(cls, parent):
        return cls(**parent.__dict__)
    
    def __init__(self, *args, **kwargs):
        # Here we override the constructor method
        # and pass all the arguments to the parent __init__()
        
        super().__init__(*args, **kwargs)



