import logging


class LoggingSetup:
    """
    this function is to call the setUp in every page rather the building it everytime.
    """
    # logging.basicConfig(filename='../final_project.log', level=logging.INFO,
    #                     format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')

    logging.basicConfig(
        filename='../test_log.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )