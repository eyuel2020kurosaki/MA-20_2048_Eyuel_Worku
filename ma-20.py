# Auteur : Eyuel Worku
# Date : 17.03.2026
# Module : MA-20
# PROJET:  2048 




import tkinter as tk
import random

numbers = [
    [4, 0, 0, 0],
    [1024   , 0, 0, 0],
    [1024, 0, 0, 0],
    [2, 2, 4, 0]
]

tile_colors = {
    0: "#E1D5E7", 2: "#94A2C3", 4: "#9CA5BF", 8: "#707DA4",
    16: "#4E5161", 32: "#D0D4E4", 64: "#E1E5EE", 128: "#C7CCDB",
    256: "#767B91", 512: "#62667A", 1024: "#F7C59F", 2048: "#E6E6E6",
    4096: "#86797A", 8192: "#741C8D",
}

Tuiles_GAP = 4


# ----------------------------------------------------------
# pack 4 des tuiles (Correction pour éviter les doubles fusions)
# ----------------------------------------------------------
def pack(a, b, c, d):

    # --- 1) Décaler à gauche tant qu'il y a des zéros au début ---
    # Objectif : "compacter" les nombres en poussant les zéros à droite.
    if a == 0:
        a, b, c, d = b, c, d, 0  # glisse tout à gauche

    if a == 0:
        a, b, c, d = b, c, d, 0  # répéter si encore un zéro en tête

    if a == 0:
        a, b, c, d = b, c, d, 0  # répéter une troisième fois (max 3 déplacements)

    # Si la deuxième case est encore vide, on continue de compacter
    if b == 0:
        b, c, d = c, d, 0

    if b == 0:
        b, c, d = c, d, 0  # une seconde fois au cas où

    # Dernier petit décalage si le troisième est vide
    if c == 0:
        c, d = d, 0

    # --- 2) Fusion des tuiles égales ---
    # Règle : on fusionne de gauche à droite. Une fusion crée un zéro à droite.
    if a == b:
        a, b, c, d = 2 * a, c, d, 0  # fusion a-b puis on tasse à gauche

    if b == c:
        b, c, d = 2 * b, d, 0        # fusion b-c puis on tasse

    if c == d:
        c, d = 2 * c, 0              # fusion c-d

    return a, b, c, d

# ----------------------------------------------------------
# APPARITION D'UNE TUILE ALEATOIRE
# ----------------------------------------------------------
def spawn_tile():
    # On crée une liste vide qui va stocker les cases vides
    cases_vides = []

    # On parcourt toute la grille pour trouver les cases qui valent 0
    for row in range(4):
        for col in range(4):
            if numbers[row][col] == 0:
                # On ajoute la position de la case vide dans la liste
                cases_vides.append((row, col))

    # Si la liste est vide, la grille est pleine, on ne fait rien
    if len(cases_vides) == 0:
        return

    # On choisit une case vide au hasard dans la liste
    case_choisie = cases_vides[random.randint(0, len(cases_vides) - 1)]

    # On récupère la ligne et la colonne de la case choisie
    row = case_choisie[0]
    col = case_choisie[1]

    # 80% de chances d'avoir un 2, 20% de chances d'avoir un 4
    if random.randint(1, 10) <= 8:
        numbers[row][col] = 2
    else:
        numbers[row][col] = 4

# ----------------------------------------------------------
# VICTOIRE : vérifie si une tuile vaut 2048
# ----------------------------------------------------------
def check_victoire():
    # On parcourt toute la grille
    for row in range(4):
        for col in range(4):
            # Si on trouve une tuile qui vaut 2048, le joueur a gagné
            if numbers[row][col] == 2048:
                return True
    # Sinon on retourne False
    return False

# ----------------------------------------------------------
# DEFAITE : vérifie si la grille est pleine et aucun mouvement possible
# ----------------------------------------------------------
def check_defaite():
    # On vérifie d'abord s'il reste des cases vides
    for row in range(4):
        for col in range(4):
            if numbers[row][col] == 0:
                # Il reste une case vide donc ce n'est pas une défaite
                return False

    # On vérifie si deux cases voisines sont égales horizontalement
    # Si oui, une fusion est encore possible donc ce n'est pas une défaite
    for row in range(4):
        if numbers[row][0] == numbers[row][1]:
            return False
        if numbers[row][1] == numbers[row][2]:
            return False
        if numbers[row][2] == numbers[row][3]:
            return False

    # On vérifie si deux cases voisines sont égales verticalement
    for col in range(4):
        if numbers[0][col] == numbers[1][col]:
            return False
        if numbers[1][col] == numbers[2][col]:
            return False
        if numbers[2][col] == numbers[3][col]:
            return False

    # Si on arrive ici : grille pleine et aucune fusion possible → défaite
    return True

# ----------------------------------------------------------
# AFFICHE UN MESSAGE DE FIN DE PARTIE
# ----------------------------------------------------------
def afficher_message(texte):
    # On affiche le texte directement sur la fenêtre tkinter
    label_fin = tk.Label(win, text=texte, font=("Arial", 24, "bold"))
    label_fin.pack(pady=10)

    # On bloque les touches du clavier pour stopper la partie
    win.unbind('<Key>')

# ----------------------------------------------------------
# les moves des tuiles
# ----------------------------------------------------------
def left():
    for li in range(4):
        #print("test : " ,pack(numbers[li]))

        a = numbers[li][0] 
        b = numbers[li][1]
        c = numbers[li][2]
        d = numbers[li][3]

        a2, b2, c2, d2 = pack(a, b, c, d)

        numbers[li][0] = a2
        numbers[li][1] = b2
        numbers[li][2] = c2
        numbers[li][3] = d2

        #numbers[li][0], numbers[li][1], numbers[li][2], numbers[li][3] = pack(*numbers[li])

    # On fait apparaître une nouvelle tuile
    spawn_tile()
    # On met à jour l'affichage
    display_grid()

    # On vérifie si le joueur a gagné ou perdu
    if check_victoire() == True:
        afficher_message("Tu as gagné !")
    elif check_defaite() == True:
        afficher_message("Game Over !")

def right():
    for li in range(4):
        print(numbers[li])
        a = numbers[li][3]
        b = numbers[li][2]
        c = numbers[li][1]
        d = numbers[li][0]


        a2, b2, c2, d2 = pack(a,b,c,d)
        print(a2,b2,c2,d2)
        numbers[li][3] = a2
        numbers[li][2] = b2
        numbers[li][1] = c2
        numbers[li][0] = d2

    # On fait apparaître une nouvelle tuile
    spawn_tile()
    # On met à jour l'affichage
    display_grid()

# ---- mouvement de la VICTOIRE/ DE LA DEFAITE ----

    # On vérifie si le joueur a gagné ou perdu
    if check_victoire() == True:
        afficher_message("Tu as gagné 🔥🔥🔥 !")
    elif check_defaite() == True:
        afficher_message("Game Over 🙂‍↕️🙂‍↕️💀💀!")

def up():
    for col in range(4):
        a, b, c, d = numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col]
        # On réinjecte le résultat dans la grille
        numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col] = pack(a, b, c, d)

    # On fait apparaître une nouvelle tuile
    spawn_tile()
    # On met à jour l'affichage
    display_grid()

# ---- mouvement de la VICTOIRE/ DE LA DEFAITE ----

    # On vérifie si le joueur a gagné ou perdu
    if check_victoire() == True:
        afficher_message("Tu as gagné !")
    elif check_defaite() == True:
        afficher_message("Game Over !")

def down():
    for col in range(4):
        a, b, c, d = numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col]
        # On réinjecte le résultat dans la grille
        numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col] = pack(a, b, c, d)

    # On fait apparaître une nouvelle tuile
    spawn_tile()
    # On met à jour l'affichage
    display_grid()

# ---- mouvement de la VICTOIRE/ DE LA DEFAITE ----

    # On vérifie si le joueur a gagné ou perdu
    if check_victoire() == True:
        afficher_message("Tu as gagné !")
    elif check_defaite() == True:
        afficher_message("Game Over !")

# ----------------------------------------------------------
# GESTION DU CLAVIER
# ----------------------------------------------------------
def press(event):
    if event.keysym == 'Up':    up()
    if event.keysym == 'Down':  down()
    if event.keysym == 'Left':  left()
    if event.keysym == 'Right': right()

# ----------------------------------------------------------
# AFFICHAGE ET INTERFACE
# ----------------------------------------------------------
def display_grid():
    for row in range(4):
        for col in range(4):
            value = numbers[row][col]
            label = labels[row][col]
            label.configure(
                text=str(value) if value != 0 else "",
                bg=tile_colors.get(value, "#BBB"),
                fg="#111" if 0 < value <= 4 else "#FFF"
            )

win = tk.Tk()
win.title("2048")
win.configure(background="#EBF5FF")

board = tk.Frame(win, bg="#C0BEBE", padx=Tuiles_GAP, pady=Tuiles_GAP)
board.pack(padx=10, pady=10)

labels = []
for row in range(4):
    line = []
    for col in range(4):
        label = tk.Label(board, width=4, height=2, font=("Arial", 20, "bold"))
        label.grid(row=row, column=col, padx=Tuiles_GAP, pady=Tuiles_GAP)
        line.append(label)
    labels.append(line)

# Liaison des touches
win.bind('<Key>', press)

display_grid()


win.mainloop()