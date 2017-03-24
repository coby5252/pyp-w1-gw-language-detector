# -*- coding: utf-8 -*-

"""This is the entry point of the program."""
import re
from languages import LANGUAGES

def score_language(text, language):
    common_words = language['common_words']
    score_list = [ 1 for x in text if x.lower() in common_words]
    return sum(score_list)
    

def detect_language(text, languages):
    """Returns the detected language of given text."""
    text_as_list = text.split(' ')
    scores = {language['name']: score_language(text_as_list, language) for language in languages}
    ## text_as_list = [re.sub('/[^A-z]/g', "", x).lower() for x in text]
    return max(scores.keys(), key=(lambda key: scores[key]))