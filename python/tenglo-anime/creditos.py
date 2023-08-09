import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget

def show_creditos():
    window = QWidget()
    window.setWindowTitle('Creditos.')
    window.setStyleSheet("QWidget {background-image: url(BG_3.png)}")
    Hbox = QHBoxLayout()
    b1=QPushButton("Volver")
    Hbox.addWidget(b1)
    b1.setStyleSheet('QPushButton {background-color: red; color: white}')
    b1.clicked.connect(window.close)
    window.resize(1024,680)
    window.setLayout(Hbox)
    vbox = QVBoxLayout()
    vbox.addLayout(Hbox)
    vbox.addWidget(b1)
    b1.setFixedSize(100,50)
    window.show()
    
    return window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_creditos()
    sys.exit(app.exec())