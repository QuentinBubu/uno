def affichage(carte:tuple) -> str:
    """Retourne une carte donnée en texte

    Args:
        carte (tuple): carte à afficher
    Returns:
        str: texte à afficher
    """
    if carte[0] == 10:
        carte_t = "+2"
        carte_c = carte[1]
    elif carte[0] == 11:
        carte_t = "Changement de sens"
        carte_c = carte[1]
    elif carte[0] == 12:
        carte_t = "Passer"
        carte_c = carte[1]
    elif carte[0] == 13:
        carte_t = "Jocker"
        carte_c = ""
    elif carte[0] == 14:
        carte_t = "+4"
        carte_c = ""
    elif carte[0] == 16:
        carte_t = ""
        carte_c = carte[1]
    else:
        carte_t = carte[0]
        carte_c = carte[1]

    return f"{carte_t} {carte_c}"

def choix(carte:str) -> tuple:
    """transforme la carte du joueur en tuple

    Args:
        carte (str): carte choisie
    
    Returns:
        tuple: carte choisie
    """
    carte = carte.split(" ")
    if len(carte) > 2:
        carte = [" ".join(carte[:-1]), carte[-1]]
    for e in carte:
        e.lower()
        e.strip()
    
    if carte[0] == "+2":
        carte[0] = 10
        carte.append("")
    elif carte[0] == "changement de sens":
        carte[0] = 11
    elif carte[0] == "passer":
        carte[0] = 12
        carte.append("")
    elif carte[0] == "jocker":
        carte[0] = 13
        carte.append("")
    elif carte[0] == "+4":
        carte[0] = 14
        carte.append("")
    elif carte[0] == "piocher":
        carte[0] = 15
        carte.append("")

    return (int(carte[0]), carte[1])

def donner_carte(nombre:int, joueur:dict, paquet:list) -> bool:
    """Donne une carte

    Args:
        nombre (int): nombre de cartes à donner
        joueur (dict): profil du joueur
        paquet (list): paquet de jeu

    Returns:
        bool: True si pas d'erreurs
    """    
    for _ in range(nombre):
        joueur['jeu'].append(paquet.pop(0))
    return True

def a_carte(joueur:dict, carte:tuple) -> bool:
    """vérifie si un joueur à une carte

    Args:
        joueur (dict): fiche joueur
        carte (tuple): carte à vérifier

    Returns:
        bool: True si il la possède, False sinon
    """    
    return True if carte in joueur['jeu'] else False