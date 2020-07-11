import joblib
import numpy as np
from glob import glob
from loguru import logger
from os.path import join, dirname, abspath
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from gerapy_auto_extractor.extractors.title import TitleExtractor
from gerapy_auto_extractor.patterns.datetime import METAS_MATCH as DATETIME_METAS
from gerapy_auto_extractor.schemas.element import Element
from gerapy_auto_extractor.utils.element import number_of_p_descendants, \
    number_of_a_descendants, number_of_punctuation, density_of_punctuation, density_of_text, number_of_clusters, \
    file2element, number_of_a_char, number_of_char, number_of_p_children
from gerapy_auto_extractor.utils.preprocess import preprocess4list_classifier
from gerapy_auto_extractor.utils.similarity import similarity1
from gerapy_auto_extractor.classifiers.base import BaseClassifier

DATASETS_DIR = join(dirname(dirname(dirname(abspath(__file__)))), 'datasets')
DATASETS_LIST_DIR = join(DATASETS_DIR, 'list')
DATASETS_DETAIL_DIR = join(DATASETS_DIR, 'detail')

MODELS_DIR = join(dirname(abspath(__file__)), 'models')


class ListClassifier(BaseClassifier):
    
    def __init__(self, model_path=None, scaler_path=None):
        """
        init features and extractors
        :param model_path: classifier model file
        """
        self.model_path = model_path if model_path else join(MODELS_DIR, 'list_model.pkl')
        self.scaler_path = scaler_path if scaler_path else join(MODELS_DIR, 'list_scaler.pkl')
        self.title_extractor = TitleExtractor()
        self.feature_funcs = {
            'number_of_a_char': number_of_a_char,
            'number_of_a_char_log10': self._number_of_a_char_log10,
            'number_of_char': number_of_char,
            'number_of_char_log10': self._number_of_char_log10,
            'rate_of_a_char': self._rate_of_a_char,
            'number_of_p_descendants': number_of_p_descendants,
            'number_of_a_descendants': number_of_a_descendants,
            'number_of_punctuation': number_of_punctuation,
            'density_of_punctuation': density_of_punctuation,
            'number_of_clusters': self._number_of_clusters,
            'density_of_text': density_of_text,
            'max_density_of_text': self._max_density_of_text,
            'max_number_of_p_children': self._max_number_of_p_children,
            'has_datetime_meta': self._has_datetime_mata,
            'similarity_of_title': self._similarity_of_title,
        }
        self.feature_names = self.feature_funcs.keys()
    
    def _number_of_clusters(self, element: Element):
        """
        get number of clusters like list
        :param element:
        :return:
        """
        tags = ['div', 'li', 'ul']
        return number_of_clusters(element, tags=tags)
    
    def _similarity_of_title(self, element: Element):
        """
        get similarity of <title> and (<h> or <meta>)
        :param element:
        :return:
        """
        _title_extract_by_title = self.title_extractor.extract_by_title(element)
        _title_extract_by_meta = self.title_extractor.extract_by_meta(element)
        _title_extract_by_h = self.title_extractor.extract_by_h(element)
        
        _title_target = None
        if _title_extract_by_meta:
            _title_target = _title_extract_by_meta
        elif _title_extract_by_h:
            _title_target = _title_extract_by_h
        
        if not _title_target:
            return 2
        if not _title_extract_by_title:
            return 3
        return similarity1(_title_target, _title_extract_by_title)
    
    def _has_datetime_mata(self, element: Element):
        """
        has datetime meta
        :param element:
        :return:
        """
        for xpath in DATETIME_METAS:
            datetime = element.xpath(xpath)
            if datetime:
                return True
        return False
    
    def _max_number_of_p_children(self, element: Element):
        """
        get max number of p children an element contains
        :param element:
        :return:
        """
        _number_of_p_children_list = []
        for descendant in element.descendants:
            _number_of_p_children = number_of_p_children(descendant)
            _number_of_p_children_list.append(_number_of_p_children)
        return max(_number_of_p_children_list)
    
    def _max_density_of_text(self, element: Element):
        """
        get max density_of_text
        :param element:
        :return:
        """
        _density_of_text_list = []
        for descendant in element.descendants:
            _density_of_text = density_of_text(descendant)
            _density_of_text_list.append(_density_of_text)
        return np.max(_density_of_text_list)
    
    def _rate_of_a_char(self, element: Element):
        """
        rate of a
        :param element:
        :return:
        """
        _number_of_a_char = number_of_a_char(element)
        _number_of_char = number_of_char(element)
        if _number_of_char == 0:
            return 0
        return _number_of_a_char / _number_of_char
    
    def _number_of_char_log10(self, element: Element):
        """
        log10 of number of char
        :param element:
        :return:
        """
        if element is None:
            return 0
        return np.log10(number_of_char(element) + 1)
    
    def _number_of_a_char_log10(self, element: Element):
        """
        log10 of number of a char
        :param element:
        :return:
        """
        if element is None:
            return 0
        return np.log10(number_of_a_char(element) + 1)
    
    def features_to_list(self, features: dict):
        """
        convert features to list
        :param features:
        :param label:
        :return:
        """
        return [features.get(feature_name) for feature_name in self.feature_names]
    
    def features(self, element: Element):
        """
        build feature map using element
        :param element:
        :return:
        """
        features = {}
        for feature_name, feature_func in self.feature_funcs.items():
            features[feature_name] = feature_func(element)
        return features
    
    def process(self, element: Element):
        """
        get probability of list
        :param element:
        :return:
        """
        preprocess4list_classifier(element)
        x = [self.features_to_list(self.features(element))]
        # scale
        ss = joblib.load(self.scaler_path)
        x = ss.transform(x)
        # load model
        clf = joblib.load(self.model_path)
        # predict
        result = clf.predict_proba(x)
        if result.any() and len(result) and len(result[0]):
            return result[0][1]
        return 0
    
    def train(self):
        """
        build dataset
        :return:
        """
        list_file_paths = list(glob(f'{DATASETS_LIST_DIR}/*.html'))
        detail_file_paths = list(glob(f'{DATASETS_DETAIL_DIR}/*.html'))
        
        x_data, y_data = [], []
        
        for index, list_file_path in enumerate(list_file_paths):
            logger.log('inspect', f'list_file_path {list_file_path}')
            element = file2element(list_file_path)
            if element is None:
                continue
            preprocess4list_classifier(element)
            x = self.features_to_list(self.features(element))
            x_data.append(x)
            y_data.append(1)
        
        for index, detail_file_path in enumerate(detail_file_paths):
            logger.log('inspect', f'detail_file_path {detail_file_path}')
            element = file2element(detail_file_path)
            if element is None:
                continue
            preprocess4list_classifier(element)
            x = self.features_to_list(self.features(element))
            x_data.append(x)
            y_data.append(0)
        
        # preprocess data
        ss = StandardScaler()
        x_data = ss.fit_transform(x_data)
        joblib.dump(ss, self.scaler_path)
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=5)
        
        # set up grid search
        c_range = np.logspace(-5, 20, 5, base=2)
        gamma_range = np.logspace(-9, 10, 5, base=2)
        param_grid = [
            {'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range},
            {'kernel': ['linear'], 'C': c_range},
        ]
        grid = GridSearchCV(SVC(probability=True), param_grid, cv=5, verbose=10, n_jobs=-1)
        clf = grid.fit(x_train, y_train)
        y_true, y_pred = y_test, clf.predict(x_test)
        logger.log('inspect', f'\n{classification_report(y_true, y_pred)}')
        score = grid.score(x_test, y_test)
        logger.log('inspect', f'test accuracy {score}')
        # save model
        joblib.dump(grid.best_estimator_, self.model_path)


list_classifier = ListClassifier()


def probability_of_list(html, **kwargs):
    """
    get probability of list page
    :param html:
    :param kwargs: other kwargs
    :return:
    """
    return list_classifier.classify(html, **kwargs)


def is_list(html, threshold=0.5, **kwargs):
    """
    judge if this page is list page
    :param html: source of html
    :param threshold:
    :param kwargs:
    :return:
    """
    _probability_of_list = probability_of_list(html, **kwargs)
    if _probability_of_list > threshold:
        return True
    return False
