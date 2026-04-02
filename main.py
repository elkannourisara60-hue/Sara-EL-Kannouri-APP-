import tkinter as tk
from tkinter import ttk

paddingX = 20
paddingY = 10

root = tk.Tk()
root.title("Boutique Vêtements Marocains")
root.geometry("800x500")

# --- Style ---
style = ttk.Style()
style.theme_use('clam')

frame = tk.Frame(root)
frame.pack(padx=paddingX, pady=paddingY)

# --- Formulaire Produit ---
tk.Label(frame, text="Nom").grid(row=0, column=0, padx=10, pady=5)
entry_nom = tk.Entry(frame)
entry_nom.grid(row=1, column=0, padx=10, pady=5)

tk.Label(frame, text="Catégorie").grid(row=0, column=1, padx=10, pady=5)
entry_cat = tk.Entry(frame)
entry_cat.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Prix").grid(row=0, column=2, padx=10, pady=5)
entry_prix = tk.Entry(frame)
entry_prix.grid(row=1, column=2, padx=10, pady=5)

tk.Label(frame, text="Taille").grid(row=0, column=3, padx=10, pady=5)
entry_taille = tk.Entry(frame)
entry_taille.grid(row=1, column=3, padx=10, pady=5)

# --- Fonctions ---
def add_product():
    nom = entry_nom.get()
    cat = entry_cat.get()
    prix = entry_prix.get()
    taille = entry_taille.get()

    if nom and cat and prix and taille:
        tree.insert('', 0, values=(nom, cat, prix, taille))

        entry_nom.delete(0, tk.END)
        entry_cat.delete(0, tk.END)
        entry_prix.delete(0, tk.END)
        entry_taille.delete(0, tk.END)
    else:
        print("Veuillez remplir tous les champs")

def delete_product():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

# --- Boutons ---
btn_add = tk.Button(frame, text="Ajouter Produit", bg="green", fg="white")
btn_add.config(command=add_product)
btn_add.grid(row=2, column=0, columnspan=4, sticky='news', pady=paddingY)

# --- Tableau ---
columns = ('Nom', 'Catégorie', 'Prix', 'Taille')
tree = ttk.Treeview(frame, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.grid(row=3, column=0, columnspan=4, pady=paddingY)

# --- Bouton supprimer ---
btn_delete = tk.Button(frame, text="Supprimer Produit", bg="red", fg="white")
btn_delete.config(command=delete_product)
btn_delete.grid(row=4, column=0, columnspan=4, sticky='news', pady=paddingY)

root.mainloop()