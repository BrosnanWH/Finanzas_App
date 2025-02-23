import tkinter as tk
from tkinter import ttk
from meta import Meta
from pagos import Pagos_calendario

def iniciar_ventana_principal():
    # Configuración de la ventana principal 
    ventana_principal = tk.Tk()
    ventana_principal.title("GastoSmart")
    ventana_principal.geometry("500x520")  
    ventana_principal.config(bg='#FFEBE5')

    # Centralizando ventana
    pantalla_ancho = ventana_principal.winfo_screenwidth()
    pantalla_alto = ventana_principal.winfo_screenheight()
    ventana_ancho = 500
    ventana_alto = 520
    posicion_x = int((pantalla_ancho - ventana_ancho) / 2)
    posicion_y = int((pantalla_alto - ventana_alto) / 2)
    ventana_principal.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

    notebook = ttk.Notebook(ventana_principal)
    notebook.pack(fill="both", expand=True)
    notebook.config(height=10)

    ventana_metas = tk.Frame(notebook, bg='#573b8a')
    ventana_calendario = tk.Frame(notebook, bg='#2a4e85')
    ventana_estadisticas = tk.Frame(notebook, bg='#3f64a0')
    ventana_registro_gastos = tk.Frame(notebook, bg='#1a3355')

    notebook.add(ventana_metas, text="Metas Financieras")
    notebook.add(ventana_calendario, text="Pagos")
    notebook.add(ventana_estadisticas, text="Estadísticas de Gastos")
    notebook.add(ventana_registro_gastos, text="Registro de Gastos")

    label_metas = tk.Label(ventana_metas, text="Metas Financieras", font=("Jost", 20, "bold"), fg="white", bg='#573b8a')
    label_metas.pack(pady=20)

    meta = Meta()
    # Botón para ir a la ventana de Agregar Meta
    boton_añadir_meta = tk.Button(ventana_metas, text="Añadir Meta", command=lambda: meta.agregar_meta(ventana_principal), bg="#F28C8C", fg="white", font=("Jost", 14, "bold"))
    boton_añadir_meta.pack(pady=10)
    # Botón para ir a la ventana de Ver Meta
    boton_ver_metas = tk.Button(ventana_metas, text="Ver Metas", command=lambda: meta.ver_metas(ventana_principal), bg="#F28C8C", fg="white", font=("Jost", 14, "bold"))
    boton_ver_metas.pack(pady=10)

    # Contenido de la ventana de Calendario
    label_pagos = tk.Label(ventana_calendario, text="Pagos", font=("Jost", 20, "bold"), fg="white", bg='#2a4e85')
    label_pagos.pack(pady=20)

    pagos_calendario = Pagos_calendario()

    # Botón para ir a la ventana de Calendario
    boton_agregar_pago = tk.Button(ventana_calendario, text="Agregar Pago", command=pagos_calendario.iniciar_ventana_calendario, bg="#F28C8C", fg="white", font=("Jost", 14, "bold"))
    boton_agregar_pago.pack(pady=5)

    label_calendario_pagos = tk.Label(ventana_calendario, text="Calendario de Pagos", font=("Jost", 20, "bold"), fg="white", bg='#2a4e85')
    label_calendario_pagos.pack(pady=30)

    boton_ver_pagos = tk.Button(ventana_calendario, text="Ver Pagos", command=lambda: pagos_calendario.ver_pagos(ventana_principal), bg="#F28C8C", fg="white", font=("Jost", 14, "bold"))
    boton_ver_pagos.pack(pady=5)

    # Contenido de la ventana de Estadísticas
    label_estadisticas = tk.Label(ventana_estadisticas, text="Estadísticas de Gastos", font=("Jost", 20, "bold"), fg="white", bg='#3f64a0')
    label_estadisticas.pack(pady=20)

    # Botón para ir a la ventana de Registro de Gastos
    boton_ir_registro_gastos = tk.Button(ventana_estadisticas, text="Ir a Registro de Gastos", command=lambda: mostrar_ventana(ventana_registro_gastos))
    boton_ir_registro_gastos.pack(pady=10)

    # Contenido de la ventana de Registro de Gastos
    label_registro_gastos = tk.Label(ventana_registro_gastos, text="Registro de Gastos", font=("Jost", 20, "bold"), fg="white", bg='#1a3355')
    label_registro_gastos.pack(pady=20)

    # Botón para volver a la ventana de Metas
    boton_volver_metas = tk.Button(ventana_registro_gastos, text="Ir a Registro de Gastos", command=lambda: mostrar_ventana(ventana_metas))
    boton_volver_metas.pack(pady=10)

    # Iniciar la aplicación
    ventana_principal.mainloop()

# Función para cambiar entre las distintas ventanas
def mostrar_ventana(ventana):
    ventana.tkraise()

# Crear la ventana principal y llamar a la función de inicio
if __name__ == "__main__":
    iniciar_ventana_principal()

