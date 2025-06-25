import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("460x220")
        self.root.configure(bg="#282C34")
        self.root.resizable(False, False)

        # Create a label to display the time
        self.time_label = tk.Label(root, font=("Consolas", 48), bg="#282C34", fg="#61AFEF")
        self.time_label.pack(expand=True)

        # Create a label for the date
        self.date_label = tk.Label(root, font=("Consolas", 24), bg="#282C34", fg="#b8b8b8")
        self.date_label.pack(expand=True)

        # Update the clock every 1000 milliseconds (1 second)
        self.update_clock()

    def update_clock(self):
        # Get the current time
        current_time = strftime("%H:%M:%S")
        current_date = strftime("%A, %B %d, %Y")

        # Update the labels
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        # Call this method again after 1 second
        self.time_label.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()