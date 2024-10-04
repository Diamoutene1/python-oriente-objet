#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Une famille est représentée sous la forme d'une liste de personnes. Chaque personne est elle même représentée par
# un tuple qui aura la forme :
#   (num_id, nom, prénom, date_naissance, date_décès, num_sexe, métier, num_id_père, num_id_mère, num_id_conjoint)
#
# De plus les dates sont des tuples à 3 valeurs (num_jour, num_mois, num_année).
# Si la personne est encore vivante, sa date de décès est un tuple vide.
# Le num_sexe est 0 pour les femmes et de 1 pour les hommes.
# les num_id_XXX sont à 0 si l'information n'est pas pertinente ou inconnue.
# E.g : Dans ADAMS_FAMILY utilisée pour les test, l'arbre généalogique est le suivant :
#          Pierre -------------- Jeanne     André (RIP) -------------- Giselle
#           /           |            \                        |
#        Pierrot     Jeanette      Ginette --------------- Joseph
#
# L'objectif des 9 fonctions suivantes est d'extraire des informations en utilisant le plus possible
# les listes en compréhension du type [{map} for {var} in {sequence} {filter}] plutôt que des boucles.

def get_living(family):
    """ Retourne la liste de toutes les personnes vivantes de 'family'"""
    return [p for p in family if not p[4]]
             
    pass


def get_gender_ranking(family):
    """ Retourne le 2-uplet correspondant aux femmes (resp. hommes) de 'family'"""
    femme=[p for p in family if p[5]==0]
    homme=[p for p in family if p[5]==1]
    return femme,homme
    


def get_married_gender_proportion(family):
    """ Retourne le 2-uplet correspondant à la proportion femmes mariées / femmes (resp. hommes mariés / hommes)
    dans 'family'. Il faudra obligatoirement utiliser 'gender_ranking'."""
    femme,homme=get_gender_ranking (family)
    married=[p for p in family if p[-1]!=0]
    femme_married,homme_married=get_gender_ranking(married)
    return len(femme_married)/len(femme),len(homme_married)/len (homme)
    


def get_death_age_average(family):
    """ Retourne la moyenne d'âge des décès dans la famille 'family' en ne considérant que l'année."""
    age = [p[4][2] - p[3][2] for p in family if p[4]]
    return sum(age) / len(age) if age else 0
    


def get_age_average(family, year):
    """ Retourne la moyenne d'âge des personnes de 'family' encore vivantes l'année 'year' incluse"""
    age = [year - p[3][2] for p in family if (not p[4] or p[4][2] >= year) and year >= p[3][2]]
    return sum(age) / len(age) if age else 0
    


def get_deans(family):
    """ Retourne la liste des doyens de 'family' en ne tenant compte que de l'année de naissance"""
    personne_vivante = get_living(family)
    min_naissance = min(p[3][2] for p in personne_vivante)
    return [p for p in personne_vivante if p[3][2] == min_naissance]


def get_parents(ident, family):
    """ Retourne la liste des parents de la personne d'identifiant 'ident' dans 'family'"""
    person = next(p for p in family if p[0] == ident)
    father_id, mother_id = person[7], person[8]
    parents = [p for p in family if p[0] in (father_id, mother_id)]
    return parents



def is_intersecting(family1, family2):
    """ Retourne 'True' si 'family1' et 'family2' ont au moins un membre en commun. 'False' sinon."""
    return any(person in family2 for person in family1)


def is_sibling(id1, id2, family):
    """ Retourne 'True' si les personnes identifiées 'id1' et 'id2' ont au moins un parent en commun. False sinon.
    Il faudra obligatoirement utiliser 'intersect' et 'parents'."""
    parents_id1 = {parent[0] for parent in get_parents(id1, family)}
    parents_id2 = {parent[0] for parent in get_parents(id2, family)}
    return is_intersecting(parents_id1, parents_id2)


if __name__ == "__main__":
    DISTANCE_TEST = "ORANGE"
    ADAMS_FAMILY = [
        (1, "Dupond", "Pierre", (4, 6, 1949), (), 1, "physicien", 0, 0, 2),
        (2, "Dupond", "Jeanne", (7, 6, 1949), (), 0, "physicienne", 0, 0, 1),
        (3, "Dupond", "Pierrot", (7, 6, 1969), (), 1, "informaticien", 1, 2, 0),
        (4, "Dupond", "Jeannette", (5, 4, 1970), (), 0, "informaticienne", 1, 2, 0),
        (5, "Durand", "Ginette", (4, 3, 1972), (), 0, "chimiste", 1, 2, 8),
        (6, "Durand", "André", (6, 3, 1948), (7, 5, 1968), 1, "chimiste", 0, 0, 7),
        (7, "Durand", "Giselle", (7, 5, 1949), (), 0, "chimiste", 0, 0, 6),
        (8, "Durand", "Joseph", (3, 2, 1968), (), 1, "médecin", 6, 7, 5)]
    assert get_living(ADAMS_FAMILY) == [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                        (2, 'Dupond', 'Jeanne', (7, 6, 1949), (), 0, 'physicienne', 0, 0, 1),
                                        (3, 'Dupond', 'Pierrot', (7, 6, 1969), (), 1, 'informaticien', 1, 2, 0),
                                        (4, 'Dupond', 'Jeannette', (5, 4, 1970), (), 0, 'informaticienne', 1, 2, 0),
                                        (5, 'Durand', 'Ginette', (4, 3, 1972), (), 0, 'chimiste', 1, 2, 8),
                                        (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6),
                                        (8, 'Durand', 'Joseph', (3, 2, 1968), (), 1, 'médecin', 6, 7, 5)]
    assert get_gender_ranking(ADAMS_FAMILY) == ([(2, 'Dupond', 'Jeanne', (7, 6, 1949), (), 0, 'physicienne', 0, 0, 1),
                                                 (4, 'Dupond', 'Jeannette', (5, 4, 1970), (), 0, 'informaticienne', 1, 2, 0),
                                                 (5, 'Durand', 'Ginette', (4, 3, 1972), (), 0, 'chimiste', 1, 2, 8),
                                                 (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6)],
                                                [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                                 (3, 'Dupond', 'Pierrot', (7, 6, 1969), (), 1, 'informaticien', 1, 2, 0),
                                                 (6, 'Durand', 'André', (6, 3, 1948), (7, 5, 1968), 1, 'chimiste', 0, 0, 7),
                                                 (8, 'Durand', 'Joseph', (3, 2, 1968), (), 1, 'médecin', 6, 7, 5)])
    assert get_married_gender_proportion(ADAMS_FAMILY) == (0.75, 0.75)
    assert get_death_age_average(ADAMS_FAMILY) == 20.0
    assert get_age_average(ADAMS_FAMILY, 1967) == 18.25
    assert get_age_average(ADAMS_FAMILY, 1969) == 12.2
    assert get_deans(ADAMS_FAMILY) == [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                       (2, 'Dupond', 'Jeanne', (7, 6, 1949), (), 0, 'physicienne', 0, 0, 1),
                                       (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6)]
    assert get_parents(3, ADAMS_FAMILY) == [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                            (2, 'Dupond', 'Jeanne', (7, 6, 1949), (), 0, 'physicienne', 0, 0, 1)]
    assert get_parents(8, ADAMS_FAMILY) == [
        (6, 'Durand', 'André', (6, 3, 1948), (7, 5, 1968), 1, 'chimiste', 0, 0, 7),
        (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6)]
    assert not is_intersecting(get_living(ADAMS_FAMILY), [p for p in ADAMS_FAMILY if p[4]])
    assert is_intersecting(get_living(ADAMS_FAMILY), get_deans(ADAMS_FAMILY))
    assert not is_sibling(6, 7, ADAMS_FAMILY)
    assert is_sibling(3, 4, ADAMS_FAMILY)
    assert is_sibling(3, 5, ADAMS_FAMILY)
    assert is_sibling(4, 5, ADAMS_FAMILY)
    assert not is_sibling(3, 6, ADAMS_FAMILY)
    print("All tests OK")
