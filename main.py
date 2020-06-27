from gerapy_auto_extractor.extractors import extract
import json

html = open('./sample.html', encoding='utf-8').read()

# with open('result.html', 'w', encoding='utf-8') as f:
#     f.write(etree.tostring(element, pretty_print=True, encoding="utf-8", method='html').decode('utf-8'))

print(json.dumps(extract(html), indent=2, ensure_ascii=False, default=str))
