import os

os.environ['APP_DEBUG'] = 'true'

import unittest
from tests.settings import SAMPLES_LIST_DIR, SAMPLES_DETAIL_DIR
from tests.test_base import TestBase
from gerapy_auto_extractor.classifiers.list import is_list, probability_of_list


class TestClassifyList(TestBase):
    samples_dir = SAMPLES_LIST_DIR
    
    def test_hrfund_announcement(self):
        html = self.html('hrfund_announcement.html', file_dir=SAMPLES_LIST_DIR)
        result = is_list(html)
        self.assertEqual(result, False)
    
    def test_dfa66_announcement(self):
        html = self.html('dfa66_announcement.html', file_dir=SAMPLES_LIST_DIR)
        result = is_list(html)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
