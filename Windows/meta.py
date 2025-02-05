import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

def agregar_meta():
      # Oculta la ventana principal
    ventana_meta = tk.Toplevel()
    ventana_meta.title("Añadir Meta")
    ventana_meta.geometry("400x500")
    ventana_meta.config(bg='#0f0c29')

    # Etiquetas y campos para los datos de la meta
    tk.Label(ventana_meta, text="Añadir Meta", font=("Jost", 20, "bold"), fg="white", bg='#573b8a').pack(pady=20)

    tk.Label(ventana_meta, text="Nombre de la Meta", fg="white", bg='#0f0c29').pack(pady=5)
    entry_nombre_meta = tk.Entry(ventana_meta)
    entry_nombre_meta.pack(pady=5)

    tk.Label(ventana_meta, text="Notas", fg="white", bg='#0f0c29').pack(pady=5)
    entry_notas = tk.Entry(ventana_meta)
    entry_notas.pack(pady=5)

    tk.Label(ventana_meta, text="Categoría", fg="white", bg='#0f0c29').pack(pady=5)
    categorias = [
        'Supermercado', 'Ropa', 'Casa', 'Entretenimiento', 'Transporte', 'Regalos', 'Viaje',
        'Educación', 'Comida', 'Electrónica', 'Deporte', 'Restaurante', 'Salud', 'Comunicaciones', 'Otros'
    ]
    combo_categoria = ttk.Combobox(ventana_meta, values=categorias)
    combo_categoria.pack(pady=5)

    tk.Label(ventana_meta, text="Cantidad Requerida (USD o CS)", fg="white", bg='#0f0c29').pack(pady=5)
    entry_cantidad_requerida = tk.Entry(ventana_meta)
    entry_cantidad_requerida.pack(pady=5)

    tk.Label(ventana_meta, text="Cantidad Acumulada (opcional)", fg="white", bg='#0f0c29').pack(pady=5)
    entry_cantidad_acumulada = tk.Entry(ventana_meta)
    entry_cantidad_acumulada.pack(pady=5)

    # Función para guardar la meta en la base de datos
    def guardar_meta():
        nombre = entry_nombre_meta.get()
        notas = entry_notas.get()
        categoria = combo_categoria.get()
        cantidad_requerida = entry_cantidad_requerida.get()
        cantidad_acumulada = entry_cantidad_acumulada.get() or "0"

        if not nombre or not categoria or not cantidad_requerida:
            messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
            return

        try:
            conn_str = (
                "DRIVER={ODBC Driver 18 for SQL Server};"
                "SERVER=Joshua;DATABASE=Northwind;"
                "UID=JOSHUA\\rugam;"
                "Trusted_Connection=yes;"
                "TrustServerCertificate=yes;"
            )
            conexion = pyodbc.connect(conn_str)
            cursor = conexion.cursor()

            # Guardar la meta en la base de datos
            cursor.execute("""
                INSERT INTO dbo.MetasFinancieras (nombre_meta, notas, categoria, cantidad_requerida, cantidad_acumulada)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, notas, categoria, cantidad_requerida, cantidad_acumulada))
            conexion.commit()

            messagebox.showinfo("Éxito", "Meta añadida correctamente.")
            ventana_meta.destroy()  # Cerrar ventana de añadir meta
            ventana_anterior.deiconify()  # Mostrar la ventana anterior

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la meta: {e}")

        finally:
            if 'conexion' in locals():
                conexion.close()

    # Botones para guardar o cancelar
    tk.Button(ventana_meta, text="Añadir Meta", command=guardar_meta, bg="#573b8a", fg="white").pack(pady=20)
    tk.Button(ventana_meta, text="Cancelar", command=lambda: (ventana_meta.destroy(), ventana_anterior.deiconify()), bg="#573b8a", fg="white").pack(pady=10)
