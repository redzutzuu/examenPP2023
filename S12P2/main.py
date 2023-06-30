import tkinter as tk
from tkinter import ttk

def save_employee():
    company = company_entry.get()
    department = department_entry.get()
    name = name_entry.get()
    birth_date = f"{birth_month.get()} {birth_day.get()}, {birth_year.get()}"
    position = position_entry.get()
    salary = salary_entry.get()

    # Aici poți să folosești datele pentru a salva informațiile angajatului într-o bază de date sau în altă formă de stocare

    # Exemplu de afișare a datelor angajatului în consolă
    print("Datele angajatului:")
    print(f"Companie: {company}")
    print(f"Departament: {department}")
    print(f"Nume: {name}")
    print(f"Data de naștere: {birth_date}")
    print(f"Funcție: {position}")
    print(f"Salariu: {salary}")

def clear_fields():
    company_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    birth_day.set("")
    birth_month.set("")
    birth_year.set("")
    position_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)

def main():
    # Crearea ferestrei principale
    window = tk.Tk()
    window.title("Introducere date angajat")
    window.geometry("400x300")

    # Frame pentru secțiunea de introducere date
    data_frame = ttk.Frame(window)
    data_frame.pack(pady=20)

    # Etichete
    company_label = ttk.Label(data_frame, text="Companie:")
    company_label.grid(row=0, column=0, sticky=tk.W)
    department_label = ttk.Label(data_frame, text="Departament:")
    department_label.grid(row=1, column=0, sticky=tk.W)
    name_label = ttk.Label(data_frame, text="Nume:")
    name_label.grid(row=2, column=0, sticky=tk.W)
    birth_label = ttk.Label(data_frame, text="Data de naștere:")
    birth_label.grid(row=3, column=0, sticky=tk.W)
    position_label = ttk.Label(data_frame, text="Funcție:")
    position_label.grid(row=4, column=0, sticky=tk.W)
    salary_label = ttk.Label(data_frame, text="Salariu:")
    salary_label.grid(row=5, column=0, sticky=tk.W)

    # Câmpuri de introducere
    company_entry = ttk.Entry(data_frame)
    company_entry.grid(row=0, column=1, padx=10)
    department_entry = ttk.Entry(data_frame)
    department_entry.grid(row=1, column=1, padx=10)
    name_entry = ttk.Entry(data_frame)
    name_entry.grid(row=2, column=1, padx=10)

    # Combobox pentru data de naștere
    birth_day = ttk.Combobox(data_frame, values=list(range(1, 32)))
    birth_day.grid(row=3, column=1, padx=10)
    birth_month = ttk.Combobox(data_frame, values=["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"])
    birth_month.grid(row=3, column=2, padx=10)
    birth_year = ttk.Entry(data_frame)
    birth_year.grid(row=3, column=3, padx=10)

    position_entry = ttk.Entry(data_frame)
    position_entry.grid(row=4, column=1, padx=10)
    salary_entry = ttk.Entry(data_frame)
    salary_entry.grid(row=5, column=1, padx=10)

    # Frame pentru secțiunea de acțiuni
    button_frame = ttk.Frame(window)
    button_frame.pack(pady=10)

    # Buton pentru salvare
    save_button = ttk.Button(button_frame, text="Salvează", command=save_employee)
    save_button.grid(row=0, column=0, padx=5)

    # Buton pentru resetarea câmpurilor
    clear_button = ttk.Button(button_frame, text="Resetare", command=clear_fields)
    clear_button.grid(row=0, column=1, padx=5)

    # Meniu
    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    window.config(menu=menu_bar)

    # Rularea aplicației
    window.mainloop()

if __name__ == "__main__":
    main()
