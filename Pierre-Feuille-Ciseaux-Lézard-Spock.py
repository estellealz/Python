import random

CHOICES = ["pierre", "feuille", "ciseaux", "lezard", "spock"]

RULES = {
    "pierre": ["ciseaux", "lezard"],
    "feuille": ["pierre", "spock"],
    "ciseaux": ["feuille", "lezard"],
    "lezard": ["spock", "feuille"],
    "spock": ["ciseaux", "pierre"]
}

def afficher_regles():
    print("📜 RÈGLES DU JEU : Pierre - Feuille - Ciseaux - Lézard - Spock\n")
    print("Chaque choix bat deux autres et perd contre deux autres.\n")
    print("✔️ Les relations sont :\n")
    print(" - Ciseaux coupent Feuille")
    print(" - Feuille couvre Pierre")
    print(" - Pierre écrase Lézard")
    print(" - Lézard empoisonne Spock")
    print(" - Spock casse Ciseaux")
    print(" - Ciseaux décapitent Lézard")
    print(" - Lézard mange Feuille")
    print(" - Feuille réfute Spock")
    print(" - Spock vaporise Pierre")
    print(" - Pierre écrase Ciseaux\n")
    print("Tapez l'un des choix pour jouer.\n")

def determine_winner(player, computer):
    if player == computer:
        return "Égalité"
    elif computer in RULES[player]:
        return "Gagné"
    else:
        return "Perdu"

def main():
    print("🎮 Bienvenue dans Pierre-Feuille-Ciseaux-Lézard-Spock !\n")
    afficher_regles()

    player_score = 0
    computer_score = 0

    while True:
        print("Choix possibles :", ", ".join(CHOICES))
        player = input("Votre choix : ").lower()

        if player not in CHOICES:
            print("❌ Choix invalide. Essayez encore.\n")
            continue

        computer = random.choice(CHOICES)
        print(f"🤖 L'ordinateur a choisi : {computer}")

        result = determine_winner(player, computer)
        if result == "Gagné":
            player_score += 1
        elif result == "Perdu":
            computer_score += 1

        print(f"📣 Résultat : {result}")
        print(f"📊 Score - Vous : {player_score} | Ordinateur : {computer_score}\n")

        rejouer = input("🔁 Voulez-vous rejouer ? (oui/non) : ").strip().lower()
        if rejouer != "oui":
            print("\n👋 Merci d'avoir joué !")
            print(f"🔚 Score final - Vous : {player_score} | Ordinateur : {computer_score}")
            break
        print()

if __name__ == "__main__":
    main()
