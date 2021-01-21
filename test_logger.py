import logging

def test_logcreation():
    logger = logging.getLogger(__name__)

    filehandle = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandle.setFormatter(formatter)
    logger.addHandler(filehandle)   # File handler object

    logger.setLevel(logging.INFO)

    logger.debug("This is to know for debugging")
    logger.info("This log for information only")
    logger.warning("This is only warning message")
    logger.error("There is an error occurs")
    logger.critical("There is some Critical error in the system")