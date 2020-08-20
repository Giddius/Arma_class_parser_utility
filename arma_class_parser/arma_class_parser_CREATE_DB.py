# region [Imports]

# *NORMAL Imports -->
import time
import sys
import timeit
import statistics

from functools import partial
# *GID Imports -->

from gidtools.gidtriumvirate import GidSQLBuilder

import gidlogger as glog

# *QT Imports -->

# * Local Imports -->
from arma_class_parser_classes import DictHandler, MasterSorterHolder
from arma_class_parser_DATA import ALL_CFG_SECTIONS
from arma_class_parser_misc import ACPImageFinder

# endregion [Imports]

__updated__ = '2020-08-14 20:03:37'

# region [Localized_Imports]
n_round = partial(round, ndigits=2)

# endregion [Localized_Imports]


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


# endregion [Class_1]

# region [DB_Creation]
def create_db():
    t0 = time.time()
    cfg_content = DictHandler()
    DB = GidSQLBuilder.get_databaser()
    DB.start_db()
    # DB.executor.enable_row_factory()
    maincheese = MasterSorterHolder(cfg_content)

    for sections in ALL_CFG_SECTIONS:
        _tabler = maincheese.get_new_tabler(sections)
        _tabler.to_db(DB)
        # _image = ACPImageFinder(sections, DB)

    DB.executor.vacuum()
    DB.executor.vacuum()
    t1 = time.time()
    transform_time(t0, t1)

# endregion [DB_Creation]


# region [Main_Exec]

if __name__ == '__main__':
    try:
        TT = timeit.Timer(create_db)
        _comb = []
        _1 = n_round(TT.timeit(number=1))

        _comb.append(_1)
        _2 = n_round(TT.timeit(number=1))

        _comb.append(_2)
        _3 = n_round(TT.timeit(number=1))

        _comb.append(_3)
        _4 = n_round(TT.timeit(number=1))

        _comb.append(_4)
        _5 = n_round(TT.timeit(number=1))
        _comb.append(_5)

        _6 = n_round(TT.timeit(number=1))
        _comb.append(_6)

        _7 = n_round(TT.timeit(number=1))
        _comb.append(_7)

        _8 = n_round(TT.timeit(number=1))
        _comb.append(_8)

        _9 = n_round(TT.timeit(number=1))
        _comb.append(_9)

        _10 = n_round(TT.timeit(number=1))
        _comb.append(_10)

        with open('time_results.txt', 'w') as resultfile:
            resultfile.write('from_list results:\n\n')
            resultfile.write(f"        {_comb[0]}\n")
            resultfile.write(f"        {_comb[1]}\n")
            resultfile.write(f"        {_comb[2]}\n")
            resultfile.write(f"        {_comb[3]}\n")
            resultfile.write(f"        {_comb[4]}\n")
            resultfile.write(f"        {_comb[5]}\n")
            resultfile.write(f"        {_comb[6]}\n")
            resultfile.write(f"        {_comb[7]}\n")
            resultfile.write(f"        {_comb[8]}\n")
            resultfile.write(f"        {_comb[9]}\n")
            resultfile.write('-------------------------------\n\n')
            resultfile.write(f"lowest = {min(_comb)}\n")
            resultfile.write(f"mean = {round(statistics.mean(_comb),3)}\n")
            resultfile.write(f"median = {round(statistics.median(_comb),3)}\n")
            resultfile.write(f"std_dev = {round(statistics.stdev(_comb),3)}\n")
            resultfile.write(f"variance = {round(statistics.variance(_comb),5)}\n")
            resultfile.write(f"mode = {round(statistics.mode(_comb),3)}\n")
            resultfile.write(f"median_grouped = {round(statistics.median_grouped(_comb),3)}\n")
            resultfile.write('###############################\n\n\n')
    except:
        log.exception(sys.exc_info()[0])
        raise

# endregion [Main_Exec]
