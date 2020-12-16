import logging
import datetime

class Logger():
    mylogger = logging.getLogger("EcountAutoRegister")
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)

    file_handler = logging.FileHandler('log/nohup.log', encoding="utf-8")
    mylogger.addHandler(file_handler)


    @classmethod
    def info(self, msg):
        self.mylogger.info(msg)

    @classmethod
    def warn(self, msg):
        self.mylogger.warn(msg)
        
    @classmethod
    def error(self, msg):
        self.mylogger.error(msg)
    
    @classmethod
    def debug(self, msg):
        self.mylogger.debug(msg)
