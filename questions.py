import random

def afficher_question(question, choix):
    print(question)
    for idx, choix in enumerate(choix, 1):
        print(f"{idx}. {choix}")
    while True:
        try:
            reponse = int(input("Entrez le numéro de votre réponse (1-4) : "))
            if 1 <= reponse <= 4:  # S'assure que la réponse est entre 1 et 4
                return reponse
            else:
                print("Veuillez entrer un numéro valide entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un numéro entier.")

def lancer_quiz(questions):
    score = 0
    questions_selectionnees = random.sample(list(questions.items()), 5)  # Sélectionner 5 questions aléatoirement
    for question, details in questions_selectionnees:
        print("\nNouvelle question :")
        reponse = afficher_question(question, details['choix'])
        if reponse == details['reponse_correcte']:
            print("Correct !")
            score += 1
        else:
            print("Incorrect.")
        print(details['explication'])  # Afficher l'explication après chaque réponse
    print(f"\nVotre score final est : {score} sur {len(questions_selectionnees)}")

def main():
    questions = {
        "Quelle est la capitale de l'Australie ?": {
            "choix": ["Sydney", "Melbourne", "Canberra", "Perth"],
            "reponse_correcte": 3,
            "explication": "Canberra est la capitale de l'Australie, située entre Sydney et Melbourne."
        },
        "Qui a écrit 'Les Misérables' ?": {
            "choix": ["Victor Hugo", "Albert Camus", "Voltaire", "Émile Zola"],
            "reponse_correcte": 1,
            "explication": "Victor Hugo est l'auteur de 'Les Misérables', publié en 1862."
        },
        "Quel est l'élément chimique le plus abondant dans l'univers ?": {
            "choix": ["Oxygène", "Hydrogène", "Carbone", "Azote"],
            "reponse_correcte": 2,
            "explication": "L'hydrogène est l'élément le plus abondant dans l'univers, constituant environ 75% de la masse baryonique."
        },
        "Quelle année a vu la chute du mur de Berlin ?": {
            "choix": ["1989", "1991", "1987", "1990"],
            "reponse_correcte": 1,
            "explication": "Le mur de Berlin est tombé en 1989, marquant un tournant majeur dans l'histoire de la Guerre froide."
        },
        "Qui a peint 'La Nuit étoilée' ?": {
            "choix": ["Claude Monet", "Vincent Van Gogh", "Pablo Picasso", "Salvador Dalí"],
            "reponse_correcte": 2,
            "explication": "Vincent Van Gogh a peint 'La Nuit étoilée' en 1889 pendant son séjour à l'asile de Saint-Rémy."
        },
        "Quel pays a remporté la Coupe du monde de football en 2018 ?": {
            "choix": ["Brésil", "France", "Allemagne", "Argentine"],
            "reponse_correcte": 2,
            "explication": "La France a remporté la Coupe du monde de football en 2018, battant la Croatie 4-2 en finale."
        },
        "Quel est le livre le plus vendu au monde après la Bible ?": {
            "choix": ["Le Seigneur des Anneaux", "Don Quichotte", "Le Petit Prince", "Harry Potter"],
            "reponse_correcte": 2,
            "explication": "Don Quichotte, écrit par Miguel de Cervantes au début du 17e siècle, est souvent considéré comme le livre le plus vendu après la Bible."
        },
        "Quel est le plus grand désert du monde ?": {
            "choix": ["Sahara", "Arctique", "Antarctique", "Gobi"],
            "reponse_correcte": 3,
            "explication": "L'Antarctique est techniquement le plus grand désert du monde, caractérisé par une extrême sécheresse et de basses précipitations."
        },
        "Qui est le fondateur de la psychanalyse ?": {
            "choix": ["Sigmund Freud", "Carl Jung", "Ivan Pavlov", "Jean Piaget"],
            "reponse_correcte": 1,
            "explication": "Sigmund Freud est reconnu comme le fondateur de la psychanalyse, développant cette méthode thérapeutique à la fin du 19e et au début du 20e siècle."
        },
        "Quel scientifique est célèbre pour sa théorie de la relativité ?": {
            "choix": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei"],
            "reponse_correcte": 2,
            "explication": "Albert Einstein est célèbre pour sa théorie de la relativité, qui a révolutionné notre compréhension de l'espace, du temps et de la gravité."
        },
        "Dans quelle ville se trouve le Colisée ?": {
            "choix": ["Athènes", "Rome", "Naples", "Milan"],
            "reponse_correcte": 2,
            "explication": "Le Colisée est situé à Rome, Italie. C'est l'un des monuments les plus célèbres de l'Empire romain."
        },
        "Quel philosophe est connu pour sa phrase 'Je pense, donc je suis' ?": {
            "choix": ["Platon", "Descartes", "Aristote", "Socrate"],
            "reponse_correcte": 2,
            "explication": "René Descartes, un philosophe français, a formulé cette célèbre déclaration, soulignant l'importance de la pensée comme preuve de l'existence."
        },
        "Qui a découvert la pénicilline ?": {
            "choix": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Gregor Mendel"],
            "reponse_correcte": 2,
            "explication": "Alexander Fleming a découvert la pénicilline en 1928, ce qui a marqué le début de l'ère moderne des antibiotiques."
        },
        "Quel pays est connu comme le 'pays du Soleil Levant' ?": {
            "choix": ["Chine", "Japon", "Corée du Sud", "Thaïlande"],
            "reponse_correcte": 2,
            "explication": "Le Japon est souvent appelé le 'pays du Soleil Levant' car il se trouve à l'est où le soleil se lève."
        },
        "Quel est le plus long fleuve du monde ?": {
            "choix": ["Nil", "Amazone", "Yangtsé", "Mississippi"],
            "reponse_correcte": 2,
            "explication": "L'Amazone est le plus long fleuve du monde, mesurant environ 7,000 kilomètres."
        },
        "Quel roi d'Angleterre a eu six épouses ?": {
            "choix": ["Henri V", "Henri VIII", "Richard III", "Édouard VII"],
            "reponse_correcte": 2,
            "explication": "Henri VIII est célèbre pour avoir eu six épouses dans sa quête d'un héritier mâle."
        },
        "Quel est le premier film de l'univers cinématographique Marvel ?": {
            "choix": ["Iron Man", "The Hulk", "Thor", "Captain America"],
            "reponse_correcte": 1,
            "explication": "Iron Man, sorti en 2008, est le premier film qui a introduit l'univers cinématographique Marvel."
        },
        "Quelle structure est plus ancienne que les autres ?": {
            "choix": ["Les pyramides d'Égypte", "Stonehenge", "Le Colisée", "La Grande Muraille de Chine"],
            "reponse_correcte": 2,
            "explication": "Stonehenge est estimé avoir été construit entre 3000 et 2000 av. J.-C., ce qui le rend plus ancien que les autres structures listées."
        },
        "Quelle est la période de règne approximative de la dynastie Ming ?": {
            "choix": ["1368-1644", "1256-1368", "1420-1650", "1300-1450"],
            "reponse_correcte": 1,
            "explication": "La dynastie Ming a régné en Chine de 1368 à 1644, une période célèbre pour son développement culturel et technologique."
        },
        "Quelle est la distance moyenne entre la Terre et le Soleil ?": {
            "choix": ["92 millions de miles", "93 millions de miles", "91 millions de miles", "94 millions de miles"],
            "reponse_correcte": 2,
            "explication": "La distance moyenne entre la Terre et le Soleil est d'environ 93 millions de miles, ou 150 millions de kilomètres."
        }
    }

    while True:
        lancer_quiz(questions)
        if input("Voulez-vous jouer une autre partie ? (oui/non) : ").lower() != 'oui':
            break

if __name__ == "__main__":
    main()
