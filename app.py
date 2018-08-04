# -*- coding: utf-8 -*-
import os
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError



MONGODB_HOST = os.environ.get('MONGO_HOST', 'ds217351.mlab.com')
MONGODB_PORT = os.environ.get('MONGO_PORT',  17351)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'root')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'root12')
MONGODB_NAME = os.environ.get('MONGO_DBNAME', 'track_man')



class Conn(MongoClient):
    '''A singleton Wrapper over pymongo connection.
    We have this abstraction to avoid instantiating a mongo db connection on module import,
     as well as avoid instantiating too many connections in a single application.

    The underlying connection object is thread-safe as well as implements thread pooling.
    It also re-connects to database if the connection fails. That makes using a single connection
    throughout the application life possible.
    '''

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls._get_connection()

        return cls._instance

    @classmethod
    def _get_connection(self):
        ''' Creates a new Mongo DB connection object'''
        # TODO: Reach from settings file
        # mongodb: // root: root12 @ ds147118.mlab.com:47118 / selfship
        if MONGO_USERNAME and MONGO_PASSWORD:
            conn_string = 'mongodb://%s:%s@%s:%s/%s' % (
                MONGO_USERNAME, MONGO_PASSWORD, MONGODB_HOST, MONGODB_PORT,
                MONGODB_NAME)
        else:
            conn_string = 'mongodb://%s:%s/%s' % (MONGODB_HOST, MONGODB_PORT,
                                                  MONGODB_NAME)
        c = MongoClient(conn_string)[MONGODB_NAME]

        return c


class DuplicateEntry(DuplicateKeyError):
    pass



data = []
for i in Conn().new_requested_tracking_data.find({"slug": "delhivery"},{"_id":0,"tracking_number":1}):
    data.append(i.get('tracking_number'))
print(data)    
#for z in data:
#    Conn().new_requested_tracking_data.remove({"tracking_number":z})