# -*- coding: utf-8 -*-
# @Time    : 26/10/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import os
import pathlib
import logging
from ..logg_print_alert import logg_alert

log_py = logging.getLogger(__name__)


def _load_files_examples(Opt: int):
    script_path = os.path.dirname(os.path.abspath(__file__))
    xlsx_info = dict()
    if Opt == 1:
        xlsx_info['xlsx_path'] = pathlib.Path(script_path).joinpath("./examples", "13NodeIEEE", "13NodeIEEE.xlsx")
        xlsx_info['prj_name'] = '13nodeIEEE'

    res = not xlsx_info
    if res:
        logg_alert.update_logg_file('Select an uploaded example, see documentation', 4, log_py)
        exit()

    return xlsx_info
