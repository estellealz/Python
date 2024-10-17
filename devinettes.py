import random

def lancer_jeu():
    nombre_mystere = random.randint(1, 100)
    tentatives = 0
    print("J'ai choisi un nombre entre 1 et 100. Pouvez-vous le deviner ?")

    while True:
        try:
            tentative = int(input("Entrez un nombre : "))
            tentatives += 1
            if tentative < nombre_mystere:
                print("Trop bas ! Essayez encore.")
            elif tentative > nombre_mystere:
                print("Trop haut ! Essayez encore.")
            else:
                print(f"Félicitations ! Vous avez trouvé le nombre après {tentatives} tentatives.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    lancer_jeu()
