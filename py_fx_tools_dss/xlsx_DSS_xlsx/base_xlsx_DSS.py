# -*- coding: utf-8 -*-
# @Time    : 26/10/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : base_xlsx_DSS.py
# @Software: PyCharm

import logging
from ..lib_py_base import base_xlsx_DSS
from .DSS_script import create_scrips_base_dss
from ..logg_print_alert import logg_alert
from .xlsx_files_examples import _load_files_examples

log_py = logging.getLogger(__name__)




def Load_examples_xlsx_files(option: int = None):
    """
     Within the module, look for the selected option in the examples tab. Return a dictionary with the keys
    ['xlsx_path'] and ['prj_name'].

    :param option: Option select. Default is None.
    :return: xlsx_dict
    """
    xlsx_dict = _load_files_examples(Opt=option)
    return xlsx_dict


class xlsx_DSS(base_xlsx_DSS):

    def __init__(self, DSS_path: str = None, xlsx_path: str = None, path_save: str = None, prj_name: str = None):
        """
        Class that initializes all xlsx routines to OpenDSS and OpenDSS to xlsx.

        :param DSS_path: Path to the OpenDSS files. Defaults is None.
        :param xlsx_path: Path to the .xlsx files. Defaults is None.
        :param path_save: Path where output files will be saved. Defaults is None.
        :param prj_name: Name of the project or case study. Defaults is None.
        """
        base_xlsx_DSS.__init__(self, DSS_path, xlsx_path, path_save)
        self.prj_name = prj_name



    def template_xlsx(self, prj_name: str = None):
        """
        creates xlsx template in the path entered

        :return: xlsx file
        """
        pass

    def create_DSS_from_xlsx(self, prj_name: str = 'default'):
        """
        Generate OpenDSS files, according to the information found in the xlsx template.

        :return: DSS files
        """
        if self.prj_name is None:
            self.prj_name = 'default'


        file_BBDD = f'{address_saves}\BBDD_DSS_{name_dss}.xlsx'
        directory = os.chdir(address_saves)
        create_scrips_base_dss(name_dss=self.prj_name, xlsx_file=file_BBDD, file_path=self.path_save)
        logg_alert.update_logg_file(f'The .DSS files are saved in:\n {self.path_save}')
        print(f'The files are located at:\n {address_saves}')

        pass


