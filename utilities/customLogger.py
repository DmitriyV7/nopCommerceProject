import logging

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        #logging.info("root")
        logging.basicConfig(filename='.\\Logs\\test.log', level=logging.DEBUG,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        return logger
