def obtenir_taux_de_change(devise_source, devise_cible):
    """Obtient le taux de change entre deux devises en utilisant un dictionnaire prédéfini."""
    # Dictionnaire complet des taux de change
    taux_de_change = {
        ('EUR', 'USD'): 1.16,
        ('USD', 'EUR'): 0.86,
        ('USD', 'JPY'): 113.5,
        ('JPY', 'USD'): 0.0088,
        ('EUR', 'JPY'): 130.15,
        ('JPY', 'EUR'): 0.00768,
    }

    # Gérer le cas où la devise source et la devise cible sont les mêmes
    if devise_source == devise_cible:
        return 1.0

    return taux_de_change.get((devise_source, devise_cible), None)

def convertir(devise_source, devise_cible, montant):
    """Convertit un montant de la devise source à la devise cible."""
    taux = obtenir_taux_de_change(devise_source, devise_cible)
    if taux:
        return montant * taux
    else:
        return None

def main():
    """Fonction principale qui exécute le convertisseur de devises."""
    print("Devises disponibles : EUR, USD, JPY")
    while True:
        try:
            montant = float(input("Entrez le montant à convertir : "))
            if montant < 0:
                print("Veuillez entrer un montant positif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    while True:
        devise_source = input("Entrez la devise source (eur, usd, jpy) : ").upper()
        devise_cible = input("Entrez la devise cible (eur, usd, jpy) : ").upper()
        if devise_source not in ['EUR', 'USD', 'JPY'] or devise_cible not in ['EUR', 'USD', 'JPY']:
            print("Devises non reconnues, veuillez utiliser uniquement EUR, USD ou JPY.")
            continue
        montant_converti = convertir(devise_source, devise_cible, montant)
        if montant_converti is not None:
            print(f"{montant} {devise_source} équivaut à {montant_converti:.2f} {devise_cible}.")
            break
        else:
            print("Désolé, la conversion entre ces devises n'est pas disponible.")

if __name__ == "__main__":
    main()
