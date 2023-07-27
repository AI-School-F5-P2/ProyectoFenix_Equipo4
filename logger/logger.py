import logging
import os

def log_info(info) -> None:

    archivo = r"basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.info(info)

    os.chmod(archivo, 0o444)


def log_debug(bug) -> None:

    archivo = r"basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.debug(bug)

    os.chmod(archivo, 0o444)

def log_error(error) -> None:

    archivo = r"basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.error(error)

    os.chmod(archivo, 0o444)

def log_warning(warning) -> None:

    archivo = r"basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.warning(warning)

    os.chmod(archivo, 0o444)

def log_critical(critical) -> None:

    archivo = r"basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.critical(critical)
    
    os.chmod(archivo, 0o444)

