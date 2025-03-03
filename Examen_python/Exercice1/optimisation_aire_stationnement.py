long_parking = 120  # en m
larg_parking = 50    # en m
long_place = 5      # en m
larg_place = 2.5     # en m
distance_range = 1     # en m

place_par_range = larg_parking // larg_place

nombre_range = long_parking // (long_place + distance_range)

nombre_places = int(place_par_range * nombre_range)

tarif_journalier = 3000  # en MGA

revenu_maximum = nombre_places * tarif_journalier

print(f"Nombre maximum de voitures pouvant être garées : {nombre_places}")
print(f"Revenu maximum du parking sur une journée : {revenu_maximum} MGA")

espace_total = long_parking * larg_parking
espace_bus = 0.15 * espace_total
espace_restant = espace_total - espace_bus


nombre_places_restant = (espace_restant // (long_place * larg_place))


revenu_maximum_restant = int(nombre_places_restant * tarif_journalier)

print(f"Nombre de places disponibles avec zone réservée aux bus : {nombre_places_restant}")
print(f"Revenu maximum du parking sur une journée avec la zone réservée aux bus : {revenu_maximum_restant} MGA")