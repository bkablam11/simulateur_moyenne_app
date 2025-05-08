matieres = [
    "Français",      # 1
    "Anglais",       # 2
    "Mathématiques", # 3
    "Physique",      # 4
    "SVT",           # 5
    "Histoire-Géo",  # 6
    "EDHC",          # 7
    "Informatique",  # 8
    "Conduite",      # 9
    "EPS"            # 10
]


def calculer_moyenne_ponderee(notes, coeffs):
    total = sum(note * coeff for note, coeff in zip(notes, coeffs))
    total_coeff = sum(coeffs)
    return total / total_coeff if total_coeff != 0 else 0

def calculer_suggestions(notes, coeffs, moy1, moy2, cible):
    total_notes = sum(n * c for n, c in zip(notes, coeffs))
    total_coeffs = sum(coeffs)
    moyenne_actuelle = total_notes / total_coeffs

    moy_t3_cible = 3 * cible - (moy1 + moy2)
    manque = moy_t3_cible - moyenne_actuelle

    resultats = f"Moyenne 3e trimestre requise : {round(moy_t3_cible,2)}\n"
    
    resultats += f"Moyenne actuelle : {round(moyenne_actuelle,2)}\n"

    objectif_atteint = manque <= 0  # Ajout : objectif atteint ou non
    
    if objectif_atteint:
        resultats += "✅ L'objectif est déjà atteint !"
    else:
        resultats += f"🔺 Points à gagner : {round(manque, 2)}\n"
        indices_zero = [i for i, note in enumerate(notes) if note == 0]
        total_coeff_zero = sum(coeffs[i] for i in indices_zero)
        resultats += f"\n📌 Suggestions pour matières à 0 :\n"
        for i in indices_zero:
            note_min = round((manque * coeffs[i]) / total_coeff_zero, 2)
            #resultats += f" - Matière {i + 1} (coeff {coeffs[i]}): ≥ {note_min}/20\n"
            nom_matiere = matieres[i] if i < len(matieres) else f"Matière {i+1}"
            resultats += f" - {nom_matiere} (coeff {coeffs[i]}): ≥ {note_min:.2f}/20\n"

    return resultats, objectif_atteint  # Retourne aussi l'état de l'objectif

def export_txt(resultats, filename="resultats.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(resultats)
        

