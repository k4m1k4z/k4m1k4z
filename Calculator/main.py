import sys

from PySide6.QtWidgets import QApplication

from GUI.CalculatorMainWindow import CalculatorController
from GUI.Model import CalculatorModel
from GUI.View import CalculatorView
from logs.logger_config  import get_logger

if __name__ == "__main__":
    app = QApplication(sys.argv)

    logger = get_logger("calculator")

    model = CalculatorModel(logger)
    view = CalculatorView()
    controller = CalculatorController(model, view,logger)

    logger.info("Aplicación iniciada:")

    view.show()
    sys.exit(app.exec())