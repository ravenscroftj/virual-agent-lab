# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1
import variables

natural_language_classifier = NaturalLanguageClassifierV1(
    username=variables.NLC_USERNAME,
    password=variables.NLC_PASSWORD)

# print(json.dumps(natural_language_classifier.list(), indent=2))

# CREATE A CLASSIFIER
with open(join(dirname(__file__), '../classifier_config/gem_training_questions.csv'), 'rb') as training_data:
    print(json.dumps(natural_language_classifier.create(training_data=training_data, name='Gemstone Classifier'), indent=2))
    print("*****Remember to copy the classifier_id to the bottom of the variables file*****")