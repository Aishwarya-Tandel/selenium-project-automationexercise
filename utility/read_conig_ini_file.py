import os
from configparser import RawConfigParser


conf = RawConfigParser()
conf.read(os.path.abspath(os.curdir) + "/configuration/config.ini")

class ReadConfig:
    @staticmethod
    def get_file_upload_path():
        file_path = (conf.get("CommonInfo" , "file_upload_path_1"))
        return file_path