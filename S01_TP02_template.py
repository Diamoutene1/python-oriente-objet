#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from S01_TP01_template import get_hamming_distance
from time import perf_counter


def get_words_from_dictionary(file_path, length=None):
    """ Retourne la liste des mots du fichier de nom 'file_name' si 'length' vaut 'None'.
        Sinon retourne la liste des mots de longueur 'length'."""
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if length is None or len(word) == length:
                words.append(word)
    return words


def get_words_hamming(word, words, hamming_distance):
    """ Retourne une sous-liste de la liste de mots 'words' qui sont à une distance de Hamming
        'hamming_distance' du mot 'word'."""
    return [w for w in words if get_hamming_distance(word, w) == hamming_distance]


def is_perfect_scale(scale):
    """Retourne 'True' si l'échelle de mots 'scale' est parfaite. 'False' sinon. Une échelle de mots est dite parfaite
    si le nombre d'étape pour passer du mot de départ au mot cible est égal à leur distance de hamming."""
    for i in range(len(scale) - 1):
        if get_hamming_distance(scale[i], scale[i+1]) != 1:
            return False
    return get_hamming_distance(scale[0], scale[-1]) == len(scale) - 1


def get_removed_words(words_to_remove, all_words):
    """ Retourne une sous-liste des mots de 'all_words' en retirant ceux de 'words_to_remove'"""
    return [word for word in all_words if word not in words_to_remove]



def get_next_scales(scale, words):
    """ retourne la liste des échelles de mots possibles constituées par l'échelle de mot 'scale' et un mot de
    la liste 'words'"""
    next_scales = []
    for word in words:
        if get_hamming_distance(scale[-1], word) == 1 and word not in scale:
            next_scales.append(scale + [word])
    return next_scales


def get_scale(file_path, word1, word2):
    """ Retourne une échelle de mots entre 'word1' et 'word2' avec les mots du dictionnaire 'file_path'"""
    all_words = get_words_from_dictionary(file_path)
    scales = [[word1]]

    while scales:
        current_scale = scales.pop(0)
        last_word = current_scale[-1]

        if last_word == word2:
            return current_scale

        next_scales = get_next_scales(current_scale, all_words)
        scales.extend(next_scales)

    return None


if __name__ == "__main__":
    DICT_NAME = PATH_DICTIONARIES + 'fr_long_dict_cleaned.txt'
    WORD6 = get_words_from_dictionary(DICT_NAME, 6)
    assert WORD6[:9] == ['A-T-IL', 'ABAQUE', 'ABATEE', 'ABATTE', 'ABATTU', 'ABBAYE', 'ABCEDE', 'ABERRE', 'ABETIE']
    assert get_words_hamming("ORANGE", WORD6, 0) == ['ORANGE']
    assert get_words_hamming("ORANGE", WORD6, 1) == ['FRANGE', 'GRANGE', 'ORANGS', 'ORANTE',
                                                     'ORONGE']
    assert get_words_hamming("ORANGE", WORD6, 2) == ['BRANDE', 'BRANLE', 'BRANTE', 'CHANGE',
                                                     'CRANTE', 'GRANDE', 'GRINGE', 'ORACLE', 'ORANTS', 'TRANSE',
                                                     'URANIE']
    assert  is_perfect_scale(['SUD', 'SUT', 'EUT', 'EST'])
    assert is_perfect_scale(['HOMME', 'COMME', 'COMTE', 'CONTE'])
    assert not is_perfect_scale(['HOMME', 'COMME', 'COMTE', 'CONTE', 'CONGE'])
    NEW_WORD6 = get_removed_words(['A-T-IL', 'ABATTU'], WORD6)
    assert WORD6[:9] == ['A-T-IL', 'ABAQUE', 'ABATEE', 'ABATTE', 'ABATTU', 'ABBAYE', 'ABCEDE', 'ABERRE', 'ABETIE']
    assert NEW_WORD6[:9] == ['ABAQUE', 'ABATEE', 'ABATTE', 'ABBAYE', 'ABCEDE', 'ABERRE', 'ABETIE', 'ABETIR', 'ABETIS']

    assert get_next_scales(['CHANGE', 'CHANTE'], WORD6) == [
        ['CHANGE', 'CHANTE', 'CHANCE'],
        ['CHANGE', 'CHANTE', 'CHANTA'],
        ['CHANGE', 'CHANTE', 'CHANTS'],
        ['CHANGE', 'CHANTE', 'CHARTE'],
        ['CHANGE', 'CHANTE', 'CHASTE'],
        ['CHANGE', 'CHANTE', 'CHATTE'],
        ['CHANGE', 'CHANTE', 'CRANTE']]

    t1 = perf_counter()
    assert get_scale(DICT_NAME, 'SUD', 'EST') == ['SUD', 'SUT', 'EUT', 'EST']
    t2 = perf_counter()
    print(t2 - t1)
    # assert get_scale(DICT_NAME, 'HOMME', 'SINGE') ==  ['HOMME', 'COMME', 'COMTE', 'CONTE', 'CONGE',
    #                                                    'SONGE', 'SINGE']
    # t3 = perf_counter()
    # print(t3 - t2)
    # assert get_scale(DICT_NAME, 'EXOS', 'MATH') == ['EXOS', 'EROS', 'GROS', 'GRIS', 'GAIS', 'MAIS',
    #                                                 'MATS', 'MATH']
    # t4 = perf_counter()
    # print(t4 - t3)
    # assert get_scale(DICT_NAME, 'TOUT', 'RIEN') == ['TOUT', 'BOUT','BRUT', 'BRUN', 'BREN', 'BIEN', 'RIEN']
    # t5 = perf_counter()
    # print(t5 - t4)
    print("All tests OK")
