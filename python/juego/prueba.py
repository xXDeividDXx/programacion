import sys
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QPalette, QColor, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("el stop")
        self.setFixedSize(QSize(500, 400))
        layout = QGridLayout()

        categories = ["¡STOP!", "Apellido:", "País:", "Objeto:", "Fruta:", "Animal:"]
        self.input_fields = {}

        for col, category in enumerate(categories):
            label = QLabel(category)
            layout.addWidget(label, 0, col)
            
            input_row = []
            for row in range(1, 9):
                input_field = QLineEdit()
                input_row.append(input_field)
                layout.addWidget(input_field, row, col)

            self.input_fields[category] = input_row

        self.time_remaining_label = QLabel('Tiempo restante:')
        layout.addWidget(self.time_remaining_label, 9, 0, 1, len(categories))
        
        self.time_remaining = 60  # Cambiar el tiempo
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(1000)

        self.stop_label = QLabel("")
        layout.addWidget(self.stop_label, 10, 0, 1, len(categories))
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_timeout(self):
        self.time_remaining -= 1
        if self.time_remaining == 0:
            print('¡Tiempo agotado!')
            self.timer.stop()

            font = QFont()
            font.setPointSize(24)
            self.stop_label.setFont(font)

            palette = QPalette()
            palette.setColor(QPalette.ColorRole.WindowText, QColor(Qt.GlobalColor.red))
            self.stop_label.setPalette(palette)
            self.stop_label.setText("¡STOP!")

            return

        mins, secs = divmod(self.time_remaining, 60)
        timer_text = '{:02d}:{:02d}'.format(mins, secs)
        self.time_remaining_label.setText(f"Tiempo restante: {timer_text}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
