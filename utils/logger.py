import logging
import os

# Ruta absoluta del archivo log
log_file = os.path.join(os.getcwd(), "test.log")

# Crear logger
logger = logging.getLogger("api_tests")
logger.setLevel(logging.INFO)

# Evitar duplicación de handlers
if not logger.handlers:
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)