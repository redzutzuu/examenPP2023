import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def calculate_sequence(N):
    seq = []
    suma = 0
    for i in range(N):
        val = N + (sum(range(N)) * i)
        if 20 < val < 50:
            seq.append(val)
            suma += val
    return seq, suma


def draw_graph(seq):
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(seq, 'b-o')
    return fig


def display_results(seq, suma):
    window = tk.Toplevel()
    window.title("Rezultate")

    sum_label = tk.Label(window, text=f"Suma: {suma}")
    sum_label.pack()

    seq_label = tk.Label(window, text=f"Valori: {seq}")
    seq_label.pack()


def main():
    N = 10
    seq, suma = calculate_sequence(N)

    fig = draw_graph(seq)

    root = tk.Tk()
    root.title("Grafic")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    results_button = tk.Button(root, text="Afiseaza rezultate", command=lambda: display_results(seq, suma))
    results_button.pack()

    tk.mainloop()


if __name__ == "__main__":
    main()
