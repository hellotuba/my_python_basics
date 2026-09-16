import tkinter as tk
import math

WIDTH = 800
HEIGHT = 500

root = tk.Tk()
root.title("baracek")
root.resizable(False, False)

c = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#87CEEB")
c.pack()

# --- Obloha ---
for i in range(60):
    ratio = i / 60
    r = int(135 + ratio * 20)
    g = int(206 + ratio * 30)
    b = int(235 - ratio * 20)
    color = f"#{r:02x}{g:02x}{b:02x}"
    c.create_rectangle(0, i * (HEIGHT // 2) // 60, WIDTH, (i + 1) * (HEIGHT // 2) // 60,
                       fill=color, outline="")

# --- travicka ---
for i in range(30):
    color = "green"
    y0 = HEIGHT // 2 + i * (HEIGHT // 2) // 30
    y1 = HEIGHT // 2 + (i + 1) * (HEIGHT // 2) // 30
    c.create_rectangle(0, y0, WIDTH, y1, fill=color, outline="")


# --- Slunce ---
c.create_oval(680, 50, 750, 120, fill="#FFD700", outline="#FFA500", width=3)
for angle in range(0, 360, 30):
    rad = math.radians(angle)
    x1 = 715 + 42 * math.cos(rad)
    y1 = 85 + 42 * math.sin(rad)
    x2 = 715 + 56 * math.cos(rad)
    y2 = 85 + 56 * math.sin(rad)
    c.create_line(x1, y1, x2, y2, fill="#FFA500", width=2)

hx, hy = 505, 470
hw, hh = 190, 158

# steny
c.create_rectangle(hx - hw//2, hy - hh, hx + hw//2, hy,
                   fill="#fffde7", outline="#888", width=2)

# strecha
c.create_polygon(
    hx - hw//2 - 8, hy - hh,
    hx + hw//2 + 8, hy - hh,
    hx, hy - hh - 38,
    fill="#c0392b", outline="#922b21", width=2
)

# dvere
c.create_rectangle(hx - 10, hy - 24, hx + 10, hy,
                   fill="#8B5E3C", outline="#5C3010", width=1)

# okno vlevo
c.create_rectangle(hx - 35, hy - 50, hx - 15, hy - 30,
                   fill="#aee4ff", outline="#555", width=1)
c.create_line(hx-25, hy-50, hx-25, hy-30, fill="#555", width=1)
c.create_line(hx-35, hy-40, hx-15, hy-40, fill="#555", width=1)

# okno vpravo
c.create_rectangle(hx + 15, hy - 50, hx + 35, hy - 30,
                   fill="#aee4ff", outline="#555", width=1)
c.create_line(hx+25, hy-50, hx+25, hy-30, fill="#555", width=1)
c.create_line(hx+15, hy-40, hx+35, hy-40, fill="#555", width=1)

# --- Ptaci ---
for bx, by in [(200, 130), (230, 115), (260, 125)]:
    c.create_arc(bx, by, bx+20, by+10, start=0, extent=180,
                 style="arc", outline="#333", width=2)
    c.create_arc(bx+18, by, bx+38, by+10, start=0, extent=180,
                 style="arc", outline="#333", width=2)

root.mainloop()