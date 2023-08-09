import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget

def show_intercambio():
    window = QWidget()
    window.setWindowTitle('Intercambiar cartas')
    window.setStyleSheet("QWidget {background-image: url(BG_2.png)}")
    Hbox = QHBoxLayout()
    window.resize(1024,680)
    window.setLayout(Hbox)
    window.show()
    #botones
    boton_intercambiar=QPushButton("Intercambiar")
    boton_intercambiar.setStyleSheet('QPushButton {background-color: red; color: white}')
    boton_intercambiar.setFixedSize(100,50)
    Hbox.addWidget(boton_intercambiar)

    b1=QPushButton("Volver")
    Hbox.addWidget(b1)
    b1.setStyleSheet('QPushButton {background-color: red; color: white}')
    b1.clicked.connect(window.close)

    lista_intercambio = QListWidget()
    lista_intercambio.addItems(['Carta 1', 'Carta 2', 'Carta 3','Carta 4','Carta 5','Carta 6','Carta 7','Carta 8', 'Carta 9', 'Carta 10'])
    Hbox.addWidget(lista_intercambio)
    lista_intercambio.setFixedSize(120,200)
    lista_intercambio.setStyleSheet('QListWidget {color : white}')

    b2=QPushButton()
    Hbox.addWidget(b2)
    b2.setFixedSize(191,243)
    b3=QPushButton()
    Hbox.addWidget(b3)
    b3.setFixedSize(191,243)

    lista_intercambio2 = QListWidget()
    lista_intercambio2.addItems(['Carta 1', 'Carta 2', 'Carta 3','Carta 4','Carta 5','Carta 6','Carta 7','Carta 8', 'Carta 9', 'Carta 10'])
    Hbox.addWidget(lista_intercambio2)
    lista_intercambio2.setFixedSize(120,200)
    lista_intercambio2.setStyleSheet('QListWidget {color : white}')

    boton_intercambiar2=QPushButton("Intercambiar")
    boton_intercambiar2.setStyleSheet('QPushButton {background-color: red; color: white}')
    boton_intercambiar2.setFixedSize(100,50)
    Hbox.addWidget(boton_intercambiar2)

    #funciones
    def on_item_clicked(item):
      image_path = f"{item.text()}.png"
      b2.setStyleSheet(f"QPushButton {{background-image: url({image_path})}}")

    def on_item_clicked2(item):
      image_path = f"{item.text()}.png"
      b3.setStyleSheet(f"QPushButton {{background-image: url({image_path})}}")

    def guardar_listas():
      items1 = [lista_intercambio.item(i).text() for i in range(lista_intercambio.count())]
      items2 = [lista_intercambio2.item(i).text() for i in range(lista_intercambio2.count())]
    
      with open('listas.txt', 'w') as f:
        f.write('\n'.join(items1) + '\n')
        f.write('\n'.join(items2) + '\n')

    def cargar_listas():
      with open('listas.txt', 'r') as f:
        lines = f.read().splitlines()
    
      index = 0
      lista_intercambio.clear()
      while index < len(lines) and lines[index] != '':
          lista_intercambio.addItem(lines[index])
          index += 1
    
      index += 1
      lista_intercambio2.clear()
      while index < len(lines):
          lista_intercambio2.addItem(lines[index])
          index += 1
    def intercambiar():
      item = lista_intercambio.takeItem(lista_intercambio.currentRow())
      if item:
        lista_intercambio2.addItem(item.text())
    def intercambiar2():
      item = lista_intercambio2.takeItem(lista_intercambio2.currentRow())
      if item:
        lista_intercambio.addItem(item.text())     
  
    #mas botones
    guardar_listas()
    lista_intercambio.itemClicked.connect(on_item_clicked)
    lista_intercambio2.itemClicked.connect(on_item_clicked2)
    boton_intercambiar.clicked.connect(intercambiar)
    boton_intercambiar2.clicked.connect(intercambiar2)
    vbox = QVBoxLayout()
    vbox.addLayout(Hbox)
    vbox.addWidget(b1)
    b1.setFixedSize(100,50)
    window.setLayout(vbox)
    return window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_intercambio()
    sys.exit(app.exec())