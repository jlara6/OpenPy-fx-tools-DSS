# -*- coding: utf-8 -*-
# @Time    : 26/08/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : IMEX_init.py
# @Software: PyCharm

from .lib_py_base import DSS_xlsx_save
from .IMEX_to_DSS.xlsx_DSS_xlsx.base_xlsx_DSS import class_xlsx_to_DSS

aux_xlsx = class_xlsx_to_DSS()

class xlsx_DSS_xlsx:

    def create_template_xlsx(self):
        """
        Generate .xlsx template for OpenDSS xlsx_data entry

        :return: .xlsx files
        """
        aux_xlsx._template_xlsx()

    def xlsx_to_OpenDSS(
            self, xlsx_path: str = None, path_save: str = None, prj_name: str = 'default', add_path: bool = True,
            coords: str = 'XY'):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :param xlsx_path:
        :param path_save:
        :param prj_name:
        :param add_path:
        :param coords:
        :return:
        """
        aux_xlsx._create_DSS_from_xlsx(xlsx_path, path_save, prj_name, add_path, coords)

    def OpenDSS_to_xlsx(self, DSS_path: str = None, path_save: str = None, prj_name: str = 'default'):
        """
        Generates .xlsx template with xlsx_data from OpenDSS scripts

        :param DSS_path:
        :param path_save:
        :param prj_name:
        :return:
        """
        aux_xlsx._create_from_DSS_scripts_to_xlsx(DSS_path, path_save, prj_name)
