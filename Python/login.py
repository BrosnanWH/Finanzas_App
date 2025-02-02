import pyodbc
import tkinter as tk
from tkinter import messagebox
from main import iniciar_ventana_principal  # Importar la función correctamente

# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Cadena de conexión utilizando el formato de interpolación correcto
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=Joshua;DATABASE=Northwind;"
        "UID=JOSHUA\\rugam;"  # Cambia si tu usuario o servidor es diferente
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"  # Desactiva la verificación del certificado SSL
    )
    
    try:
        conexion = pyodbc.connect(conn_str)
        cursor = conexion.cursor()

        # Consulta para verificar las credenciales (ajusta según tu tabla Usuarios)
        cursor.execute("SELECT * FROM dbo.Usuario_login WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
        if cursor.fetchone():
            ventana.destroy()  # Cerrar ventana de login
            iniciar_ventana_principal()  # Llamar a la función para abrir la ventana principal

        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

    finally:
        if 'conexion' in locals():
            conexion.close()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("GastoSmart - Inicio de Sesión")
ventana.geometry("400x600")
ventana.config(bg='#0f0c29')

# Función para manejar el hover sobre los botones
def on_enter(e):
    e.widget['background'] = '#6d44b8'

def on_leave(e):
    e.widget['background'] = '#573b8a'

# Frame principal
frame = tk.Frame(ventana, bg='#573b8a', bd=5, relief='raised')
frame.place(relx=0.5, rely=0.5, anchor='center', width=350, height=500)

# Etiqueta de título
label_titulo = tk.Label(frame, text="Login", bg='#573b8a', fg="white", font=("Jost", 24, "bold"))
label_titulo.pack(pady=40)

# Campo de entrada para el usuario
entry_usuario = tk.Entry(frame, width=25, bg="#e0dede", border=0, font=("Jost", 12))
entry_usuario.pack(pady=10)
entry_usuario.insert(0, "")

# Campo de entrada para la contraseña
entry_contrasena = tk.Entry(frame, width=25, bg="#e0dede", border=0, show="*", font=("Jost", 12))
entry_contrasena.pack(pady=10)
entry_contrasena.insert(0, "")

# Botón de inicio de sesión
boton_login = tk.Button(frame, text="Iniciar Sesión", command=verificar_login, width=20, height=2, bg="#573b8a", fg="white", font=("Jost", 12, "bold"), bd=0)
boton_login.pack(pady=40)

# Efecto hover en el botón
boton_login.bind("<Enter>", on_enter)
boton_login.bind("<Leave>", on_leave)

# Iniciar la ventana principal
ventana.mainloop()
