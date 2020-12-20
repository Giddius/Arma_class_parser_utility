

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
import hashlib
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
import armaclass

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
from arma_class_parser.extraction.subcfg_processing import SubCfgHolder
from arma_class_parser.utility.decorators import debug_timing_log

# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [AppUserData]


# endregion [AppUserData]

# region [Logging]

log = glog.aux_logger(__name__)


# endregion[Logging]

# region [Constants]


# endregion[Constants]


class ConfigDataHolder:
    save_location = 'config_data_holder.pkl'
    cfg_excludes = ["CfgMovesFishes_F",
                    "CfgMovesSharks_F",
                    "CfgMovesRabbit_F",
                    "CfgMovesSnakes_F",
                    "CfgMovesTurtle_F",
                    "CfgMovesHen_F",
                    "CfgMovesCock_F",
                    "CfgMovesDog_F",
                    "CfgMovesGoat_F",
                    "CfgMovesSheep_F",
                    "CfgMovesAnimal_Base_F",
                    "CfgMovesMaleSdr",
                    "CfgMovesWomen",
                    "CfgMovesMaleSdr_TC3",
                    "CfgMovesMaleSdr_TC4",
                    "CfgMovesAnimalsBase",
                    "CfgMovesDog"]

    def __init__(self, config_file):
        self.config_file = config_file
        self.raw_content = self._read_content()
        self.parsed_content = self._parse_content()

        self.hash = self._hash_config_file()
        self.cfg_names = self._get_cfg_names()
        self.cfg_pairs = self.cfg_name_pairs()
        self.serialize()
        glog.class_init_notification(log, self)

    def _get_cfg_names(self):
        _out = []
        for key in self.parsed_content:
            if key.casefold().startswith('cfg'):
                # if key not in self.cfg_excludes:
                _out.append(key)
        return _out

    @classmethod
    def set_save_location(cls, path, filename='config_data_holder.pkl'):
        if os.path.isdir(path) is False:
            os.makedirs(path)
        cls.save_location = pathmaker(path, filename)

    @debug_timing_log(log)
    def cfg_name_pairs(self):
        _out = []
        all_names = list(self.parsed_content)
        amount_items = len(all_names)
        for index, key in enumerate(all_names):
            if index < (amount_items - 1):
                _out.append((key, all_names[index + 1]))
            else:
                _out.append((key, None))
        return _out

    @debug_timing_log(log)
    def _hash_config_file(self):
        return hashlib.md5(bytes(self.raw_content, 'utf-8')).hexdigest()

    @debug_timing_log(log)
    def _read_content(self):
        return readit(self.config_file, in_encoding='utf-8')

    @debug_timing_log(log)
    def _parse_content(self):
        _out = {}
        parsed_config = armaclass.parse(self.raw_content)
        if "bin\\config.bin" in parsed_config:
            for key, value in parsed_config.items():
                for subkey, subvalue in value.items():
                    _out[subkey] = subvalue
        else:
            _out = parsed_config
        return _out

    @debug_timing_log(log)
    def serialize(self):
        pickleit(self, self.save_location)

    @classmethod
    def unserialize(cls):
        return get_pickled(cls.save_location)

    @classmethod
    def checked_init(cls, config_file):
        if os.path.exists('config_data_holder.pkl'):
            pickled_holder = get_pickled(cls.save_location)
            if pickled_holder.hash == hashlib.md5(bytes(readit(config_file), 'utf-8')).hexdigest():
                return pickled_holder
        return cls(config_file)

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.config_file})"

# region[Main_Exec]


if __name__ == '__main__':
    pass
# endregion[Main_Exec]
