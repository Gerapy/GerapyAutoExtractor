from gerapy_auto_extractor import extract_list, extract_detail, jsonify

html = open('samples/list/sample.html', encoding='utf-8').read()
print(jsonify(extract_list(html)))

html = open('samples/content/sample.html', encoding='utf-8').read()
print(jsonify(extract_detail(html)))
