# Gerapy Auto Extractor Changelog

## 0.1.1 (2020-07-31)

### Bug Fixes

* Fix bug of get best cluster when extract result is None

## 0.1.0 (2020-07-11)

### Bug Fixes

* Fix extraction of title from `h` tag

## Features

* Add support for distinguishing list page between detail page
* Add test cases for classification
* Add `content` method support to get html content by file path
* Move `jsonify` to `helper` module

## 0.0.4 (2020-07-09)

### Bug Fixes

* Fix missed extraction of list extractor
* Removed unnecessary logs unless set `APP_DEBUG` to `true`
* Fix extraction of content from `<footer>` tag

### Features

* Add support for `base_url` arg of `extract_list` method
* Add test cases in `tests` folder
* Add more samples in `samples` folder
* Add `jsonify` method for converting json format
* Remove blank lines from result of `extract_content` method
* Add property `nth` in Element Class
* Add `nth` suffix of `alias` property in Element Class