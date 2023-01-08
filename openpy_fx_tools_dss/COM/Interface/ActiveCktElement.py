# -*- coding: utf-8 -*-
# @Time    : 07/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ActiveCktElement.py
# @Software: PyCharm

from .Base import Base

class ActiveCktElement(Base):
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSActiveElemen = self.DSSObject.ActiveCktElement
        