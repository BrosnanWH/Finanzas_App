import tkinter as tk
import meta

# Función para inicializar la ventana principal
def iniciar_ventana_principal():
    # Configuración de la ventana principal con el mismo tamaño que la ventana de login
    ventana_principal = tk.Tk()
    ventana_principal.title("GastoSmart")
    ventana_principal.geometry("300x496")  # Cambiado para coincidir con la ventana de login
    ventana_principal.config(bg='#0f0c29')

    # Definir el contenedor principal donde se cargarán las diferentes ventanas
    contenedor = tk.Frame(ventana_principal)
    contenedor.pack(fill="both", expand=True)

    # Definir las distintas ventanas (frames)
    ventana_metas = tk.Frame(contenedor, bg='#573b8a')
    ventana_metas.grid(row=1, column=0, sticky='nsew')

    ventana_calendario = tk.Frame(contenedor, bg='#2a4e85')
    ventana_calendario.grid(row=2, column=0, sticky='nsew')

    ventana_estadisticas = tk.Frame(contenedor, bg='#3f64a0')
    ventana_estadisticas.grid(row=3, column=0, sticky='nsew')

    ventana_registro_gastos = tk.Frame(contenedor, bg='#1a3355')
    ventana_registro_gastos.grid(row=4, column=0, sticky='nsew')

    # Contenido de la ventana de Metas
    label_metas = tk.Label(ventana_metas, text="Metas Financieras", font=("Jost", 20, "bold"), fg="white", bg='#573b8a')
    label_metas.pack(pady=20)

    # Botón para ir a la ventana de Calendario
    boton_añadir_meta = tk.Button(ventana_metas, text="Añadir Meta", command=lambda: meta.agregar_meta(ventana_metas))
    boton_añadir_meta.pack(pady=10)
    
    # Contenido de la ventana de Calendario
    label_calendario = tk.Label(ventana_calendario, text="Calendario de Pagos", font=("Jost", 20, "bold"), fg="white", bg='#2a4e85')
    label_calendario.pack(pady=20)

    # Botón para ir a la ventana de Estadísticas
    boton_ir_estadisticas = tk.Button(ventana_calendario, text="Ir a Calendario", command=lambda: mostrar_ventana(ventana_estadisticas))
    boton_ir_estadisticas.pack(pady=10)

    # Contenido de la ventana de Estadísticas
    label_estadisticas = tk.Label(ventana_estadisticas, text="Estadísticas de Gastos", font=("Jost", 20, "bold"), fg="white", bg='#3f64a0')
    label_estadisticas.pack(pady=20)

    # Botón para ir a la ventana de Registro de Gastos
    boton_ir_registro_gastos = tk.Button(ventana_estadisticas, text="Ir a Estadísticas", command=lambda: mostrar_ventana(ventana_registro_gastos))
    boton_ir_registro_gastos.pack(pady=10)

    # Contenido de la ventana de Registro de Gastos
    label_registro_gastos = tk.Label(ventana_registro_gastos, text="Registro de Gastos", font=("Jost", 20, "bold"), fg="white", bg='#1a3355')
    label_registro_gastos.pack(pady=20)

    # Botón para volver a la ventana de Metas
    boton_volver_metas = tk.Button(ventana_registro_gastos, text="Ir a Registro de Gastos", command=lambda: mostrar_ventana(ventana_metas))
    boton_volver_metas.pack(pady=10)

    # Mostrar la primera ventana (Metas) al iniciar la aplicación
    mostrar_ventana(ventana_metas)

    # Iniciar la aplicación
    ventana_principal.mainloop()

# Función para cambiar entre las distintas ventanas
def mostrar_ventana(ventana):
    ventana.tkraise()
