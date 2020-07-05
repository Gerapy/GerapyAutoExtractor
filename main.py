from gerapy_auto_extractor.extractors.list import extract_list
from gerapy_auto_extractor.extractors import extract_detail
import json
from os.path import join, dirname, abspath

html = open(join(dirname(abspath(__file__)), 'samples/list/sample4.html'), encoding='utf-8').read()
print(json.dumps(extract_list(html), indent=2, ensure_ascii=False, default=str))


html = open(join(dirname(abspath(__file__)), 'samples/content/sample2.html'), encoding='utf-8').read()
print(json.dumps(extract_detail(html), indent=2, ensure_ascii=False, default=str))
