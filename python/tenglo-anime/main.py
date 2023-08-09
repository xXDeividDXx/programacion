import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
import albums
import intercambio
import creditos

windows = []

def open_new_window():
    new_window = albums.show_albums()
    windows.append(new_window)

def open_new_window2():
    new_window = intercambio.show_intercambio()
    windows.append(new_window)

def open_new_window3():
    new_window = creditos.show_creditos()
    windows.append(new_window)        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Tenglo-Anime')
    window.setStyleSheet("QWidget {background-image: url(fondo.png)}")
    Hbox = QHBoxLayout()
    window.resize(1024,680)
    
    b1 = QPushButton("Albumnes.")
    b1.setStyleSheet('QPushButton {background-color: red; color: white}')
    b2 = QPushButton("Intercambiar cartas.")
    b2.setStyleSheet('QPushButton {background-color: red; color: white}')
    b3 = QPushButton("Creditos.")
    b3.setStyleSheet('QPushButton {background-color: red; color: white}')
    
    Hbox.addWidget(b1)
    Hbox.addWidget(b2)
    Hbox.addWidget(b3)
    
    b1.clicked.connect(open_new_window)
    b2.clicked.connect(open_new_window2)
    b3.clicked.connect(open_new_window3)
    
    window.setLayout(Hbox)
    window.show()
    sys.exit(app.exec())