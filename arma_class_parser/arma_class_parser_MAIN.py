# region [Imports]

# *NORMAL Imports -->
import sys
import os
# *GID Imports -->
from gidqtutils.gidqtstuff import buttongroup_factory
from gidtools.gidtriumvirate import GidSQLBuilder
import gidlogger as glog

# *QT Imports -->
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCompleter

# *Local Imports -->
from ui_Arma_class_parser_maininterface import Ui_Arma_Class_parser_maingui
from arma_class_parser_DATA import ALL_CFG_SECTIONS, TYPE_DICTS
from arma_class_parser_classes import ACPTableViewModel, DictHandler

# endregion [Imports]

__updated__ = '2020-09-06 15:59:25'


# region [Logging]

_log_file = glog.log_folderer('__main__')
log = glog.main_logger(_log_file, 'DEBUG')
log.info(glog.NEWRUN())

# endregion [Logging]


# region [Constants]


# endregion [Constants]


# region [Misc]


# endregion [Misc]


# region [GUI_MainWindow]

class ArmaClassParserMainWindow(Ui_Arma_Class_parser_maingui):
    def __init__(self, mainwindow):
        super().setupUi(mainwindow)
        self.dict_handler = DictHandler()
        self.content, self.parsed_content, self.parsed_as_benedict = self.dict_handler()
        self.db = GidSQLBuilder.get_database()
        self.tablemodel = ACPTableViewModel(self.db)
        self.autocomplete_BG = buttongroup_factory(self.use_classnames_radioButton, self.use_displaynames_radioButton)
        self.tabWidget.setCurrentIndex(0)
        self.dockWidget_2.setFloating(True)
        self.fill_combos()
        self.update()
        self.actions()

    def actions(self):
        self.cfg_selection_search_comboBox.activated.connect(self.update)
        self.cfg_selection_search_comboBox.activated.connect(self.type_combo_fill)
        self.search_comboinput_comboBox.activated.connect(self.filter_type)
        self.autocomplete_BG.buttonToggled.connect(self.set_up_completer)
        self.search_input_lineEdit.textChanged.connect(self.continous_search)
        self.output_tableView.clicked.connect(self.show_picture)
        self.only_with_images_checkBox.toggled.connect(self.filter_table)
        self.show_data_tree_pushButton.pressed.connect(self.create_data_tree)

    def filter_type(self):
        if self.search_comboinput_comboBox.currentText() != 'ALL':
            for i, _ in enumerate(self.tablemodel._data):
                if self.tablemodel._data[i][6].casefold() == self.search_comboinput_comboBox.currentText().casefold():
                    self.output_tableView.setRowHidden(i, False)

                else:
                    self.output_tableView.setRowHidden(i, True)
        else:
            for i, _ in enumerate(self.tablemodel._data):
                self.output_tableView.setRowHidden(i, False)

    def filter_table(self):
        for i, _ in enumerate(self.tablemodel._data):
            if self.only_with_images_checkBox.isChecked():
                if self.tablemodel._data[i][-1] is None or self.tablemodel._data[i][-1] == 'none' or self.tablemodel._data[i][-1] == '':
                    self.output_tableView.setRowHidden(i, True)
                else:
                    self.output_tableView.setRowHidden(i, False)
            else:
                self.output_tableView.setRowHidden(i, False)

    def show_picture(self, index):
        if self.tablemodel._data[index.row()][-1] is not None and self.tablemodel._data[index.row()][-1] != 'none' and self.tablemodel._data[index.row()][-1] != '':
            self.picture_label.clear()
            self.picture_label.setPixmap(self.tablemodel.present_image(index.row()))
            self.picture_label.adjustSize()

    def create_data_tree(self):
        if self.cfg_selection_search_comboBox.currentText() != 'CfgVehicles':
            self.plotting_DataTreeWidget.setData(self.parsed_content['start'][self.cfg_selection_search_comboBox.currentText()])
        # self.plotting_DataTreeWidget.update()

    def update(self):
        self.statusbar.showMessage(self.cfg_selection_search_comboBox.currentText())
        self.only_with_images_checkBox.setChecked(False)
        self.clear_all()
        self.set_up_completer()
        self.fill_table()

    def fill_table(self):
        self.search_comboinput_comboBox.setCurrentText('ALL')
        self.only_with_images_checkBox.setChecked(False)
        self.tablemodel.layoutAboutToBeChanged.emit()
        self.tablemodel.set_table(self.cfg_selection_search_comboBox.currentText().casefold())
        self.tablemodel.query_data()
        self.output_tableView.setModel(self.tablemodel)
        self.output_tableView.resizeColumnsToContents()
        self.output_tableView.setColumnHidden(0, True)
        self.check_column_visibility()
        self.tablemodel.layoutChanged.emit()

    def check_column_visibility(self):
        pass

    def continous_search(self):
        self.only_with_images_checkBox.setChecked(False)
        _text = self.search_input_lineEdit.text()
        _name_type = 'classname' if self.use_classnames_radioButton.isChecked() is True else 'displayname'
        for i, _ in enumerate(self.tablemodel._data):
            self.output_tableView.setRowHidden(i, True)
        for index in self.tablemodel.search(_text, _name_type):
            self.output_tableView.setRowHidden(index, False)

    def clear_all(self):
        self.plotting_DataTreeWidget.clear()

    def type_combo_fill(self):
        self.search_comboinput_comboBox.clear()
        self.search_comboinput_comboBox.addItem('ALL')
        _item_list = []
        for key, item in TYPE_DICTS.get(self.cfg_selection_search_comboBox.currentText().casefold() + '_items_tbl', 'none').items():
            if item not in _item_list:
                _item_list.append(item)
        self.search_comboinput_comboBox.addItems(_item_list)

    def fill_combos(self):
        self.cfg_selection_search_comboBox.clear()
        self.cfg_selection_search_comboBox.addItems(ALL_CFG_SECTIONS)
        self.cfg_selection_search_comboBox.setCurrentIndex(0)
        self.type_combo_fill()

    def set_up_completer(self):
        _name_list = []
        _table = self.cfg_selection_search_comboBox.currentText().casefold() + '_items_tbl'
        if self.use_classnames_radioButton.isChecked() is True:
            _name_cat = "item_classname"
        else:
            _name_cat = "item_displayname"
        _phrase = f'SELECT "{_name_cat}" FROM "{_table}"'
        _results = self.db.executor(_phrase)
        for _names in _results:
            _name_list.append(_names[0])
        self.completer = QCompleter(_name_list)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.search_input_lineEdit.setCompleter(self.completer)


# endregion [GUI_MainWindow]

# region [GUI_SettingsWindow]

# endregion [GUI_SettingsWindow]

# region [Dialog_1]

# endregion [Dialog_1]

# region [Dialog_2]

# endregion [Dialog_2]

# region [Dialog_3]

# endregion [Dialog_3]

# region [Dialog_4]

# endregion [Dialog_4]

# region [Dialog_5]

# endregion [Dialog_5]

# region [Main_Exec]

if __name__ == '__main__':
    try:
        print(os.getcwd())
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = ArmaClassParserMainWindow(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except:
        log.exception(sys.exc_info()[0])
        raise

# endregion [Main_Exec]
