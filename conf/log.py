#!encoding:utf-8
import json, time
import logging.config
import os

def setup_logging(
    default_path='logging.json', 
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def format_tumple(attention, argues):
    for i in range(len(argues)):
        attention = attention + " %s,"
    return attention[:-1]


def test():
    # setup_logging()
    logger = logging.getLogger(__name__)    #当前py文件名
    logger = logging.getLogger(test.__name__)   #当前函数名

    count = 1000
    while count:
        logger.info("It has run %d times" % count)
        logger.info("Current Time: %s" % get_time())
        #print(count,os.getcwd())
        count -= 1
        time.sleep(1)

class Test:
    def test(self):
        logger = logging.getLogger(self.__class__.__name__) #当前类中函数名

#获取当前时间
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



setup_logging()

