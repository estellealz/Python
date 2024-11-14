import random

def afficher_grille(grille):
    print("\nGrille de jeu:")
    print("  0 1 2")
    for index, ligne in enumerate(grille):
        print(f"{index} " + "|".join(ligne))
        print("  " + "-" * 5)

def verifier_gagnant(grille, joueur):
    lignes = any(all(c == joueur for c in ligne) for ligne in grille)
    colonnes = any(all(ligne[i] == joueur for ligne in grille) for i in range(3))
    diagonales = all(grille[i][i] == joueur for i in range(3)) or all(grille[i][2 - i] == joueur for i in range(3))
    return lignes or colonnes or diagonales

def obtenir_coup_valide(grille):
    while True:
        ligne = input("Entrez la ligne (0-2) ou tapez 'exit' pour quitter: ").strip().lower()
        if ligne == "exit":
            return "exit", "exit"
        try:
            ligne = int(ligne)
            if ligne in range(3):
                colonne = int(input("Entrez la colonne (0-2): ").strip())
                if colonne in range(3) and grille[ligne][colonne] == " ":
                    return ligne, colonne
                else:
                    print("Cette case est déjà prise ou numéro de colonne invalide !")
            else:
                print("Numéro de ligne invalide. Veuillez choisir entre 0 et 2.")
        except ValueError:
            print("Veuillez entrer un numéro entier ou 'exit'.")

def jouer():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    scores = {'X': 0, 'O': 0}
    noms = {'X': input("Entrez le nom du joueur pour 'X': "), 'O': input("Entrez le nom du joueur pour 'O': ")}
    tour = random.choice(['X', 'O'])
    
    while True:
        print(f"\nTour du joueur {noms[tour]} ({tour}):")
        afficher_grille(grille)
        ligne, colonne = obtenir_coup_valide(grille)

        if ligne == "exit":
            print("Jeu terminé par le joueur. Merci d'avoir joué !")
            break

        grille[ligne][colonne] = tour
        if verifier_gagnant(grille, tour):
            print(f"Félicitations {noms[tour]} ({tour}) ! Vous avez trouvé le mot.")
            scores[tour] += 1
            print(f"Score - {noms['X']} (X): {scores['X']}, {noms['O']} (O): {scores['O']}")
            if input("Voulez-vous rejouer ? (oui/non) : ").lower() != 'oui':
                print("Merci d'avoir joué au jeu du Tic-Tac-Toe ! À bientôt !")
                break
            grille = [[" " for _ in range(3)] for _ in range(3)]
            tour = random.choice(['X', 'O'])
        else:
            tour = 'O' if tour == 'X' else 'X'
        
        if all(cell != " " for row in grille for cell in row):
            print("Match nul !")
            afficher_grille(grille)
            if input("Voulez-vous rejouer ? (oui/non) : ").lower() != 'oui':
                print("Merci d'avoir joué. À bientôt !")
                break
            grille = [[" " for _ in range(3)] for _ in range(3)]
            tour = random.choice(['X', 'O'])

if __name__ == "__main__":
    jouer()
