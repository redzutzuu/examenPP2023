import tkinter as tk

canvas = None  # Variabilă globală pentru canvas

def on_mouse_down(event):
    x = event.x
    y = event.y
    print(f"Apăsat la coordonatele ({x}, {y})")

def on_mouse_drag(event):
    x = event.x
    y = event.y
    print(f"Tras de la coordonatele anterioare la ({x}, {y})")

def on_mouse_up(event):
    x = event.x
    y = event.y
    print(f"Releasat la coordonatele ({x}, {y})")

def create_triangle():
    canvas.create_line(50, 50, 150, 150, fill="black")
    canvas.create_line(150, 150, 250, 50, fill="black")
    canvas.create_line(250, 50, 50, 50, fill="black")

def main():
    global canvas  # Referință la variabila globală

    root = tk.Tk()
    root.title("Aplicație de desen")

    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    canvas.bind("<Button-1>", lambda event: on_mouse_down(event))
    canvas.bind("<B1-Motion>", lambda event: on_mouse_drag(event))
    canvas.bind("<ButtonRelease-1>", lambda event: on_mouse_up(event))

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Fișier", menu=file_menu)
    file_menu.add_command(label="Ieșire", command=root.quit)

    draw_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Desenează", menu=draw_menu)
    draw_menu.add_command(label="Triunghi", command=create_triangle)

    root.mainloop()

if __name__ == "__main__":
    main()
