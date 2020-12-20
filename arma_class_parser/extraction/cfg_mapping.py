

# region [Imports]

# * Standard Library Imports -->

import asyncio
import gc
import logging
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


CfgModsEntry = namedtuple('CfgModsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgExperienceEntry = namedtuple('CfgExperienceEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAISkillEntry = namedtuple('CfgAISkillEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAILevelPresetsEntry = namedtuple('CfgAILevelPresetsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDifficultyPresetsEntry = namedtuple('CfgDifficultyPresetsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDifficultiesEntry = namedtuple('CfgDifficultiesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgInventoryEntry = namedtuple('CfgInventoryEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCuratorEntry = namedtuple('CfgCuratorEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSteamSettingsEntry = namedtuple('CfgSteamSettingsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgBrainsEntry = namedtuple('CfgBrainsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgTextureToMaterialEntry = namedtuple('CfgTextureToMaterialEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMaterialsEntry = namedtuple('CfgMaterialsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgTLMaterialsEntry = namedtuple('CfgTLMaterialsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVehicleActionsEntry = namedtuple('CfgVehicleActionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWeaponCursorsEntry = namedtuple('CfgWeaponCursorsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMineTriggersEntry = namedtuple('CfgMineTriggersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAmmoEntry = namedtuple('CfgAmmoEntry', ['classname', 'parent', 'displayName', 'scope', 'author', 'model', 'hit', 'indirectHit',
                                           'indirectHitRange', 'explosive', 'autoSeekTarget'], defaults=(None, None, None, None, None, None, None, None, None, None))
CfgRecoilsEntry = namedtuple('CfgRecoilsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMagazinesEntry = namedtuple('CfgMagazinesEntry', ['classname', 'parent', 'displayName', 'scope', 'author', 'model', 'picture', 'displayNameShort',
                                                     'ammo', 'weight', 'count', 'initSpeed'], defaults=(None, None, None, None, None, None, None, None, None, None, None))
CfgWeaponsEntry = namedtuple('CfgWeaponsEntry', ['classname', 'parent', 'displayName', 'scope', 'author', 'picture', 'model', 'UiPicture',
                                                 'hiddenSelections', 'descriptionShort', 'typus'], defaults=(None, None, None, None, None, None, None, None, None, None))
CfgInventoryGlobalVariableEntry = namedtuple('CfgInventoryGlobalVariableEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDestroySoundsEntry = namedtuple('CfgDestroySoundsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCloudletsEntry = namedtuple('CfgCloudletsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgOpticsEffectEntry = namedtuple('CfgOpticsEffectEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDestructPosEntry = namedtuple('CfgDestructPosEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDamageAroundEntry = namedtuple('CfgDamageAroundEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLightsEntry = namedtuple('CfgLightsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgClothEntry = namedtuple('CfgClothEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVehicleClassesEntry = namedtuple('CfgVehicleClassesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFactionClassesEntry = namedtuple('CfgFactionClassesEntry', ['classname', 'parent', 'displayName', 'priority', 'side', 'icon', 'flag', 'genericNames'], defaults=(None, None, None, None, None, None, None))
CfgVehiclesEntry = namedtuple('CfgVehiclesEntry', ['classname', 'parent', 'displayName', 'scope', 'scopeCurator', 'author', 'model', 'editorCategory', 'editorSubcategory', 'vehicleClass', 'icon', 'editorPreview', 'picture', 'hiddenSelectionsTextures',
                                                   'destrType', 'faction', 'side', 'DLC', 'hiddenSelectionsMaterials', 'uniformClass', 'EventHandlers'], defaults=(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None))
CfgNonAIVehiclesEntry = namedtuple('CfgNonAIVehiclesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMarkedTargetsEntry = namedtuple('CfgMarkedTargetsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFSMsEntry = namedtuple('CfgFSMsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFatigueEntry = namedtuple('CfgFatigueEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFirstAidEntry = namedtuple('CfgFirstAidEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDivingEntry = namedtuple('CfgDivingEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgBleedingEntry = namedtuple('CfgBleedingEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgPriorityEntry = namedtuple('CfgPriorityEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSkeletonParametersEntry = namedtuple('CfgSkeletonParametersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgImprecisionEntry = namedtuple('CfgImprecisionEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgBreathingEntry = namedtuple('CfgBreathingEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWeaponHandlingEntry = namedtuple('CfgWeaponHandlingEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgPersonTurretEntry = namedtuple('CfgPersonTurretEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesBasicEntry = namedtuple('CfgMovesBasicEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgGesturesMaleEntry = namedtuple('CfgGesturesMaleEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSlopeLimitsEntry = namedtuple('CfgSlopeLimitsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAnimationEntry = namedtuple('CfgAnimationEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCollisionsEntry = namedtuple('CfgCollisionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSlingLoadingEntry = namedtuple('CfgSlingLoadingEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVoiceEntry = namedtuple('CfgVoiceEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVoiceTypesEntry = namedtuple('CfgVoiceTypesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCoreDataEntry = namedtuple('CfgCoreDataEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVehicleIconsEntry = namedtuple('CfgVehicleIconsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCloudletShapesEntry = namedtuple('CfgCloudletShapesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSaveThumbnailsEntry = namedtuple('CfgSaveThumbnailsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
cfgFormationsEntry = namedtuple('cfgFormationsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
cfgWaypointsEntry = namedtuple('cfgWaypointsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRagDollSkeletonsEntry = namedtuple('CfgRagDollSkeletonsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVideoOptionsEntry = namedtuple('CfgVideoOptionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSurfaceCharactersEntry = namedtuple('CfgSurfaceCharactersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSurfacesEntry = namedtuple('CfgSurfacesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundEnvironToControllersEntry = namedtuple('CfgSoundEnvironToControllersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDefaultSettingsEntry = namedtuple('CfgDefaultSettingsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgPatchesEntry = namedtuple('CfgPatchesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFontFamiliesEntry = namedtuple('CfgFontFamiliesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFontsEntry = namedtuple('CfgFontsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgEditCameraEntry = namedtuple('CfgEditCameraEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWrapperUIEntry = namedtuple('CfgWrapperUIEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgInGameUIEntry = namedtuple('CfgInGameUIEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
cfgGroupIconsEntry = namedtuple('cfgGroupIconsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgTaskTypesEntry = namedtuple('CfgTaskTypesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSimpleTasksEntry = namedtuple('CfgSimpleTasksEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDiaryEntry = namedtuple('CfgDiaryEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgActionsEntry = namedtuple('CfgActionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMissionsEntry = namedtuple('CfgMissionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRanksEntry = namedtuple('CfgRanksEntry', ['classname', 'parent', 'displayName', 'rank', 'displayNameShort', 'texture'], defaults=(None, None, None, None, None))
CfgDefaultKeysPresetsEntry = namedtuple('CfgDefaultKeysPresetsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDetectorsEntry = namedtuple('CfgDetectorsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFaceWoundsEntry = namedtuple('CfgFaceWoundsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgGlassesEntry = namedtuple('CfgGlassesEntry', ['classname', 'parent', 'displayName', 'scope', 'author', 'model', 'picture', 'mass', 'hiddenSelections'], defaults=(None, None, None, None, None, None, None, None))
CfgFacesEntry = namedtuple('CfgFacesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMimicsEntry = namedtuple('CfgMimicsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgEnvSoundsEntry = namedtuple('CfgEnvSoundsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgHQIdentitiesEntry = namedtuple('CfgHQIdentitiesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgHeadsEntry = namedtuple('CfgHeadsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMusicEntry = namedtuple('CfgMusicEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundsEntry = namedtuple('CfgSoundsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWhistleSoundEntry = namedtuple('CfgWhistleSoundEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgTitlesEntry = namedtuple('CfgTitlesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgIntroEntry = namedtuple('CfgIntroEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCreditsEntry = namedtuple('CfgCreditsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCutScenesEntry = namedtuple('CfgCutScenesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCameraEffectsEntry = namedtuple('CfgCameraEffectsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMarkersEntry = namedtuple('CfgMarkersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMarkerColorsEntry = namedtuple('CfgMarkerColorsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMarkerBrushesEntry = namedtuple('CfgMarkerBrushesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLocationTypesEntry = namedtuple('CfgLocationTypesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWorldsEntry = namedtuple('CfgWorldsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWorldListEntry = namedtuple('CfgWorldListEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgGroupsEntry = namedtuple('CfgGroupsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAddonsEntry = namedtuple('CfgAddonsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgEditorObjectsEntry = namedtuple('CfgEditorObjectsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMPGameTypesEntry = namedtuple('CfgMPGameTypesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLiveStatsEntry = namedtuple('CfgLiveStatsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAchievementsEntry = namedtuple('CfgAchievementsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVoiceMaskEntry = namedtuple('CfgVoiceMaskEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRumbleEntry = namedtuple('CfgRumbleEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
cfgBuldozerEntry = namedtuple('cfgBuldozerEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCameraShakeEntry = namedtuple('CfgCameraShakeEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLensFlareEntry = namedtuple('CfgLensFlareEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundEffectsEntry = namedtuple('CfgSoundEffectsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMineDetectionCoefsEntry = namedtuple('CfgMineDetectionCoefsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFireEntry = namedtuple('CfgFireEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgIRLaserSettingsEntry = namedtuple('CfgIRLaserSettingsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFunctionsEntry = namedtuple('CfgFunctionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRespawnTemplatesEntry = namedtuple('CfgRespawnTemplatesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgPostProcessTemplatesEntry = namedtuple('CfgPostProcessTemplatesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRemoteExecCommandsEntry = namedtuple('CfgRemoteExecCommandsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRemoteExecEntry = namedtuple('CfgRemoteExecEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCommandsEntry = namedtuple('CfgCommandsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgORBATDefaultEntry = namedtuple('CfgORBATDefaultEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSFXEntry = namedtuple('CfgSFXEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgEditorCategoriesEntry = namedtuple('CfgEditorCategoriesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgEditorSubcategoriesEntry = namedtuple('CfgEditorSubcategoriesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMuzzleFlashesEntry = namedtuple('CfgMuzzleFlashesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgBushNoMipmapTexturesEntry = namedtuple('CfgBushNoMipmapTexturesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgIdentitiesEntry = namedtuple('CfgIdentitiesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCuratorChallengesEntry = namedtuple('CfgCuratorChallengesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgHintCategoriesEntry = namedtuple('CfgHintCategoriesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgHintsEntry = namedtuple('CfgHintsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
Cfg3DENEntry = namedtuple('Cfg3DENEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgObjectCompositionsEntry = namedtuple('CfgObjectCompositionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCommunicationMenuEntry = namedtuple('CfgCommunicationMenuEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFiringDrillsEntry = namedtuple('CfgFiringDrillsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMusicClassesEntry = namedtuple('CfgMusicClassesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDestroyEntry = namedtuple('CfgDestroyEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesAnimalEntry = namedtuple('CfgMovesAnimalEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesButterflyEntry = namedtuple('CfgMovesButterflyEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesBirdEntry = namedtuple('CfgMovesBirdEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgTasksEntry = namedtuple('CfgTasksEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesAnimal_Base_FEntry = namedtuple('CfgMovesAnimal_Base_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesFishes_FEntry = namedtuple('CfgMovesFishes_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesSharks_FEntry = namedtuple('CfgMovesSharks_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesRabbit_FEntry = namedtuple('CfgMovesRabbit_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesSnakes_FEntry = namedtuple('CfgMovesSnakes_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesTurtle_FEntry = namedtuple('CfgMovesTurtle_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesHen_FEntry = namedtuple('CfgMovesHen_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesCock_FEntry = namedtuple('CfgMovesCock_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesDog_FEntry = namedtuple('CfgMovesDog_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesGoat_FEntry = namedtuple('CfgMovesGoat_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesSheep_FEntry = namedtuple('CfgMovesSheep_FEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesMaleSdrEntry = namedtuple('CfgMovesMaleSdrEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgCommunityGuideEntry = namedtuple('CfgCommunityGuideEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgUIColorsEntry = namedtuple('CfgUIColorsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgUIGridsEntry = namedtuple('CfgUIGridsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLanguagesEntry = namedtuple('CfgLanguagesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWeaponIconsEntry = namedtuple('CfgWeaponIconsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLoadingTextsEntry = namedtuple('CfgLoadingTextsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLoadingScreensEntry = namedtuple('CfgLoadingScreensEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgChainOfCommandEntry = namedtuple('CfgChainOfCommandEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgScriptPathsEntry = namedtuple('CfgScriptPathsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgEditorLayoutsEntry = namedtuple('CfgEditorLayoutsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgNotificationsEntry = namedtuple('CfgNotificationsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDebriefingEntry = namedtuple('CfgDebriefingEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDLCNotificationsEntry = namedtuple('CfgDLCNotificationsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgUnitInsigniaEntry = namedtuple('CfgUnitInsigniaEntry', ['classname', 'parent', 'displayName', 'author', 'material', 'textureVehicle'], defaults=(None, None, None, None, None))
CfgHoldActionsEntry = namedtuple('CfgHoldActionsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgFeedbackEffectsEntry = namedtuple('CfgFeedbackEffectsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMainMenuSpotlightEntry = namedtuple('CfgMainMenuSpotlightEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMarkerClassesEntry = namedtuple('CfgMarkerClassesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDiaryPicturesEntry = namedtuple('CfgDiaryPicturesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMagazineWellsEntry = namedtuple('CfgMagazineWellsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesFatigueEntry = namedtuple('CfgMovesFatigueEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSentencesEntry = namedtuple('CfgSentencesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgAnimationSourceSoundsEntry = namedtuple('CfgAnimationSourceSoundsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundShapesEntry = namedtuple('CfgSoundShapesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundCurvesEntry = namedtuple('CfgSoundCurvesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundShadersEntry = namedtuple('CfgSoundShadersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundSetsEntry = namedtuple('CfgSoundSetsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSound3DProcessorsEntry = namedtuple('CfgSound3DProcessorsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgDistanceFiltersEntry = namedtuple('CfgDistanceFiltersEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundGlobalsEntry = namedtuple('CfgSoundGlobalsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSoundCategoriesEntry = namedtuple('CfgSoundCategoriesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesWomenEntry = namedtuple('CfgMovesWomenEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgModSettingsEntry = namedtuple('CfgModSettingsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgArmorSimulationsEntry = namedtuple('CfgArmorSimulationsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgORBATEntry = namedtuple('CfgORBATEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesMaleSdr_TC3Entry = namedtuple('CfgMovesMaleSdr_TC3Entry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesMaleSdr_TC4Entry = namedtuple('CfgMovesMaleSdr_TC4Entry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgArmoryEntry = namedtuple('CfgArmoryEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesAnimalsBaseEntry = namedtuple('CfgMovesAnimalsBaseEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMovesDogEntry = namedtuple('CfgMovesDogEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgTimeTrialsEntry = namedtuple('CfgTimeTrialsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVRNoMipmapTexturesEntry = namedtuple('CfgVRNoMipmapTexturesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgVRCoursesEntry = namedtuple('CfgVRCoursesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRadioEntry = namedtuple('CfgRadioEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgGroundSupportRequestTypesEntry = namedtuple('CfgGroundSupportRequestTypesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgMarkNoMipmapTexturesEntry = namedtuple('CfgMarkNoMipmapTexturesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgReviveEntry = namedtuple('CfgReviveEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgHvtObjectivesEntry = namedtuple('CfgHvtObjectivesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgExtendedAnimationEntry = namedtuple('CfgExtendedAnimationEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgRolesEntry = namedtuple('CfgRolesEntry', ['classname', 'parent', 'displayName', 'icon'], defaults=(None, None, None))
CfgArgoNoMipmapTexturesEntry = namedtuple('CfgArgoNoMipmapTexturesEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgLeafletsEntry = namedtuple('CfgLeafletsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgWLRequisitionPresetsEntry = namedtuple('CfgWLRequisitionPresetsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))
CfgSettingsEntry = namedtuple('CfgSettingsEntry', ['classname', 'parent', 'displayName'], defaults=(None, None))


CFG_NAMED_TUPLES = {
    'CfgMods': CfgModsEntry,
    'CfgExperience': CfgExperienceEntry,
    'CfgAISkill': CfgAISkillEntry,
    'CfgAILevelPresets': CfgAILevelPresetsEntry,
    'CfgDifficultyPresets': CfgDifficultyPresetsEntry,
    'CfgDifficulties': CfgDifficultiesEntry,
    'CfgInventory': CfgInventoryEntry,
    'CfgCurator': CfgCuratorEntry,
    'CfgSteamSettings': CfgSteamSettingsEntry,
    'CfgBrains': CfgBrainsEntry,
    'CfgTextureToMaterial': CfgTextureToMaterialEntry,
    'CfgMaterials': CfgMaterialsEntry,
    'CfgTLMaterials': CfgTLMaterialsEntry,
    'CfgVehicleActions': CfgVehicleActionsEntry,
    'CfgWeaponCursors': CfgWeaponCursorsEntry,
    'CfgMineTriggers': CfgMineTriggersEntry,
    'CfgAmmo': CfgAmmoEntry,
    'CfgRecoils': CfgRecoilsEntry,
    'CfgMagazines': CfgMagazinesEntry,
    'CfgWeapons': CfgWeaponsEntry,
    'CfgInventoryGlobalVariable': CfgInventoryGlobalVariableEntry,
    'CfgDestroySounds': CfgDestroySoundsEntry,
    'CfgCloudlets': CfgCloudletsEntry,
    'CfgOpticsEffect': CfgOpticsEffectEntry,
    'CfgDestructPos': CfgDestructPosEntry,
    'CfgDamageAround': CfgDamageAroundEntry,
    'CfgLights': CfgLightsEntry,
    'CfgCloth': CfgClothEntry,
    'CfgVehicleClasses': CfgVehicleClassesEntry,
    'CfgFactionClasses': CfgFactionClassesEntry,
    'CfgVehicles': CfgVehiclesEntry,
    'CfgNonAIVehicles': CfgNonAIVehiclesEntry,
    'CfgMarkedTargets': CfgMarkedTargetsEntry,
    'CfgFSMs': CfgFSMsEntry,
    'CfgFatigue': CfgFatigueEntry,
    'CfgFirstAid': CfgFirstAidEntry,
    'CfgDiving': CfgDivingEntry,
    'CfgBleeding': CfgBleedingEntry,
    'CfgPriority': CfgPriorityEntry,
    'CfgSkeletonParameters': CfgSkeletonParametersEntry,
    'CfgImprecision': CfgImprecisionEntry,
    'CfgBreathing': CfgBreathingEntry,
    'CfgWeaponHandling': CfgWeaponHandlingEntry,
    'CfgPersonTurret': CfgPersonTurretEntry,
    'CfgMovesBasic': CfgMovesBasicEntry,
    'CfgGesturesMale': CfgGesturesMaleEntry,
    'CfgSlopeLimits': CfgSlopeLimitsEntry,
    'CfgAnimation': CfgAnimationEntry,
    'CfgCollisions': CfgCollisionsEntry,
    'CfgSlingLoading': CfgSlingLoadingEntry,
    'CfgVoice': CfgVoiceEntry,
    'CfgVoiceTypes': CfgVoiceTypesEntry,
    'CfgCoreData': CfgCoreDataEntry,
    'CfgVehicleIcons': CfgVehicleIconsEntry,
    'CfgCloudletShapes': CfgCloudletShapesEntry,
    'CfgSaveThumbnails': CfgSaveThumbnailsEntry,
    'cfgFormations': cfgFormationsEntry,
    'cfgWaypoints': cfgWaypointsEntry,
    'CfgRagDollSkeletons': CfgRagDollSkeletonsEntry,
    'CfgVideoOptions': CfgVideoOptionsEntry,
    'CfgSurfaceCharacters': CfgSurfaceCharactersEntry,
    'CfgSurfaces': CfgSurfacesEntry,
    'CfgSoundEnvironToControllers': CfgSoundEnvironToControllersEntry,
    'CfgDefaultSettings': CfgDefaultSettingsEntry,
    'CfgPatches': CfgPatchesEntry,
    'CfgFontFamilies': CfgFontFamiliesEntry,
    'CfgFonts': CfgFontsEntry,
    'CfgEditCamera': CfgEditCameraEntry,
    'CfgWrapperUI': CfgWrapperUIEntry,
    'CfgInGameUI': CfgInGameUIEntry,
    'cfgGroupIcons': cfgGroupIconsEntry,
    'CfgTaskTypes': CfgTaskTypesEntry,
    'CfgSimpleTasks': CfgSimpleTasksEntry,
    'CfgDiary': CfgDiaryEntry,
    'CfgActions': CfgActionsEntry,
    'CfgMissions': CfgMissionsEntry,
    'CfgRanks': CfgRanksEntry,
    'CfgDefaultKeysPresets': CfgDefaultKeysPresetsEntry,
    'CfgDetectors': CfgDetectorsEntry,
    'CfgFaceWounds': CfgFaceWoundsEntry,
    'CfgGlasses': CfgGlassesEntry,
    'CfgFaces': CfgFacesEntry,
    'CfgMimics': CfgMimicsEntry,
    'CfgEnvSounds': CfgEnvSoundsEntry,
    'CfgHQIdentities': CfgHQIdentitiesEntry,
    'CfgHeads': CfgHeadsEntry,
    'CfgMusic': CfgMusicEntry,
    'CfgSounds': CfgSoundsEntry,
    'CfgWhistleSound': CfgWhistleSoundEntry,
    'CfgTitles': CfgTitlesEntry,
    'CfgIntro': CfgIntroEntry,
    'CfgCredits': CfgCreditsEntry,
    'CfgCutScenes': CfgCutScenesEntry,
    'CfgCameraEffects': CfgCameraEffectsEntry,
    'CfgMarkers': CfgMarkersEntry,
    'CfgMarkerColors': CfgMarkerColorsEntry,
    'CfgMarkerBrushes': CfgMarkerBrushesEntry,
    'CfgLocationTypes': CfgLocationTypesEntry,
    'CfgWorlds': CfgWorldsEntry,
    'CfgWorldList': CfgWorldListEntry,
    'CfgGroups': CfgGroupsEntry,
    'CfgAddons': CfgAddonsEntry,
    'CfgEditorObjects': CfgEditorObjectsEntry,
    'CfgMPGameTypes': CfgMPGameTypesEntry,
    'CfgLiveStats': CfgLiveStatsEntry,
    'CfgAchievements': CfgAchievementsEntry,
    'CfgVoiceMask': CfgVoiceMaskEntry,
    'CfgRumble': CfgRumbleEntry,
    'cfgBuldozer': cfgBuldozerEntry,
    'CfgCameraShake': CfgCameraShakeEntry,
    'CfgLensFlare': CfgLensFlareEntry,
    'CfgSoundEffects': CfgSoundEffectsEntry,
    'CfgMineDetectionCoefs': CfgMineDetectionCoefsEntry,
    'CfgFire': CfgFireEntry,
    'CfgIRLaserSettings': CfgIRLaserSettingsEntry,
    'CfgFunctions': CfgFunctionsEntry,
    'CfgRespawnTemplates': CfgRespawnTemplatesEntry,
    'CfgPostProcessTemplates': CfgPostProcessTemplatesEntry,
    'CfgRemoteExecCommands': CfgRemoteExecCommandsEntry,
    'CfgRemoteExec': CfgRemoteExecEntry,
    'CfgCommands': CfgCommandsEntry,
    'CfgORBATDefault': CfgORBATDefaultEntry,
    'CfgSFX': CfgSFXEntry,
    'CfgEditorCategories': CfgEditorCategoriesEntry,
    'CfgEditorSubcategories': CfgEditorSubcategoriesEntry,
    'CfgMuzzleFlashes': CfgMuzzleFlashesEntry,
    'CfgBushNoMipmapTextures': CfgBushNoMipmapTexturesEntry,
    'CfgIdentities': CfgIdentitiesEntry,
    'CfgCuratorChallenges': CfgCuratorChallengesEntry,
    'CfgHintCategories': CfgHintCategoriesEntry,
    'CfgHints': CfgHintsEntry,
    'Cfg3DEN': Cfg3DENEntry,
    'CfgObjectCompositions': CfgObjectCompositionsEntry,
    'CfgCommunicationMenu': CfgCommunicationMenuEntry,
    'CfgFiringDrills': CfgFiringDrillsEntry,
    'CfgMusicClasses': CfgMusicClassesEntry,
    'CfgDestroy': CfgDestroyEntry,
    'CfgMovesAnimal': CfgMovesAnimalEntry,
    'CfgMovesButterfly': CfgMovesButterflyEntry,
    'CfgMovesBird': CfgMovesBirdEntry,
    'CfgTasks': CfgTasksEntry,
    'CfgMovesAnimal_Base_F': CfgMovesAnimal_Base_FEntry,
    'CfgMovesFishes_F': CfgMovesFishes_FEntry,
    'CfgMovesSharks_F': CfgMovesSharks_FEntry,
    'CfgMovesRabbit_F': CfgMovesRabbit_FEntry,
    'CfgMovesSnakes_F': CfgMovesSnakes_FEntry,
    'CfgMovesTurtle_F': CfgMovesTurtle_FEntry,
    'CfgMovesHen_F': CfgMovesHen_FEntry,
    'CfgMovesCock_F': CfgMovesCock_FEntry,
    'CfgMovesDog_F': CfgMovesDog_FEntry,
    'CfgMovesGoat_F': CfgMovesGoat_FEntry,
    'CfgMovesSheep_F': CfgMovesSheep_FEntry,
    'CfgMovesMaleSdr': CfgMovesMaleSdrEntry,
    'CfgCommunityGuide': CfgCommunityGuideEntry,
    'CfgUIColors': CfgUIColorsEntry,
    'CfgUIGrids': CfgUIGridsEntry,
    'CfgLanguages': CfgLanguagesEntry,
    'CfgWeaponIcons': CfgWeaponIconsEntry,
    'CfgLoadingTexts': CfgLoadingTextsEntry,
    'CfgLoadingScreens': CfgLoadingScreensEntry,
    'CfgChainOfCommand': CfgChainOfCommandEntry,
    'CfgScriptPaths': CfgScriptPathsEntry,
    'CfgEditorLayouts': CfgEditorLayoutsEntry,
    'CfgNotifications': CfgNotificationsEntry,
    'CfgDebriefing': CfgDebriefingEntry,
    'CfgDLCNotifications': CfgDLCNotificationsEntry,
    'CfgUnitInsignia': CfgUnitInsigniaEntry,
    'CfgHoldActions': CfgHoldActionsEntry,
    'CfgFeedbackEffects': CfgFeedbackEffectsEntry,
    'CfgMainMenuSpotlight': CfgMainMenuSpotlightEntry,
    'CfgMarkerClasses': CfgMarkerClassesEntry,
    'CfgDiaryPictures': CfgDiaryPicturesEntry,
    'CfgMagazineWells': CfgMagazineWellsEntry,
    'CfgMovesFatigue': CfgMovesFatigueEntry,
    'CfgSentences': CfgSentencesEntry,
    'CfgAnimationSourceSounds': CfgAnimationSourceSoundsEntry,
    'CfgSoundShapes': CfgSoundShapesEntry,
    'CfgSoundCurves': CfgSoundCurvesEntry,
    'CfgSoundShaders': CfgSoundShadersEntry,
    'CfgSoundSets': CfgSoundSetsEntry,
    'CfgSound3DProcessors': CfgSound3DProcessorsEntry,
    'CfgDistanceFilters': CfgDistanceFiltersEntry,
    'CfgSoundGlobals': CfgSoundGlobalsEntry,
    'CfgSoundCategories': CfgSoundCategoriesEntry,
    'CfgMovesWomen': CfgMovesWomenEntry,
    'CfgModSettings': CfgModSettingsEntry,
    'CfgArmorSimulations': CfgArmorSimulationsEntry,
    'CfgORBAT': CfgORBATEntry,
    'CfgMovesMaleSdr_TC3': CfgMovesMaleSdr_TC3Entry,
    'CfgMovesMaleSdr_TC4': CfgMovesMaleSdr_TC4Entry,
    'CfgArmory': CfgArmoryEntry,
    'CfgMovesAnimalsBase': CfgMovesAnimalsBaseEntry,
    'CfgMovesDog': CfgMovesDogEntry,
    'CfgTimeTrials': CfgTimeTrialsEntry,
    'CfgVRNoMipmapTextures': CfgVRNoMipmapTexturesEntry,
    'CfgVRCourses': CfgVRCoursesEntry,
    'CfgRadio': CfgRadioEntry,
    'CfgGroundSupportRequestTypes': CfgGroundSupportRequestTypesEntry,
    'CfgMarkNoMipmapTextures': CfgMarkNoMipmapTexturesEntry,
    'CfgRevive': CfgReviveEntry,
    'CfgHvtObjectives': CfgHvtObjectivesEntry,
    'CfgExtendedAnimation': CfgExtendedAnimationEntry,
    'CfgRoles': CfgRolesEntry,
    'CfgArgoNoMipmapTextures': CfgArgoNoMipmapTexturesEntry,
    'CfgLeaflets': CfgLeafletsEntry,
    'CfgWLRequisitionPresets': CfgWLRequisitionPresetsEntry,
    'CfgSettings': CfgSettingsEntry,
}


def get_entry_tuple(cfg_name: str):
    return CFG_NAMED_TUPLES.get(cfg_name)
# region[Main_Exec]


if __name__ == '__main__':
    pass

# endregion[Main_Exec]
