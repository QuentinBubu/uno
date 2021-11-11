import cartes, jeu, os

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

        joueurs[0]['jeu'] = [(13, '')]

        ordre = [x for x in joueurs]
        joueur_en_cours = ordre[-1]

        retour = jeu.premiere_carte(ordre, talon, paquet)
        if retour == "passe":
            joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)
        elif retour == "sens":
            joueur_en_cours = ordre[-2]

        while en_cours:
            joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)
            os.system('cls')
            input(f"{joueur_en_cours['nom']}, à toi de jouer! Appuies sur entrée!")
            os.system('cls')
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
            if retour == "passe":
                joueur_en_cours = jeu.suivant(joueur_en_cours, ordre)

            if jeu.verification_fin(joueur_en_cours):
                en_cours = False

        print(f"Fin du jeu! {joueur_en_cours['nom']} a gagné!")

        for j in joueurs:
            j['pts'] += cartes.points(j)
            j['jeu'] = []

        joueurs.sort(key = lambda x: x['pts'])
        print("Classement:")
        for c, n in enumerate(joueurs):
            print(f"n°{c}: {n['nom']} avec {n['pts']} points")

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