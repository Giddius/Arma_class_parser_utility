"""parsing ArmA 3 config dump"""

__version__ = '0.1'

import gidlogger as glog
from dotenv import load_dotenv, find_dotenv
import os
import multiprocessing_logging

if os.path.isfile(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\tools\_project_devmeta.env"):
    load_dotenv(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\tools\_project_devmeta.env")

log_file = glog.log_folderer(__name__)
log = glog.main_logger(log_file, in_level='debug', log_to='stdout')


multiprocessing_logging.install_mp_handler()
