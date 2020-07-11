import re
from dateparser import parse
from lxml.html import HtmlElement
from gerapy_auto_extractor.patterns.datetime import METAS_CONTENT, REGEXES
from loguru import logger
from gerapy_auto_extractor.extractors.base import BaseExtractor


class DatetimeExtractor(BaseExtractor):
    """
    Datetime Extractor which auto extract datetime info.
    """
    
    def extract_by_regex(self, element: HtmlElement) -> str:
        """
        extract datetime according to predefined regex
        :param element:
        :return:
        """
        text = ''.join(element.xpath('.//text()'))
        for regex in REGEXES:
            result = re.search(regex, text)
            if result:
                return result.group(1)
    
    def extract_by_meta(self, element: HtmlElement) -> str:
        """
        extract according to meta
        :param element:
        :return: str
        """
        for xpath in METAS_CONTENT:
            datetime = element.xpath(xpath)
            if datetime:
                return ''.join(datetime)
    
    def process(self, element: HtmlElement):
        """
        extract datetime
        :param html:
        :return:
        """
        return self.extract_by_meta(element) or \
               self.extract_by_regex(element)


datetime_extractor = DatetimeExtractor()


def parse_datetime(datetime):
    """
    parse datetime using dateparser lib
    :param datetime:
    :return:
    """
    if not datetime:
        return None
    try:
        return parse(datetime)
    except TypeError:
        logger.exception(f'Error Occurred while parsing datetime extracted. datetime is {datetime}')


def extract_datetime(html, parse=True):
    """
    extract datetime from html
    :param parse:
    :param html:
    :return:
    """
    result = datetime_extractor.extract(html)
    if not parse:
        return result
    return parse_datetime(result)
