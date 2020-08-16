import os

from gerapy_auto_extractor.utils.element import html2element

os.environ['APP_DEBUG'] = 'true'

import unittest
from tests.settings import SAMPLES_DETAIL_DIR
from tests.test_base import TestBase
from gerapy_auto_extractor.extractors.title import title_extractor

import unittest


class TestExtractTitle(TestBase):
    samples_dir = SAMPLES_DETAIL_DIR
    
    def test_extract_by_h(self):
        html = self.html('ifeng_news1.html')
        element = html2element(html)
        title = title_extractor.process(element)
        print('Title', title)
        self.assertEqual(title, '故宫，你低调点！故宫：不，实力已不允许我继续低调')


if __name__ == '__main__':
    unittest.main()
