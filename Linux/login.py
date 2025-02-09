import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QSpacerItem, QSizePolicy

class BordeRedondeadoWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)

    def set_borde_redondeado(self, color_fondo, radio_borde):
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {color_fondo};
                border-radius: {radio_borde}px;
            }}
        """)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # Definir estilos y colores
        self.color_fondo_ventana = "#A9B5DF"
        self.color_cuadro = "#FFF2F2"
        self.color_texto = "#333333"
        self.color_botones = "#2D336B"
        self.color_texto_botones = "#FFFFFF"
        self.radio_borde = 30
        self.tamano_inicial_ventana = (600, 400)
        self.tamano_inicial_cuadro = (600, 400)
        self.tamano_max_cuadro = (400, 350)
        self.tamano_min_cuadro = (300, 200)
        self.tamano_texto_titulo = "24px"
        self.tamano_texto_formulario = "16px"
        self.tamano_texto_botones = "18px"

        # Configuración inicial de la ventana
        self.setWindowTitle("GastoSmart - Iniciar Sesión / Crear Cuenta")
        self.resize(*self.tamano_inicial_ventana)
        self.centrar_ventana()

        # Fondo con gradiente
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor(self.color_fondo_ventana))
        self.setPalette(palette)

        # Layout principal
        self.layout = QVBoxLayout(self)

        # Frame con bordes redondeados (cuadro interior)
        self.frame_borde = BordeRedondeadoWidget(self)
        self.frame_borde.set_borde_redondeado(self.color_cuadro, self.radio_borde)

        # Tamaños ajustables del cuadro (redimensionable)
        self.frame_borde.setMinimumSize(*self.tamano_min_cuadro)
        self.frame_borde.setMaximumSize(*self.tamano_max_cuadro)
        self.frame_borde.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Agregar el cuadro redondeado al layout principal con un espaciador
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.frame_borde, alignment=Qt.AlignCenter)
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout para el formulario dentro del cuadro
        self.form_layout = QVBoxLayout(self.frame_borde)

        # Título
        self.title = QLabel("Iniciar Sesión", self)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(f"font-size: {self.tamano_texto_titulo}; font-weight: bold; color: {self.color_texto};")
        self.form_layout.addWidget(self.title)

        # Campos de texto
        self.email_label = QLabel("Email", self)
        self.email_label.setStyleSheet(f"font-size: {self.tamano_texto_formulario}; color: {self.color_texto};")
        self.email_entry = QLineEdit(self)
        self.email_entry.setPlaceholderText("Ingrese su correo")
        self.password_label = QLabel("Contraseña", self)
        self.password_label.setStyleSheet(f"font-size: {self.tamano_texto_formulario}; color: {self.color_texto};")
        self.password_entry = QLineEdit(self)
        self.password_entry.setPlaceholderText("Ingrese su contraseña")
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.form_layout.addWidget(self.email_label)
        self.form_layout.addWidget(self.email_entry)
        self.form_layout.addWidget(self.password_label)
        self.form_layout.addWidget(self.password_entry)

        # Botones
        self.sign_in_btn = QPushButton("Iniciar Sesión", self)
        self.sign_in_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.color_botones};
                color: {self.color_texto_botones};
                font-size: {self.tamano_texto_botones};
                padding: 10px;
                border-radius: 15px;
            }}
        """)
        self.form_layout.addWidget(self.sign_in_btn)

        self.switch_btn = QPushButton("Crear Cuenta", self)
        self.switch_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.color_botones};
                color: {self.color_texto_botones};
                font-size: {self.tamano_texto_botones};
                padding: 10px;
                border-radius: 15px;
            }}
        """)
        self.form_layout.addWidget(self.switch_btn)

        # Conectar eventos
        self.switch_btn.clicked.connect(self.mostrar_registro)

        # Añadir animación de tamaño para el cuadro
        self.animation = QPropertyAnimation(self.frame_borde, b"geometry")
        self.animation.setDuration(700)

        # Iniciar animación al cargar la ventana
        self.animar_entrada()

    def animar_entrada(self):
        # Tamaño de la ventana y cuadro
        ancho_ventana, alto_ventana = self.size().width(), self.size().height()
        ancho_cuadro_final, alto_cuadro_final = -400, 400

        # Posición inicial (pequeño y centrado)
        ancho_cuadro_inicial, alto_cuadro_inicial = 50, 50
        x_inicial = (ancho_ventana - ancho_cuadro_inicial) // 2
        y_inicial = (alto_ventana - alto_cuadro_inicial) // 2
        pos_inicial = QRect(x_inicial, y_inicial, ancho_cuadro_inicial, alto_cuadro_inicial)

        # Posición final (tamaño normal y centrado)
        x_final = (ancho_ventana - ancho_cuadro_final) // 2 + 2
        y_final = (alto_ventana - alto_cuadro_final) // 2 + 200
        pos_final = QRect(x_final, y_final, ancho_cuadro_final, alto_cuadro_final)

        # Configurar animación
        self.animation.setStartValue(pos_inicial)
        self.animation.setEndValue(pos_final)
        self.animation.start()

    def mostrar_registro(self):
        self.title.setText("Crear Cuenta")
        self.email_label.setText("Nombre")
        self.password_label.setText("Correo")
        self.password_entry.setPlaceholderText("Ingrese su correo")
        self.switch_btn.setText("Iniciar Sesión")
        self.switch_btn.clicked.connect(self.mostrar_login)

        # Animación para cambiar de ventana
        self.animar_cuadro(QRect(self.frame_borde.geometry().x(), self.frame_borde.geometry().y(), 250, 320))

    def mostrar_login(self):
        self.title.setText("Iniciar Sesión")
        self.email_label.setText("Email")
        self.password_label.setText("Contraseña")
        self.password_entry.setPlaceholderText("Ingrese su contraseña")
        self.switch_btn.setText("Crear Cuenta")
        self.switch_btn.clicked.connect(self.mostrar_registro)

        # Animación para cambiar de ventana
        self.animar_cuadro(QRect(self.frame_borde.geometry().x(), self.frame_borde.geometry().y(), 180, 290))

    def animar_cuadro(self, nueva_geo):
        self.animation.setStartValue(self.frame_borde.geometry())
        self.animation.setEndValue(nueva_geo)
        self.animation.start()

    def centrar_ventana(self):
        # Obtener el tamaño de la pantalla y ajustar la posición para centrar la ventana
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# Inicializar la aplicación
app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(app.exec_())