import random

# Le programme choisit un nombre aléatoire entre 1 et 100
nombre_a_trouver = random.randint(1, 100)

# Initialisation des variables
essais = 0  # Pour compter le nombre d'essais
trouve = False  # Pour indiquer si l'utilisateur a trouvé le nombre

print("Bienvenue dans le jeu de devinette ! Le programme a choisi un nombre entre 1 et 100.")
print("Essayez de deviner ce nombre. Entrez votre proposition :")

# Boucle principale
while not trouve:
    # L'utilisateur entre une proposition
    try:
        proposition = int(input("Proposer un nombre : "))
        essais += 1  # Incrément du nombre d'essais

        # Vérification de la proposition
        if proposition > nombre_a_trouver:
            print("Trop grand!")
        elif proposition < nombre_a_trouver:
            print("Trop petit!")
        else:
            print(f"Congrats ! Vous avez trouvé le nombre {nombre_a_trouver} en {essais} essais.")
            trouve = True  # L'utilisateur a trouvé la bonne réponse
    except ValueError:
        print("Entrer un nombre valide !")
