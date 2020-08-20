# region [Imports]


# *NORMAL Imports -->
# from collections import namedtuple
# from contextlib import contextmanager
# from jinja2 import Environment, BaseLoader
# from natsort import natsorted
# from pprint import *
# import argparse
# import datetime
# import lzma
# import os
# import pyperclip
# import re
# import shutil
# import sys
# import time

# *GID Imports -->
import gidlogger as glog

# *QT Imports -->
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtGui import QIcon, QPixmap, QColor, QBrush, QCursor
# from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QTreeWidgetItem, QListWidgetItem, QHeaderView, QButtonGroup, QTreeWidgetItemIterator, QMenu

# * Local Imports -->


# endregion [Imports]

__updated__ = '2020-08-12 10:15:16'

# region [Localized_Imports]

# endregion [Localized_Imports]


# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]


# region [Global_Functions]


# endregion [Global_Functions]


# region [Misc]

STD_HEADER = [
    "item_id",
    "item_classname",
    "item_displayname",
    "item_inheritance",
    "item_mod",
    "item_scope",
    "item_type",
    "item_descriptionshort",
    "item_preview_location",
    "item_preview",
]
CFGVEHICLES_HEADER = [
    "item_id",
    "item_classname",
    "item_displayname",
    "item_mod",
    "item_inheritance",
    "item_scope",
    "item_type",
    "item_subtype",
    "item_descriptionShort",
    "item_preview_location",
    "item_preview",
]

CFGUNITINSIGNIA_HEADER = [
    "item_id",
    "item_classname",
    "item_displayname",
    "item_inheritance",
    "item_mod",
    "item_scope",
    "item_type",
    "item_descriptionshort",
    "item_preview_location",
    "item_preview",
]

HEADER_DICT = {'cfgvehicles_items_tbl': CFGVEHICLES_HEADER, 'cfgunitinsignia_items_tbl': CFGUNITINSIGNIA_HEADER}

# endregion [Misc]


# region [Data_1]

ALL_CFG_SECTIONS = [
    # 'CfgMods',
    # 'CfgExperience',
    # 'CfgAISkill',
    # 'CfgAILevelPresets',
    # 'CfgDifficultyPresets',
    # 'CfgDifficulties',
    # 'CfgInventory',
    # 'CfgCurator',
    # 'CfgSteamSettings',
    # 'CfgBrains',
    # 'CfgTextureToMaterial',
    # 'CfgMaterials',
    # 'CfgTLMaterials',
    # 'CfgVehicleActions',
    # 'CfgWeaponCursors',
    # 'CfgMineTriggers',
    # 'CfgAmmo',
    # 'CfgRecoils',
    # 'CfgMagazines',
    'CfgWeapons',
    # 'CfgInventoryGlobalVariable',
    # 'CfgDestroySounds',
    # 'CfgCloudlets',
    # 'CfgOpticsEffect',
    # 'CfgDestructPos',
    # 'CfgDamageAround',
    # 'CfgLights',
    # 'CfgCloth',
    # 'CfgVehicleClasses',
    'CfgFactionClasses',
    'CfgVehicles',
    # 'CfgNonAIVehicles',
    # 'CfgMarkedTargets',
    # 'CfgFSMs',
    # 'CfgFatigue',
    # 'CfgFirstAid',
    # 'CfgDiving',
    # 'CfgBleeding',
    # 'CfgPriority',
    # 'CfgSkeletonParameters',
    # 'CfgImprecision',
    # 'CfgBreathing',
    # 'CfgWeaponHandling',
    # 'CfgPersonTurret',
    # 'CfgMovesBasic',
    # 'CfgGesturesMale',
    # 'CfgSlopeLimits',
    # 'CfgAnimation',
    # 'CfgCollisions',
    # 'CfgSlingLoading',
    # 'CfgVoice',
    # 'CfgVoiceTypes',
    # 'CfgCoreData',
    # 'CfgVehicleIcons',
    # 'CfgCloudletShapes',
    # 'CfgSaveThumbnails',
    # 'cfgFormations',
    # 'cfgWaypoints',
    # 'CfgRagDollSkeletons',
    # 'CfgVideoOptions',
    # 'CfgSurfaceCharacters',
    # 'CfgSurfaces',
    # 'CfgSoundEnvironToControllers',
    # 'CfgDefaultSettings',
    # 'CfgPatches',
    # 'CfgFontFamilies',
    # 'CfgFonts',
    # 'CfgEditCamera',
    # 'CfgWrapperUI',
    # 'CfgInGameUI',
    # 'cfgGroupIcons',
    # 'CfgTaskTypes',
    # 'CfgSimpleTasks',
    # 'CfgDiary',
    # 'CfgActions',
    # 'CfgMissions',
    # 'CfgRanks',
    # 'CfgDefaultKeysPresets',
    # 'CfgDetectors',
    # 'CfgFaceWounds',
    # 'CfgGlasses',
    # 'CfgFaces',
    # 'CfgMimics',
    # 'CfgEnvSounds',
    # 'CfgHQIdentities',
    # 'CfgHeads',
    # 'CfgMusic',
    # 'CfgSounds',
    # 'CfgWhistleSound',
    # 'CfgTitles',
    # 'CfgIntro',
    # 'CfgCredits',
    # 'CfgCutScenes',
    # 'CfgCameraEffects',
    # 'CfgMarkers',
    # 'CfgMarkerColors',
    # 'CfgMarkerBrushes',
    # 'CfgLocationTypes',
    # 'CfgWorlds',
    # 'CfgWorldList',
    # 'CfgGroups',
    # 'CfgAddons',
    # 'CfgEditorObjects',
    # 'CfgMPGameTypes',
    # 'CfgLiveStats',
    # 'CfgAchievements',
    # 'CfgVoiceMask',
    # 'CfgRumble',
    # 'cfgBuldozer',
    # 'CfgCameraShake',
    # 'CfgLensFlare',
    # 'CfgSoundEffects',
    # 'CfgMineDetectionCoefs',
    # 'CfgFire',
    # 'CfgIRLaserSettings',
    # 'CfgFunctions',
    # 'CfgRespawnTemplates',
    # 'CfgPostProcessTemplates',
    # 'CfgRemoteExecCommands',
    # 'CfgRemoteExec',
    # 'CfgCommands',
    # 'CfgORBATDefault',
    # 'CfgEditorCategories',
    # 'CfgEditorSubcategories',
    # 'CfgMuzzleFlashes',
    # 'CfgBushNoMipmapTextures',
    # 'CfgIdentities',
    # 'CfgCuratorChallenges',
    # 'CfgHintCategories',
    # 'CfgHints',
    # 'Cfg3DEN',
    # 'CfgObjectCompositions',
    # 'CfgCommunicationMenu',
    # 'CfgFiringDrills',
    # 'CfgMusicClasses',
    # 'CfgDestroy',
    # 'CfgMovesAnimal',
    # 'CfgMovesButterfly',
    # 'CfgMovesBird',
    # 'CfgTasks',
    # 'CfgMovesAnimal_Base_F',
    # 'CfgCommunityGuide',
    # 'CfgUIColors',
    # 'CfgUIGrids',
    # 'CfgLanguages',
    # 'CfgWeaponIcons',
    # 'CfgLoadingTexts',
    # 'CfgLoadingScreens',
    # 'CfgChainOfCommand',
    # 'CfgScriptPaths',
    # 'CfgEditorLayouts',
    # 'CfgNotifications',
    # 'CfgDebriefing',
    # 'CfgDLCNotifications',
    'CfgUnitInsignia',
    # 'CfgHoldActions',
    # 'CfgFeedbackEffects',
    # 'CfgMainMenuSpotlight',
    # 'CfgMarkerClasses',
    # 'CfgDiaryPictures',
    # 'CfgMagazineWells',
    # 'CfgMovesFatigue',
    # 'CfgSentences',
    # 'CfgSFX',
    # 'CfgAnimationSourceSounds',
    # 'CfgSoundShapes',
    # 'CfgSoundCurves',
    # 'CfgSoundShaders',
    # 'CfgSoundSets',
    # 'CfgSound3DProcessors',
    # 'CfgDistanceFilters',
    # 'CfgSoundGlobals',
    # 'CfgSoundCategories',
    # 'CfgArmorSimulations',
    # 'CfgORBAT',
    # 'CfgTimeTrials',
    # 'CfgVRNoMipmapTextures',
    # 'CfgVRCourses',
    # 'CfgRadio',
    # 'CfgGroundSupportRequestTypes',
    # 'CfgMarkNoMipmapTextures',
    # 'CfgRevive',
    # 'CfgHvtObjectives',
    # 'CfgExtendedAnimation',
    # 'CfgRoles',
    # 'CfgArgoNoMipmapTextures',
    # 'CfgLeaflets',
    # 'CfgWLRequisitionPresets'
]

# endregion [Data_1]


# region [Data_2]

CFG_VEHICLES_MUSTS = [
    'displayname',
    'scope',
    'author',
    'picture',
    'editorpreview',
    'faction',
    'editorsubcategory',
    'side',
    'uniformclass',
    'category',
]


CFGVEHICLES_COLUMNS = [
    'classname',
    'mod',
    'scope',
    'displayName',
    'scopeCurator',
    'editorPreview',
    'SimpleObject',
    'model',
    'icon',
    'editorSubcategory',
    'mapSize',
    'DLC',
    'editorCategory',
    'vehicleClass',
    'hiddenSelectionsTextures',
    'TransportItems',
    'cost',
    'faction',
    'destrType',
    'AnimationSources',
    'DestructionEffects',
    'weapons',
    'side',
    'Damage',
    'TransportMagazines',
    'magazines',
    'hiddenSelections',
    'uniformClass',
    'crew',
    'linkedItems',
    'respawnWeapons',
    'picture',
    'respawnLinkedItems',
    'textureList',
    'respawnMagazines',
    'armor',
    'accuracy',
    'role',
    'TransportWeapons',
    'UserActions',
    'HitPoints',
    'typicalCargo',
    'EventHandlers',
    'numberOfDoors',
    'backpack',
    'Turrets',
    'category',
]


# endregion [Data_2]


# region [Data_3]

CFGMAGAZINES_COLUMNS = [
    'classname',
    'mod',
    'displayName',
    'ammo',
    'count',
    'descriptionShort',
    'initSpeed',
    'picture',
    'displayNameShort',
    'model',
    'mass',
    'scope',
    'tracersEvery',
]


# endregion [Data_3]


# region [Data_4]

CFGWEAPONS_COLUMNS = [
    ('displayName', 'text'),
    ('picture', 'text'),
    ('scope', 'integer'),
    ('hiddenSelectionsTextures', 'text'),
    ('model', 'text'),
    ('ItemInfo', 'text'),
    ('hiddenSelections', 'text'),
    ('DLC', 'text'),
    ('LinkedItems', 'text'),
    ('magazines', 'text'),
    ('descriptionShort', 'text'),
    ('baseWeapon', 'text'),
    ('inertia', 'text'),
    ('WeaponSlotsInfo', 'text'),
    ('modes', 'text'),
]


# endregion [Data_4]


# region [Data_5]


# endregion [Data_5]


# region [Dict_1]

cfgweapons_type_dict = {
    'Default': 'Default',
    'ItemCore': 'Item',
    'PistolCore': 'Pistol',
    'RifleCore': 'Rifle',
    'DetectorCore': 'Detector',
    'MGunCore': 'MG',
    'LauncherCore': 'Launcher',
    'GrenadeCore': 'Grenade',
    'CannonCore': 'Cannon',
    'InventoryItem_Base_F': 'Inventor_Item',
    'Uniform_Base': 'Uniform',
    'Vest_Camo_Base': 'Vest',
    'Vest_NoCamo_Base': 'Vest',
    'HelmetBase': 'Helmet',
    'H_HelmetB': 'Helmet',
    'UavTerminal_base': 'Uav_Terminal',
    'Binocular': 'Binocular',
    'NVGoggles': 'NVG',
    'MineDetector': 'Mine_detector',
    'CarHorn': 'Car_Horn',
    'GrenadeLauncher': 'Grenade_Launcher',
    'MuzzleSlot': 'Muzzle_Slot',
    'H_FakeHeadgear_Syndikat_F': 'FakeHeadgear_Syndikat',
}


cfgvehicles_type_dict = {
    'Logic': 'Logic',
    'AllVehicles': 'Vehicles',
    'LaserTarget': 'Laser_Target',
    'NVTarget': 'NV_Target',
    'ArtilleryTarget': 'Artillery_Target',
    'FireSectorTarget': 'Fire_Sector_Target',
    'Static': 'Static',
    'Rope': 'Rope',
    'Thing': 'Thing',
    'WindAnomaly': 'Wind_Anomaly',
    'FloatingStructure_F': 'Floating_Structure_F',
    'Object': 'Object',
    'placed_chemlight_green': 'Placed_Chemlight_green',
    'NVG_TargetBase': 'NVG_Target_Base',
    'placed_B_IR_grenade': 'Placed_B_IR_Grenade',
    'Sound': 'Sound',
    'Man': 'Man'
}


# endregion [Dict_1]


# region [Dict_2]

_MOD_AUTHOR_DICT = {
    'Bohemia Interactive': 'bi',
    'Raspu, Nkey': 'taskforce',
    'Raspu': 'taskforce',
    'Red Hammer Studios': 'rhs',
    'ACE-Team': 'ace',
    'Bravo Zero One Studios': 'bi',
    'xrufix': 'ace',
    'tema': 'rhs',
    'jokoho48': 'ace',
    'Toadie': 'rhs',
    'Ruthberg': 'ace',
    'Rocko, Scubaman3D': 'ace'
}

# endregion [Dict_2]


# region [Dict_3]

PICTURE_ALIASES = {
    'iconPaperCar': '#(argb,8,8,3)color(1,1,1,1)',
    'iconModule': '/A3/modules_f/data/portraitModule_ca.paa',
    'IconTimeline': '/A3/Ui_f/data/GUI/Cfg/KeyframeAnimation/IconTimeline_CA.paa',
    'IconCurve': '/A3/Ui_f/data/GUI/Cfg/KeyframeAnimation/IconCurve_CA.paa',
    'IconKey': '/A3/Ui_f/data/GUI/Cfg/KeyframeAnimation/IconKey_CA.paa',
    'IconControlPoint': '/A3/Ui_f/data/GUI/Cfg/KeyframeAnimation/IconControlPoint_CA.paa',
    'IconCamera': '/A3/Ui_f/data/GUI/Cfg/KeyframeAnimation/IconCamera_CA.paa',
    'iconObject': '/A3/ui_f/data/map/vehicleicons/iconObject_ca.paa',
    'iconLogic': '/A3/ui_f/data/map/vehicleicons/iconLogic_ca.paa',
    'iconVirtual': '/A3/ui_f/data/map/vehicleicons/iconVirtual_ca.paa',
    'iconVehicle': '/A3/ui_f/data/map/vehicleicons/iconVehicle_ca.paa',
    'iconCar': '/A3/ui_f/data/map/vehicleicons/iconCar_ca.paa',
    'iconMotorcycle': '/A3/ui_f/data/map/vehicleicons/iconMotorcycle_ca.paa',
    'iconTank': '/A3/ui_f/data/map/vehicleicons/iconTank_ca.paa',
    'iconAPC': '/A3/ui_f/data/map/vehicleicons/iconAPC_ca.paa',
    'iconHelicopter': '/A3/ui_f/data/map/vehicleicons/iconHelicopter_ca.paa',
    'iconPlane': '/A3/ui_f/data/map/vehicleicons/iconPlane_ca.paa',
    'iconShip': '/A3/ui_f/data/map/vehicleicons/iconShip_ca.paa',
    'iconParachute': '/A3/ui_f/data/map/vehicleicons/iconParachute_ca.paa',
    'iconCrate': '/A3/ui_f/data/map/vehicleicons/iconCrate_ca.paa',
    'iconCrateAmmo': '/A3/ui_f/data/map/vehicleicons/iconCrateAmmo_ca.paa',
    'iconCrateWpns': '/A3/ui_f/data/map/vehicleicons/iconCrateWpns_ca.paa',
    'iconCrateLarge': '/A3/ui_f/data/map/vehicleicons/iconCrateLarge_ca.paa',
    'iconCrateLong': '/A3/ui_f/data/map/vehicleicons/iconCrateLong_ca.paa',
    'iconCrateOrd': '/A3/ui_f/data/map/vehicleicons/iconCrateOrd_ca.paa',
    'iconCrateGrenades': '/A3/ui_f/data/map/vehicleicons/iconCrateGrenades_ca.paa',
    'iconCrateSupp': '/A3/ui_f/data/map/vehicleicons/iconCrateSupp_ca.paa',
    'iconCrateVeh': '/A3/ui_f/data/map/vehicleicons/iconCrateVeh_ca.paa',
    'iconBackpack': '/A3/ui_f/data/map/vehicleicons/iconBackpack_ca.paa',
    'iconAnimal': '/A3/ui_f/data/map/vehicleicons/iconAnimal_ca.paa',
    'iconSound': '/A3/ui_f/data/map/vehicleicons/iconSound_ca.paa',
    'iconStaticAA': '/A3/ui_f/data/map/vehicleicons/iconStaticAA_ca.paa',
    'iconStaticCannon': '/A3/ui_f/data/map/vehicleicons/iconStaticCannon_ca.paa',
    'iconStaticMG': '/A3/ui_f/data/map/vehicleicons/iconStaticMG_ca.paa',
    'iconStaticMGNest': '/A3/ui_f/data/map/vehicleicons/iconStaticMGNest_ca.paa',
    'iconStaticMortar': '/A3/ui_f/data/map/vehicleicons/iconStaticMortar_ca.paa',
    'iconStaticSearchlight': '/A3/ui_f/data/map/vehicleicons/iconStaticSearchlight_ca.paa',
    'iconEmpty': '#(argb,8,8,3)color(0,0,0,0)',
    'iconAir': '/A3/ui_f/data/map/vehicleicons/iconhelicopter_ca.paa',
    'iconStaticObject': '/A3/ui_f/data/map/vehicleicons/iconobject_ca.paa',
    'iconThing': '/A3/ui_f/data/map/vehicleicons/iconobject_ca.paa',
    'iconLaserTarget': '/A3/ui_f/data/map/vehicleicons/iconobject_ca.paa',
    'iconObject_1x1': '/A3/ui_f/data/map/vehicleicons/iconObject_1x1_ca.paa',
    'iconObject_1x2': '/A3/ui_f/data/map/vehicleicons/iconObject_1x2_ca.paa',
    'iconObject_1x3': '/A3/ui_f/data/map/vehicleicons/iconObject_1x3_ca.paa',
    'iconObject_1x4': '/A3/ui_f/data/map/vehicleicons/iconObject_1x4_ca.paa',
    'iconObject_1x5': '/A3/ui_f/data/map/vehicleicons/iconObject_1x5_ca.paa',
    'iconObject_1x7': '/A3/ui_f/data/map/vehicleicons/iconObject_1x7_ca.paa',
    'iconObject_1x10': '/A3/ui_f/data/map/vehicleicons/iconObject_1x10_ca.paa',
    'iconObject_2x3': '/A3/ui_f/data/map/vehicleicons/iconObject_2x3_ca.paa',
    'iconObject_2x5': '/A3/ui_f/data/map/vehicleicons/iconObject_2x5_ca.paa',
    'iconObject_4x5': '/A3/ui_f/data/map/vehicleicons/iconObject_4x5_ca.paa',
    'iconObject_2x1': '/A3/ui_f/data/map/vehicleicons/iconObject_2x1_ca.paa',
    'iconObject_3x1': '/A3/ui_f/data/map/vehicleicons/iconObject_3x1_ca.paa',
    'iconObject_4x1': '/A3/ui_f/data/map/vehicleicons/iconObject_4x1_ca.paa',
    'iconObject_5x1': '/A3/ui_f/data/map/vehicleicons/iconObject_5x1_ca.paa',
    'iconObject_7x1': '/A3/ui_f/data/map/vehicleicons/iconObject_7x1_ca.paa',
    'iconObject_10x1': '/A3/ui_f/data/map/vehicleicons/iconObject_10x1_ca.paa',
    'iconObject_3x2': '/A3/ui_f/data/map/vehicleicons/iconObject_3x2_ca.paa',
    'iconObject_5x2': '/A3/ui_f/data/map/vehicleicons/iconObject_5x2_ca.paa',
    'iconObject_5x4': '/A3/ui_f/data/map/vehicleicons/iconObject_5x4_ca.paa',
    'iconObject_circle': '/A3/ui_f/data/map/vehicleicons/iconObject_circle_ca.paa',
    'iconObject_elipse_H': '/A3/ui_f/data/map/vehicleicons/iconObject_elipse_H_ca.paa',
    'iconObject_elipse_V': '/A3/ui_f/data/map/vehicleicons/iconObject_elipse_V_ca.paa',
    'iconMan': '/A3/ui_f/data/map/vehicleicons/iconMan_ca.paa',
    'iconManMedic': '/A3/ui_f/data/map/vehicleicons/iconManMedic_ca.paa',
    'iconManEngineer': '/A3/ui_f/data/map/vehicleicons/iconManEngineer_ca.paa',
    'iconManExplosive': '/A3/ui_f/data/map/vehicleicons/iconManExplosive_ca.paa',
    'iconManRecon': '/A3/ui_f/data/map/vehicleicons/iconManRecon_ca.paa',
    'iconManVirtual': '/A3/ui_f/data/map/vehicleicons/iconManVirtual_ca.paa',
    'iconManAT': '/A3/ui_f/data/map/vehicleicons/iconManAT_ca.paa',
    'iconManLeader': '/A3/ui_f/data/map/vehicleicons/iconManLeader_ca.paa',
    'iconManMG': '/A3/ui_f/data/map/vehicleicons/iconManMG_ca.paa',
    'iconManOfficer': '/A3/ui_f/data/map/vehicleicons/iconManOfficer_ca.paa',
    'iconExplosiveAP': '/A3/ui_f/data/map/vehicleicons/iconExplosiveAP_ca.paa',
    'iconExplosiveAPDirectional': '/A3/ui_f/data/map/vehicleicons/iconExplosiveAPDirectional_ca.paa',
    'iconExplosiveAT': '/A3/ui_f/data/map/vehicleicons/iconExplosiveAT_ca.paa',
    'iconExplosiveUW': '/A3/ui_f/data/map/vehicleicons/iconExplosiveUW_ca.paa',
    'iconExplosiveGP': '/A3/ui_f/data/map/vehicleicons/iconExplosiveGP_ca.paa',
    'iconExplosiveGPDirectional': '/A3/ui_f/data/map/vehicleicons/iconExplosiveGPDirectional_ca.paa',
    'pictureExplosive': '/A3/ui_f/data/map/vehicleicons/pictureExplosive_ca.paa',
    'pictureHeal': '/A3/ui_f/data/map/vehicleicons/pictureHeal_ca.paa',
    'pictureRepair': '/A3/ui_f/data/map/vehicleicons/pictureRepair_ca.paa',
    'pictureLogic': '/A3/ui_f/data/map/vehicleicons/pictureLogic_ca.paa',
    'pictureParachute': '/A3/ui_f/data/map/vehicleicons/pictureParachute_ca.paa',
    'picturePaperCar': '/A3/ui_f/data/map/vehicleicons/picturePaperCar_ca.paa',
    'pictureLaserTarget': '/A3/ui_f/data/map/vehicleicons/picturelogic_ca.paa',
    'pictureStaticObject': '/A3/ui_f/data/map/vehicleicons/picturelogic_ca.paa',
    'pictureThing': '/A3/ui_f/data/map/vehicleicons/picturelogic_ca.paa',
    'uiPictureMG': '/A3/ui_f/data/map/vehicleicons/uiPictureMG_ca.paa',
    'uiPictureArifle': '/A3/ui_f/data/map/vehicleicons/uiPictureArifle_ca.paa',
    'uiPictureLaunch': '/A3/ui_f/data/map/vehicleicons/uiPictureLaunch_ca.paa',
    'uiPictureUnarmed': '/A3/ui_f/data/map/vehicleicons/uiPictureUnarmed_ca.paa',
    'iconExplosiveUXO': '/A3/ui_f_orange/Data/CfgVehicleIcons/iconExplosiveUXO_ca.paa',
}

# endregion [Dict_3]


# region [Dict_4]

TYPE_DICTS = {
    'cfgweapons_items_tbl': cfgweapons_type_dict,
    'cfgvehicles_items_tbl': cfgvehicles_type_dict,

}

# endregion [Dict_4]


# region [Dict_5]


# endregion [Dict_5]


# region [List_1]


# endregion [List_1]


# region [List_2]


# endregion [List_2]


# region [List_3]


# endregion [List_3]


# region [List_4]


# endregion [List_4]


# region [List_5]


# endregion [List_5]


# region [Main_Exec]

if __name__ == '__main__':
    pass


# endregion [Main_Exec]
