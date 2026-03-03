# 2048 - UI de base (fusion de tes deux versions)
# Auteur : Eyuel
# Date : mars 2026

import tkinter as tk

numbers = [
    [2048, 1024, 512, 256],
    [128, 64, 32, 16],
    [8, 4, 2, 4096],
    [8192, 0, 0, 0]
]

tile_colors = {
    0: "#E1D5E7", 2: "#94A2C3", 4: "#9CA5BF", 8: "#707DA4",
    16: "#4E5161", 32: "#D0D4E4", 64: "#E1E5EE", 128: "#C7CCDB",
    256: "#767B91", 512: "#62667A", 1024: "#F7C59F", 2048: "#E6E6E6",
    4096: "#86797A", 8192: "#741C8D",
}

GRILLE = 4
Tuiles_GAP = 6
score_value = 67

# ----------------------------------------------------------
# pack 4 des tuiles
# ----------------------------------------------------------
def pack(a,b,c,d):
    if a == 0:
        a,b,c,d = b,c,d,0
    if b ==0:
        b,c,d = c,d,0
    if c== 0:
        c,d,d=d,0,0
    if a==b:
        a,b,c,d= 2*a,c,d,0
    if b==c:
        b,c,d = 2*b,d,0
    if c==d :
        c,d= 2*c,0
    return(a,b,c,d)

def display_grid():
    global game
# ----------------------------------------------------------
# les moves des tuiles
# ----------------------------------------------------------
def left():
    global game
    for li in range(4):
        numbers[li][0], numbers[li][1], numbers[li][2], numbers[li][3] = pack(*numbers[li])
    display()
def right():
    for li in range(4):
        global game
        a, b, c, d = numbers[li][3], numbers[li][2], numbers[li][1], numbers[li][0]
        numbers[li][3], numbers[li][2], numbers[li][1], numbers[li][0] = pack(a, b, c, d)
    display()
def up():
    for col in range(4):
        global game
        a, b, c, d = numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col]

    display()

def down():
    for col in range(4):
        global game
        a, b, c, d = numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col]
    display()



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

win.bind('<Key>', )
display_grid()
win.mainloop()