# -*- coding: utf-8 -*-
# @Time    : 02/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Base.py
# @Software: PyCharm

import numpy as np

class Base:
    def __init__(self, DSSObject):
        self.DSSObject = DSSObject

    def _tuple_to_list(self, parameter: tuple):
        return list(parameter)

    def _tuple_to_ndarray(self, parameter: tuple):
        return np.asarray(parameter)

    def _check_str(self, parameter):
        pass