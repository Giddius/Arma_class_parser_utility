# region [Imports]

# *NORMAL Imports -->
import time
import sys
import timeit
import statistics
from pprint import pprint, pformat
import subprocess
from functools import partial
from gidtools.gidfiles.classes import QuickFile
from gidtools.gidfiles.functions import writejson
from gidtools.gidfiles import ext_splitter, splitoff, pathmaker
# *GID Imports -->

from gidtools.gidtriumvirate import GidSQLBuilder

import gidlogger as glog

# *QT Imports -->

# * Local Imports -->
from arma_class_parser_classes import DictHandler, MasterSorterHolder
from arma_class_parser_DATA import ALL_CFG_SECTIONS
from arma_class_parser_misc import ACPImageFinder, FileIndexer

# endregion [Imports]

__updated__ = '2020-09-05 22:38:48'


n_round = partial(round, ndigits=2)


# region [Logging]

_log_file = glog.log_folderer('__main__')
log = glog.main_logger(_log_file, 'info')
log.info(glog.NEWRUN())

# endregion [Logging]


# region [Constants]


# endregion [Constants]


# region [Misc]


# endregion [Misc]

# region [Global_Functions]

def transform_time(in_t0, in_t1):
    _minutes = (in_t1 - in_t0) // 60
    _minutes = str(_minutes).split('.')[0]
    _seconds = (in_t1 - in_t0) - (int(_minutes) * 60)
    _seconds = str(_seconds).split('.')[0]

    log.critical(f" Initialization of the Database was completed in [{_minutes}] minutes and [{_seconds}] seconds!")

# endregion [Global_Functions]


# region [Class_1]
def transform_paa(full_path):
    _out_path = "D:/Dropbox/hobby/Modding/Programs/Github/My_Repos/Arma_class_parser_utility/arma_class_parser/ressources/paa_conversions"
    _old = full_path
    _dir, _file = splitoff(full_path)
    _basefile = ext_splitter(_file)
    _new = pathmaker(_out_path, _basefile + '.png')
    _command = r'"C:\Program Files (x86)\Steam\steamapps\common\Arma 3 Tools\ImageToPAA\ImageToPAA.exe"' + ' ' + _old + ' ' + _new
    _cmd = subprocess.run(_command, check=False, shell=True, capture_output=True)
    log.debug(pformat(_cmd.stdout))

# endregion [Class_1]

# region [DB_Creation]


def create_db():
    indexer = FileIndexer(['c:/', 'd:/'])
    _out = QuickFile()
    _out.write(indexer.paths, pretty=True)
    t0 = time.time()
    cfg_content = DictHandler()
    DBbuilder = GidSQLBuilder()
    DB = DBbuilder.database
    DB.start_db()
    # DB.executor.enable_row_factory()
    maincheese = MasterSorterHolder(cfg_content)

    for sections in ALL_CFG_SECTIONS:
        if sections in ALL_CFG_SECTIONS:
            print("working on " + sections)
            _tabler = maincheese.get_new_tabler(sections)
            _tabler.to_db(DB)

    DB.executor.vacuum()
    DB.executor.vacuum()
    t1 = time.time()
    transform_time(t0, t1)

# endregion [DB_Creation]


# region [Main_Exec]

if __name__ == '__main__':
    create_db()

# endregion [Main_Exec]
