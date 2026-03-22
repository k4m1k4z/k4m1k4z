from GUI.Model import CalculatorModel
from GUI.View import CalculatorView


class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView, logger):
        self.model = model
        self.view = view
        self.logger = logger

        self._connect_signals()

    def _connect_signals(self):
        for key, button in self.view.buttons.items():
            if key == "=":
                button.clicked.connect(self.calculate)
            elif key == "C":
                button.clicked.connect(self.clear)
            else:
                button.clicked.connect(lambda _, k=key: self.add(k))

    def add(self, value: str):
        self.logger.info(f"Botón pulsado: {value}")
        self.model.append(value)
        self.view.set_display(self.model.expression)

    def clear(self):
        self.logger.info("Acción: Clear")
        self.model.clear()
        self.view.set_display("")

    def calculate(self):
        self.logger.info(f"Evaluando: {self.model.expression}")
        result = self.model.evaluate()

        if result == "Error":
            self.logger.error("Error en cálculo")
        else:
            self.logger.info(f"Resultado: {result}")

        self.view.set_display(result)