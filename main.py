import tkinter as tk
from tkinter import messagebox
import sys, os

sys.path.append(os.getcwd())
from calculs import calculer_suggestions, export_txt


def calculer():
    try:
        # Récupération des données saisies
        notes = list(map(float, entree_notes.get().split(',')))
        coeffs = list(map(int, entree_coeffs.get().split(',')))
        moy1 = float(entree_moy1.get())
        moy2 = float(entree_moy2.get())
        cible = float(entree_cible.get())

        # Vérification des longueurs des listes
        if len(notes) != len(coeffs):
            raise ValueError("Le nombre de notes et de coefficients doit être identique.")

        # Calcul des résultats
        resultats, objectif_atteint = calculer_suggestions(notes, coeffs, moy1, moy2, cible)

        # Déterminer la couleur en fonction de l'objectif
        couleur = "green" if objectif_atteint else "red"

        # Affichage des résultats
        sortie_resultats.config(state='normal', fg=couleur)
        sortie_resultats.delete('1.0', tk.END)
        sortie_resultats.insert(tk.END, resultats)
        sortie_resultats.config(state='disabled')

    except ValueError as ve:
        messagebox.showerror("Erreur de saisie", str(ve))
    except Exception as e:
        messagebox.showerror("Erreur", str(e))


def exporter():
    contenu = sortie_resultats.get("1.0", tk.END)
    export_txt(contenu)
    messagebox.showinfo("Exportation", "Les résultats ont été exportés avec succès.")


# --- Interface ---
fenetre = tk.Tk()
fenetre.title("Simulateur de moyenne")

# Explications
explication = tk.Label(
    fenetre,
    text=(
        "📘 Principe : Calculez la note minimale au 3e trimestre pour atteindre une moyenne annuelle.\n\n"
        "🧮 Ordre des matières (avec coefficients) :\n"
        "1. Français (3)\n"
        "2. Anglais (2)\n"
        "3. Mathématiques (3)\n"
        "4. Physique-Chimie (2)\n"
        "5. SVT (2)\n"
        "6. Histoire-Géo (2)\n"
        "7. EDHC (1)\n"
        "8. Informatique (1)\n"
        "9. Conduite (1)\n"
        "10. EPS (1)"
    ),
    justify="left",
    anchor="w"
)
explication.pack(padx=10, pady=(10, 0), fill="both")

# Champs de saisie
tk.Label(fenetre, text="Notes (séparées par des virgules)").pack()
entree_notes = tk.Entry(fenetre, width=60)
entree_notes.pack()

tk.Label(fenetre, text="Coefficients correspondants").pack()
entree_coeffs = tk.Entry(fenetre, width=60)
entree_coeffs.pack()

tk.Label(fenetre, text="Moyenne 1er trimestre").pack()
entree_moy1 = tk.Entry(fenetre)
entree_moy1.pack()

tk.Label(fenetre, text="Moyenne 2e trimestre").pack()
entree_moy2 = tk.Entry(fenetre)
entree_moy2.pack()

tk.Label(fenetre, text="Moyenne annuelle souhaitée").pack()
entree_cible = tk.Entry(fenetre)
entree_cible.pack()

# Boutons
tk.Button(fenetre, text="Calculer", command=calculer).pack(pady=10)
tk.Button(fenetre, text="Exporter", command=exporter).pack(pady=5)

# Zone de résultats
sortie_resultats = tk.Text(fenetre, height=12, width=80, state='disabled', bg='#f0f0f0')
sortie_resultats.pack()

fenetre.mainloop()