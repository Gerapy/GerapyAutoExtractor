from lxml.html import HtmlElement
from pydantic import BaseModel





class ElementInfo(BaseModel):
    id: int = None
    tag_name: str = None
    element: HtmlElement = None
    number_of_char: int = 0
    number_of_linked_char: int = 0
    number_of_tag: int = 0
    number_of_linked_tag: int = 0
    number_of_p_tag: int = 0
    number_of_punctuation: int = 0
    density_of_punctuation: int = 1
    density_of_text: int = 0
    density_score: int = 0
    
    
    
    class Config:
        arbitrary_types_allowed = True
    