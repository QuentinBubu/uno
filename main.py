import cartes
import jeu
import os

paquet = jeu.creation_jeu()

joueurs = [
    {
        "nom": "j0",
        "jeu": [(14, '')]
    },
    {
        "nom": "j1",
        "jeu": [(14, '')]
    },
    {
        "nom": "j2",
        "jeu": []
    },
]

talon = {
    "dernier_index": None,
    "jeu": []
}

cartes.donner_carte(1, talon, paquet)
talon["dernier_index"] = 0

for j in joueurs:
    cartes.donner_carte(7, j, paquet)



en_cours = True

ordre = [x for x in joueurs]
joueur_en_cours = ordre[-1]



if jeu.premiere_carte(ordre[-1], ordre, talon, paquet) == "passe":
    joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)

while en_cours:
    os.system("cls")
    joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)
    print(f"Dernière carte: {cartes.affichage(talon['jeu'][-1])}")
    carte = cartes.choix(input(f"Quelle carte jouer {joueur_en_cours['nom']}?: \n{jeu.jeu_joueur(joueur_en_cours)}\n"))
    retour = jeu.pose_carte(joueur_en_cours, ordre, talon, carte, paquet)
    if retour == "passe":
        joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)
    elif retour == False:
        print("Vous ne pouvez pas jouer cette carte!")
        joueur_en_cours = ordre[ordre.index(joueur_en_cours) - 1]
    else:
        if jeu.verification_fin(joueur_en_cours):
            en_cours = False


print("end")


"""
if carte in ['+2', '+4', 'sens interdit']
-> surencherir?
    -> oui -> poser carte
    -> non -> compter au dernier index enregistré le nb de +X ou passer son tour
"""