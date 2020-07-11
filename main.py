from gerapy_auto_extractor import extract_list, extract_detail, is_detail, is_list, probability_of_detail, \
    probability_of_list
from gerapy_auto_extractor.helpers import content, jsonify

html = content('samples/list/sample.html')
print(jsonify(extract_list(html)))

html = content('samples/detail/sample.html')
print(jsonify(extract_detail(html)))

html = content('samples/detail/sample.html')
print(probability_of_detail(html), probability_of_list(html))
print(is_detail(html), is_list(html))

html = content('samples/list/sample.html')
print(probability_of_detail(html), probability_of_list(html))
print(is_detail(html), is_list(html), )
