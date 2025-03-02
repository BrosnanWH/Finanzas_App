import tkinter as tk
from tkinter import messagebox, ttk
import pyodbc
from datetime import datetime

class RegistroGastos:
    def __init__(self):
        self.balance_actual = 0
        self.balance_anterior = 0
        self.conectar_bd()
        self.crear_interfaz()
    
    def conectar_bd(self):
        self.conn_str = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=DESKTOP-DK0D7AB;DATABASE=Northwind;"
            "UID=JOSHUA\\rugam;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        self.conexion = pyodbc.connect(self.conn_str)
        self.cursor = self.conexion.cursor()
        
    def cargar_balance(self):
        self.cursor.execute("SELECT TOP 1 balance FROM registro_gastos ORDER BY id DESC")
        row = self.cursor.fetchone()
        if row:
            self.balance_actual = row[0]
            self.balance_anterior = row[0]
        self.actualizar_pantalla()
    
    def actualizar_balance(self):
        nuevo_balance = self.entry_balance.get()
        if not nuevo_balance.isdigit():
            messagebox.showerror("Error", "Ingrese un balance válido.")
            return
        self.balance_anterior = self.balance_actual
        self.balance_actual = int(nuevo_balance)
        self.cursor.execute("INSERT INTO registro_gastos (balance) VALUES (?)", (self.balance_actual,))
        self.conexion.commit()
        self.actualizar_pantalla()
    
    def agregar_gasto(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        fecha = self.entry_fecha.get()
        descripcion = self.entry_descripcion.get()
        categoria = self.combo_categoria.get()
        
        if not nombre or not cantidad.isdigit() or not fecha:
            messagebox.showerror("Error", "Ingrese datos válidos para el gasto.")
            return
        
        cantidad = int(cantidad)
        self.balance_anterior = self.balance_actual
        self.balance_actual -= cantidad
        
        self.cursor.execute("INSERT INTO registro_gastos (nombre_gasto, cantidad_gastada, fecha_gasto, descripcion, balance, categoria) VALUES (?, ?, ?, ?, ?,?)",
                            (nombre, cantidad, fecha, descripcion, self.balance_actual, categoria))
        self.conexion.commit()
        
        self.actualizar_pantalla()
        self.tree.insert("", tk.END, values=(nombre, cantidad, fecha, descripcion, categoria))
    
    def actualizar_pantalla(self):
        self.label_balance_actual.config(text=f"Balance Actual: {self.balance_actual}")
        self.label_balance_anterior.config(text=f"Balance Anterior: {self.balance_anterior}")
    
    def crear_interfaz(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de Gastos")
        self.ventana.geometry("500x600")
        
        self.label_balance_actual = tk.Label(self.ventana, text="Balance Actual: 0", font=("Arial", 14))
        self.label_balance_actual.pack()
        
        self.label_balance_anterior = tk.Label(self.ventana, text="Balance Anterior: 0", font=("Arial", 12))
        self.label_balance_anterior.pack()
        
        tk.Label(self.ventana, text="Nuevo Balance:").pack()
        self.entry_balance = tk.Entry(self.ventana)
        self.entry_balance.pack()
        tk.Button(self.ventana, text="Actualizar Balance", command=self.actualizar_balance).pack()
        
        tk.Label(self.ventana, text="Nombre del Gasto:").pack()
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()
        
        tk.Label(self.ventana, text="Cantidad:").pack()
        self.entry_cantidad = tk.Entry(self.ventana)
        self.entry_cantidad.pack()
        
        tk.Label(self.ventana, text="Fecha (YYYY-MM-DD):").pack()
        self.entry_fecha = tk.Entry(self.ventana)
        self.entry_fecha.pack()
        
        tk.Label(self.ventana, text="Descripción:").pack()
        self.entry_descripcion = tk.Entry(self.ventana)
        self.entry_descripcion.pack()

        # Crear combobox para las categorías y asignarlo a un atributo de la clase
        tk.Label(self.ventana, text="Categoría", fg="#4A4A4A", bg='#FFEBE5').pack(pady=5)
        categorias = [
            'Supermercado', 'Ropa', 'Casa', 'Entretenimiento', 'Transporte', 'Regalos', 'Viaje',
            'Educación', 'Comida', 'Electrónica', 'Deporte', 'Restaurante', 'Salud', 'Comunicaciones', 'Otros'
        ]
        self.combo_categoria = ttk.Combobox(self.ventana, values=categorias)  # Asignación a self
        self.combo_categoria.pack(pady=5)
        
        tk.Button(self.ventana, text="Agregar Gasto", command=self.agregar_gasto).pack()
        
        self.tree = ttk.Treeview(self.ventana, columns=("Nombre", "Cantidad", "Fecha", "Descripción", "Categoría"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.pack()
        
        self.cargar_balance()
        self.ventana.mainloop()


if __name__ == "__main__":
    RegistroGastos()