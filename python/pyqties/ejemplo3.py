import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Ventana principal')
    hbox = QHBoxLayout()
    window.resize(500,500)
    hbox.addWidget(QPushButton('Botón 1'))
    hbox.addWidget(QPushButton('Botón 2'))
    window.setLayout(hbox)
    window.show()
    sys.exit(app.exec())
 