import re
import numpy as np
import pandas as pd
from functools import partial, reduce


def string_norm(min_letter, string):
    return reduce(lambda prev, cur: prev + cur ** 2, map(lambda x: ord(x) - ord(min_letter) + 1, string))


def eval_vowel_num(string):
    vowels = set('ЁУЕЫАОЭЯИЮ')
    return sum([*map(lambda x: string.count(x), vowels)])


def eval_vowel_ratio(string):
    if type(string) != str:
        return 0
    return eval_vowel_num(string.upper()) / len(string)


def preprocess(surname, name):
    string_norm_app = partial(string_norm, 'А')
    preprocess_str = lambda x: re.sub(r'\s+ ', '', str(x).upper()).replace('Ё', 'Е')

    surname, name = map(lambda x: '~' if pd.isna(x) else x, [surname, name])

    surname_n = preprocess_str(surname)[-2:]
    name_n = preprocess_str(name)[-2:]
    #father_n = preprocess_str(father_name)[-2:]
    vowel_rate = eval_vowel_ratio(name)
    num_let_sur = len(surname)
    num_let_nam = len(name)
    #num_let_fat = len(father_name)
    #has_m_fatend = int(father_name[-2:] in set(['ИЧ', 'ЛЫ']))
    has_m_surend = int(surname[-2:] in set(['ОВ', 'ИН', 'ЯН']))
    has_m_namend = int(name[-2:] in set(['ИЙ', 'ЕЙ', 'ДР', 'ИР', 'АН', 'АЙ', 'ОР']))
    return np.array([
        vowel_rate,
        string_norm_app(surname_n),
        string_norm_app(name_n),
        #string_norm_app(father_n),
        num_let_sur,
        num_let_nam,
        #num_let_fat,
        #has_m_fatend,
        has_m_surend,
        has_m_namend
    ])
