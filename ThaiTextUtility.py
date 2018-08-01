import os
import deepcut
import re
from fuzzywuzzy import fuzz

class ThaiTextUtility:

    def __init__(self):
        self.word_list = []
        self.load_dict()

    def load_dict(self):
        dict_path = ['resource', 'thaiword.txt']
        dict_path = os.sep.join(dict_path)
        dict_file = open(dict_path, encoding='utf-8')
        for word in dict_file:
            word = word.rstrip()
            self.word_list.append(word)

    def lemmatize(self,text):
        text = re.sub(r'(.)\1+', r'\1\1', text)
        text_token = deepcut.tokenize(text)
        for word in text_token:
            if word in self.word_list:
                print(word)
            else:
                for cursor in self.word_list:
                    fuzz_ratio = fuzz.ratio(word, cursor)
                    if fuzz_ratio > 85:
                        print('sugguestion of '+word+' : '+cursor)