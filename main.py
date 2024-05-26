import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS 
import logging
import logging.handlers
import Constant
import os, time

LOGGER = None
INFLUX_CLIENT = None

def init_influxdb():
    global INFLUX_CLIENT
    try:
        INFLUX_CLIENT  = influxdb_client.InfluxDBClient(
            url=Constant.INFLUX_HOST, 
            token=Constant.INFLUX_TOKEN,
            org=Constant.INFLUX_USERNAME)
        
        LOGGER.info(("Succes init influx db"))
    except Exception as e:
        LOGGER.warning(("Failed init infludxdb with errror" + str(e)))
        
def configure_log():
    global LOGGER
    try:
        if not os.path.exists(Constant.PATH_LOG + '/log/'):
            os.makedirs(Constant.PATH_LOG  + '/log/')
        handler = logging.handlers.TimedRotatingFileHandler(filename=Constant.PATH_LOG + '/log/base.log',
                                                            when='MIDNIGHT',
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
    init_influxdb()
    
    write_api = INFLUX_CLIENT.write_api(write_options=SYNCHRONOUS)
    bucket = "prayogo"
    for value in range(5):
        point = (
            Point("measurement1")
            .tag("tagname1", "tagvalue1")
            .field("field1", value)
        )
        write_api.write(bucket=bucket, org="prayogo", record=point)
        time.sleep(5) # separate points by 1 second
