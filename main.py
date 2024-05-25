from influxdb import InfluxDBClient
import logging
import logging.handlers
import Constant
import os

LOGGER = None

def configure_log():
    global LOGGER
    try:
        if not os.path.exists(Constant.PATH_LOG + '/log/'):
            os.makedirs(Constant.PATH_LOG  + '/log/')
        handler = logging.handlers.TimedRotatingFileHandler(filename=Constant.PATH_LOG + '/log/base.log',
                                                            when='D',
                                                            interval=1,
                                                            backupCount=14)
        logging.basicConfig(handlers=[handler],
                            level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s',
                            datefmt='%Y/%m/%d %H:%M:%S')
        LOGGER = logging.getLogger()
    except Exception as e:
        print("Logging Configuration ERROR : ", e)

if __name__ == '__main__':
    configure_log()