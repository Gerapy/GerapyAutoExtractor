import unittest
from os.path import join


class TestBase(unittest.TestCase):
    samples_dir = None
    
    def html(self, file_name):
        """
        get html content of file
        :param file_name:
        :return:
        """
        file_path = join(self.samples_dir, file_name)
        with open(file_path, encoding='utf-8') as f:
            return f.read()
