import unittest
from os.path import join


class TestBase(unittest.TestCase):
    samples_dir = None
    
    def content(self, file_path):
        """
        get content of file
        :param file_path:
        :return:
        """
        with open(file_path, encoding='utf-8') as f:
            return f.read()
    
    def html(self, file_name, file_dir=None):
        """
        get html content of file
        :param file_name:
        :param file_dir:
        :return:
        """
        file_path = join(file_dir if file_dir else self.samples_dir, file_name)
        return self.content(file_path)
