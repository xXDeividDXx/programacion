import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget

def show_albums():
    window = QWidget()
    window.setWindowTitle('Albumnes.')
    window.setStyleSheet("QWidget {background-image: url(BG_2.png)}")
    Hbox = QHBoxLayout()
    window.resize(1024,680)
    window.setLayout(Hbox)
    window.show()

    b1=QPushButton("Volver")
    Hbox.addWidget(b1)
    b1.setStyleSheet('QPushButton {background-color: red; color: white}')
    b1.clicked.connect(window.close)

    b2=QPushButton()
    Hbox.addWidget(b2)
    b2.setFixedSize(191,243)

    #albums
    lista_intercambio = QListWidget()
    lista_intercambio.addItems(['Carta 1', 'Carta 2', 'Carta 3','Carta 4','Carta 5','Carta 6','Carta 7','Carta 8', 'Carta 9', 'Carta 10'])
    Hbox.addWidget(lista_intercambio)
    lista_intercambio.setFixedSize(120,200)
    lista_intercambio.setStyleSheet('QListWidget {color : white}')

    lista_intercambio2 = QListWidget()
    lista_intercambio2.addItems(['Carta 1', 'Carta 2', 'Carta 3','Carta 4','Carta 5','Carta 6','Carta 7','Carta 8', 'Carta 9', 'Carta 10'])
    Hbox.addWidget(lista_intercambio2)
    lista_intercambio2.setFixedSize(120,200)
    lista_intercambio2.setStyleSheet('QListWidget {color : white}')

    lista_intercambio3 = QListWidget()
    lista_intercambio3.addItems(['Carta 1', 'Carta 2', 'Carta 3','Carta 4','Carta 5','Carta 6','Carta 7','Carta 8', 'Carta 9', 'Carta 10'])
    Hbox.addWidget(lista_intercambio3)
    lista_intercambio3.setFixedSize(120,200)
    lista_intercambio3.setStyleSheet('QListWidget {color : white}')

    lista_intercambio4 = QListWidget()
    lista_intercambio4.addItems(['Carta 1', 'Carta 2', 'Carta 3','Carta 4','Carta 5','Carta 6','Carta 7','Carta 8', 'Carta 9', 'Carta 10'])
    Hbox.addWidget(lista_intercambio4)
    lista_intercambio4.setFixedSize(120,200)
    lista_intercambio4.setStyleSheet('QListWidget {color : white}')

    def on_item_clicked(item):
      image_path = f"{item.text()}.png"
      b2.setStyleSheet(f"QPushButton {{background-image: url({image_path})}}")
    def on_item_clicked2(item):
      image_path = f"{item.text()}.png"
      b2.setStyleSheet(f"QPushButton {{background-image: url({image_path})}}")
    def on_item_clicked3(item):
      image_path = f"{item.text()}.png"
      b2.setStyleSheet(f"QPushButton {{background-image: url({image_path})}}")
    def on_item_clicked4(item):
      image_path = f"{item.text()}.png"
      b2.setStyleSheet(f"QPushButton {{background-image: url({image_path})}}")

    lista_intercambio.itemClicked.connect(on_item_clicked)
    lista_intercambio2.itemClicked.connect(on_item_clicked2)
    lista_intercambio3.itemClicked.connect(on_item_clicked3)
    lista_intercambio4.itemClicked.connect(on_item_clicked4)        

    vbox = QVBoxLayout()
    vbox.addLayout(Hbox)
    vbox.addWidget(b1)
    b1.setFixedSize(100,50)
    
    window.setLayout(vbox)
    return window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_albums()
    sys.exit(app.exec())