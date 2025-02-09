import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

class Meta:
    def agregar_meta(self, ventana_metas):
        ventana_metas.withdraw()  
        ventana_añadir_meta = tk.Toplevel()
        ventana_añadir_meta.title("Añadir Meta")
        ventana_añadir_meta.geometry("400x500")
        ventana_añadir_meta.config(bg='#FFEBE5') 

        # Centralizando ventana
        pantalla_ancho = ventana_añadir_meta.winfo_screenwidth()
        pantalla_alto = ventana_añadir_meta.winfo_screenheight()
        ventana_ancho = 500
        ventana_alto = 650
        posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
        posicion_y = int((pantalla_alto - ventana_alto) / 2)
        ventana_añadir_meta.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

        tk.Label(ventana_añadir_meta, text="Añadir Meta", font=("Jost", 20, "bold"), fg="#4A4A4A", bg='#FFEBE5').pack(pady=20)

        tk.Label(ventana_añadir_meta, text="Nombre de la Meta", fg="#4A4A4A", bg='#FFEBE5').pack(pady=5)
        entry_nombre_meta = tk.Entry(ventana_añadir_meta)
        entry_nombre_meta.pack(pady=5)

        tk.Label(ventana_añadir_meta, text="Notas", fg="#4A4A4A", bg='#FFEBE5').pack(pady=5)
        entry_notas = tk.Entry(ventana_añadir_meta)
        entry_notas.pack(pady=5)

        tk.Label(ventana_añadir_meta, text="Categoría", fg="#4A4A4A", bg='#FFEBE5').pack(pady=5)
        categorias = [
            'Supermercado', 'Ropa', 'Casa', 'Entretenimiento', 'Transporte', 'Regalos', 'Viaje',
            'Educación', 'Comida', 'Electrónica', 'Deporte', 'Restaurante', 'Salud', 'Comunicaciones', 'Otros'
        ]
        combo_categoria = ttk.Combobox(ventana_añadir_meta, values=categorias)
        combo_categoria.pack(pady=5)

        tk.Label(ventana_añadir_meta, text="Cantidad Requerida (USD o CS)", fg="#4A4A4A", bg='#FFEBE5').pack(pady=5)
        entry_cantidad_requerida = tk.Entry(ventana_añadir_meta)
        entry_cantidad_requerida.pack(pady=5)

        tk.Label(ventana_añadir_meta, text="Cantidad Acumulada (opcional)", fg="#4A4A4A", bg='#FFEBE5').pack(pady=5)
        entry_cantidad_acumulada = tk.Entry(ventana_añadir_meta)
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
                    "SERVER=DESKTOP-DK0D7AB;DATABASE=Northwind;"
                    "UID=JOSHUA\\rugam;"  # Cambia si tu usuario o servidor es diferente
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
                ventana_añadir_meta.destroy()  # Cerrar ventana de añadir meta
                ventana_metas.deiconify()  # Mostrar la ventana principal

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la meta: {e}")

            finally:
                if 'conexion' in locals():
                    conexion.close()
        

        # Botones para guardar o cancelar
        tk.Button(ventana_añadir_meta, text="Añadir Meta", command=guardar_meta, bg="#F28C8C", fg="white", font=("Jost", 14, "bold")).pack(pady=20)
        tk.Button(ventana_añadir_meta, text="Cancelar", command=lambda: (ventana_añadir_meta.destroy(), ventana_metas.deiconify()), bg="#F28C8C", fg="white", font=("Jost", 14, "bold")).pack(pady=10)

    def ver_metas(self, ventana_ver_metas):
            ventana_ver_metas = tk.Toplevel()
            ventana_ver_metas.title("Ver Metas")
            ventana_ver_metas.geometry("1200x500")
            ventana_ver_metas.config(bg='#FFEBE5')

            # Centralizando ventana
            pantalla_ancho = ventana_ver_metas.winfo_screenwidth()
            pantalla_alto = ventana_ver_metas.winfo_screenheight()
            ventana_ancho = 500
            ventana_alto = 650
            posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
            posicion_y = int((pantalla_alto - ventana_alto) / 2)
            ventana_ver_metas.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

            frame_tree = tk.Frame(ventana_ver_metas)
            frame_tree.pack(fill="both", expand=True)

            tree = ttk.Treeview(frame_tree, columns=("Nombre", "Notas", "Categoría", "Cantidad Requerida", "Cantidad Acumulada", "Progreso"), show='headings')
    
            tree.heading("Nombre", text="Nombre")
            tree.heading("Notas", text="Notas")
            tree.heading("Categoría", text="Categoría")
            tree.heading("Cantidad Requerida", text="Cantidad Requerida")
            tree.heading("Cantidad Acumulada", text="Cantidad Acumulada")
            tree.heading("Progreso", text="Progreso")
            
            tree.column("Nombre", width=100, anchor="center", stretch=True)
            tree.column("Notas", width=100, anchor="center", stretch=True)
            tree.column("Categoría", width=100, anchor="center", stretch=True)
            tree.column("Cantidad Requerida", width=100, anchor="center", stretch=True)
            tree.column("Cantidad Acumulada", width=100, anchor="center", stretch=True)
            tree.column("Progreso", width=100, anchor="center", stretch=True)
            tree.pack(fill="both", expand=True)

            conn_str = (
                "DRIVER={ODBC Driver 18 for SQL Server};"
                "SERVER=DESKTOP-DK0D7AB;DATABASE=Northwind;"
                "UID=JOSHUA\\rugam;"  
                "Trusted_Connection=yes;"
                "TrustServerCertificate=yes;"  
            )       
            conexion = pyodbc.connect(conn_str)
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM dbo.MetasFinancieras")
            rows = cursor.fetchall()

            for row in rows:
                 
                nombre_meta, notas, categoria, cantidad_requerida, cantidad_acumulada = row
                progreso = round((cantidad_acumulada / cantidad_requerida) * 100, 2) if cantidad_requerida > 0 else 0
                tree.insert("", tk.END, values=(nombre_meta, notas, categoria, cantidad_requerida, cantidad_acumulada, f"{progreso}%"))

            def actualizar_progreso():
                selected_item = tree.selection()[0]
                cantidad_acumulada = float(tree.item(selected_item)['values'][4])
                cantidad_acumulada += 10  # Incrementa en 10 como ejemplo, puedes personalizar esto

                nombre_meta = tree.item(selected_item)['values'][0]

                cursor.execute("UPDATE dbo.MetasFinancieras SET cantidad_acumulada = ? WHERE nombre_meta = ?", (cantidad_acumulada, nombre_meta))
                conexion.commit()

                new_values = list(tree.item(selected_item)['values'])
                new_values[4] = cantidad_acumulada
                new_values[5] = f"{round((cantidad_acumulada / new_values[3]) * 100, 2)}%"
                tree.item(selected_item, values=new_values)

            tk.Button(ventana_ver_metas, text="Actualizar Progreso", command=actualizar_progreso, bg="#F28C8C", fg="white", font=("Jost", 14, "bold")).pack(pady=10)

            ventana_ver_metas.mainloop()

def iniciar_ventana_principal():
        
            
    meta_ventana_principal = tk.Tk()
    meta_ventana_principal.title("GastoSmart")
    meta_ventana_principal.geometry("400x496")
    meta_ventana_principal.config(bg='#FFEBE5')

    contenedor = tk.Frame(meta_ventana_principal)
    contenedor.pack(fill="both", expand=True)

    ventana_metas = tk.Frame(contenedor, bg='#FFEBE5')
    ventana_metas.grid(row=0, column=0, sticky='nsew')

    label_metas = tk.Label(ventana_metas, text="Metas Financieras", font=("Jost", 20, "bold"), fg="#4A4A4A", bg='#FFEBE5')
    label_metas.pack(pady=20)

    meta_ventana_principal.mainloop()
