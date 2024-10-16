# Demande à l'utilisateur de saisir le nombre de notes
nombre_de_notes = int(input("Combien de notes veux-tu entrer ? "))

# Initialise une liste pour stocker les notes
notes = []

# Boucle pour obtenir les notes
for i in range(nombre_de_notes):
    while True:
        note = float(input(f"Entre la note {i + 1} (doit être entre 0 et 20) : "))
        if 0 <= note <= 20:
            notes.append(note)
            break
        else:
            print("Erreur : la note doit être entre 0 et 20. Essaie à nouveau.")

# Calcul de la moyenne des notes
moyenne = sum(notes) / nombre_de_notes

# Affichage de la moyenne et du message de réussite ou d'échec
print(f"La moyenne des notes est : {moyenne:.2f}")
if moyenne >= 10:
    print("Félicitations ! Tu as passé.")
else:
    print("Désolé, tu n'as pas passé cette fois.")
