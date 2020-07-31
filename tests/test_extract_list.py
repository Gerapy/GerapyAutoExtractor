import os

os.environ['APP_DEBUG'] = 'true'

import unittest
from tests.settings import SAMPLES_LIST_DIR
from tests.test_base import TestBase
from gerapy_auto_extractor import extract_list
from gerapy_auto_extractor.helpers import jsonify


class TestExtractList(TestBase):
    samples_dir = SAMPLES_LIST_DIR
    
    def test_hrfund_announcement(self):
        html = self.html('hrfund_announcement.html')
        result = extract_list(html, base_url='http://www.hr-fund.com.cn/news')
        print(jsonify(result))
        self.assertEqual(len(result), 10)
    
    def test_dfa66_announcement(self):
        html = self.html('dfa66_announcement.html')
        result = extract_list(html, base_url='https://www.dfa66.com/')
        print(jsonify(result))
        self.assertEqual(len(result), 10)
    
    def test_hsqhfunds_announcement(self):
        html = self.html('hsqhfunds_announcement.html')
        result = extract_list(html, base_url='https://www.hsqhfunds.com/')
        print(jsonify(result))
        self.assertEqual(len(result), 20)
    
    def test_rtfund_xxpl(self):
        html = self.html('rtfund_xxpl.html')
        result = extract_list(html, base_url='http://www.rtfund.com/')
        print(jsonify(result))
        self.assertEqual(len(result), 15)
    
    def test_netease_leaderboard_news(self):
        html = self.html('netease_leaderboard_news.html')
        result = extract_list(html)
        print(jsonify(result))
        self.assertEqual(len(result), 700)
    
    def test_netease_international_news(self):
        html = self.html('netease_international_news.html')
        result = extract_list(html)
        print(jsonify(result))
        self.assertEqual(len(result), 7)
    
    def test_netease_rolling_news(self):
        html = self.html('netease_rolling_news.html')
        result = extract_list(html)
        print(jsonify(result))
        self.assertEqual(len(result), 40)
    
    def test_tencent_important_news(self):
        # TODO: this test case is wrong
        html = self.html('tencent_important_news.html')
        result = extract_list(html)
        print(jsonify(result), len(result))
        self.assertEqual(len(result), 10)
    
    def test_zhihu_search_result(self):
        html = self.html('zhihu_search_result.html')
        result = extract_list(html)
        print(jsonify(result), len(result))
        self.assertEqual(len(result), 56)


if __name__ == '__main__':
    unittest.main()
