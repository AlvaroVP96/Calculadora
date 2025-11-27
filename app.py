import tkinter as tk
from tkinter import messagebox
from calc import suma, resta, multiplicacion, division

def on_sum():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = suma(a, b)
        label_result.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce dos números")

def on_res():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = resta(a, b)
        label_result.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce dos números")
def on_mult():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = multiplicacion(a, b)
        label_result.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce dos números")

def on_div():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = division(a, b)
        label_result.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce dos números")

root = tk.Tk()
root.title("Suma")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="A:").grid(row=0, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)

tk.Label(frame, text="B:").grid(row=1, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1)

btn = tk.Button(frame, text="Sumar", command=on_sum)
btn.grid(row=2, column=0, columnspan=2, pady=5)

btn = tk.Button(frame, text="Restar", command=on_res)
btn.grid(row=3, column=0, columnspan=2, pady=5)

btn = tk.Button(frame, text="Multiplicar", command=on_mult)
btn.grid(row=4, column=0, columnspan=2, pady=5)

btn = tk.Button(frame, text="Dividir", command=on_div)
btn.grid(row=5, column=0, columnspan=2, pady=5)

label_result = tk.Label(frame, text="Resultado: ")
label_result.grid(row=6, column=0, columnspan=2)

if __name__ == "__main__":
    root.mainloop()