from lxml.html import HtmlElement, etree
from numpy import mean


class Element(HtmlElement):
    _id: int = None
    _selector: str = None
    _parent_selector: str = None
    _alias: str = None
    _tag_name: str = None
    _parent_id: int = None
    _number_of_char: int = None
    _number_of_linked_char: int = None
    _number_of_tag: int = None
    _number_of_linked_tag: int = None
    _number_of_p_tag: int = None
    _number_of_punctuation: int = None
    _number_of_children: int = None
    _number_of_siblings: int = None
    _number_of_descendants: int = None
    _density_of_punctuation: int = None
    _density_of_text: float = None
    _density_score: float = None
    _similarity_with_siblings: float = None
    _linked_descendants: list = None
    _linked_descendants_group: dict = None
    _linked_descendants_group_text_length: dict = None
    _linked_descendants_group_text_min_length: float = None
    _linked_descendants_group_text_max_length: float = None
    
    alias: str = None
    tag_name: str = None
    parent_id: int = None
    number_of_char: int = None
    number_of_linked_char: int = None
    number_of_tag: int = None
    number_of_linked_tag: int = None
    number_of_p_tag: int = None
    number_of_punctuation: int = None
    number_of_children: int = None
    number_of_siblings: int = None
    number_of_descendants: int = None
    density_of_punctuation: int = None
    density_of_text: float = None
    density_score: float = None
    similarity_with_siblings: float = None
    
    @property
    def id(self):
        """
        get id by hashed element
        :return:
        """
        if self._id is not None:
            return self._id
        self._id = id(self)
        return self._id
    
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
    def parent_selector(self):
        """
        get id by hashed element
        :return:
        """
        if self._parent_selector is not None:
            return self._parent_selector
        from gerapy_auto_extractor.utils.element import selector, parent
        # TODO: change parent(self) to self.parent
        parent = parent(self)
        if parent:
            self._parent_selector = selector(parent)
        return self._parent_selector
    
    @property
    def string(self):
        """
        return string of element
        :return:
        """
        return etree.tostring(self, pretty_print=True, encoding="utf-8", method='html').decode('utf-8')
    
    @property
    def tag_path(self):
        """
        get tag path using external tag_path function
        :return:
        """
        from gerapy_auto_extractor.utils.element import tag_path
        return tag_path(self)
    
    @property
    def linked_descendants(self):
        """
        get linked descendants
        :return:
        """
        if self._linked_descendants is not None:
            return self._linked_descendants
        from gerapy_auto_extractor.utils.element import linked_descendants
        self._linked_descendants = linked_descendants(self)
        return self._linked_descendants
    
    @property
    def linked_descendants_group(self):
        """
        get linked descendants group
        :return:
        """
        if self._linked_descendants_group is not None:
            return self._linked_descendants_group
        from gerapy_auto_extractor.utils.element import linked_descendants_group
        self._linked_descendants_group = linked_descendants_group(self)
        return self._linked_descendants_group
    
    @property
    def linked_descendants_group_text_length(self):
        """
        grouped linked text length
        :return:
        """
        if self._linked_descendants_group_text_length is not None:
            return self._linked_descendants_group_text_length
        result = {}
        from gerapy_auto_extractor.utils.element import text
        for path, elements in self.linked_descendants_group.items():
            lengths = []
            for element in elements:
                # TODO: convert len(text(element)) to element.number_of_char
                lengths.append(len(text(element)))
            mean_length = mean(lengths) if len(lengths) else 0
            result[path] = mean_length
        return result
    
    @property
    def linked_descendants_group_text_min_length(self):
        """
        get grouped linked text min length
        :return:
        """
        if self._linked_descendants_group_text_min_length is not None:
            return self._linked_descendants_group_text_min_length
        values = self.linked_descendants_group_text_length.values()
        self._linked_descendants_group_text_min_length = min(values) if values else 0
        return self._linked_descendants_group_text_min_length
    
    @property
    def linked_descendants_group_text_max_length(self):
        """
        get grouped linked text max length
        :return:
        """
        if self._linked_descendants_group_text_max_length is not None:
            return self._linked_descendants_group_text_max_length
        values = self.linked_descendants_group_text_length.values()
        self._linked_descendants_group_text_max_length = max(values) if values else 0
        return self._linked_descendants_group_text_max_length

    @property
    def linked_descendants_group_text_avg_length(self):
        """
        get grouped linked text avg length
        :return:
        """
        if self._linked_descendants_group_text_max_length is not None:
            return self._linked_descendants_group_text_max_length
        values = self.linked_descendants_group_text_length.values()
        self._linked_descendants_group_text_max_length = max(values) if values else 0
        return self._linked_descendants_group_text_max_length
