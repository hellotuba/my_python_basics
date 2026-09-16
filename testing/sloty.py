import sys
import random
 
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Tkinter není nainstalovaný.")
    sys.exit()
 
 
class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Lucky Slot")
        self.root.geometry("800x600")
        self.root.configure(bg="#1b1b2f")
        self.root.resizable(False, False)
 
        self.money = 1000
        self.spinning = False
 
        self.symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]
 
        self.payouts = {
            "🍒": 3,
            "🍋": 4,
            "🔔": 6,
            "⭐": 10,
            "💎": 20
        }
 
        title = tk.Label(
            root,
            text="🎰 LUCKY SLOT 🎰",
            font=("Arial", 30, "bold"),
            bg="#1b1b2f",
            fg="gold"
        )
        title.pack(pady=20)
 
        self.money_label = tk.Label(
            root,
            text=f"💰 Peníze: {self.money}$",
            font=("Arial", 18, "bold"),
            bg="#1b1b2f",
            fg="#00ff88"
        )
        self.money_label.pack()
 
        machine_frame = tk.Frame(
            root,
            bg="#8b0000",
            bd=8,
            relief="ridge"
        )
        machine_frame.pack(pady=30)
 
        self.reels = []
 
        for i in range(3):
            reel = tk.Label(
                machine_frame,
                text="❔",
                font=("Segoe UI Emoji", 64),
                width=2,
                bg="white",
                relief="sunken",
                bd=5
            )
            reel.grid(row=0, column=i, padx=10, pady=10)
            self.reels.append(reel)
 
        bet_frame = tk.Frame(root, bg="#1b1b2f")
        bet_frame.pack()
 
        tk.Label(
            bet_frame,
            text="Sázka:",
            font=("Arial", 14, "bold"),
            bg="#1b1b2f",
            fg="white"
        ).pack(side="left", padx=5)
 
        self.bet_entry = tk.Entry(
            bet_frame,
            font=("Arial", 14),
            justify="center",
            width=10
        )
        self.bet_entry.insert(0, "50")
        self.bet_entry.pack(side="left")
 
        self.spin_btn = tk.Button(
            root,
            text="🎲 ROZTOČIT",
            font=("Arial", 18, "bold"),
            bg="gold",
            width=15,
            command=self.spin
        )
        self.spin_btn.pack(pady=20)
 
        self.result_label = tk.Label(
            root,
            text="Vítej v kasinu!",
            font=("Arial", 16, "bold"),
            bg="#1b1b2f",
            fg="white"
        )
        self.result_label.pack()
 
        # Mezerník roztočí automat
        self.root.bind_all("<space>", lambda event: self.spin())
 
    def update_money(self):
        self.money_label.config(text=f"💰 Peníze: {self.money}$")
 
    def spin(self):
        if self.spinning:
            return
 
        try:
            bet = int(self.bet_entry.get())
        except ValueError:
            messagebox.showerror("Chyba", "Zadej číslo.")
            return
 
        if bet <= 0:
            messagebox.showerror("Chyba", "Sázka musí být větší než 0.")
            return
 
        if bet > self.money:
            messagebox.showerror("Chyba", "Nemáš dost peněz.")
            return
 
        self.money -= bet
        self.update_money()
 
        self.spinning = True
        self.spin_btn.config(state="disabled")
 
        self.animate(0, bet)
 
    def animate(self, step, bet):
        if step < 25:
            for reel in self.reels:
                reel.config(text=random.choice(self.symbols))
 
            self.root.after(
                70,
                lambda: self.animate(step + 1, bet)
            )
            return
 
        result = [
            random.choice(self.symbols),
            random.choice(self.symbols),
            random.choice(self.symbols)
        ]
 
        for i in range(3):
            self.reels[i].config(text=result[i])
 
        self.check_win(result, bet)
 
        self.spinning = False
        self.spin_btn.config(state="normal")
 
    def check_win(self, result, bet):
        if result[0] == result[1] == result[2]:
 
            multiplier = self.payouts[result[0]]
            win = bet * multiplier
 
            self.money += win
 
            self.result_label.config(
                text=f"🎉 JACKPOT! Vyhrál jsi {win}$",
                fg="gold"
            )
 
        elif len(set(result)) == 2:
 
            win = bet * 2
 
            self.money += win
 
            self.result_label.config(
                text=f"✨ Dva stejné symboly! +{win}$",
                fg="#00ff88"
            )
 
        else:
            self.result_label.config(
                text="❌ Bez výhry",
                fg="red"
            )
 
        self.update_money()
 
        if self.money <= 0:
            self.spin_btn.config(state="disabled")
 
            messagebox.showinfo(
                "Konec hry",
                "Došly ti fake peníze!"
            )
 
 
def main():
    root = tk.Tk()
    SlotMachine(root)
    root.mainloop()
 
 
if __name__ == "__main__":
    main()