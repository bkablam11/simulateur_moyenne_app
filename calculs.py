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
    """Calcule la moyenne pondérée des notes avec leurs coefficients."""
    total = sum(note * coeff for note, coeff in zip(notes, coeffs))
    total_coeff = sum(coeffs)
    return total / total_coeff if total_coeff != 0 else 0


def calculer_suggestions(notes, coeffs, moy1, moy2, cible):
    """Calcule les suggestions pour atteindre une moyenne annuelle cible."""
    try:
        # Calcul de la moyenne actuelle pondérée
        total_notes = sum(n * c for n, c in zip(notes, coeffs))
        total_coeffs = sum(coeffs)
        moyenne_actuelle = total_notes / total_coeffs if total_coeffs != 0 else 0

        # Coefficients des trimestres
        coeff1, coeff2, coeff3 = 1, 2, 2

        # Calcul de la moyenne actuelle annuelle
        moyenne_annuelle_actuelle = (moy1 * coeff1 + moy2 * coeff2 + moyenne_actuelle * coeff3) / (coeff1 + coeff2 + coeff3)

        # Vérification de l'objectif
        objectif_atteint = moyenne_annuelle_actuelle >= cible

        # Résultats initiaux
        resultats = f"Moyenne actuelle du 3e trimestre : {round(moyenne_actuelle, 2)}\n"
        resultats += f"Moyenne actuelle annuelle : {round(moyenne_annuelle_actuelle, 2)}\n"
        resultats += f"Moyenne annuelle souhaitée : {cible}\n"

        if objectif_atteint:
            resultats += "✅ L'objectif est déjà atteint !\n"
        else:
            manque = cible * (coeff1 + coeff2 + coeff3) - (moy1 * coeff1 + moy2 * coeff2 + moyenne_actuelle * coeff3)
            resultats += f"🔺 Points à gagner pour atteindre l'objectif : {round(manque*total_coeffs, 2)}\n"

            # Suggestions pour les matières
            resultats += "\n📌 Suggestions pour améliorer les notes :\n"
            for i, (note, coeff) in enumerate(zip(notes, coeffs)):
                if note < 20:  # On ne peut pas dépasser 20
                    note_min = round((manque / coeffs[i]) + notes[i], 2)
                    if note_min > 20:
                        note_min = 20
                    resultats += f" - {matieres[i]} : Note minimale requise = {note_min}\n"

        return resultats, objectif_atteint

    except ZeroDivisionError:
        raise ValueError("Les coefficients ne peuvent pas être tous nuls.")
    except Exception as e:
        raise ValueError(f"Erreur lors du calcul : {e}")


def export_txt(resultats, filename="resultats.txt"):
    """Exporte les résultats dans un fichier texte."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(resultats)