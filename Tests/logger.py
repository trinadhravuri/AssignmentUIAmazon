import logging
import time



class Logger():
    def __init__(self,logger,file_level = logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        frmt = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')

        curr_time = time.strftime('%Y_%m-%d')

        self.LogFileName = '../Logs/Log'+curr_time+'.txt'

        fh = logging.FileHandler(self.LogFileName, mode='w')

        fh.setFormatter(frmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)