import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QLineEdit

def digito_verificador(rut):
    rut = str(rut)
    suma = 0
    multiplicador = 2
    for i in range(len(rut)-1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    dv = 11 - resto
    if dv == 10:
        return 'K'
    elif dv == 11:
        return '0'
    else:
        return str(dv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Verificador de RUT")
        self.setFixedSize(QSize(400, 200))
        
        layout = QGridLayout()
        self.rut_label = QLabel("RUT:")
        self.rut_input = QLineEdit()
        self.dv_label = QLabel("Dígito verificador:")
        self.dv_input = QLineEdit()
        self.dv_input.setFixedWidth(25)
        self.verify_button = QPushButton("Verificar")
        self.verify_button.clicked.connect(self.verify_rut)
        self.result_label = QLabel()
        layout.addWidget(self.rut_label, 0, 0)
        layout.addWidget(self.rut_input, 0, 1)
        layout.addWidget(self.dv_label, 0, 2)
        layout.addWidget(self.dv_input, 0, 3)
        layout.addWidget(self.verify_button, 2, 1, 1, 1)
        layout.addWidget(self.result_label, 3, 0, 1, 2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def verify_rut(self):
        rut = self.rut_input.text()
        dv = digito_verificador(rut)
        dv_comparativo = self.dv_input.text()
        if dv == dv_comparativo:
            self.result_label.setText("Su RUT es válido.")
            self.result_label.setStyleSheet("color: green")
        else:
            self.result_label.setText("Su RUT es falso.")
            self.result_label.setStyleSheet("color: red")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
