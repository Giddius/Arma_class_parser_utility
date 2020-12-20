

# region [Imports]

# * Standard Library Imports -->

import asyncio
import gc
import os
import re
import sys
import json
import lzma
import time
import queue
import platform
import subprocess
from enum import Enum, Flag, auto
from time import sleep
from pprint import pprint, pformat
from typing import Union
from datetime import tzinfo, datetime, timezone, timedelta
from functools import wraps, lru_cache, singledispatch, total_ordering, partial
from contextlib import contextmanager
from collections import Counter, ChainMap, deque, namedtuple, defaultdict
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import traceback
import shutil
# * Third Party Imports -->

# import requests
# import pyperclip
# import matplotlib.pyplot as plt
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# from github import Github, GithubException
# from jinja2 import BaseLoader, Environment
# from natsort import natsorted
# from fuzzywuzzy import fuzz, process


# * PyQt5 Imports -->

# from PyQt5.QtGui import QFont, QIcon, QBrush, QColor, QCursor, QPixmap, QStandardItem, QRegExpValidator
# from PyQt5.QtCore import (Qt, QRect, QSize, QObject, QRegExp, QThread, QMetaObject, QCoreApplication,
#                           QFileSystemWatcher, QPropertyAnimation, QAbstractTableModel, pyqtSlot, pyqtSignal)
# from PyQt5.QtWidgets import (QMenu, QFrame, QLabel, QDialog, QLayout, QWidget, QWizard, QMenuBar, QSpinBox, QCheckBox, QComboBox,
#                              QGroupBox, QLineEdit, QListView, QCompleter, QStatusBar, QTableView, QTabWidget, QDockWidget, QFileDialog,
#                              QFormLayout, QGridLayout, QHBoxLayout, QHeaderView, QListWidget, QMainWindow, QMessageBox, QPushButton,
#                              QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout, QWizardPage, QApplication, QButtonGroup, QRadioButton,
#                              QFontComboBox, QStackedWidget, QListWidgetItem, QTreeWidgetItem, QDialogButtonBox, QAbstractItemView,
#                              QCommandLinkButton, QAbstractScrollArea, QGraphicsOpacityEffect, QTreeWidgetItemIterator, QAction, QSystemTrayIcon)


# * Gid Imports -->

import gidlogger as glog
from gidtools.gidfiles import (QuickFile, readit, clearit, readbin, writeit, loadjson, pickleit, writebin, pathmaker, writejson,
                               dir_change, linereadit, get_pickled, ext_splitter, appendwriteit, create_folder, from_dict_to_file)


# * Local Imports -->
from arma_class_parser.extraction.cfg_processing import ConfigDataHolder
from arma_class_parser.extraction.subcfg_processing import SubCfgHolder

# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [AppUserData]


# endregion [AppUserData]

# region [Logging]

log = glog.aux_logger(__name__)


# endregion[Logging]

# region [Constants]
CONFIG_PATH_DICT = {
    "vanilla": "D:/Dropbox/hobby/Modding/Ressources/Templates/Config_dumb/diverse_config_dumps/vanilla/ALL_config_dump_vanilla.cpp",
    "rhs": "D:/Dropbox/hobby/Modding/Ressources/Templates/Config_dumb/diverse_config_dumps/RHS/ALL_config_dump_rhs_ace.cpp",
    "3cb": "D:/Dropbox/hobby/Modding/Ressources/Templates/Config_dumb/diverse_config_dumps/3CB/ALL_config_dump_rhs_ace_3CB.cpp",
}


OUTPUT_FOLDER = pathmaker(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\temp\temp_output")
INPUT_CONFIG_FILE = CONFIG_PATH_DICT.get('vanilla')
output_path = partial(pathmaker, OUTPUT_FOLDER)
CFG_TO_PROCESS = ['CfgWeapons',
                  'CfgVehicles',
                  'CfgUnitInsignia',
                  'CfgRanks',
                  'CfgVehicleClasses',
                  'CfgRoles',
                  'CfgMagazines',
                  'CfgAmmo',
                  'CfgEditorCategories',
                  'CfgEditorSubcategories',
                  'CfgFactionClasses',
                  'CfgGlasses']

# endregion[Constants]


def do_subs(cfg_namepack, holder):
    errored_cfg = ''
    y = SubCfgHolder(cfg_namepack[0], cfg_namepack[1], holder.raw_content, holder.parsed_content[cfg_namepack[0]])

    try:
        y.mmake_items()
    except AttributeError as error:
        log.error(error)
        log.critical('AttributeError error was with "%s"', cfg_namepack[0])
        errored_cfg = (str(error), traceback.format_exc().splitlines())
        appendwriteit('error.txt', "".join(traceback.format_exception(*sys.exc_info())) + '\n\n########\n\n')
    except KeyError as error:
        log.error(error)
        log.critical('KeyError error was with "%s"', cfg_namepack[0])
        errored_cfg = (str(error), traceback.format_exc().splitlines())
        appendwriteit('error.txt', "".join(traceback.format_exception(*sys.exc_info())) + '\n\n########\n\n')
    return y, errored_cfg


def main():
    _error_cfg = {}
    _sub_cfgs = []
    x = ConfigDataHolder.checked_init(INPUT_CONFIG_FILE)
    writejson(x.parsed_content, output_path('all_parsed_content.json'), sort_keys=False, indent=4)
    writejson(x.cfg_names, output_path('all_cfg_names.json'), sort_keys=False, indent=4)
    do_it = partial(do_subs, holder=x)
    for pack in x.cfg_pairs:
        if pack[0] not in x.cfg_excludes and pack[0].casefold().startswith('cfg'):
            if pack[0] in CFG_TO_PROCESS:
                cfg_instance, is_error = do_subs(pack, x)
                if not is_error:
                    writejson(cfg_instance.child_parent_map, output_path(f'{cfg_instance.sub_cfg_name}_child_parent_map.json'), sort_keys=False, indent=4)
                    writejson([item._asdict() for item in cfg_instance.items], output_path(f'{cfg_instance.sub_cfg_name}_items.json'), sort_keys=False, indent=4)
                    writejson(x.parsed_content[cfg_instance.sub_cfg_name], output_path(f'{cfg_instance.sub_cfg_name}_parsed_content.json'), sort_keys=False, indent=4)
                    writejson(cfg_instance.item_names(), output_path(f'{cfg_instance.sub_cfg_name}_item_names.json'), sort_keys=False, indent=4)
                else:
                    _error_cfg[cfg_instance.sub_cfg_name] = is_error
    # with ThreadPoolExecutor(len(CFG_TO_PROCESS)) as pool:
    #     results = pool.map(do_it, [pack for pack in x.cfg_pairs if pack[0].casefold() in CFG_TO_PROCESS])
    #     for result_item in results:
    #         if result_item[1] is False:
    #             y = result_item[0]
    #             writejson(y.child_parent_map, output_path(f'{y.sub_cfg_name}_child_parent_map.json'), sort_keys=False, indent=4)
    #             writejson(y.items, output_path(f'{y.sub_cfg_name}_items.json'), sort_keys=False, indent=4)
    #             writejson(x.parsed_content[y.sub_cfg_name], output_path(f'{y.sub_cfg_name}_parsed_content.json'), sort_keys=False, indent=4)
    #             writejson(y.item_names(), output_path(f'{y.sub_cfg_name}_item_names.json'), sort_keys=False, indent=4)
    #         else:
    #             _error_cfg.append(result_item[0].sub_cfg_name)
    writejson(_error_cfg, 'error_cfgs.json', sort_keys=False, indent=4)

# region[Main_Exec]


if __name__ == '__main__':
    shutil.rmtree(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\temp\temp_output")
    if os.path.exists(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\temp\temp_output") is False:
        os.makedirs(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\temp\temp_output")
    main()

# endregion[Main_Exec]
