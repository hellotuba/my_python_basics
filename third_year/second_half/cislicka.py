import tkinter as tk

class Cislicka:
    def __init__(self, master):
        self.root = master
        self.root.title("CISLICKA - Slots")
        frame = tk.Frame(self.root, bg="gray")
        frame.pack(pady=10)

        self.numbers = [1, 2, 3, 4, 5, 6, 7]
        self.slots = []
        for i in range(3):
            lbl = tk.Label(frame, text='1', font=("Helvetica", 48), fg="red", bg="black", width=2)
            lbl.pack(side=tk.LEFT, padx=5)
            self.slots.append(lbl)
        
        self.score = 0
        self.score_label = tk.Label(master, text=f"Score: {self.score}", fg="white", bg="gray")
        self.score_label.pack()

        self.msg_label = tk.Label(master, text="Press SPACE to start/stop", fg="white", bg="gray")
        self.msg_label.pack(pady=5)

        self.running = False
        self.spin_flags = [False, False, False]
        self.next_stop = 0
        self.root.bind("<space>", self.toggle)

    def toggle(self, event):
        if not self.running:
            # toci se vsechno
            self.running = True
            self.spin_flags = [True, True, True]
            self.next_stop = 0
            for i in range(3):
                self._spin(i)
            self.msg_label.config(text="Spinning... press SPACE to stop")
        else:
            # jeden stop space
            i = self.next_stop
            while i < 3:
                if self.spin_flags[i]:
                    self._stop_slot(i)
                    self.next_stop = i + 1
                    break
                i += 1
            if all(not flag for flag in self.spin_flags):
                self.running = False
    
    def _spin(self, index):
        if self.spin_flags[index]:
            cur = int(self.slots[index].cget('text'))
            next_idx = (self.numbers.index(cur) + 1) % len(self.numbers)
            self.slots[index].config(text=str(self.numbers[next_idx]))
            #rycheljsi spin uprostred
            delay = 100 if index == 1 else 200
            self.root.after(delay, lambda: self._spin(index))

    def _stop_slot(self, index):
        self.spin_flags[index] = False
        # finalni dispay, nic vic nedelat
        if not any(self.spin_flags):
            # vsechny zastaveny, vyhodnotit
            self.evaluate()
    
    def evaluate(self):
        vals = [int(lbl.cget('text')) for lbl in self.slots]
        counts = {v: vals.count(v) for v in set(vals)}
        points = 0
        # 100 bodu za 3 stejna, 20 bodu za 2 stejna, jinak nic
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