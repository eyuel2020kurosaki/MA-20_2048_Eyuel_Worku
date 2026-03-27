# Auteur : Eyuel Worku
# Date : 17.03.2026
# Module : MA-20
# PROJET:  2048

import tkinter as tk
import random

numbers = [
    [4, 0, 0, 0],
    [1024, 0, 0, 0],
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

# Garde la référence du label de message pour pouvoir le supprimer au rejouer
label_fin_ref = None

# Score actuel et meilleur score
score = 0
meilleur_score = 0

# ----------------------------------------------------------
# pack 4 des tuiles — retourne aussi les points gagnés
# ----------------------------------------------------------
def pack(a, b, c, d):
    points = 0

    if a == 0:
        a, b, c, d = b, c, d, 0
    if a == 0:
        a, b, c, d = b, c, d, 0
    if a == 0:
        a, b, c, d = b, c, d, 0
    if b == 0:
        b, c, d = c, d, 0
    if b == 0:
        b, c, d = c, d, 0
    if c == 0:
        c, d = d, 0

    if a == b:
        a = 2 * a
        points += a
        b, c, d = c, d, 0
    if b == c:
        b = 2 * b
        points += b
        c, d = d, 0
    if c == d:
        c = 2 * c
        points += c
        d = 0

    return a, b, c, d, points

# ----------------------------------------------------------
# APPARITION D'UNE TUILE ALEATOIRE
# ----------------------------------------------------------
def spawn_tile():
    cases_vides = []
    for row in range(4):
        for col in range(4):
            if numbers[row][col] == 0:
                cases_vides.append((row, col))
    if len(cases_vides) == 0:
        return
    case_choisie = cases_vides[random.randint(0, len(cases_vides) - 1)]
    row = case_choisie[0]
    col = case_choisie[1]
    if random.randint(1, 10) <= 8:
        numbers[row][col] = 2
    else:
        numbers[row][col] = 4

# ----------------------------------------------------------
# VICTOIRE / DEFAITE
# ----------------------------------------------------------
def check_victoire():
    for row in range(4):
        for col in range(4):
            if numbers[row][col] == 2048:
                return True
    return False

def check_defaite():
    for row in range(4):
        for col in range(4):
            if numbers[row][col] == 0:
                return False
    for row in range(4):
        if numbers[row][0] == numbers[row][1]: return False
        if numbers[row][1] == numbers[row][2]: return False
        if numbers[row][2] == numbers[row][3]: return False
    for col in range(4):
        if numbers[0][col] == numbers[1][col]: return False
        if numbers[1][col] == numbers[2][col]: return False
        if numbers[2][col] == numbers[3][col]: return False
    return True

# ----------------------------------------------------------
# AFFICHE UN MESSAGE DE FIN DE PARTIE
# ----------------------------------------------------------
def afficher_message(texte, game_over=False):
    global label_fin_ref
    if label_fin_ref is not None:
        label_fin_ref.destroy()
    label_fin_ref = tk.Label(
        win, text=texte,
        font=("Arial", 20, "bold"),
        bg="#EBF5FF", fg="#333"
    )
    label_fin_ref.pack(pady=5)
    if game_over:
        win.unbind('<Key>')

# ----------------------------------------------------------
# MET A JOUR LE SCORE ET LE MEILLEUR SCORE
# ----------------------------------------------------------
def ajouter_score(points):
    global score, meilleur_score
    score += points
    if score > meilleur_score:
        meilleur_score = score
    label_score.configure(text=f"Score\n{score}")
    label_best.configure(text=f"Meilleur\n{meilleur_score}")

# ----------------------------------------------------------
# REJOUER
# ----------------------------------------------------------
def rejouer():
    global label_fin_ref, score
    for row in range(4):
        for col in range(4):
            numbers[row][col] = 0
    spawn_tile()
    spawn_tile()
    if label_fin_ref is not None:
        label_fin_ref.destroy()
        label_fin_ref = None
    score = 0
    label_score.configure(text=f"Score\n{score}")
    win.bind('<Key>', press)
    display_grid()

# ----------------------------------------------------------
# MOUVEMENTS
# ----------------------------------------------------------
def left():
    total_points = 0
    for li in range(4):
        a, b, c, d, pts = pack(
            numbers[li][0], numbers[li][1],
            numbers[li][2], numbers[li][3]
        )
        numbers[li][0], numbers[li][1] = a, b
        numbers[li][2], numbers[li][3] = c, d
        total_points += pts
    ajouter_score(total_points)
    spawn_tile()
    display_grid()
    if check_victoire():
        afficher_message("🎉 Tu as gagné ! Continue !", game_over=False)
    elif check_defaite():
        afficher_message("💀 Game Over !", game_over=True)

def right():
    total_points = 0
    for li in range(4):
        a, b, c, d, pts = pack(
            numbers[li][3], numbers[li][2],
            numbers[li][1], numbers[li][0]
        )
        numbers[li][3], numbers[li][2] = a, b
        numbers[li][1], numbers[li][0] = c, d
        total_points += pts
    ajouter_score(total_points)
    spawn_tile()
    display_grid()
    if check_victoire():
        afficher_message("🎉 Tu as gagné ! Continue !", game_over=False)
    elif check_defaite():
        afficher_message("💀 Game Over !", game_over=True)

def up():
    total_points = 0
    for col in range(4):
        a, b, c, d, pts = pack(
            numbers[0][col], numbers[1][col],
            numbers[2][col], numbers[3][col]
        )
        numbers[0][col], numbers[1][col] = a, b
        numbers[2][col], numbers[3][col] = c, d
        total_points += pts
    ajouter_score(total_points)
    spawn_tile()
    display_grid()
    if check_victoire():
        afficher_message("🎉 Tu as gagné ! Continue !", game_over=False)
    elif check_defaite():
        afficher_message("💀 Game Over !", game_over=True)

def down():
    total_points = 0
    for col in range(4):
        a, b, c, d, pts = pack(
            numbers[3][col], numbers[2][col],
            numbers[1][col], numbers[0][col]
        )
        numbers[3][col], numbers[2][col] = a, b
        numbers[1][col], numbers[0][col] = c, d
        total_points += pts
    ajouter_score(total_points)
    spawn_tile()
    display_grid()
    if check_victoire():
        afficher_message(" Tu as gagné ! Continue !", game_over=False)
    elif check_defaite():
        afficher_message(" Game Over !", game_over=True)

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

# ---- Fenetre principale ----
win = tk.Tk()
win.title("2048")
win.configure(background="#EBF5FF")

# ---- Barre titre + scores ----
barre_score = tk.Frame(win, bg="#EBF5FF")
barre_score.pack(padx=10, pady=(10, 0), fill="x")

label_titre = tk.Label(
    barre_score, text="2048",
    font=("Arial", 32, "bold"),
    bg="#EBF5FF", fg="#707DA4"
)
label_titre.pack(side="left", padx=10)

cadre_scores = tk.Frame(barre_score, bg="#EBF5FF")
cadre_scores.pack(side="right", padx=10)

label_score = tk.Label(
    cadre_scores, text=f"Score\n{score}",
    font=("Arial", 13, "bold"),
    bg="#707DA4", fg="white",
    width=8, pady=6
)
label_score.pack(side="left", padx=4)

label_best = tk.Label(
    cadre_scores, text=f"Meilleur\n{meilleur_score}",
    font=("Arial", 13, "bold"),
    bg="#F7C59F", fg="white",
    width=8, pady=6
)
label_best.pack(side="left", padx=4)

# ---- Grille ----
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

# ---- Bouton Rejouer ----
btn_rejouer = tk.Button(
    win, text=" Rejouer", font=("Arial", 14, "bold"),
    bg="#707DA4", fg="white", relief="flat",
    padx=10, pady=5, cursor="hand2",
    command=rejouer
)
btn_rejouer.pack(pady=8)

win.bind('<Key>', press)

display_grid()
win.mainloop()