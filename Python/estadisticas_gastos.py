import matplotlib.pyplot as plt
import pyodbc

class EstadisticasGastos:
    def __init__(self):
        self.conectar_bd()
        self.obtener_datos()
        self.generar_grafico()

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

    def obtener_datos(self):
        self.cursor.execute(
            "SELECT categoria, SUM(cantidad_gastada) AS total_gastado "
            "FROM registro_gastos "
            "GROUP BY categoria"
        )
        self.datos = self.cursor.fetchall()

    def generar_grafico(self):
        categorias = [fila[0] for fila in self.datos]
        totales = [fila[1] for fila in self.datos]

        plt.figure(figsize=(8, 6))
        plt.pie(totales, labels=categorias, autopct='%1.1f%%', startangle=140)
        plt.title("Distribución de Gastos por Categoría")
        plt.axis('equal')  # Para que el gráfico sea un círculo
        plt.show()

if __name__ == "__main__":
    EstadisticasGastos()
