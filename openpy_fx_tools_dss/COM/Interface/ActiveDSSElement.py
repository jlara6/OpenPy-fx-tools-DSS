# -*- coding: utf-8 -*-
# @Time    : 07/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ActiveDSSElement.py
# @Software: PyCharm

from .Base import Base

class ActiveDSSElement(Base):
    """
    This interface can be used to examine the properties of the active DSS object.
    This interface is embedded within the ActiveCircuit interface,
    requiring the definition of this interface before getting access the to ActiveDSSElement interface.
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSElement = self.DSSCircuit.ActiveDSSElement

    def AllPropertyNames(self, ClassName: str = None):
        """
        (read only) - This property returns a variant array (strings) containing all property names of the active DSS object.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.Base._tuple_to_list(self.DSSElement.AllPropertyNames)
    def Name(self):
        """
        (read only) - This property returns the name of the active DSS object.

        :param ClassName:
        :return:
        """
        return self.DSSElement.Name
    def NumProperties(self):
        """
        (read only) - This property returns the number of properties of the active DSS object.

        :return:
        """
        return self.DSSElement.NumProperties
    def Properties_read(self, property: str = None):
        """
        (read/write) - This method returns the Collection of properties for Active DSS object (general element or circuit element).
        The property name has to be specified in the argument. use this method to get the value of a particular property
        of the active element in case this is not included in the specific interface.

        :return:
        """
        return self.DSSElement.Properties(property).Val
    def Properties_write(self, property: str = None, value = None):
        """
        (read/write) - This method returns the Collection of properties for Active DSS object (general element or circuit element).
        The property name has to be specified in the argument. use this method to get the value of a particular property
        of the active element in case this is not included in the specific interface.

        :return:
        """
        self.DSSElement.Properties(property).Val = value