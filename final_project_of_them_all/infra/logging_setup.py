import logging


class LoggingSetup:
    """
    This class configures the logging setup for the application.
    """

    def __init__(self):
        logging.basicConfig(
            filename='../final_project.log',  # Path to your log file
            level=logging.INFO,  # Set the logging level
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d/%m/%y %H:%M:%S'
        )
