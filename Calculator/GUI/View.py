from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora (PySide6)")
        self.setFixedSize(300, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)

        self.layout.addWidget(self.display)

        self.buttons = {}
        self._create_buttons()

    def _create_buttons(self):
        grid = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(60, 60)
            grid.addWidget(btn, row, col)
            self.buttons[text] = btn

        self.layout.addLayout(grid)

    def set_display(self, text: str):
        self.display.setText(text)