import os

os.environ['APP_DEBUG'] = 'true'

import unittest
from tests.test_base import TestBase
from gerapy_auto_extractor import extract_list, extract_detail, is_detail, is_list, probability_of_list
import requests


class TestProdCase(TestBase):
    
    def test_case1(self):
        result = None
        content = requests.get("https://www.qukuaiwang.com.cn/Index/ku_detail/kid/4812.html").text
        if is_list(content):
            result = extract_list(content)
        print(probability_of_list(content))
        self.assertEqual(bool(result), True)


if __name__ == '__main__':
    unittest.main()
