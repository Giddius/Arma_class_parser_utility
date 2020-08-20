# region [Imports]
# *NORMAL Imports -->

from PyQt5.QtCore import QAbstractTableModel
import armaclass
import re

# *GID Imports -->
from gidtools.gidfiles import get_pickled, hash_to_solidcfg, hash_to_solidcfg, ishash_same, ishash_same, linereadit, readit, splitoff, pathmaker
from gidtools.gidfiles.functions import pickleit
from gidtools.gidtriumvirate import GiUserConfig
import gidlogger as glog

# *QT Imports -->
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPixmap

# * Local Imports -->
from arma_class_parser_DATA import HEADER_DICT, PICTURE_ALIASES, STD_HEADER, TYPE_DICTS

# endregion [Imports]

__updated__ = '2020-08-13 15:44:55'

# region [Localized_Imports]


# endregion [Localized_Imports]


# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]


# region [Constants]


# endregion [Constants]


# region [Misc]


# endregion [Misc]


# region [Global_Functions]

# endregion [Global_Functions]


# region [Class_1]


# endregion [Class_1]


# region [Class_2]


# endregion [Class_2]


# region [Class_3]
def get_type(baseparent, inheritance_dict):
    _temp_list = [baseparent]
    _index = -1
    while _index != 1:
        _temp = type_looper(_temp_list, inheritance_dict)
        if all(_tempitem in _temp_list for _tempitem in _temp):
            _index = 1
        elif _temp != []:
            for key in _temp:
                if key not in _temp_list:
                    _temp_list.append(key)
    return _temp_list


# endregion [Class_3]

# region [Class_4]


def type_looper(in_list, inheritance_dict):
    _out_list = []
    for key, value in inheritance_dict.items():
        if value in in_list:
            _out_list.append(key)
    return _out_list


# endregion [Class_4]


# region [Class_5]


class SortedItemHolder:
    def __init__(self, in_section, in_next_section, in_dict_holder):
        self.section = in_section
        self.table = f'{self.section.casefold()}_items_tbl'
        self.cfg_content_holder = in_dict_holder()
        self.seperated_content = self.condense_content(self.cfg_content_holder[0], in_next_section)
        self.classes = []
        self.inheritance_dict = {}
        self.values_dict = {}
        self.process(self.cfg_content_holder[1])
        if self.table in TYPE_DICTS:
            self.type_dict = TYPE_DICTS.get(self.table)
            for key, value in self.type_dict.items():
                for _class in get_type(key, self.inheritance_dict):
                    self.values_dict[_class]['type'] = value

        log.info(glog.class_initiated(self.__class__))

    def process(self, in_parsed_cfg):
        self.get_classnames_and_inheritance(in_parsed_cfg)
        self.get_values(in_parsed_cfg)
        self.get_missing_from_parent()
        log.info(f"Processing data for table '{self.section.casefold()}_items_tbl' from section '{self.section}' complete!")

    def condense_content(self, in_full_cfg, in_next_section):
        if in_next_section is not None:
            _section_regex = re.compile(f"class {self.section}.*?(?=class {in_next_section})", re.DOTALL)
        else:
            _section_regex = re.compile(f"class {self.section}.*", re.DOTALL)
        _result = _section_regex.search(in_full_cfg)
        _result = _result.group()
        # if self.section in ALL_CFG_SECTIONS:
        # writeit(pathmaker('cwd', 'dev_ressources', 'output', 'seperated_sections', self.section + '_seperated_section.md'), f'# {self.section}\n\n```cpp\n' + _result.strip().replace('\t', '  ').replace('\s', ' ').replace('\s\s', ' ') + '\n```\n\n')
        log.info("finished condensing section'{self.section}'")
        _temp_list = []
        for lines in _result.splitlines():
            if 'class' in lines and ':' in lines:
                _temp_list.append(lines)
        # writeit(self.section + '_condensed.txt', '\n'.join(_temp_list))
        return '\n'.join(_temp_list)

    def get_classnames_and_inheritance(self, in_parsed_cfg):

        for key in in_parsed_cfg['start'][self.section]:
            log.debug(f"found classname '{key}'")
            self.classes.append(key)
            _inheritance = 'none'
            for lines in self.seperated_content.strip().splitlines():
                if ' ' + key + ':' in lines:
                    _inheritance = lines.split(':')[1].strip()
                    break
            # _inheritance = re.search(f"(?<=class {key}: ).*", self.seperated_content)
            # if _inheritance is not None:
            #     _inheritance = _inheritance.group()
            # else:
            #     log.error(f"no inheritance found for '{key}'")
            #     _inheritance = 'none'
            if _inheritance == 'none':
                log.error(f"no inheritance found for '{key}'")
            self.inheritance_dict[key] = _inheritance

            log.debug(f"inheritance for class '{key}' found as ['{key}': '{_inheritance}']")

        log.debug(f"finished inheritance search for section {self.section}")

    def get_values(self, in_parsed_cfg):
        _term_list = ['displayname', 'scope', 'author', 'descriptionshort']
        if self.section == 'CfgVehicles':
            _term_list.append('editorpreview')
        elif self.section == 'CfgUnitInsignia':
            _term_list.append('texture')
        elif self.section == 'CfgFactionClasses':
            _term_list.append('icon')
        else:
            _term_list.append('picture')
        for _classname in self.classes:
            self.values_dict[_classname] = {'displayName': 'none', 'descriptionShort': 'none', 'mod': 'none', 'scope': 'none', 'picture': 'none'}
            if isinstance(in_parsed_cfg['start'][self.section][_classname], dict):
                for key, value in in_parsed_cfg['start'][self.section][_classname].items():
                    if key == 'DLC':
                        self.values_dict[_classname][key] = value
                    elif key == 'author':

                        self.values_dict[_classname]['mod'] = value
                    elif key.casefold() in _term_list:
                        self.values_dict[_classname][key] = value
            else:
                log.error(f"Item '{in_parsed_cfg['start'][self.section][_classname]}' is not a dict!")

    def get_missing_from_parent(self):
        self.classes.append('Default')
        self.classes.append('access')
        self.inheritance_dict['Default'] = 'none'
        self.inheritance_dict['access'] = 'none'
        self.values_dict['Default'] = {}
        self.values_dict['access'] = {}
        self.values_dict['Default']['mod'] = 'Bohemia Interactive'
        self.values_dict['access']['mod'] = 'Bohemia Interactive'
        for _class, _value in self.values_dict.items():
            if 'tf' in _class:
                self.values_dict[_class]['mod'] = 'Taskforce'
            elif 'rhs_' in _class:
                self.values_dict[_class]['mod'] = 'Red Hammer Studios'
            for key, _attribute in _value.items():
                if _attribute == 'none':
                    self._get_missing_helper(_class, key)

    def _get_missing_helper(self, in_class, in_key):

        orig_class = in_class
        _temp_name = in_class
        while self.values_dict[orig_class][in_key] == 'none':
            try:
                _parent = self.inheritance_dict[_temp_name]
                self.values_dict[orig_class][in_key] = self.values_dict[_parent][in_key]
                _old_temp_name = _temp_name
                _temp_name = _parent
                if _parent == 'none' or _old_temp_name == _temp_name:
                    break
            except KeyError:
                log.error(f"KEYERROR No value for '{in_key}' found inside inheritance Tree of '{orig_class}'")
                break
        log.debug(f"value for '{in_key}' was set to '{self.values_dict[orig_class][in_key]}' for '{orig_class}'")

    def to_db(self, in_db):
        _table_name = f'{self.section.casefold()}_items_tbl'
        _phrase_list = []
        for _classname, column_dict in self.values_dict.items():
            _displayname = column_dict.get('displayName', 'none').replace('"', "'")
            _description_short = column_dict.get('descriptionShort', 'none')
            _inheritance = self.inheritance_dict.get(_classname, 'none')
            _mod = column_dict.get('mod', 'none')
            _scope = column_dict.get('scope', 'none')
            _type = column_dict.get('type', 'none')
            if self.section == 'CfgVehicles':
                _preview_location = column_dict.get('editorPreview', 'none')
            elif self.section == 'CfgUnitInsignia':
                _preview_location = column_dict.get('texture', 'none')
            elif self.section == 'CfgFactionClasses':
                _preview_location = column_dict.get('icon', 'none')
            else:
                _preview_location = column_dict.get('picture', 'none')
                if _preview_location in PICTURE_ALIASES:
                    _preview_location = PICTURE_ALIASES.get(_preview_location)
            _phrase = f"""INSERT OR IGNORE INTO "{_table_name}"
             ("item_classname", "item_displayname", "item_inheritance", "item_mod", "item_scope","item_type", "item_descriptionShort", "item_preview_location")
             VALUES ("{_classname}", "{_displayname}", "{_inheritance}", "{_mod}", "{_scope}", "{_type}", "{_description_short}", "{_preview_location}")"""
            _phrase_list.append(_phrase)
        in_db.executor(';'.join(_phrase_list), is_script=True)

# endregion [Class_5]


# region [Class_6]

class MasterSorterHolder:
    subtable_list = [
        'dlc_tbl',
        'mod_tbl',
    ]

    def __init__(self, in_dict_holder):
        self.cfg_content_holder = in_dict_holder
        self.cfg_content, self.parsed_cfg, self.parsed_as_benedict = self.cfg_content_holder()
        self.tablers = {}

        self.full_section_list = self.get_all_sections()
        log.info(glog.class_initiated(self.__class__))

    def get_all_sections(self):
        _list_1 = []
        _list_2 = []
        for lines in self.cfg_content.splitlines():
            if 'class cfg' in lines.casefold():
                _list_1.append(lines)
        for lines in _list_1:
            if lines.startswith('	c') and ':' not in lines:
                _list_2.append(lines.strip().replace('class ', ''))
        return _list_2

    def get_new_tabler(self, in_section):
        _section_index = self.full_section_list.index(in_section)
        try:
            _next_index = self.full_section_list[_section_index + 1]
        except IndexError:
            log.error(f"Section '{in_section}' seems to be the last section")
            _next_index = None
        _tabler = SortedItemHolder(in_section, _next_index, self.cfg_content_holder)
        self.tablers[in_section] = _tabler
        return _tabler

    def __getitem__(self, key):
        return self.tablers[key]


# endregion [Class_6]


# region [Class_7]


# endregion [Class_7]


# region [Class_8]

class DictHandler:
    def __init__(self):
        self.u_cfg = GiUserConfig()
        self.cfg_path = pathmaker(self.u_cfg.cfg_dump_files['current_file'])
        self.content = self.read_content()
        self.parsed_content = self.select_parsed_content()
        self.parsed_as_benedict = 'none'

    def select_parsed_content(self):
        _conf_hash_name = splitoff(self.cfg_path)[1].replace('.cpp', '')
        if ishash_same(self.cfg_path, _conf_hash_name) is True:
            _pickle_name = _conf_hash_name + '.pkl'
            _parsed_cfg = get_pickled(_pickle_name)
        else:
            _parsed_cfg = armaclass.parse(self.content)
            _pickle_name = _conf_hash_name + '.pkl'
            pickleit(_parsed_cfg, _pickle_name)
            hash_to_solidcfg(self.cfg_path, _conf_hash_name)

        _out = {}
        for key, value in _parsed_cfg.items():
            _out['start'] = value
        return _out

    def read_content(self, per_lines=False):
        if per_lines is False:
            _out = readit(self.cfg_path)
        else:
            _out = linereadit(self.cfg_path)
        return _out

    def __call__(self):
        return (self.content, self.parsed_content, self.parsed_as_benedict)

# endregion [Class_8]


# region [Class_9]

class ACPTableViewModel(QAbstractTableModel):
    def __init__(self, in_db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.execute = in_db.executor
        self.table = ''
        self._data = []
        self.header = []

    def set_table(self, in_table):
        if '_items_tbl' in in_table.casefold():
            self.table = in_table
        else:
            self.table = in_table.casefold() + '_items_tbl'

        self.header = HEADER_DICT.get(self.table, STD_HEADER)

    def query_data(self):
        self._data = []
        _phrase = f'SELECT * from "{self.table}"'
        _results = self.execute(_phrase)
        for row in _results:
            row_data = tuple(row)
            self._data.append(row_data)

    def query_image(self, _index):
        _phrase = f'SELECT "blob_data" FROM "image_blob_tbl" WHERE "blob_id" = "{_index}"'
        _result = self.execute(_phrase, fetch='one')
        return _result[0]

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.BackgroundRole:
            if self._data[index.row()][-1] is not None and self._data[index.row()][-1] != 'none' and self._data[index.row()][-1] != '':
                return QBrush(QColor(0, 200, 0, 50))
            else:
                return QBrush(QColor(200, 0, 0, 50))

    def present_image(self, row):
        if self._data[row][-1] is not None and self._data[row][-1] != 'none' and self._data[row][-1] != '':
            _image = self.query_image(self._data[row][-1])
            _pixmapimage = QPixmap()
            _pixmapimage.loadFromData(_image)

            return _pixmapimage

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, parent):
        return len(self.header)

    def search(self, in_text, in_name_type):
        _out_list = []
        for index, row in enumerate(self._data):
            if in_name_type == 'classname':
                if in_text.casefold() in row[1].casefold():
                    _out_list.append(index)
            elif in_name_type == 'displayname':
                if in_text.casefold() in row[2].casefold():
                    _out_list.append(index)
        return _out_list


# endregion [Class_9]

# region [Main_Exec]
if __name__ == '__main__':
    pass


# endregion [Main_Exec]
