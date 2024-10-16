def creer_grille():
    """Crée une grille vide pour le jeu Puissance 4."""
    return [[' ' for _ in range(7)] for _ in range(6)]

def afficher_grille(grille):
    """Affiche la grille actuelle du jeu."""
    for row in grille:
        print('|' + '|'.join(row) + '|')
    print(' ' + '-' * 15)  # Bas de la grille
    print(' 1 2 3 4 5 6 7 ')  # Numéro des colonnes pour référence, commencant par 1

def jouer(grille, colonne, symbole):
    """Permet à un joueur de placer son symbole dans une colonne."""
    for i in range(5, -1, -1):  # Commencer par le bas de la grille
        if grille[i][colonne - 1] == ' ':
            grille[i][colonne - 1] = symbole
            return True
    return False  # Colonne pleine

def verifier_gagnant(grille, symbole):
    """Vérifie si le joueur utilisant le symbole spécifié a gagné."""
    # Vérification horizontale, verticale, et diagonale
    for c in range(7):
        for r in range(6):
            if (c <= 3 and all(grille[r][c + i] == symbole for i in range(4))) or \
               (r <= 2 and all(grille[r + i][c] == symbole for i in range(4))) or \
               (c <= 3 and r <= 2 and all(grille[r + i][c + i] == symbole for i in range(4))) or \
               (c >= 3 and r <= 2 and all(grille[r + i][c - i] == symbole for i in range(4))):
                return True
    return False

def jouer_puissance_4():
    """Fonction principale pour jouer au jeu Puissance 4."""
    joueur_noms = {}
    scores = {'Joueur 1': 0, 'Joueur 2': 0}
    joueur_noms['Joueur 1'] = input("Entrez le prénom du Joueur 1 : ")
    joueur_noms['Joueur 2'] = input("Entrez le prénom du Joueur 2 : ")

    while True:
        grille = creer_grille()
        joueur_actuel, symbole_actuel = 1, 'X'

        while True:
            afficher_grille(grille)
            try:
                colonne = int(input(f"{joueur_noms['Joueur ' + str(joueur_actuel)]} ({symbole_actuel}), choisis une colonne (1-7): "))
                if colonne < 1 or colonne > 7:
                    print("Colonne invalide. Les colonnes valides sont de 1 à 7.")
                    continue
            except ValueError:
                print("Veuillez entrer un numéro de colonne valide.")
                continue

            if jouer(grille, colonne, symbole_actuel):
                if verifier_gagnant(grille, symbole_actuel):
                    afficher_grille(grille)
                    print(f"{joueur_noms['Joueur ' + str(joueur_actuel)]} gagne !")
                    scores['Joueur ' + str(joueur_actuel)] += 1
                    break
                joueur_actuel, symbole_actuel = (2, 'O') if joueur_actuel == 1 else (1, 'X')
            else:
                print("Colonne pleine ! Essayez une autre colonne.")

            if all(grille[0][c] != ' ' for c in range(7)):
                afficher_grille(grille)
                print("Match nul ! La grille est pleine.")
                break

        # Afficher les scores
        print(f"Scores: {joueur_noms['Joueur 1']} {scores['Joueur 1']} - {joueur_noms['Joueur 2']} {scores['Joueur 2']}")
        if input("Voulez-vous jouer une autre partie ? (oui/non) : ").lower() != 'oui':
            break

if __name__ == "__main__":
    jouer_puissance_4()
