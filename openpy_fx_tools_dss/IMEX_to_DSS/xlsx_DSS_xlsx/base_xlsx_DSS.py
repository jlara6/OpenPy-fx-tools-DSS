# -*- coding: utf-8 -*-
# @Time    : 26/10/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : DSS_xlsx_save.py
# @Software: PyCharm

import logging
import os
import pathlib
from ...lib_py_base import DSS_xlsx_save
from .DSS_script import create_scrips_base_dss
from ...logg_print_alert import logg_alert
from .create_file_xlsx import _Create_DSS_to_xlsx_files

log_py = logging.getLogger(__name__)

class class_xlsx_to_DSS:

    def _template_xlsx(self) -> object:
        """
        creates xlsx template in the path_save entered

        :return: xlsx file
        """
        logg_alert.update_logg_file('The function that creates the xlsx template is under development', 3, log_py)

    def _create_DSS_from_xlsx(self, xlsx_path: str, path_save: str, prj_name: str, path: bool, coords: str):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :return: DSS files
        """
        if prj_name is None:
            prj_name = 'default'
            logg_alert.alert_messages('OpenDSS scripts are called ClassName_default.DSS', 3)
        create_scrips_base_dss(
            name_dss=prj_name,
            xlsx_file=xlsx_path,
            path_save=path_save,
            add_path=path,
            coords=coords)
        logg_alert.update_logg_file(f'The .DSS files are saved in:\n {path_save}')


    def _create_from_DSS_scripts_to_xlsx(self, DSS_path: str, path_save: str, prj_name: str):

        aux_save = path_save is None
        aux_DSS = DSS_path is None

        if aux_save and aux_DSS:
            logg_alert.update_logg_file(
                'You must indicate the path_save to save the .xlsx file and path_save to OpenDSS files.', 4, log_py)
            exit()
        elif aux_save:
            logg_alert.update_logg_file('You must indicate the path_save to save the .xlsx file.', 4, log_py)
            exit()
        elif aux_DSS:
            logg_alert.update_logg_file('You must indicate the path_save to OpenDSS files', 4, log_py)
            exit()
        else:
            _Create_DSS_to_xlsx_files(DSS_path, path_save, prj_name)


