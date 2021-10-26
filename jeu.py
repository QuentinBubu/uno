from random import shuffle
from cartes import affichage, a_carte, donner_carte

def creation_jeu() -> list:
    """Creation du packet de jeu

    Returns:
        list: packet de jeu
    """    
    jeu = []
    x = list(range(1, 12+1))
    cartes = [i for i in x for _ in (0, 1)]
    cartes.append(0)
    for couleur in ["jaune", "bleu", "rouge", "vert"]:
        for el in cartes:
            jeu.append((el, couleur))

    jeu.extend([(i, "") for i in [13, 14] for _ in (0, 4)])

    shuffle(jeu)
    return jeu

def jeu_joueur(joueur:list) -> str:
    """retourne le jeu du joueur

    Args:
        joueur (list): fiche joueur

    Returns:
        str: texte du jeu du joueur
    """    
    txt = ""
    jeu = joueur['jeu']
    jeu.sort(key = lambda x:(x[1], x[0]))
    for el in jeu:
        txt += "\n" + affichage(el)
    txt = txt.strip()
    return txt

def premiere_carte(joueur:dict, ordre:list, talon: list, paquet:list) -> any:
    """pose la carte du joueur

    Args:
        talon (list): talon du jeu
        carte (tuple): carte à poser

    Returns:
        bool: True si la carte est posée, False sinon
    """    
    talon['jeu'].append(paquet.pop(0))
    if talon['jeu'][-1][0] >= 10:
        retour = special_carte(joueur, ordre, talon, paquet)
        if talon['jeu'][-1][0] == 11:
            return "sens"
        else:
            return retour
    return True


def pose_carte(joueur:dict, ordre:list, talon: list, carte:tuple, paquet:list) -> any:
    """pose la carte du joueur

    Args:
        joueur (dict): fiche joueur
        talon (list): talon du jeu
        carte (tuple): carte à poser

    Returns:
        bool: True si la carte est posée, False sinon
    """    
    if carte[0] == 15:
        piocher(joueur, paquet)
        return True
    elif verification_choix(joueur, talon, carte):
        talon['jeu'].append(carte)
        joueur['jeu'].remove(carte)
        if carte[0] >= 10:
            return special_carte(joueur, ordre, talon, paquet)
        return True
    else:
        return False


def verification_choix(joueur:dict, talon:dict, carte:tuple) -> bool:
    """vérifie si le joueur peux poser sa carte

    Args:
        joueur (dict): fiche joueur
        talon (dict): talon de jue

    Returns:
        bool: True si il peut poser, False sinon
    """    
    if not a_carte(joueur, carte): # si le joueur n'a pas sa carte
        return False

    if carte[0] == talon['jeu'][-1][0]: # même numéro
        return True
    elif carte[1] == talon['jeu'][-1][1] or carte[1] == "": # même couleur ou carte jocker
        return True

def verification_fin(joueur:list) -> str:
    if len(joueur['jeu']) == 0:
        return True
    else:
        return False

def suivant(joueur_en_cours:dict, ordre:list) -> dict:
    return ordre[0] if joueur_en_cours == ordre[-1] else ordre[ordre.index(joueur_en_cours) + 1]

def special_carte(joueur:dict, ordre:list, talon:list, paquet:list) -> None:
    if talon['jeu'][-1][0] == 10:
        donner_carte(2, suivant(joueur, ordre), paquet)
        return True

    elif talon['jeu'][-1][0] == 11:
        ordre.reverse()
        return True

    elif talon['jeu'][-1][0] == 12:
        return "passe"

    elif talon['jeu'][-1][0] == 13 or talon['jeu'][-1][0] == 14:
        couleur = input("Couleur? ").lower()
        while couleur not in ['jaune', 'bleu', 'rouge', 'vert']:
            couleur = input("Couleur? ").lower()
        if talon['jeu'][-1][0] == 14:
            donner_carte(4, suivant(joueur, ordre), paquet)
        talon['jeu'].__delitem__(-1)
        talon['jeu'].append((16, couleur))
        return True

def piocher(joueur:dict, paquet:list):
    joueur['jeu'].append(paquet.pop(0))
    return True