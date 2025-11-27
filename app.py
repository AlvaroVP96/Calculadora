import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from calc import suma, resta, multiplicacion, division
from datetime import datetime

def agregar_log(mensaje):
    """Agrega un mensaje al log con timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f"[{timestamp}] {mensaje}\n")
    log_text.see(tk.END)
    log_text.config(state=tk.DISABLED)

def guardar_log():
    """Guarda el contenido del log en un archivo"""
    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(log_text.get(1.0, tk.END))
            messagebox.showinfo("Éxito", "Log guardado correctamente")
            agregar_log(f"Log guardado en: {archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el log: {str(e)}")

def limpiar_log():
    """Limpia el contenido del log"""
    log_text.config(state=tk.NORMAL)
    log_text.delete(1.0, tk.END)
    log_text.config(state=tk.DISABLED)
    agregar_log("Log iniciado")

def on_sum():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = suma(a, b)
        label_result.config(text=f"Resultado: {resultado}")
        agregar_log(f"Suma: {a} + {b} = {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", "Introduce dos números")
        agregar_log(f"Error en suma: {a} + {b} - {str(e)}")

def on_res():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = resta(a, b)
        label_result.config(text=f"Resultado: {resultado}")
        agregar_log(f"Resta: {a} - {b} = {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", "Introduce dos números")
        agregar_log(f"Error en resta: {a} - {b} - {str(e)}")

def on_mult():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = multiplicacion(a, b)
        label_result.config(text=f"Resultado: {resultado}")
        agregar_log(f"Multiplicación: {a} * {b} = {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", "Introduce dos números")
        agregar_log(f"Error en multiplicación: {a} * {b} - {str(e)}")

def on_div():
    a = entry_a.get()
    b = entry_b.get()
    try:
        resultado = division(a, b)
        label_result.config(text=f"Resultado: {resultado}")
        agregar_log(f"División: {a} / {b} = {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        agregar_log(f"Error en división: {a} / {b} - {str(e)}")

root = tk.Tk()
root.title("Calculadora")
root.geometry("600x500")

# Frame principal para la calculadora
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

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

# Frame para el log
log_frame = tk.Frame(root, padx=10, pady=10)
log_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(log_frame, text="Registro de Operaciones", font=("Arial", 10, "bold")).pack()

# Área de texto con scroll para el log
log_text = scrolledtext.ScrolledText(log_frame, width=40, height=20, state=tk.DISABLED, wrap=tk.WORD)
log_text.pack(pady=5, fill=tk.BOTH, expand=True)

# Botones para el log
log_buttons_frame = tk.Frame(log_frame)
log_buttons_frame.pack()

btn_guardar_log = tk.Button(log_buttons_frame, text="Guardar Log", command=guardar_log)
btn_guardar_log.pack(side=tk.LEFT, padx=5)

btn_limpiar_log = tk.Button(log_buttons_frame, text="Limpiar Log", command=limpiar_log)
btn_limpiar_log.pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    agregar_log("Calculadora iniciada")
    root.mainloop()