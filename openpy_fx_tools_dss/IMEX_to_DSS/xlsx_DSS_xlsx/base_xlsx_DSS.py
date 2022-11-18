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

def _test_DSS_files(Opt: int):
    script_path = os.path.dirname(os.path.abspath(__file__))
    DSS_info = dict()
    if Opt == 1:
        DSS_info['DSS_path'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE", "Empty.dss")
        DSS_info['path_save'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE")
        DSS_info['prj_name'] = 'default'

    if Opt == 2:
        DSS_info['DSS_path'] = pathlib.Path(script_path).joinpath(
            "Examples", "13NodeIEEE", "DSS_files", "IEEE13Nodeckt.dss")
        DSS_info['path_save'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE", "xlsx_files")
        DSS_info['prj_name'] = '13nodeIEEE'

    if Opt == 3:
        DSS_info['DSS_path'] = pathlib.Path(script_path).joinpath(
            "Examples", "37Bus", "DSS_files", "ieee37.dss")
        DSS_info['path_save'] = pathlib.Path(script_path).joinpath("Examples", "37Bus", "xlsx_files")
        DSS_info['prj_name'] = '37BusIEEE'

    return DSS_info


def _test_xlsx_files(Opt: int) -> object:
    script_path = os.path.dirname(os.path.abspath(__file__))
    xlsx_info = dict()
    if Opt == 2:
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath(
            "Examples", "13NodeIEEE", "xlsx_files", "BBDD_DSS_13nodeIEEE.xlsx")
        xlsx_info['path_save'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE", "xlsx_files")
        xlsx_info['prj_name'] = '13nodeIEEE'

    if Opt == 3:
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath(
            "Examples", "37Bus", "xlsx_files", "BBDD_DSS_37BusIEEE.xlsx")
        xlsx_info['path_save'] = pathlib.Path(script_path).joinpath("Examples", "37Bus", "xlsx_files")
        xlsx_info['prj_name'] = '37BusIEEE'


    res = not xlsx_info
    if res:
        logg_alert.update_logg_file('Select an uploaded example, see documentation', 4, log_py)
        exit()

    return xlsx_info

class class_xlsx_to_DSS:

    def _template_xlsx(self) -> object:
        """
        creates xlsx template in the path_save entered

        :return: xlsx file
        """
        logg_alert.update_logg_file('The function that creates the xlsx template is under development', 3, log_py)

    def _create_DSS_from_xlsx(self, xlsx_path: str, path_save: str, prj_name: str, path: bool):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :return: DSS files
        """
        if prj_name is None:
            prj_name = 'default'
            logg_alert.alert_messages('OpenDSS scripts are called ClassName_default.DSS', 3)

        create_scrips_base_dss(name_dss=prj_name, xlsx_file=xlsx_path, path_save=path_save, add_path=path)
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


