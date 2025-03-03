distance = 450  # en km
consommation_ancienne = 14  # en L/100 km
prix_carburant = 4800  # en MGA/L

# Calcul de la quantité de carburant nécessaire pour l'ancien modèle
carburant_necessaire_ancienne = (consommation_ancienne / 100) * distance
cout_total_ancienne = carburant_necessaire_ancienne * prix_carburant

# Affichage des résultats pour l'ancien modèle
print(f"Carburant nécessaire pour l'ancien modèle: {carburant_necessaire_ancienne:.2f} L")
print(f"Coût total pour l'ancien modèle: {cout_total_ancienne:.2f} MGA")

# Calcul pour le nouveau modèle
reduction_consommation = 0.20
consommation_nouvelle = consommation_ancienne * (1 - reduction_consommation)
carburant_necessaire_nouvelle = (consommation_nouvelle / 100) * distance
cout_total_nouvelle = carburant_necessaire_nouvelle * prix_carburant

# Affichage des résultats pour le nouveau modèle
print(f"Carburant nécessaire pour le nouveau modèle: {carburant_necessaire_nouvelle:.2f} L")
print(f"Coût total pour le nouveau modèle: {cout_total_nouvelle:.2f} MGA")