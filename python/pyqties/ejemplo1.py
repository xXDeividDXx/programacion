import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget

class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    def inicializarUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("primera ventana en pyqt6")
        self.show() #muestre efectivamente en pantalla(obligatorio).

if __name__ == "__main__":
   app = QApplication(sys.argv) # lanzar la aplicacion con una llamada al sistema.
   #montar ventana.
   ventana = ventana()
   sys.exit(app.exec())