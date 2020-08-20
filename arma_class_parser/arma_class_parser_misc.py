# region [Imports]

# *NORMAL Imports -->
from pprint import pformat
import os
import shutil
import time
import subprocess
from PIL import Image
import configparser
# *GID Imports -->
from gidtools.gidfiles import QuickFile, ext_splitter, file_walker, pathmaker, splitoff, create_folder
import gidlogger as glog

# *QT Imports -->

# *Local Imports -->

# endregion [Imports]

__updated__ = '2020-08-14 17:34:28'

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]

# region [Constants]


# endregion [Constants]


# region [Global_Functions]


# endregion [Global_Functions]


# region [Functions_1]


# endregion [Functions_1]


# region [Functions_2]


# endregion [Functions_2]


# region [Functions_3]


# endregion [Functions_3]


# region [Functions_4]


# endregion [Functions_4]


# region [Functions_5]


# endregion [Functions_5]


# region [Functions_6]


# endregion [Functions_6]


# region [Functions_7]


# endregion [Functions_7]


# region [Functions_8]

# class ImageManipulator:
#     def __init__(self, image_list=None):
#         self.images = [] if image_list is None else image_list

#     def resize(self, targetsize, quality):
#         for _old_path, _new_path in self.images:
#             _image = Image.open(_old_path)
#             _image = _image.crop(_image.getbbox())
#             _ratio = _image.size[1] / _image.size[0]
#             _image = _image.resize((targetsize, round(targetsize * _ratio)), Image.LANCZOS)
#             _image.save(_new_path, optimize=True, quality=quality)

#     def append_to(self, item):
#         if isinstance(item, tuple):
#             self.images.append(item)

# # endregion [Functions_8]


# # region [Functions_9]
# class ACPImageConverter:
#     def __init__(self, target_size, quality):
#         self.target_size = target_size
#         self.quality = quality
#         self.image_handler = ImageManipulator()
#         self.input_folder = pathmaker('cwd', 'ressources', 'output_paa')
#         self.output_loc = pathmaker('cwd', 'ressources', 'output_final')
#         if os.path.isdir(self.output_loc) is False:
#             os.makedirs(self.output_loc)
#         self.paa_files = []
#         self.quickfile = QuickFile()
#         self.jpg_files = []

#     def run_it(self):
#         self.paa_files, self.jpg_files = self.list_paa()
#         print(f"amount of images total: '{len(self.paa_files) + len(self.jpg_files)}', paa only: '{len(self.paa_files)}', jpg only: '{len(self.jpg_files)}'!")
#         log.critical(f"amount of images total: '{len(self.paa_files) + len(self.jpg_files)}', paa only: '{len(self.paa_files)}', jpg only: '{len(self.jpg_files)}'!")
#         self.move_jpgs()
#         self.transform_paa()
#         self.list_for_optimize()
#         self.image_handler.resize(self.target_size, self.quality)

#     def list_paa(self):
#         _paa_out_list = []
#         _jpg_out_list = []
#         for file in os.listdir(self.input_folder):
#             _ext = ext_splitter(file, _out='ext')
#             if _ext == 'paa':
#                 _paa_out_list.append(pathmaker(self.input_folder, file))
#             elif _ext == 'jpg':
#                 _jpg_out_list.append(pathmaker(self.input_folder, file))
#         return (_paa_out_list, _jpg_out_list)

#     def move_jpgs(self):
#         for jpg_file in self.jpg_files:
#             shutil.move(jpg_file, self.output_loc)

#     def transform_paa(self):
#         for paa_file in self.paa_files:
#             _old = paa_file
#             _dir, _file = splitoff(paa_file)
#             _basefile = ext_splitter(_file)
#             _new = pathmaker(self.output_loc, _basefile + '.png')
#             _command = r'"C:\Program Files (x86)\Steam\steamapps\common\Arma 3 Tools\ImageToPAA\ImageToPAA.exe"' + ' ' + _old + ' ' + _new
#             _cmd = subprocess.run(_command, check=False, shell=True, capture_output=True)
#             log.debug(pformat(_cmd.stdout))

#     def list_for_optimize(self):
#         for imagefile in os.listdir(self.output_loc):
#             _old_path = ''
#             _new_path = ''
#             if '.jpg' in imagefile:
#                 _old_path = pathmaker(self.output_loc, imagefile)
#                 _new_path = _old_path.replace('.jpg', '.png')
#             elif '.png' in imagefile:
#                 _old_path = pathmaker(self.output_loc, imagefile)
#                 _new_path = _old_path
#             if _old_path != '' and _new_path != '':
#                 self.image_handler.append_to((_old_path, _new_path))


# endregion [Functions_9]


# region [Class_1]

# class ACPImageFinder:
#     def __init__(self, in_db, in_section, in_search_dirs=None, target_size=256, quality=95):
#         self.section = in_section
#         self.converter = ACPImageConverter(target_size, quality)
#         self.db = in_db
#         self.output_loc = pathmaker('cwd', 'ressources', 'output_paa')
#         self.final_loc = pathmaker('cwd', 'ressources', 'output_final')
#         self.make_folders()
#         self.clear_dir('paa')
#         self.clear_dir('final')
#         self.search_dirs = ['C:/', 'D:/'] if in_search_dirs is None else in_search_dirs
#         self.run_it()
#         self.converter.run_it()
#         self.clear_dir('paa')
#         self.to_db()
#         # shutil.copytree(self.final_loc, pathmaker(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\arma_class_parser_src\dev_ressources\converted_images_" + self.section))
#         self.clear_dir('paa')
#         self.clear_dir('final')
#         os.rmdir(self.output_loc)
#         os.rmdir(self.final_loc)

#         log.info(glog.class_initiated(self.__class__))

#     def run_it(self):

#         self.query_result = self.query_path()
#         self.found_paths = self.find_images()
#         self.copied_images = self.copy_images()

#     def make_folders(self):
#         if os.path.isdir(self.output_loc) is False:
#             os.makedirs(self.output_loc)
#         if os.path.isdir(self.final_loc) is False:
#             os.makedirs(self.final_loc)

#     def clear_dir(self, in_kind):
#         if in_kind == 'paa':
#             for file in os.listdir(self.output_loc):
#                 os.remove(pathmaker(self.output_loc, file))
#         elif in_kind == 'final':
#             for file in os.listdir(self.final_loc):
#                 os.remove(pathmaker(self.final_loc, file))

#     @ staticmethod
#     def sort_filename(in_item):
#         if isinstance(in_item, tuple):
#             _name, _file = in_item
#         else:
#             _file = in_item
#         return ext_splitter(splitoff(_file)[1])

#     def query_path(self):
#         log.info('starting image query')
#         _out_list = []
#         _table = self.section.casefold() + '_items_tbl'
#         _phrase = f'SELECT "item_classname", "item_preview_location" FROM "{_table}"'
#         _results = self.db.executor(_phrase)
#         for _name, _path in _results:

#             if _path != 'none' and _path != '':
#                 _ext = ext_splitter(splitoff(_path.casefold())[1], _out='ext')
#                 if _ext in ['paa', 'jpg']:

#                     _out_list.append((_name, pathmaker(_path.casefold())))

#         return sorted(_out_list, key=self.sort_filename)

#     def find_images(self):
#         log.info('starting image search')
#         _out_list = []
#         _file_list = []
#         for _dir in self.search_dirs:
#             for file in file_walker(_dir):
#                 if ext_splitter(splitoff(file.casefold())[1], _out='ext') in ['paa', 'jpg']:

#                     _file_list.append(file.casefold())
#         _file_list = sorted(_file_list, key=self.sort_filename)
#         for _name, _path in self.query_result:
#             _path_file = splitoff(_path)[1]
#             for file in _file_list:
#                 if file.casefold().endswith(_path_file):

#                     if (_name, file.casefold()) not in _out_list:

#                         _out_list.append((_name, pathmaker(file.casefold())))

#         return _out_list

#     def copy_images(self):
#         log.info('starting image copying')
#         _out_list = []
#         if os.path.isdir(self.output_loc) is False:
#             os.makedirs(self.output_loc)
#         for name, path in self.found_paths:
#             _new_path = pathmaker(self.output_loc, name + '.' + ext_splitter(splitoff(path)[1], _out='ext'))

#             shutil.copy(path, _new_path)
#             log.debug(f"copied image for '{name}' from '{path}', to '{_new_path}'")
#             _out_list.append((name, _new_path))
#         return _out_list

#     def to_db(self):

#         _phrase = 'INSERT OR IGNORE INTO "image_blob_tbl" ("blob_name", "blob_data") VALUES (?, ?)'
#         for files in os.listdir(self.final_loc):
#             _name = ext_splitter(files)
#             _path = pathmaker(self.final_loc, files)
#             with open(_path, 'rb') as binfile:
#                 _content = binfile.read()

#             _phrase_2 = f'UPDATE "{self.section}_items_tbl" SET "item_preview" = (SELECT "blob_id" FROM "image_blob_tbl" WHERE "blob_name" = "{_name.lower()}") WHERE LOWER("item_classname") = "{_name.lower()}"'

#             self.db.executor(_phrase, in_variables=(_name, _content))
#             log.debug(f"Inserted Blob '{_name}' for section '{self.section}'")
#             self.db.executor(_phrase_2)
#             log.debug(f"Updated table '{self.section}_items_tbl' where 'item_classname' == '{_name.lower()}'")
#         self.db.executor.vacuum()


# endregion [Class_1]


# region [Class_2]


# endregion [Class_2]


# region [Class_3]

class ACPMarkDownPrinter:
    def __init__(self):
        pass

# endregion [Class_3]


# region [Class_4]


# endregion [Class_4]


# region [Class_5]

class ACPImageFinder:
    def __init__(self, section, in_db):
        self.db = in_db
        self.section = section
        self.table = f"{self.section}_items_tbl"
        self.orig_path_dict = self.query_paths()
        self.paa_to_png_loc = ''
        self.locations = self.get_locations()
        create_folder(pathmaker('cwd', 'ressources', 'temp'))
        self.temp_loc = pathmaker('cwd', 'ressources', 'temp')
        self.final_path_dict = {}
        self.process_images()
        self.to_db()

    def query_paths(self):
        log.info('starting image query')
        _out_dict = {}
        _table = self.section.casefold() + '_items_tbl'
        _phrase = f'SELECT "item_classname", "item_preview_location" FROM "{_table}"'
        _results = self.db.executor(_phrase)
        for row in _results:
            if row[1] != 'none' and row[1] != '' and row[1] is not None:
                _out_dict[row[0]] = row[1]
        return _out_dict

    def get_locations(self):
        _out_dict = {}
        _cfg = configparser.ConfigParser()
        _cfg.read("config/user_config.ini")
        for key in _cfg.options('locations'):
            _out_dict[key] = pathmaker(_cfg.get('locations', key))
        self.paa_to_png_loc = pathmaker(_cfg.get('apps', 'pal2pace'))
        return _out_dict

    def process_images(self):
        _list = []
        for classname, image_path in self.orig_path_dict.items():
            image_path = image_path.replace('\\', '/').lstrip('/')
            _full_path = ''
            if image_path.split('/')[0].casefold() == 'a3':
                _full_path = pathmaker(self.locations['p_drive'], image_path)
                log.debug(f" full path found for '{classname}' in '{_full_path}'")
            else:
                for folder in os.listdir(pathmaker(self.locations['user_mods'])):
                    if '.' not in folder:
                        if image_path.split('/')[0].casefold() == folder:
                            _full_path = pathmaker(self.locations['user_mods'], image_path)
                            log.debug(f" full path found for '{classname}' in '{_full_path}'")
                            break
                        for subfolder in os.listdir(pathmaker(self.locations['user_mods'], folder)):
                            if image_path.split('/')[0].casefold() == subfolder:
                                _full_path = pathmaker(self.locations['user_mods'], folder, image_path)
                                log.debug(f" full path found for '{classname}' in '{_full_path}'")
                                break

            if _full_path != '':
                if ext_splitter(_full_path, _out='ext').casefold() == 'jpg':
                    self.final_path_dict[classname] = pathmaker(_full_path)
                elif ext_splitter(_full_path, _out='ext').casefold() == 'paa':
                    _new_path = pathmaker(_full_path.split('.')[0] + '.png')
                    if _new_path not in set(_list):
                        _cmd_object = subprocess.run([self.paa_to_png_loc, _full_path, _new_path], check=False, shell=False, capture_output=True)
                        if 'error' in str(_cmd_object.stdout).casefold():
                            log.critical('paa2png output: ' + str(_cmd_object.stdout))
                        else:
                            log.debug('paa2png output: ' + str(_cmd_object.stdout))
                        _list.append(_new_path)
                    self.final_path_dict[classname] = _new_path
            else:
                log.debug(f" NO full path found for '{classname}' with original path '{image_path}'")

    def to_db(self):
        _phrase_list = []
        for classname, new_path in self.final_path_dict.items():
            _classname = classname.casefold()
            _phrase = f'UPDATE "{self.table}" SET "item_preview" = "{new_path}" WHERE LOWER("item_classname") = "{_classname}"'
            _phrase_list.append(_phrase)
        self.db.executor(';'.join(_phrase_list), is_script=True)

# endregion [Class_5]


# region [Class_6]


# endregion [Class_6]


# region [Class_7]


# endregion [Class_7]


# region [Class_8]


# endregion [Class_8]


# region [Class_9]


# endregion [Class_9]


# region [Model_1]


# endregion [Model_1]


# region [Model_2]


# endregion [Model_2]


# region [Model_3]


# endregion [Model_3]


# region [Model_4]


# endregion [Model_4]


# region [Model_5]


# endregion [Model_5]


# region [Model_6]


# endregion [Model_6]


# region [Model_7]


# endregion [Model_7]


# region [Model_8]


# endregion [Model_8]


# region [Model_9]


# endregion [Model_9]


# region [Main_Exec]
if __name__ == '__main__':
    pass


# endregion [Main_Exec]
