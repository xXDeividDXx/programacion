import sys
from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog

class InstructionsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("¡STOP!")
        self.setFixedSize(QSize(400, 200))
        layout = QVBoxLayout()
        instructions_label = QLabel("Instrucciones del juego: Rellena cada campo de texto con lo que se pide antes de que el temporizador llegue a 0.")
        layout.addWidget(instructions_label)
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("¡STOP!")
        self.setFixedSize(QSize(500, 300))

        layout = QVBoxLayout()

        self.name_label = QLabel("Nombre:")
        self.name_input1 = QLineEdit()    
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input1)
    
        self.surname_label = QLabel("Apellido:")
        self.surname_input1 = QLineEdit()
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input1)

        self.fruit_label = QLabel("Fruta:")
        self.fruit_input1 = QLineEdit()
        layout.addWidget(self.fruit_label)
        layout.addWidget(self.fruit_input1)

        self.country_label = QLabel("País:")
        self.country_input = QLineEdit()
        layout.addWidget(self.country_label)
        layout.addWidget(self.country_input)

        self.animal_label = QLabel("Animal:")
        self.animal_input = QLineEdit()
        layout.addWidget(self.animal_label)
        layout.addWidget(self.animal_input)

        self.object_label = QLabel("Objeto:")
        self.object_input = QLineEdit()
        layout.addWidget(self.object_label)
        layout.addWidget(self.object_input)

        self.time_remaining_label = QLabel('Tiempo restante: ')
        layout.addWidget(self.time_remaining_label)
        self.time_remaining = 10 #Para cambiar el tiempo
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(1000)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_timeout(self):
        # Actualizar el tiempo restante
        self.time_remaining -= 1
        if self.time_remaining == 0:
            # Acción a realizar cuando el tiempo se agota
            print('¡STOP!')
            # Detener el temporizador
            self.timer.stop()
            return

         # Actualizar la etiqueta con el tiempo restante
        mins, secs = divmod(self.time_remaining, 60)
        timer_text = '{:02d}:{:02d}'.format(mins, secs)
        self.time_remaining_label.setText(f"Tiempo restante: {timer_text}")

app = QApplication(sys.argv)
instructions_dialog = InstructionsDialog()
if instructions_dialog.exec() == QDialog.DialogCode.Accepted:
    window = MainWindow()
    window.show()
    app.exec()
