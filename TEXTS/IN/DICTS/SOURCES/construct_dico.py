import string

ACCENTS_FR = {'a': 'àâ', 'e': 'éèêë', 'i': 'îï', 'o': 'ô', 'u': 'ùûü', 'y': 'ÿ', 'c': 'ç'}


def remove_accent(char):
    for key, value in ACCENTS_FR.items():
        if char in value:
            return key
    return char


def remove_accents(word):
    return ''.join(remove_accent(char) for char in word)


with open('mots_cleaned.txt', 'w', encoding='utf-8') as f_out:
    for letter in string.ascii_lowercase:
        with open(f"DICOS/{letter}.txt", 'r', encoding='utf-8') as f:
            words = [line.split('\t')[0] for line in f.readlines()]
            i_beg = words.index("----------------------- FIN DE LA LICENCE ABU --------------------------------\n")
            i_end = words.index("------------------------- FIN DU FICHIER --------------------------------\n")
            words = sorted(list(set(remove_accents(word).upper().strip() for word in words[i_beg + 1:i_end] if word != '\n')))
            for word in words:
                f_out.write(word + '\n')
