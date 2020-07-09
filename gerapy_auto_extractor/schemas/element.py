from lxml.html import HtmlElement, etree
from numpy import mean


class Element(HtmlElement):
    _id: int = None
    _selector: str = None
    _parent_selector: str = None
    _alias: str = None
    _tag_name: str = None
    _path: str = None
    _path_raw: str = None
    _children = None
    _parent = None
    _siblings = None
    _descendants = None
    _text = None
    _number_of_char: int = None
    _number_of_a_char: int = None
    _number_of_punctuation: int = None
    _number_of_a_descendants: int = None
    _number_of_p_descendants: int = None
    _number_of_children: int = None
    _number_of_siblings: int = None
    _number_of_descendants: int = None
    _density_of_punctuation: int = None
    _density_of_text: float = None
    _density_score: float = None
    _similarity_with_siblings: float = None
    _a_descendants: list = None
    _a_descendants_group: dict = None
    _a_descendants_group_text_length: dict = None
    _a_descendants_group_text_min_length: float = None
    _a_descendants_group_text_max_length: float = None
    
    density_score: float = None
    
    @property
    def id(self):
        """
        get id by hashed element
        :return:
        """
        if self._id is not None:
            return self._id
        self._id = hash(self)
        return self._id
    
    @property
    def nth(self):
        """
        get nth index of this element in parent element
        :return:
        """
        return len(list(self.itersiblings(preceding=True))) + 1
    
    
    @property
    def alias(self):
        """
        get alias of element, using all attributes to construct it.
        :return: string
        """
        if self._alias is not None:
            return self._alias
        from gerapy_auto_extractor.utils.element import alias
        self._alias = alias(self)
        return self._alias
    
    @property
    def selector(self):
        """
        get id by hashed element
        :return:
        """
        if self._selector is not None:
            return self._selector
        from gerapy_auto_extractor.utils.element import selector
        self._selector = selector(self)
        return self._selector
    
    @property
    def children(self):
        """
        get children of this element
        :return: 
        """
        if self._children is not None:
            return self._children
        from gerapy_auto_extractor.utils.element import children
        self._children = list(children(self))
        return self._children
    
    @property
    def siblings(self):
        """
        get siblings of this element
        :return: 
        """
        if self._siblings is not None:
            return self._siblings
        from gerapy_auto_extractor.utils.element import siblings
        self._siblings = list(siblings(self))
        return self._siblings
    
    @property
    def descendants(self):
        """
        get descendants of this element
        :return: 
        """
        if self._descendants is not None:
            return self._descendants
        from gerapy_auto_extractor.utils.element import descendants
        self._descendants = list(descendants(self))
        return self._descendants
    
    @property
    def parent_selector(self):
        """
        get id by hashed element
        :return:
        """
        if self._parent_selector is not None:
            return self._parent_selector
        from gerapy_auto_extractor.utils.element import selector, parent
        # TODO: change parent(self) to self.parent
        p = parent(self)
        if p is not None:
            self._parent_selector = selector(p)
        return self._parent_selector
    
    @property
    def tag_name(self):
        """
        return tag name
        :return:
        """
        if self._tag_name:
            return self._tag_name
        self._tag_name = self.tag
        return self._tag_name
    
    @property
    def text(self):
        """
        get text of element
        :return:
        """
        if self._text is not None:
            return self._text
        from gerapy_auto_extractor.utils.element import text
        self._text = text(self)
        return self._text
    
    @property
    def string(self):
        """
        return string of element
        :return:
        """
        return etree.tostring(self, pretty_print=True, encoding="utf-8", method='html').decode('utf-8')
    
    @property
    def path(self):
        """
        get tag path using external path function
        :return:
        """
        if self._path is not None:
            return self._path
        from gerapy_auto_extractor.utils.element import path
        self._path = path(self)
        return self._path
    
    @property
    def path_raw(self):
        """
        get tag raw path using external path raw function
        :return:
        """
        if self._path_raw is not None:
            return self._path_raw
        from gerapy_auto_extractor.utils.element import path_raw
        self._path_raw = path_raw(self)
        return self._path_raw
    
    @property
    def number_of_char(self):
        """
        get text length
        :return:
        """
        if self._number_of_char is not None:
            return self._number_of_char
        from gerapy_auto_extractor.utils.element import number_of_char
        self._number_of_char = number_of_char(self)
        return self._number_of_char
    
    @property
    def number_of_a_descendants(self):
        """
        get number of a descendants
        :return:
        """
        if self._number_of_a_descendants is not None:
            return self._number_of_a_descendants
        from gerapy_auto_extractor.utils.element import number_of_a_descendants
        self._number_of_a_descendants = number_of_a_descendants(self)
        return self._number_of_a_descendants
    
    @property
    def number_of_a_char(self):
        """
        get a text length
        :return:
        """
        if self._number_of_a_char is not None:
            return self._number_of_a_char
        from gerapy_auto_extractor.utils.element import number_of_a_char
        self._number_of_a_char = number_of_a_char(self)
        return self._number_of_a_char
    
    @property
    def number_of_p_descendants(self):
        """
        return number of paragraph
        :return:
        """
        if self._number_of_p_descendants is not None:
            return self._number_of_p_descendants
        from gerapy_auto_extractor.utils.element import number_of_p_descendants
        self._number_of_p_descendants = number_of_p_descendants(self)
        return self._number_of_p_descendants
    
    @property
    def number_of_punctuation(self):
        """
        get number of punctuation
        :return:
        """
        if self._number_of_punctuation is not None:
            return self._number_of_punctuation
        from gerapy_auto_extractor.utils.element import number_of_punctuation
        self._number_of_punctuation = number_of_punctuation(self)
        return self._number_of_punctuation
    
    @property
    def number_of_children(self):
        """
        get children number
        :return:
        """
        if self._number_of_children is not None:
            return self._number_of_children
        self._number_of_children = len(list(self.children))
        return self._number_of_children
    
    @property
    def number_of_siblings(self):
        """
        get number of siblings
        :return:
        """
        if self._number_of_siblings is not None:
            return self._number_of_siblings
        self._number_of_siblings = len(list(self.siblings))
        return self._number_of_siblings
    
    @property
    def number_of_descendants(self):
        """
        get number of descendants
        :return:
        """
        if self._number_of_descendants is not None:
            return self._number_of_descendants
        from gerapy_auto_extractor.utils.element import number_of_descendants
        self._number_of_descendants = len(list(self.descendants))
        return self._number_of_descendants
    
    @property
    def density_of_punctuation(self):
        """
        get density of punctuation
        :return:
        """
        if self._density_of_punctuation is not None:
            return self._density_of_punctuation
        from gerapy_auto_extractor.utils.element import density_of_punctuation
        self._density_of_punctuation = density_of_punctuation(self)
        return self._density_of_punctuation
    
    @property
    def density_of_text(self):
        """
        get density of text
        :return:
        """
        if self._density_of_text is not None:
            return self._density_of_text
        from gerapy_auto_extractor.utils.element import density_of_text
        self._density_of_text = density_of_text(self)
        return self._density_of_text
    
    @property
    def similarity_with_siblings(self):
        """
        get similarity with siblings
        :return:
        """
        if self._similarity_with_siblings is not None:
            return self._similarity_with_siblings
        from gerapy_auto_extractor.utils.element import similarity_with_siblings
        self._similarity_with_siblings = similarity_with_siblings(self)
        return self._similarity_with_siblings
    
    @property
    def a_descendants(self):
        """
        get linked descendants
        :return:
        """
        if self._a_descendants is not None:
            return self._a_descendants
        from gerapy_auto_extractor.utils.element import a_descendants
        self._a_descendants = a_descendants(self)
        return self._a_descendants
    
    @property
    def a_descendants_group(self):
        """
        get linked descendants group
        :return:
        """
        if self._a_descendants_group is not None:
            return self._a_descendants_group
        from gerapy_auto_extractor.utils.element import a_descendants_group
        self._a_descendants_group = a_descendants_group(self)
        return self._a_descendants_group
    
    @property
    def a_descendants_group_text_length(self):
        """
        grouped linked text length
        :return:
        """
        if self._a_descendants_group_text_length is not None:
            return self._a_descendants_group_text_length
        result = {}
        from gerapy_auto_extractor.utils.element import text
        for path, elements in self.a_descendants_group.items():
            lengths = []
            for element in elements:
                # TODO: convert len(text(element)) to element.number_of_char
                lengths.append(len(text(element)))
            mean_length = mean(lengths) if len(lengths) else 0
            result[path] = mean_length
        return result
    
    @property
    def a_descendants_group_text_min_length(self):
        """
        get grouped linked text min length
        :return:
        """
        if self._a_descendants_group_text_min_length is not None:
            return self._a_descendants_group_text_min_length
        values = self.a_descendants_group_text_length.values()
        self._a_descendants_group_text_min_length = min(values) if values else 0
        return self._a_descendants_group_text_min_length
    
    @property
    def a_descendants_group_text_max_length(self):
        """
        get grouped linked text max length
        :return:
        """
        if self._a_descendants_group_text_max_length is not None:
            return self._a_descendants_group_text_max_length
        values = self.a_descendants_group_text_length.values()
        self._a_descendants_group_text_max_length = max(values) if values else 0
        return self._a_descendants_group_text_max_length
    
    @property
    def a_descendants_group_text_avg_length(self):
        """
        get grouped linked text avg length
        :return:
        """
        if self._a_descendants_group_text_max_length is not None:
            return self._a_descendants_group_text_max_length
        values = self.a_descendants_group_text_length.values()
        self._a_descendants_group_text_max_length = max(values) if values else 0
        return self._a_descendants_group_text_max_length
    
    def __str__(self):
        """
        rewrite str
        :return:
        """
        return f'<Element {self.tag} of {self.path}>'
    
    def __repr__(self):
        """
        rewrite repr
        :return:
        """
        return self.__str__()
