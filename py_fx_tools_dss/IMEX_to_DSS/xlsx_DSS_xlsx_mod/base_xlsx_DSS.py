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

def _test_xlsx_files(Opt: int) -> object:
    script_path = os.path.dirname(os.path.abspath(__file__))
    xlsx_info = dict()
    if Opt == 1:
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE", "13NodeIEEE.xlsx")
        xlsx_info['path_save'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE")
        xlsx_info['prj_name'] = '13nodeIEEE'


    res = not xlsx_info
    if res:
        logg_alert.update_logg_file('Select an uploaded example, see documentation', 4, log_py)
        exit()

    return xlsx_info

class class_xlsx_to_DSS:

    def _template_xlsx(self) -> object:
        """
        creates xlsx template in the path entered

        :return: xlsx file
        """
        print('The function that creates the xlsx template is under development.')

    def _create_DSS_from_xlsx(self, xlsx_path: str, path_save: str, prj_name: str, path: bool):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :return: DSS files
        """
        if prj_name is None:
            prj_name = 'default'
            logg_alert.alert_messages('OpenDSS scripts are called Script_default.DSS', 3)

        create_scrips_base_dss(name_dss=prj_name, xlsx_file=xlsx_path, path_save=path_save, path=path)
        logg_alert.update_logg_file(f'The .DSS files are saved in:\n {path_save}')


    def _create_xlsx_from_DSS(self, DSS_path: str, path_save: str, prj_name: str):

        aux_save = path_save is None
        aux_DSS = DSS_path is None
        if aux_save == True and aux_DSS == True:
            logg_alert.update_logg_file(
                'You must indicate the path to save the .xlsx file and path to OpenDSS files.', 4, log_py)
            exit()
        elif aux_save:
            logg_alert.update_logg_file('You must indicate the path to save the .xlsx file.', 4, log_py)
            exit()
        elif aux_DSS:
            logg_alert.update_logg_file('You must indicate the path to OpenDSS files', 4, log_py)
            exit()
        else:
            _Create_DSS_to_xlsx_files(DSS_path, path_save, prj_name)
