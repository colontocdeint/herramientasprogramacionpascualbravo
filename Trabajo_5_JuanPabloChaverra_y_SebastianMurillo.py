#sebastian Murillo Gonzales 
#juan Pablo Chaverra Hoyos
import tkinter as tk
from tkinter import messagebox

# FUNCIONES DE CADA SUBMENU
def abrir_menu1():
    ventana1 = tk.Toplevel()
    ventana1.title("Boton Interactivo")
    ventana1.geometry("300x200")

    tk.Label(ventana1, text="Has abierto el Menu 1", font=("Arial", 12)).pack(pady=10)

    def accion_boton():
        messagebox.showinfo("Accion", "Boton del Menu 1 presionado")

    tk.Button(ventana1, text="Presionar", command=accion_boton, bg="#4CAF50", fg="white").pack(pady=5)

    tk.Button(ventana1, text="Regresar", command=ventana1.destroy, bg="#f44336", fg="white").pack(pady=10)


def abrir_menu2():
    ventana2 = tk.Toplevel()
    ventana2.title("Formulario")
    ventana2.geometry("300x250")

    tk.Label(ventana2, text="Formulario de ejemplo", font=("Arial", 12)).pack(pady=10)

    tk.Label(ventana2, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana2)
    entrada_nombre.pack(pady=5)

    def enviar_formulario():
        nombre = entrada_nombre.get()
        if nombre.strip() == "":
            messagebox.showwarning("Advertencia", "Por favor ingresa un nombre.")
        else:
            messagebox.showinfo("Enviado", f"Hola {nombre}, formulario recibido correctamente.")

    tk.Button(ventana2, text="Enviar", command=enviar_formulario, bg="#2196F3", fg="white").pack(pady=5)
    tk.Button(ventana2, text="Regresar", command=ventana2.destroy, bg="#f44336", fg="white").pack(pady=10)


def abrir_menu3():
    ventana3 = tk.Toplevel()
    ventana3.title("Cambio de Puntero")
    ventana3.geometry("300x200")

    tk.Label(ventana3, text="Pasa el mouse sobre el boton", font=("Arial", 12)).pack(pady=10)

    boton_cursor = tk.Button(ventana3, text="Pasa el mouse", bg="#FFC107", fg="black")
    boton_cursor.pack(pady=10)

    # Cambiar puntero 
    boton_cursor.bind("<Enter>", lambda e: ventana3.config(cursor="hand2"))
    boton_cursor.bind("<Leave>", lambda e: ventana3.config(cursor="arrow"))

    tk.Button(ventana3, text="Regresar", command=ventana3.destroy, bg="#f44336", fg="white").pack(pady=10)


# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Menu Principal GUI")
ventana.geometry("400x300")
ventana.config(bg="#E0E0E0")

tk.Label(ventana, text="MENU GUI", font=("Arial", 14, "bold"), bg="#E0E0E0").pack(pady=20)

# Marco para los botones principales
frame_botones = tk.Frame(ventana, bg="#8F6464")
frame_botones.pack(pady=20)

# Botones principales
tk.Button(frame_botones, text="Abrir Menu 1", command=abrir_menu1, bg="#4CAF50", fg="white", width=20).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_botones, text="Abrir Menu 2", command=abrir_menu2, bg="#2196F3", fg="white", width=20).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_botones, text="Abrir Menu 3", command=abrir_menu3, bg="#FFC107", fg="black", width=20).grid(row=1, column=0, columnspan=2, pady=10)

ventana.mainloop()
