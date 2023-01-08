# -*- coding: utf-8 -*-
# @Time    : 02/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : COM_Interface.py
# @Software: PyCharm

import win32com.client
from openpy_fx_tools_dss.COM.Interface.ActiveBus import ActiveBus
from openpy_fx_tools_dss.COM.Interface.ActiveCktElement import ActiveCktElement
from openpy_fx_tools_dss.COM.Interface.ActiveClass import ActiveClass
from openpy_fx_tools_dss.COM.Interface.ActiveDSSElement import ActiveDSSElement
from openpy_fx_tools_dss.COM.Interface.PDElement.Capacitor import Capacitor
from openpy_fx_tools_dss.COM.Interface.Text import Text

class COM_DLL:

    def __init__(self):
        self.DSSObject = _Check_DSS_Connection()
        self.Text = self.DSSObject.Text
        self.Text.Command = "Clear"

        self.Text = Text(self.DSSObject)
        self.ActiveBus = ActiveBus(self.DSSObject)
        self.ActiveCktElement = ActiveCktElement(self.DSSObject)
        self.ActiveClass = ActiveClass(self.DSSObject)
        self.ActiveDSSElement = ActiveDSSElement(self.DSSObject)
        self.Capacitor = Capacitor(self.DSSObject)
def _Check_DSS_Connection(DSSObject=None, version:bool=True):

    DSSObject = win32com.client.Dispatch("OpenDSSEngine.DSS")
    DSSObject.Start("0")

    if DSSObject.Start("0") == False:
        print("DSS Failed to Start")
        exit()
    else:
        if version:
            print(f'{DSSObject.Version}\n')
    return DSSObject
