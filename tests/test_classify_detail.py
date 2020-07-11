import os

os.environ['APP_DEBUG'] = 'true'

import unittest
from tests.settings import SAMPLES_LIST_DIR, SAMPLES_DETAIL_DIR
from tests.test_base import TestBase
from gerapy_auto_extractor.classifiers.detail import is_detail, probability_of_detail


class TestClassifyDetail(TestBase):
    
    def test_china_news1(self):
        html = self.html('china_news1.html', file_dir=SAMPLES_DETAIL_DIR)
        result = is_detail(html)
        self.assertEqual(result, False)
    
    def test_netease_news1(self):
        html = self.html('netease_news1.html', file_dir=SAMPLES_DETAIL_DIR)
        result = is_detail(html)
        self.assertEqual(result, False)
    
    def test_netease_news2(self):
        html = self.html('netease_news1.html', file_dir=SAMPLES_DETAIL_DIR)
        result = probability_of_detail(html)
        self.assertGreater(result, 0.5)


if __name__ == '__main__':
    unittest.main()
