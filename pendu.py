import random

def choisir_mot(niveau):
    mots_faciles = ["chat", "chien", "maison", "arbre", "livre", "pomme", "soleil", "pluie", "lune", "étoile"]
    mots_moyens = ["éléphant", "ordinateur", "bibliothèque", "girafe", "parapluie", "chocolat", "cuisine", "jardin", "horloge", "ballon"]
    mots_difficiles = ["cryptographie", "sphygmomanomètre", "quintessence", "ziggourat", "pamplemousse", "hippopotame", "juridiction", "xylophone", "quadrilatère", "otorhinolaryngologiste"]
    
    if niveau == "facile":
        return random.choice(mots_faciles)
    elif niveau == "moyen":
        return random.choice(mots_moyens)
    elif niveau == "difficile":
        return random.choice(mots_difficiles)
    else:
        print("Niveau invalide, choix par défaut du niveau facile.")
        return random.choice(mots_faciles)

def afficher_mot(mot, lettres_devinees):
    affichage = [lettre if lettre in lettres_devinees else '_' for lettre in mot]
    print("Mot:", ' '.join(affichage))

def jouer_pendu():
    print("Bienvenue au jeu du Pendu!")
    niveau = input("Choisissez un niveau (facile, moyen, difficile): ").lower()
    mot = choisir_mot(niveau)
    lettres_devinees = set()
    tentatives = 7

    while tentatives > 0:
        afficher_mot(mot, lettres_devinees)
        tentative = input("Devinez une lettre: ").lower()

        if tentative in mot:
            lettres_devinees.add(tentative)
            if all(lettre in lettres_devinees for lettre in mot):
                print("Félicitations ! Vous avez trouvé le mot :", mot)
                break
        else:
            tentatives -= 1
            print(f"Non, la lettre '{tentative}' n'est pas dans le mot. Tentatives restantes : {tentatives}")
        
        if tentatives == 0:
            print("Vous avez perdu ! Le mot était :", mot)
    
    if input("Voulez-vous rejouer ? (oui/non) : ").lower() == "oui":
        jouer_pendu()
    else:
        print("Merci d'avoir joué au jeu du Pendu ! À bientôt !")

if __name__ == "__main__":
    jouer_pendu()
