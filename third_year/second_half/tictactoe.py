import tkinter
from tkinter import messagebox # import pro tkinter.messagebox

#definice tahu
global tah
tah = 'X'

# Test barev v terminálu
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

#intnuty input pro velikost pole a vyherniho poctu znaku 
velikost = int(input(f"{BLUE}{BOLD}[INPUT]{RESET}{CYAN} Zadej velikost pole (3-5 pro klasické tic tac toe): {RESET}"))

# kontrola pole mezi 3-5
if velikost < 3:
    print(f"{GREEN}{BOLD}[SETUP]{RESET}{CYAN} Velikost musí být alespoň 3. Nastavuji na 3.{RESET}")
    velikost = 3
elif velikost > 5:
    print(f"{YELLOW}{BOLD}[SETUP]{RESET}{CYAN} Velikost musí být nejvýše 5. Nastavuji na 5.{RESET}")
    velikost = 5

#hlavni funkce pro spousteni a definici pole 
def main():
    window = tkinter.Tk()
    window.title("Tic Tac Toe")
    # pokud vetsi velikost vetsi pole
    if velikost >= 5:
        window.geometry("700x690")
    else:
        window.geometry("400x400")
    buttons(window)
    window.mainloop()

# generace tlacitek podle promene velikost a jejich umisteni do gridu
def buttons(window):
    buttons_list = []
    for i in range(velikost):
        row = []
        for j in range(velikost): # for loop pro generovani tlacitek podle velikosti (automaticke)
            button = tkinter.Button(window, text=" ", width=10, height=5, font=("Arial", 16, "bold"),
                                   bg="#333333", fg="#ffffff", activebackground="#444444") # config vzhledu
            button.grid(row=i, column=j) # umisteni do gridu
            button.config(command=lambda b=button, btns=buttons_list: on_button_click(b, btns)) # config tlacitek
            row.append(button) # pridani tlacitek do radku
        buttons_list.append(row) # pridani radku do seznamu tlacitek
    return buttons_list

# hlavni logika po kliknuti na tlacitko znema textu z " " na "X" nebo "O" podle tahu
def on_button_click(button, buttons_list):
    global tah
    if button['text'] == " ": # kontrola jestli je tlacitko prazdne
        button['text'] = tah # nastaveni textu na "X" nebo "O"
        button.config(fg="#FF6B6B" if tah == 'X' else "#4ECDC4", font=("Arial", 16, "bold")) # config vzhledu
        if check_winner(buttons_list) == tah:
            print(f"{RED}{BOLD}Vyhrál {tah}!{RESET}") # vypis v terminalu
            tkinter.messagebox.showinfo("Game Over", f"Player {tah} wins!") # vypis v okne
            for row in buttons_list:
                for btn in row:
                    btn['text'] = " "
            return
        tah = 'O' if tah == 'X' else 'X' # znema tahu

# kontrala pro vyhru
def check_winner(buttons_list):
    for i in range(velikost):
        if all(buttons_list[i][j]['text'] == tah for j in range(velikost)):
            return tah
    for j in range(velikost):
        if all(buttons_list[i][j]['text'] == tah for i in range(velikost)):
            return tah
    if all(buttons_list[i][i]['text'] == tah for i in range(velikost)):
        return tah
    if all(buttons_list[i][velikost - 1 - i]['text'] == tah for i in range(velikost)):
        return tah
    return None

# "starter"
if __name__ == "__main__":
    main()