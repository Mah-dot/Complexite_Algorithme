import sqlite3


# Fonction pour ajouter un nouveau livre
def ajouter_livre(titre, auteur, annee_publication, disponible):
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO livres (titre, auteur, annee_publication, disponible)
        VALUES (?, ?, ?, ?)
    """, (titre, auteur, annee_publication, disponible))
    conn.commit()
    conn.close()
    print("Livre ajouté avec succès !")


# Fonction pour consulter les livres disponibles
def consulter_livres_disponibles():
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM livres WHERE disponible = 1
    """)
    livres = cursor.fetchall()
    conn.close()
    if livres:
        print("Livres disponibles :")
        for livre in livres:
            print(f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}")
    else:
        print("Aucun livre disponible.")


# Fonction pour rechercher un livre par titre
def rechercher_livre_par_titre(titre):
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM livres WHERE titre LIKE ?
    """, ('%' + titre + '%',))
    livres = cursor.fetchall()
    conn.close()
    if livres:
        print("Résultats de la recherche :")
        for livre in livres:
            disponibilite = "Oui" if livre[4] else "Non"
            print(
                f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}, Disponible: {disponibilite}")
    else:
        print("Aucun livre trouvé avec ce titre.")


# Fonction pour mettre à jour l'état de disponibilité d'un livre
def mettre_a_jour_disponibilite(id_livre, disponible):
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE livres SET disponible = ? WHERE id = ?
    """, (disponible, id_livre))
    if cursor.rowcount > 0:
        print("État de disponibilité mis à jour avec succès.")
    else:
        print("Aucun livre trouvé avec cet ID.")
    conn.commit()
    conn.close()


# Menu principal
def menu():
    while True:
        print("\n--- Menu de la bibliothèque ---")
        print("1. Ajouter un nouveau livre")
        print("2. Consulter les livres disponibles")
        print("3. Rechercher un livre par titre")
        print("4. Mettre à jour l'état de disponibilité d'un livre")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == '1':
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            annee_publication = int(input("Année de publication : "))
            disponible = int(input("Disponible (1 = Oui, 0 = Non) : "))
            ajouter_livre(titre, auteur, annee_publication, disponible)
        elif choix == '2':
            consulter_livres_disponibles()
        elif choix == '3':
            titre = input("Entrez le titre du livre à rechercher : ")
            rechercher_livre_par_titre(titre)
        elif choix == '4':
            id_livre = int(input("ID du livre : "))
            disponible = int(input("Disponible (1 = Oui, 0 = Non) : "))
            mettre_a_jour_disponibilite(id_livre, disponible)
        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


# Exécution du programme
if __name__ == "__main__":
    menu()
