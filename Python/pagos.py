import tkinter as tk
from tkinter import messagebox
import pyodbc
from tkinter import ttk

class Pagos_calendario:
    def __init__(self):
        self.entry_pago_nombre = None
        self.entry_pago_fecha = None
        self.entry_pago_descripcion = None
        self.entry_pago_cantidad = None

    def agregar_pago(self):
        
        pago_nombre = self.entry_pago_nombre.get()
        pago_fecha = self.entry_pago_fecha.get()
        pago_descripcion = self.entry_pago_descripcion.get()
        pago_cantidad = self.entry_pago_cantidad.get()

        if not pago_nombre or not pago_fecha or not pago_cantidad:
            messagebox.showwarning("¡Error!", "El nombre del pago, la fecha y la cantidad son obligatorios.")
            return

        
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

            # Consulta para insertar los datos del pago en la base de datos
            cursor.execute("""
                INSERT INTO dbo.Pagos (nombre_pago, fecha_pago, descripcion, cantidad)
                VALUES (?, ?, ?, ?)
            """, (pago_nombre, pago_fecha, pago_descripcion, pago_cantidad))

            conexion.commit()
            messagebox.showinfo("Éxito", "Pago guardado exitosamente.")
            # Limpiar los campos de entrada
            self.entry_pago_nombre.delete(0, tk.END)
            self.entry_pago_fecha.delete(0, tk.END)
            self.entry_pago_descripcion.delete(0, tk.END)
            self.entry_pago_cantidad.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error de Conexión", f"No se pudo guardar el pago: {e}")

        finally:
            if 'conexion' in locals():
                conexion.close()
    def ver_pagos(self, ventana_ver_pagos):
        ventana_ver_pagos = tk.Toplevel()
        ventana_ver_pagos.title("Ver Pagos")
        ventana_ver_pagos.geometry("500x520")
        ventana_ver_pagos.config(bg='#FFEBE5')

        pantalla_ancho = ventana_ver_pagos.winfo_screenwidth()
        pantalla_alto = ventana_ver_pagos.winfo_screenheight()
        ventana_ancho = 500
        ventana_alto = 520
        posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
        posicion_y = int((pantalla_alto - ventana_alto) / 2)
        ventana_ver_pagos.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

        frame_tree = tk.Frame(ventana_ver_pagos)
        frame_tree.pack(fill="both", expand=True)

        tree = ttk.Treeview(frame_tree, columns=("Pago", "Fecha de Pago", "Descripcion", "Cantidad a Pagar", "Estado"), show='headings')
        tree.heading("Pago", text="Pago")
        tree.heading("Fecha de Pago", text="Fecha de Pago")
        tree.heading("Descripcion", text="Descripcion")
        tree.heading("Cantidad a Pagar", text="Cantidad a Pagar")
        

        tree.column("Pago", width=100, anchor="center", stretch=True)
        tree.column("Fecha de Pago", width=100, anchor="center", stretch=True)
        tree.column("Descripcion", width=100, anchor="center", stretch=True)
        tree.column("Cantidad a Pagar", width=100, anchor="center", stretch=True)
        
        tree.pack(fill="both", expand=True)
        tk.Button(ventana_ver_pagos, text="Volver", command=lambda: (ventana_ver_pagos.destroy()), bg="#F28C8C", fg="white", font=("Jost", 14, "bold")).pack(pady=10)

        conn_str = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=DESKTOP-DK0D7AB;DATABASE=Northwind;"
            "UID=JOSHUA\\rugam;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        conexion = pyodbc.connect(conn_str)
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre_pago, fecha_pago, descripcion, cantidad FROM dbo.Pagos")
        rows = cursor.fetchall()

        from datetime import datetime
        

        for row in rows:
            nombre_pago, fecha_pago, descripcion, cantidad = row
            
            tree.insert("", tk.END, values=(nombre_pago, fecha_pago, descripcion, cantidad))


    def iniciar_ventana_calendario(self):
        ventana_calendario = tk.Toplevel()
        ventana_calendario.title("Calendario de Pagos")
        ventana_calendario.geometry("500x520")
        ventana_calendario.config(bg='#2a4e85')

        pantalla_ancho = ventana_calendario.winfo_screenwidth()
        pantalla_alto = ventana_calendario.winfo_screenheight()
        ventana_ancho = 500
        ventana_alto = 520
        posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
        posicion_y = int((pantalla_alto - ventana_alto) / 2)
        ventana_calendario.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

        # Etiqueta de título
        label_titulo = tk.Label(ventana_calendario, text="Agregar Pago", font=("Jost", 20, "bold"), fg="white", bg='#2a4e85')
        label_titulo.pack(pady=20)

        # Campo de entrada para el nombre del pago
        label_pago_nombre = tk.Label(ventana_calendario, text="Nombre del Pago", bg='#2a4e85', fg="white")
        label_pago_nombre.pack(pady=5)
        self.entry_pago_nombre = tk.Entry(ventana_calendario, width=30, font=("Jost", 12))
        self.entry_pago_nombre.pack(pady=5)

        # Campo de entrada para la fecha del pago
        label_pago_fecha = tk.Label(ventana_calendario, text="Fecha del Pago (YYYY-MM-DD)", bg='#2a4e85', fg="white")
        label_pago_fecha.pack(pady=5)
        self.entry_pago_fecha = tk.Entry(ventana_calendario, width=30, font=("Jost", 12))
        self.entry_pago_fecha.pack(pady=5)

        # Campo de entrada para la cantidad del pago
        label_pago_cantidad = tk.Label(ventana_calendario, text="Cantidad a Pagar (USD)", bg='#2a4e85', fg="white")
        label_pago_cantidad.pack(pady=5)
        self.entry_pago_cantidad = tk.Entry(ventana_calendario, width=30, font=("Jost", 12))
        self.entry_pago_cantidad.pack(pady=5)

        # Campo de entrada para la descripción del pago (opcional)
        label_pago_descripcion = tk.Label(ventana_calendario, text="Descripción (Opcional)", bg='#2a4e85', fg="white")
        label_pago_descripcion.pack(pady=5)
        self.entry_pago_descripcion = tk.Entry(ventana_calendario, width=30, font=("Jost", 12))
        self.entry_pago_descripcion.pack(pady=5)

        # Botón para guardar el pago
        boton_guardar_pago = tk.Button(ventana_calendario, text="Guardar Pago", command=self.agregar_pago, bg="#F28C8C", fg="white", font=("Jost", 12, "bold"))
        boton_guardar_pago.pack(pady=20)

        tk.Button(ventana_calendario, text="Cancelar", command=lambda: (ventana_calendario.destroy()), bg="#F28C8C", fg="white", font=("Jost", 14, "bold")).pack(pady=10)
        
        ventana_calendario.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    app = Pagos_calendario()
    app.iniciar_ventana_calendario()

