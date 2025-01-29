import os
import random
import sys
import msvcrt  # Importation nécessaire pour les entrées clavier sous Windows
import time

def afficher_grille(grille):
    os.system('cls' if os.name == 'nt' else 'clear')
    for ligne in grille:
        print(''.join(ligne))

def initialiser_grille(hauteur, largeur):
    # Crée une grille avec des bordures
    grille = [[' ' for _ in range(largeur)] for _ in range(hauteur)]
    
    # Dessine les bordures horizontales
    for y in range(largeur):
        grille[0][y] = '🟫'  # Bordure supérieure
        grille[hauteur-1][y] = '🟫'  # Bordure inférieure
    
    # Dessine les bordures verticales
    for x in range(hauteur):
        grille[x][0] = '🟫'  # Bordure gauche
        grille[x][largeur-1] = '🟫'  # Bordure droite
    
    return grille

def placer_pomme(grille, hauteur, largeur, serpent):
    # Trouve des positions libres qui ne sont pas occupées par le serpent
    positions_libres = [
        (x, y) for x in range(1, hauteur-1) 
        for y in range(1, largeur-1) 
        if (x, y) not in serpent and grille[x][y] == ' '
    ]
    
    if positions_libres:
        x, y = random.choice(positions_libres)
        grille[x][y] = '🍎'
        return x, y
    
    return None, None

def afficher_score(score):
    print(f"Score: {score}")

def jeu_snake():
    hauteur, largeur = 20, 40
    grille = initialiser_grille(hauteur, largeur)
    x, y = hauteur // 2, largeur // 2
    serpent = [(x, y)]
    direction = 'DROITE'
    pomme_x, pomme_y = placer_pomme(grille, hauteur, largeur, serpent)
    score = 0
    vitesse = 0.2  # Vitesse initiale légèrement ajustée

    while True:
        # Réinitialise la grille avec les bordures
        grille = initialiser_grille(hauteur, largeur)
        
        # Place la pomme
        if pomme_x is not None and pomme_y is not None:
            grille[pomme_x][pomme_y] = '🍎'
        
        # Dessine le serpent
        for sx, sy in serpent:
            grille[sx][sy] = '🟢'  # Utilise un emoji vert pour le serpent

        if msvcrt.kbhit():  # Vérifie si une touche a été pressée
            touche = msvcrt.getch()  # Lit la touche pressée
            if touche in [b'w', b'H'] and direction != 'BAS':  # Flèche haut ou 'w'
                direction = 'HAUT'
            elif touche in [b's', b'P'] and direction != 'HAUT':  # Flèche bas ou 's'
                direction = 'BAS'
            elif touche in [b'a', b'K'] and direction != 'DROITE':  # Flèche gauche ou 'a'
                direction = 'GAUCHE'
            elif touche in [b'd', b'M'] and direction != 'GAUCHE':  # Flèche droite ou 'd'
                direction = 'DROITE'
            elif touche == b'\x1b':  # Touche 'Échap' pour quitter
                break

        # Ajuste la vitesse en fonction de la direction
        if direction in ['HAUT', 'BAS']:
            time.sleep(vitesse * 1.5)  # Un peu plus lent verticalement
        else:
            time.sleep(vitesse)

        # Déplace le serpent
        x += (direction == 'BAS') - (direction == 'HAUT')
        y += (direction == 'DROITE') - (direction == 'GAUCHE')

        # Vérifie la collision avec les bordures
        if (x <= 0 or x >= hauteur-1 or y <= 0 or y >= largeur-1 or 
            (x, y) in serpent):
            print("Jeu terminé. Votre score est :", score)
            break

        # Ajoute la nouvelle position en tête de serpent
        serpent.insert(0, (x, y))

        # Mange la pomme
        if (x, y) == (pomme_x, pomme_y):
            score += 1
            vitesse = max(0.05, vitesse - 0.01)  # Augmente la vitesse
            pomme_x, pomme_y = placer_pomme(grille, hauteur, largeur, serpent)
        else:
            serpent.pop()  # Retire la dernière position du serpent

        afficher_grille(grille)
        afficher_score(score)

    print("Game Over! Appuyez sur une touche pour quitter...")
    msvcrt.getch()

if __name__ == "__main__":
    jeu_snake()