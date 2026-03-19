# Será mi clase que va a tener un método para poder añadir a log
import logging
import os
import traceback

class Logger():

    @classmethod
    def __set_logger(cls):
        base_dir = os.path.dirname(os.path.abspath(__file__)) # para  ruta absoluta y no la relativa
        log_directory = os.path.join(base_dir, 'logs') # cogemos la ruta absoluta
        log_filename = 'app.log'

        # 🔥 Crear carpeta si no existe
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)

        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            "%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)
        return logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger()

            if level == "critical":
                logger.critical(message)
            elif level == "debug":
                logger.debug(message)
            elif level == "error":
                logger.error(message)
            elif level == "info":
                logger.info(message)
            elif level == "warn":
                logger.warning(message)

        except Exception as ex:
            print(traceback.format_exc())
            print(ex)




