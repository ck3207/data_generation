# -*- coding: utf-8 -*-
__author__ = "chenk"
import  json, os, sys
import  logging

# from ..py import log.setup_logging
import pymysql
from conf.log import setup_logging

class Connect_mysql:
    """Get Configuration and Connect to Mysql!"""
    def __init__(self):
        setup_logging()

    def get_config(self, file_name="config"):
        """Get Configuration!"""
        with open(file_name, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config

    def conn_mysql(self, host, port, user, password, database, charset="utf8"):
        """Connetct to Mysql."""
        logger = logging.getLogger(self.__class__.__name__)
        try:
            conn = pymysql.connect(host=host, port=port, user=user, password=password,  database=database, charset=charset)
            cur = conn.cursor()
            return conn, cur
        except Exception as e:
            logger.info('Connect to mysql Error!')
            logger.error(e)

    def disconnect(self, conn, cur):
        cur.close()
        conn.close()

connect_mysql = Connect_mysql()
mysql_config = connect_mysql.get_config("../conf/mysql_config.json")
conn, cur = connect_mysql.conn_mysql(host=mysql_config["localhost_cf_test"]["host"], port=mysql_config["localhost_cf_test"]["port"],\
                         user=mysql_config["localhost_cf_test"]["user"], password=mysql_config["localhost_cf_test"]["password"], \
                        database=mysql_config["localhost_cf_test"]["database"], charset=mysql_config["localhost_cf_test"]["charset"])


