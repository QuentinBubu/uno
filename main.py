import cartes, jeu
from os import system as clear

joueurs = []
rejouer_meme_joueur = True
rejouer = True

while rejouer:
    for _ in range(int(input("Nombre de joueurs? "))):
        joueurs.append(
            {
                "nom": input("Nom du joueur? "),
                "jeu": [],
                "pts": 0
            }
        )

    talon = {
        "dernier_index": None,
        "jeu": []
    }

    paquet = jeu.creation_jeu()

    while rejouer_meme_joueur:
        for j in joueurs:
            cartes.donner_carte(7, j, paquet)

        en_cours = True

        ordre = [x for x in joueurs]
        joueur_en_cours = ordre[-1]

        retour = jeu.premiere_carte(ordre, talon, paquet)
        if retour == "passe":
            joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)
        elif retour == "sens":
            joueur_en_cours = ordre[-2]

        while en_cours:
            joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)
            clear('cls')
            input(f"{joueur_en_cours['nom']}, à toi de jouer! Appuies sur entrée!")
            clear('cls')
            print(f"Dernière carte: {cartes.affichage(talon['jeu'][-1])}")
            carte = cartes.choix(input(f"Quelle carte jouer {joueur_en_cours['nom']}?: \n{jeu.jeu_joueur(joueur_en_cours)}\n"))

            loop = True
            while loop:
                while carte == (17, 'undefined'):
                    print("Saisissez une carte valide")
                    carte = cartes.choix(input(f"Quelle carte jouer {joueur_en_cours['nom']}?: \n{jeu.jeu_joueur(joueur_en_cours)}\n"))

                retour = jeu.pose_carte(joueur_en_cours, ordre, talon, carte, paquet)

                if retour == False:
                    carte = (17, 'undefined')
                else:
                    loop = False

                if carte == (15, ""):
                    print(f"Carte piocher: {cartes.affichage(joueur_en_cours['jeu'][-1])}")
                    if input("Souhaitez-vous la posez maintenant? o/n ") == "o":
                        joueur_en_cours = ordre[-1]

            if retour == "passe":
                joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)

            if jeu.verification_fin(joueur_en_cours):
                en_cours = False

        print(f"Fin du jeu! {joueur_en_cours['nom']} a gagné!")

        print(jeu.classement(joueurs))

        if input("Voulez-vous rejouer avec les mêmes joueur? o/n ") != "o":
            rejouer_meme_joueur = False
            if input("Voulez-vous recommencer une partie à 0? o/n ") != "o":
                rejouer = False


"""
if carte in ['+2', '+4', 'sens interdit']
-> surencherir?
    -> oui -> poser carte
    -> non -> compter au dernier index enregistré le nb de +X ou passer son tour
"""