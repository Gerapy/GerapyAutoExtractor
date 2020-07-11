from gerapy_auto_extractor.settings import APP_DEBUG
from gerapy_auto_extractor.extractors import extract_detail, extract_list, extract_datetime, extract_content, \
    extract_title
from gerapy_auto_extractor.classifiers.list import is_list, probability_of_list
from gerapy_auto_extractor.classifiers.detail import is_detail, probability_of_detail
from loguru import logger

try:
    logger.level('inspect', no=100000 if APP_DEBUG else 0, color='<yellow>')
except (ValueError, TypeError):
    pass
