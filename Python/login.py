import pyodbc
import tkinter as tk
from tkinter import messagebox
from main import iniciar_ventana_principal

def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    
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

        # Consulta para verificar las credenciales
        cursor.execute("SELECT * FROM dbo.Usuario_login WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
        if usuario == "" or contrasena == "":
                messagebox.showerror("Error", "Por Favor ingrese un nombre de usuario valido.")

        elif cursor.fetchone():
                ventana.destroy()  # Cerrar ventana de login
                iniciar_ventana_principal()  
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

    finally:
        if 'conexion' in locals():
            conexion.close()

def crear_new_account():
    from sign_up import sign_up
    sign_up(ventana)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("GastoSmart - Inicio de Sesión")
ventana.config(bg='#D97762') 

# Centralizando ventana
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
ventana_ancho = 500
ventana_alto = 520
posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
posicion_y = int((pantalla_alto - ventana_alto) / 2)
ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

# Función para manejar el hover sobre los botones
def on_enter(e):
    e.widget['background'] = '#6D44B8'  # Color al pasar el mouse

def on_leave(e):
    e.widget['background'] = '#573B8A'  # Color al salir el mouse

# Frame principal (formulario de login)
frame = tk.Frame(ventana, bg='#F28D9F', bd=5, relief='raised', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center', width=390, height=400)

# Etiqueta de título
label_titulo = tk.Label(frame, text="GastoSmart Login", bg='#D93B58', fg="white", font=("Playfair Display", 22, "bold"))
label_titulo.pack(pady=10)

# Campo de entrada para el usuario
entry_usuario = tk.Entry(frame, width=25, bg="#e0dede", border=0, font=("Jost", 12), relief='flat', highlightthickness=1, highlightbackground="#0378A6")
entry_usuario.pack(pady=10)
entry_usuario.insert(0, "")

# Campo de entrada para la contraseña
entry_contrasena = tk.Entry(frame, width=25, bg="#e0dede", border=0, show="*", font=("Jost", 12), relief='flat', highlightthickness=1, highlightbackground="#0378A6")
entry_contrasena.pack(pady=10)
entry_contrasena.insert(0, "")

# Botón de "Crear Cuenta"
boton_crear_cuenta = tk.Button(frame, text="Crear Cuenta", command=crear_new_account, width=20, height=2, bg="#D93B58", fg="white", font=("Playfair Display", 12, "bold"), bd=0)
boton_crear_cuenta.pack(pady=20)

# Botón de inicio de sesión
boton_login = tk.Button(frame, text="Iniciar Sesión", command=verificar_login, width=20, height=2, bg="#D93B58", fg="white", font=("Playfair Display", 12, "bold"), bd=0)
boton_login.pack(pady=10)

# Efecto hover en el botón
boton_login.bind("<Enter>", on_enter)
boton_login.bind("<Leave>", on_leave)

# Iniciar la ventana principal
ventana.mainloop()


