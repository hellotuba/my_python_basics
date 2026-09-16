# v tkinteru zobrazuje číslo se pomoci text a meni se plynule v case a hra se spousti na stisk klavese mezernik a zastavuje postupne bezici rotovaci cisla 1-7 a po zastaveni program musi vyhodnotit a pricte body podle toho kolik stejnych a jaky stejnych cisel chytne 
import tkinter as tk
class Cislicka:
    def __init__(self, master):
        self.root = master
        self.root.title("CISLICKA - Slot Machine")
        frame = tk.Frame(self.root, background="gray")
        frame.pack(pady=10)

        self.numbers = [1, 2, 3, 4, 5, 6, 7]
        self.slots = []
        for i in range(3):
            lbl = tk.Label(frame, text='1', font=("Helvetica", 48), fg="red", background="black", width=2)
            lbl.grid(row=0, column=i, padx=10)
            self.slots.append(lbl)

        self.score = 0
        self.score_label = tk.Label(master, text=f"Skóre: {self.score}", fg="white", background="gray")
        self.score_label.pack()

        self.msg_label = tk.Label(master, text="Zmáčkni SPACE pro start/stop", fg="white", background="gray")
        self.msg_label.pack(pady=5)

        self.running = False
        self.spin_flags = [False, False, False]
        self.next_stop = 0
        self.root.bind("<space>", self.toggle)

    def toggle(self, event):
        if not self.running:
            # vsechno spustit
            self.running = True
            self.spin_flags[0] = True
            self.spin_flags[1] = True
            self.spin_flags[2] = True
            self.next_stop = 0
            self._spin(0)
            self._spin(1)
            self._spin(2)
            self.msg_label.config(text="Spinning... press SPACE to stop")
        else:
            # zastavit jedno slot po stisku SPACE
            i = self.next_stop
            while i < 3:
                if self.spin_flags[i]:
                    self._stop_slot(i)
                    self.next_stop = i + 1
                    break
                i = i + 1
            # reset pokud nic 
            if self.spin_flags[0] == False and self.spin_flags[1] == False and self.spin_flags[2] == False:
                self.running = False

    def _spin(self, index):
        if self.spin_flags[index]:
            # advance number
            cur = int(self.slots[index].cget('text'))
            next_idx = (self.numbers.index(cur) + 1) % len(self.numbers)
            self.slots[index].config(text=str(self.numbers[next_idx]))
            # rychlejsi stred
            delay = 80 if index == 1 else 100
            self.root.after(delay, lambda idx=index: self._spin(idx))

    def _stop_slot(self, index):
        self.spin_flags[index] = False
        # finalni zobrazeni, nic vic nedelat
        if not any(self.spin_flags):
            # all stopped, evaluate
            self.evaluate()

    def evaluate(self):
        vals = [int(lbl.cget('text')) for lbl in self.slots]
        counts = {v: vals.count(v) for v in set(vals)}
        points = 0
        # simple scoring: three of a kind =100, two of a kind =20
        if 3 in counts.values():
            points = 100
        elif 2 in counts.values():
            points = 20
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")
        if points > 0:
            self.msg_label.config(text=f"You win {points} points!")
        else:
            self.msg_label.config(text="No match. Press SPACE to play again")
if __name__ == "__main__":
    root = tk.Tk()
    app = Cislicka(root)
    root.mainloop()