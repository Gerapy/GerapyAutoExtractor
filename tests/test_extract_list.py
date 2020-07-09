import os

os.environ['APP_DEBUG'] = 'true'

import unittest
from tests.settings import SAMPLES_LIST_DIR
from tests.test_base import TestBase
from gerapy_auto_extractor.extractors import extract_list


class TestExtractList(TestBase):
    samples_dir = SAMPLES_LIST_DIR
    
    def test_hrfund_announcement(self):
        html = self.html('hrfund_announcement.html')
        result = extract_list(html, base_url='http://www.hr-fund.com.cn/news')
        self.assertEqual(len(result) == 10, True)


if __name__ == '__main__':
    unittest.main()
