import pyodbc
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

# Función para verificar el inicio de sesión
def sign_up():
    new_usuario = new_entry_usuario.get()
    new_contrasena = new_entry_contrasena.get()

    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-DK0D7AB;DATABASE=Northwind;"
        "UID=JOSHUA\\rugam;"  # Cambia si tu usuario o servidor es diferente
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"  # Desactiva la verificación del certificado SSL
    )

    try:
        conexion = pyodbc.connect(conn_str)
        cursor = conexion.cursor()

        if new_usuario == "" or new_contrasena == "":
            messagebox.showwarning("!!!ERROR!!!", "Es obligatorio llenar todos los campos.")
        else:
            # Consulta para insertar un nuevo usuario
            cursor.execute("INSERT INTO dbo.Usuario_login (usuario, contrasena) VALUES (?, ?)", (new_usuario, new_contrasena))
            conexion.commit()  # Asegúrate de hacer commit para guardar los cambios
            progressbar()
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            ventana_sign_up.destroy()
    
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

    finally:
        if 'conexion' in locals():
            conexion.close()

def progressbar():
    barra = ttk.Progressbar(ventana_sign_up, orient='horizontal', length=280, mode='determinate', maximum=100, style="TProgressbar")
    barra.place(x=100, y=340)
    for i in range(101):
        barra["value"] += 1
        ventana_sign_up.update()
        time.sleep(0.02)
    barra["value"] = 0
    barra.destroy()

# Configuración de la ventana registro
ventana_sign_up = tk.Tk()
ventana_sign_up.title("GastoSmart - Registrate")
ventana_sign_up.geometry("500x600")
ventana_sign_up.config(bg='#0f0c29')

# Frame registro
frame_sign_Up = tk.Frame(ventana_sign_up, bg='#573b8a', bd=5, relief='raised')
frame_sign_Up.place(relx=0.5, rely=0.5, anchor='center', width=350, height=550)

# Campo de entrada para registrarse
new_entry_usuario = tk.Entry(frame_sign_Up, width=25, bg="#808080", border=0, font=("Jost", 12))
new_entry_usuario.pack(pady=10)
new_entry_usuario.insert(0, "")

# Campo de entrada para nueva contrasena
new_entry_contrasena = tk.Entry(frame_sign_Up, width=25, bg="#808080", border=0, font=("Jost", 12))
new_entry_contrasena.pack(pady=10)
new_entry_contrasena.insert(0, "")

# Botón de registrar nuevo usuario
boton_login = tk.Button(frame_sign_Up, text="Registrarse", command=sign_up, width=20, height=2, bg="#573b8a", fg="white", font=("Jost", 12, "bold"), bd=0)
boton_login.pack(pady=20)

ventana_sign_up.mainloop()


