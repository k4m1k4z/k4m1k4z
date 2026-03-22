

class CalculatorModel:
    def __init__(self,logger=None):
        self.expression = ""
        self.logger = logger

    def append(self, value: str):
        self.expression += value

    def clear(self):
        self.expression = ""

    def evaluate(self) -> str:
        try:
            result = str(eval(self.expression))
            self.expression = result
            return result
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error en evaluación: {e}")
            self.expression = ""
            return "Error"