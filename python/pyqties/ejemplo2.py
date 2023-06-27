import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QLineEdit
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("calculadora fruna")
        self.setFixedSize(QSize(300,300))

        self.cuadro_texto = QLineEdit(self)
        self.cuadro_texto.move(100, 0)
        self.cuadro_texto.setReadOnly(True)

        self.numero = 0 
        self.operacion = ""
        self.primer_operando = 0 

        caja = QGridLayout()
        b1 = QPushButton("1")
        b2 = QPushButton("2")
        b3 = QPushButton("3")
        b4 = QPushButton("4")
        b5 = QPushButton("5")
        b6 = QPushButton("6")
        b7 = QPushButton("7")
        b8 = QPushButton("8")
        b9 = QPushButton("9")
        b10 = QPushButton("/")
        b11 = QPushButton("*")
        b12 = QPushButton("+")
        b13 = QPushButton("-")
        b14 = QPushButton("=")
        b15 = QPushButton("0")
        caja.addWidget(b1, 0,0)
        caja.addWidget(b2, 0,1)
        caja.addWidget(b3, 0,2)
        caja.addWidget(b4, 1,0)
        caja.addWidget(b5, 1,1)
        caja.addWidget(b6, 1,2)
        caja.addWidget(b7, 2,0)
        caja.addWidget(b8, 2, 1)
        caja.addWidget(b9, 2, 2)
        caja.addWidget(b10, 0, 3)
        caja.addWidget(b11, 1, 3)
        caja.addWidget(b12, 2, 3)
        caja.addWidget(b13, 3, 3)
        caja.addWidget(b14, 3, 2)
        caja.addWidget(b15, 3, 1)

        #valor botones:
        boton1 = 1
        boton2 = 2
        boton3 = 3
        boton4 = 4
        boton5 = 5
        boton6 = 6
        boton7 = 7
        boton8 = 8
        boton9 = 9
        b1.clicked.connect(lambda: self.actualizar_cuadro_texto(1))
        b2.clicked.connect(lambda: self.actualizar_cuadro_texto(2))
        b3.clicked.connect(lambda: self.actualizar_cuadro_texto(3))
        b4.clicked.connect(lambda: self.actualizar_cuadro_texto(4))
        b5.clicked.connect(lambda: self.actualizar_cuadro_texto(5))
        b6.clicked.connect(lambda: self.actualizar_cuadro_texto(6))
        b7.clicked.connect(lambda: self.actualizar_cuadro_texto(7))
        b8.clicked.connect(lambda: self.actualizar_cuadro_texto(8))
        b9.clicked.connect(lambda: self.actualizar_cuadro_texto(9))
        b12.clicked.connect(self.sumar)
        b13.clicked.connect(self.restar)
        b10.clicked.connect(self.dividir)
        b11.clicked.connect(self.multiplicar)
        b14.clicked.connect(self.calcular_resultado)
        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    def actualizar_cuadro_texto(self, valor):
      contenido_actual = self.cuadro_texto.text()
      nuevo_contenido = contenido_actual + str(valor)
      self.cuadro_texto.setText(nuevo_contenido)
    def sumar(self):
        self.operacion = "+"
        self.primer_operando = float(self.cuadro_texto.text())
        self.cuadro_texto.clear()
    def restar(self):
        self.operacion = "-"
        self.primer_operando = float(self.cuadro_texto.text())
        self.cuadro_texto.clear()
    def multiplicar(self):
        self.operacion = "*"
        self.primer_operando = float(self.cuadro_texto.text())
        self.cuadro_texto.clear()
    def dividir(self):
        self.operacion = ":"
        self.primer_operando = float(self.cuadro_texto.text())
        self.cuadro_texto.clear()        
    def calcular_resultado(self):
        segundo_operando = float(self.cuadro_texto.text())
        if self.operacion == "+":
            resultado = self.primer_operando + segundo_operando
        elif self.operacion == "-":
            resultado = self.primer_operando - segundo_operando
        elif self.operacion == "*":
            resultado = self.primer_operando * segundo_operando
        elif self.operacion == "/":
            resultado = self.primer_operando / segundo_operando
        self.cuadro_texto.setText(str(resultado))      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()

# muchas gracias Bing Chat
# fuck you profe                      