import sys
import random
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QPalette, QColor, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGridLayout, QWidget, QSpacerItem, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Juego del STOP")
        self.setFixedSize(QSize(700, 500))
        layout = QGridLayout()

        self.name_label = QLabel("¡STOP!")
        layout.addWidget(self.name_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.categories = ["Nombre", "Apellido", "Fruta", "País", "Animal", "Objeto"]
        self.inputs = []

        for row, category in enumerate(self.categories, start=1):
            label = QLabel(category + ":")
            layout.addWidget(label, row, 0)

            input_line = QLineEdit()
            layout.addWidget(input_line, row, 1)
            self.inputs.append(input_line)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer, len(self.categories) + 1, 0, 1, 2)

        self.time_remaining_label = QLabel('Tiempo restante:')
        layout.addWidget(self.time_remaining_label, len(self.categories) + 2, 0, 1, 2)

        self.time_remaining = 10
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(1000)

        self.stop_label = QLabel("")
        layout.addWidget(self.stop_label, len(self.categories) + 3, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_timeout(self):
        self.time_remaining -= 1
        if self.time_remaining == 0:
            self.timer.stop()
            self.stop_label.setStyleSheet("color: red; font-size: 24px;")
            self.stop_label.setText("¡STOP!")
            return

        mins, secs = divmod(self.time_remaining, 60)
        timer_text = '{:02d}:{:02d}'.format(mins, secs)
        self.time_remaining_label.setText(f"Tiempo restante: {timer_text}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())