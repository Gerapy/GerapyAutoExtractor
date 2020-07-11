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
        html = self.html('china_news1.html')
        element = html2element(html)
        content = title_extractor.extract_by_h(element)
        print('Content', content)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
