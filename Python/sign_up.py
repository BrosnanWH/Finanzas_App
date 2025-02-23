import pyodbc
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

def sign_up(ventana_login):

    def register_user():
        new_usuario = new_entry_usuario.get()
        new_contrasena = new_entry_contrasena.get()

        conn_str = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=DESKTOP-DK0D7AB;DATABASE=Northwind;"
            "UID=JOSHUA\\rugam;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

        try:
            conexion = pyodbc.connect(conn_str)
            cursor = conexion.cursor()

            if new_usuario == "" or new_contrasena == "":
                messagebox.showwarning("¡ERROR!", "Es obligatorio llenar todos los campos.")
            else:
                
                cursor.execute("INSERT INTO dbo.Usuario_login (usuario, contrasena) VALUES (?, ?)", (new_usuario, new_contrasena))
                conexion.commit()

                
                progressbar()

                
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                ventana_sign_up.destroy()  
                ventana_login.deiconify()  

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

    # Configuración de la ventana de registro
    ventana_sign_up = tk.Tk()
    ventana_sign_up.title("GastoSmart - Regístrate")
    ventana_sign_up.geometry("500x520")
    ventana_sign_up.config(bg='#D97762')

    # Centralización de la ventana
    pantalla_ancho = ventana_sign_up.winfo_screenwidth()
    pantalla_alto = ventana_sign_up.winfo_screenheight()
    ventana_ancho = 500
    ventana_alto = 520
    posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
    posicion_y = int((pantalla_alto - ventana_alto) / 2)
    ventana_sign_up.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

    # Frame de registro
    frame_sign_up = tk.Frame(ventana_sign_up, bg='#F28D9F', bd=5, relief='raised')
    frame_sign_up.place(relx=0.5, rely=0.5, anchor='center', width=350, height=500)

    # Título del formulario
    label_titulo = tk.Label(frame_sign_up, text="Crear Cuenta", bg='#D93B58', fg="white", font=("Playfair Display", 20, "bold"))
    label_titulo.pack(pady=20)

    # Campo de entrada para el nombre de usuario
    new_entry_usuario = tk.Entry(frame_sign_up, width=25, bg="#e0dede", border=0, font=("Jost", 12))
    new_entry_usuario.pack(pady=10)
    new_entry_usuario.insert(0, "")

    # Campo de entrada para la contraseña
    new_entry_contrasena = tk.Entry(frame_sign_up, width=25, bg="#e0dede", border=0, font=("Jost", 12), show="*")
    new_entry_contrasena.pack(pady=10)

    # Funciones para el hover en botones
    def on_enter(e):
        e.widget['background'] = '#6d44b8'

    def on_leave(e):
        e.widget['background'] = '#573b8a'

    # Botón de registro
    boton_registro = tk.Button(frame_sign_up, text="Registrarse", command=register_user, width=20, height=2, bg="#D93B58", fg="white", font=("Jost", 12, "bold"), bd=0)
    boton_registro.pack(pady=20)

    
    boton_registro.bind("<Enter>", on_enter)
    boton_registro.bind("<Leave>", on_leave)

    # Iniciar la ventana
    ventana_sign_up.mainloop()