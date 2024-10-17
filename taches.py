def charger_taches():
    try:
        with open('taches.txt', 'r') as file:
            taches = [line.strip() for line in file.readlines()]
        print("Tâches chargées avec succès.")
        return taches
    except FileNotFoundError:
        print("Aucun fichier de tâches trouvé, démarrage avec une liste vide.")
        return []

def sauvegarder_taches(taches):
    with open('taches.txt', 'w') as file:
        for tache in taches:
            file.write(tache + '\n')
    print("Tâches sauvegardées avec succès.")

def afficher_taches(taches):
    print("\n" + "=" * 50)
    print("Voici vos tâches actuelles:")
    if taches:
        for index, tache in enumerate(taches, start=1):
            print(f"{index}. {tache}")
    else:
        print("Vous n'avez aucune tâche en cours.")
    print("=" * 50)

def ajouter_tache(taches):
    tache = input("Entrez la tâche à ajouter : ")
    taches.append(tache)
    print("Tâche ajoutée avec succès.\n")

def supprimer_tache(taches):
    afficher_taches(taches)
    if taches:
        choix = input("Entrez le numéro de la tâche à supprimer : ")
        try:
            choix = int(choix) - 1
            if 0 <= choix < len(taches):
                taches.pop(choix)
                print("Tâche supprimée avec succès.\n")
            else:
                print("Numéro de tâche invalide. Aucune tâche supprimée.\n")
        except ValueError:
            print("Veuillez entrer un numéro valide.\n")

def menu():
    taches = charger_taches()
    while True:
        print("\n" + "=" * 20 + " MENU " + "=" * 20)
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        print("=" * 50)

        choix = input("Choisissez une option : ")
        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            supprimer_tache(taches)
        elif choix == "4":
            sauvegarder_taches(taches)
            print("Merci d'avoir utilisé le gestionnaire de tâches !")
            break
        else:
            print("Option invalide. Veuillez choisir une action valide.")

if __name__ == "__main__":
    menu()
