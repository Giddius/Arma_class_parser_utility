

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
from time import time
import traceback
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
from arma_class_parser.utility.exceptions import ContentFilterNoneError
from arma_class_parser.utility.decorators import debug_timing_log
from arma_class_parser.extraction.cfg_mapping import get_entry_tuple
# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [AppUserData]


# endregion [AppUserData]

# region [Logging]

log = glog.aux_logger(__name__)


# endregion[Logging]

# region [Constants]

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))

# endregion[Constants]


class SubCfgHolder:
    @debug_timing_log(log)
    def __init__(self, sub_cfg_name, next_sub_cfg_name, raw_content, parsed_content):
        self.cfg_entry = get_entry_tuple(sub_cfg_name)
        self.sub_cfg_name = sub_cfg_name
        self.next_sub_cfg_name = next_sub_cfg_name
        self.parsed_content = parsed_content
        self.filter_regex = re.compile(f"class {self.sub_cfg_name}\n.*?(?=class {self.next_sub_cfg_name}\n)", re.DOTALL) if self.next_sub_cfg_name is not None else re.compile(f"class {self.sub_cfg_name}\n.*", re.DOTALL)
        self.filtered_raw_content = self._filter_raw_content(raw_content)

        self.items = []
        self.child_parent_map = self._mmake_child_parent_map()
        glog.class_init_notification(log, self, use='str')

    def _filter_raw_content(self, content):
        _result = self.filter_regex.search(content)

        if _result:
            return [line for line in _result.group().splitlines() if all(indicator_word in line for indicator_word in ['class', ':'])]

        else:
            # raise ContentFilterNoneError(self.sub_cfg_name, self.next_sub_cfg_name)
            return [line for line in content.splitlines() if all(indicator_word in line for indicator_word in ['class', ':'])]

    # def _helper_generator_child_parent(self):
    #     for line in self.filtered_raw_content.splitlines():
    #         if all(indicator_word in line for indicator_word in ['class', ':']):
    #             yield line

    def _find_parent(self, classname):
        if classname == 'MuzzleSlot':
            return
        regex = re.compile(f"(?<=class {classname})" + r"\:\s+(?P<parent>.*)")
        for line in self.filtered_raw_content:
            _result = regex.search(line)

            if _result:
                return classname, _result.groupdict().get('parent')

        return classname, None

    # def _find_parent(self, classname):
    #     for line in self.filtered_raw_content.splitlines():
    #         if f"class {classname}: " in line:
    #             parent = line.split(': ')[-1]
    #             return classname, parent
    #     return classname, None

    # def _find_parent(self, classname):
    #     regex = re.compile(f"(?<=class {classname})" + r"\:\s+(?P<parent>.*)")
    #     _result = regex.search(self.filtered_raw_content)
    #     if _result:
    #         return classname, _result.groupdict().get('parent')
    #     else:
    #         return classname, None

    def item_names(self, to_set=False):
        _out = [key for key in self.parsed_content]
        if to_set is True:
            _out = set(_out)
        return _out

    def _get_from_parent(self, classname, attribute_name):
        if classname is None or classname in ['MuzzleSlot', 'Default', 'Combo', 'ACE_Box_82mm_Mo_Combo']:
            return

        try:
            _out = self.parsed_content[classname].get(attribute_name, None)

            if _out is None:
                parent = self.child_parent_map.get(classname)
                if parent:
                    return self._get_from_parent(parent, attribute_name)
            return _out
        except RecursionError:
            return

    @lru_cache
    def _get_typus(self, classname):

        if classname is None or classname in ['MuzzleSlot', 'StepScope', 'Combo', 'ACE_Box_82mm_Mo_Combo']:
            return
        if 'Core' in classname or classname in ['All', 'Default']:
            return classname
        else:
            try:
                return self._get_typus(self.child_parent_map.get(classname))
            except RecursionError as error:
                log.critical("RecursionError with '%s'", classname)
                return

    @debug_timing_log(log)
    def _make_child_parent_map(self):

        _out = {}
        for key in self.parsed_content:
            if key != 'access':
                _out[key] = self._find_parent(key)[1]
        return _out

    @debug_timing_log(log)
    def _mmake_child_parent_map(self):
        log.debug('mapping child_parent for "%s"', str(self))
        _out = {}
        with ProcessPoolExecutor(25) as pool:
            key_list = [key for key in self.parsed_content if key != 'access']
            for classname, parent in pool.map(self._find_parent, key_list, chunksize=max(10, len(key_list) // 25)):
                _out[classname] = parent
        return _out

    @debug_timing_log(log)
    def make_items(self):

        for key in self.parsed_content:
            if key not in ['access', 'Combo', 'ACE_Box_82mm_Mo_Combo']:

                classname = key
                parent = self._find_parent(key)
                displayName = self.parsed_content[key].get('displayName', self._get_from_parent(parent, 'displayName'))
                scope = self.parsed_content[key].get('scope', self._get_from_parent(parent, 'scope'))
                author = self.parsed_content[key].get('author', self._get_from_parent(parent, 'author'))
                picture = self.parsed_content[key].get('picture', self._get_from_parent(parent, 'picture'))
                model = self.parsed_content[key].get('model', self._get_from_parent(parent, 'model'))
                UiPicture = self.parsed_content[key].get('UiPicture', self._get_from_parent(parent, 'UiPicture'))
                hiddenSelections = self.parsed_content[key].get('hiddenSelections', self._get_from_parent(parent, 'hiddenSelections'))
                descriptionShort = self.parsed_content[key].get('descriptionShort', self._get_from_parent(parent, 'descriptionShort'))
                typus = self._get_typus(parent)
                self.items.append(self.cfg_entry(classname, parent, displayName, scope, author, picture, model, UiPicture, hiddenSelections, descriptionShort, typus))

    def _helper_mmake_items(self, classname):
        _att_dict = {'classname': classname, 'parent': self.child_parent_map.get(classname, None)}
        for att_name in self.cfg_entry._fields:
            if att_name not in ['typus', 'classname', 'parent']:
                _att_dict[att_name] = self.parsed_content[classname].get(att_name, self._get_from_parent(_att_dict['parent'], att_name))
            elif att_name == 'typus':
                _att_dict[att_name] = self._get_typus(classname)

        return self.cfg_entry(**_att_dict)

    @debug_timing_log(log)
    def mmake_items(self):
        log.debug('making items for "%s"', str(self))
        with ProcessPoolExecutor(12) as pool:
            key_list = [key for key in self.parsed_content if key != 'access']
            results = pool.map(self._helper_mmake_items, key_list, chunksize=max(10, len(key_list) // 12))
            for result in results:
                self.items.append(result)

    def __str__(self):
        return f"{self.__class__.__name__}({self.sub_cfg_name})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.sub_cfg_name}, {self.next_sub_cfg_name})"

# region[Main_Exec]


if __name__ == '__main__':
    pass

# endregion[Main_Exec]
