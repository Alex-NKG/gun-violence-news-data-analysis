import logging
import traceback
import warnings

warnings.filterwarnings('ignore')


class record_bug:
    def __init__(self):
        logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def recordlog(self):
        logging.debug(traceback.format_exc())

    def msg_record(self, x):
        logging.debug(x)
