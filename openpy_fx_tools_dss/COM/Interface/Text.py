# -*- coding: utf-8 -*-
# @Time    : 02/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Text.py
# @Software: PyCharm

import logging
from openpy_fx_tools_dss.logg_print_alert import logg_alert

class Text:
    """
    This interface is the general command interpreter for OpenDSS.
    It executes commands and queries and return results just like the OpenDSS edit window in the Executable.
    This is one of the most used interfaces when driving OpenDSS through COM.
    The Text interface is exposed directly by the OpenDSSEngine.
    """
    def __init__(self, DSSObject):
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text

    def compile(self, path_DSS: str):
        '''
        :param path_DSS: path to the file with .DSS extension
        :return:
        '''
        self.DSSText.Command = "Compile " + path_DSS

    def Command(self, parameter : str):
        if parameter == '':
            print('must insert a command')
            exit()
        else:
            self.DSSText.Command = parameter
