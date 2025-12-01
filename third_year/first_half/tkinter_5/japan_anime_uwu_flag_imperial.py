import math
import tkinter as tk
from tkinter import filedialog

W, H = 1200, 800
BACKGROUND = "#ffffff"
RED = "#b30a2e"
RAYS = 16
sector_ratio = 0.88

def draw_flag_on_canvas(canvas, width, height):
    canvas.configure(background=BACKGROUND)
    canvas.delete("all")

    center_x = int(width * 0.40)
    center_y = height // 2
    sun_radius = int(height * 0.20)
    far_radius = max(width, height) * 2

    for i in range(RAYS):
        angle = (2 * math.pi * i) / RAYS
        sector = (2 * math.pi) / RAYS
        half = (sector * sector_ratio) / 2

        ax = center_x + math.cos(angle - half) * sun_radius
        ay = center_y + math.sin(angle - half) * sun_radius
        bx = center_x + math.cos(angle + half) * sun_radius
        by = center_y + math.sin(angle + half) * sun_radius
        cx = center_x + math.cos(angle + half) * far_radius
        cy = center_y + math.sin(angle + half) * far_radius
        dx = center_x + math.cos(angle - half) * far_radius
        dy = center_y + math.sin(angle - half) * far_radius

        poly = [ax, ay, bx, by, cx, cy, dx, dy]
        canvas.create_polygon(poly, fill=RED, outline="")

    bbox = (
        center_x - sun_radius,
        center_y - sun_radius,
        center_x + sun_radius,
        center_y + sun_radius,
    )
    canvas.create_oval(bbox, fill=RED, outline="")

class FlagApp(tk.Tk):
    def __init__(self, width=W, height=H):
        super().__init__()
        self.title("Rising Sun Flag - Tkinter")
        self.geometry(f"{width}x{height+40}")
        self.resizable(True, True)

        self.width = width
        self.height = height

        self.canvas = tk.Canvas(self, bg=BACKGROUND)
        self.canvas.pack(fill="both", expand=True)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", padx=4, pady=2)
        tk.Button(btn_frame, text="Save PS...", command=self.save_image).pack(side="right")
        tk.Button(btn_frame, text="Regenerate", command=self.redraw).pack(side="right")

        self._last_size = (0, 0)
        self.redraw()
        self.bind("<Configure>", self._on_configure)

    def redraw(self):
        w = max(100, self.canvas.winfo_width()) or self.width
        h = max(100, self.canvas.winfo_height()) or self.height
        draw_flag_on_canvas(self.canvas, w, h)
        self._last_size = (w, h)

    def _on_configure(self, event):
        w = max(100, self.canvas.winfo_width())
        h = max(100, self.canvas.winfo_height())
        if (w, h) != self._last_size:
            self.after(50, self.redraw)

if __name__ == "__main__":
    app = FlagApp()
    app.mainloop()
