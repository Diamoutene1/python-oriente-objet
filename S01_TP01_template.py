#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TP sur les types de base et les chaines de caractères
# Attention à bien réutiliser toute fonction déjà écrite si cela est pertinent.

def are_chars(chars, string):
    """ Retourne 'True' si tous les caractères 'chars' appartiennent la chaine 'string'.
    False sinon."""
    for c in chars:
        if c not in string:
            return False
    return True
    
print(are_chars("bonjourz", "bonjour tout"))

# Les 3 fonctions suivantes simulent un brin d'ADN sous la forme d'une chaîne de caractères combinant les lettres
# A, T, G et C pour représenter les bases susceptibles de le composer. L'Adénine (A) est la base complémentaire de la
# Thymine (T) et la Guanine (G) est la complémentaire de la Cytozine (C). Les bases ont également une masse molaire :
# - A pèse 135 g/mol
# - T pèse 126 g/mol
# - G pèse 151 g/mol
# - C pèse 111 g/mol

# TP sur les types de base et les chaines de caractères
# Attention à bien réutiliser toute fonction déjà écrite si cela est pertinent.

def are_chars(chars, string):
    """ Retourne 'True' si tous les caractères 'chars' appartiennent la chaine 'string'.
    False sinon."""
    for c in chars:
        if c not in string:
            return False
    return True

print(are_chars("bonjourz", "bonjour tout"))

def is_dna(dna):
    """ Retourne 'True' si le brin 'dna' contient uniquement des bases A, T, G ou C (et au moins une).
    'False' sinon. Il faudra utiliser la fonction 'are_chars'."""
    if not dna:
        return False
    return all(char in "ATGC" for char in dna.upper())

def get_molar_mass(dna):
    """ Retourne 0 si dna n'est pas un brin. Sinon, retourne la masse molaire du brin 'dna'.
    Il faudra utiliser la fonction 'is_dna'."""
    if is_dna(dna) ==True:
        compt=0
        for base in dna:
            if base=="A":
                compt+=135
            elif base=="T":
                 compt+=126
            elif base=="G":
                 compt+=151
            elif base=="C":
                 compt+=111  # Correction de l'opérateur +=
        return compt
    return 0

def get_complementary(dna):
    """ Si 'dna' est un brin, retourne son complémentaire. Sinon retourne 'None'."""
    if is_dna(dna)==True:
        complement = ''
        for base in dna:
            if base == 'A':
                complement += 'T'
            elif base == 'T':
                complement += 'A'
            elif base == 'C':
                complement += 'G'
            elif base == 'G':
                complement += 'C'
        return complement
    else:
        return None  # Correction de la valeur de retour

def get_first_deleted(char, string):
    """ Retourne la chaine 'string' amputée de la première occurrence du caractère 'char'"""
    if char in string:
        index = string.index(char)
        return string[:index] + string[index + 1:]
    else:
        return string

def is_scrabble(word, letters):
    """ Retourne True si le mot 'word' peut être construit comme au jeu du Scrabble à partir des lettres de la chaîne
    'letters' (les lettres répétées dans 'word' seront donc également répétées au moins le même nombre de fois dans
    'letters'). False sinon. Il faudra obligatoirement utiliser 'get_first_deleted'."""
    for char in word:
        if char not in letters:
            return False
        else:
            letters = get_first_deleted(char, letters)
    return True

def is_anagram(word1, word2):
    """ Retourne 'True' si 'word1' et 'word2' sont deux anagrammes.
    'False' sinon. Il faudra obligatoirement utiliser 'is_scrabble'."""
    return is_scrabble(word1, word2) and is_scrabble(word2, word1)

def get_hamming_distance(word1, word2):
    """ Retourne la distance de Hamming entre 'word1' et 'word2' ou -1 si son calcul n'est pas possible.
    La distance de Hamming entre deux chaines de même longueur correspond au nombre de positions auxquelles sont
    associés des caractères différents. """
    if len(word1) != len(word2):
        return -1
    distance = 0
    # Parcourir les deux mots caractère par caractère
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            distance += 1
    return distance

if __name__ == "__main__":
    DNA_TEST = 'GTATTCTCA'
    NOT_DNA_TEST = 'GTAITCTCA'
    WORDS1_TEST = "test"
    WORDS2_TEST = "tester"
    WORDS3_TEST = "est"
    SCRABBLE_TEST = "aeeigmnrrrstuwz"
    WORDS4_TEST = "marguerites"
    WORDS5_TEST = "rose"
    WORDS6_TEST = "gewurztraminers"

    assert are_chars(WORDS1_TEST, WORDS3_TEST)
    assert not are_chars(WORDS2_TEST, WORDS3_TEST)
    assert not is_dna('')
    assert is_dna(DNA_TEST)
    assert is_dna(DNA_TEST.lower())
    assert not is_dna(NOT_DNA_TEST)
    assert get_molar_mass('') == 0
    assert get_molar_mass(DNA_TEST) == 1147
    assert get_molar_mass(NOT_DNA_TEST) == 0
    assert get_complementary('') == None
    assert get_complementary(DNA_TEST) == 'CATAAGAGT'
    assert get_complementary(NOT_DNA_TEST) == None
    assert get_first_deleted('r', SCRABBLE_TEST) == 'aeeigmnrrstuwz'
    assert is_scrabble(WORDS4_TEST, WORDS6_TEST)
    assert not is_scrabble(WORDS5_TEST, WORDS6_TEST)
    assert is_anagram(WORDS6_TEST, SCRABBLE_TEST)
    assert not is_anagram(WORDS4_TEST, SCRABBLE_TEST)
    assert get_hamming_distance(WORDS6_TEST, SCRABBLE_TEST) == 13
    assert get_hamming_distance(WORDS4_TEST, SCRABBLE_TEST) == -1
    print("All tests OK")
