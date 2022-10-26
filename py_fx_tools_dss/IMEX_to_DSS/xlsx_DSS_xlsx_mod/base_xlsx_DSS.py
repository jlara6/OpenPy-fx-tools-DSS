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

log_py = logging.getLogger(__name__)

def _test_xlsx_files(Opt: int) -> object:
    """
     Within the module, look for the selected option in the examples tab. Return a dictionary with the keys
    ['xlsx_path'] and ['prj_name'].

    :rtype: object
    :param option: Option select. Default is None.
    :return: xlsx_dict
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    xlsx_info = dict()
    if Opt == 1:
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath("Examples", "13NodeIEEE", "13NodeIEEE.xlsx")
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

    def _create_DSS_from_xlsx(self, xlsx_path: str, path_save: str, prj_name: str):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :return: DSS files
        """
        if prj_name is None:
            prj_name = 'default'
            logg_alert.alert_messages('OpenDSS scripts are called Script_default.DSS', 3)

        create_scrips_base_dss(name_dss=prj_name, xlsx_file=xlsx_path, file_path=path_save)
        logg_alert.update_logg_file(f'The .DSS files are saved in:\n {path_save}')


