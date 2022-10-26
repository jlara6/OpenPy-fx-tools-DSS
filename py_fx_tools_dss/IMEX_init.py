# -*- coding: utf-8 -*-
# @Time    : 26/08/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : IMEX_init.py
# @Software: PyCharm

from .lib_py_base import DSS_xlsx_save
from .IMEX_to_DSS.xlsx_DSS_xlsx_mod.base_xlsx_DSS import _test_xlsx_files, class_xlsx_to_DSS

aux_xlsx = class_xlsx_to_DSS()

class xlsx_DSS_xlsx:

    def load_examples(self, Option: int = None) -> dict:
        """
        Within the module, look for the selected option in the examples tab. Return a dictionary with the keys
        ['xlsx_path'], ['path_save'] and ['prj_name'].

        :param Option: Option select. Default is None.
        :return: dict_xlsx
        """
        dict_xlsx = _test_xlsx_files(Opt=Option)

        return dict_xlsx

    def create_template_xlsx(self):
        """
        Generate .xlsx template for OpenDSS data entry

        :return: .xlsx files
        """
        aux_xlsx._template_xlsx()

    def xlsx_to_DSS_scripts(self, xlsx_path: str = None, path_save: str = None, prj_name: str = 'default', path: bool = True):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :param xlsx_path:
        :param path_save:
        :param prj_name:
        :param path:
        :return:
        """
        aux_xlsx._create_DSS_from_xlsx(xlsx_path, path_save, prj_name, path)

    def DSS_scripts_to_xlsx(self, DSS_path: str = None, path_save: str = None):
        """
        Generates .xlsx template with data from OpenDSS scripts

        :param DSS_path:
        :param path_save:
        :return:
        """
