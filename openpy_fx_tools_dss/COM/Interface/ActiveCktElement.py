# -*- coding: utf-8 -*-
# @Time    : 07/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ActiveCktElement.py
# @Software: PyCharm

from .Base import Base

class ActiveCktElement(Base):
    """
    This interface can be used to gain access to the features of the active circuit element without having to use a specific element interface.
    This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to ActiveCktElement interface.
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSLoads = self.DSSCircuit.Loads
        self.DSSActiveElement = self.DSSCircuit.ActiveCktElement
    def AllPropertyNames(self, elem_DSS: str = None):
        """
        (read only) - This property returns a variant array (strings) containing all property names of the active device.

        :param elem_DSS:
        :return:
        """
        if ActiveCktElement(self.DSSObject)._check_element(elem_DSS):
            self.DSSCircuit.SetActiveElement(elem_DSS)
            return self.Base._tuple_to_list(self.DSSActiveElement.AllPropertyNames)
        else:
            return None
    def AllVariableNames(self, elem_DSS: str = None):
        """
        (read only) - This property returns a variant array of strings listing all the published variable names,
        if a PCElement. Otherwise, null string.

        :param elem_DSS:
        :return:
        """
        if ActiveCktElement(self.DSSObject)._check_element(elem_DSS):
            self.DSSCircuit.SetActiveElement(elem_DSS)
            return self.DSSActiveElement.AllVariableNames
        else:
            return None
    def AllVariableValues(self, elem_DSS: str = None):
        """
        (read only) - This property returns a variant array of strings listing all the published variable names,
        if a PCElement. Otherwise, null string.

        :param elem_DSS:
        :return:
        """
        if ActiveCktElement(self.DSSObject)._check_element(elem_DSS):
            self.DSSCircuit.SetActiveElement(elem_DSS)
            return self.DSSActiveElement.AllVariableValues
        else:
            return None
    def BusNames_read(self):
        """
        (read/write) This property set/get a variant array of strings.
        Get  Bus definitions to which each terminal is connected. 0-based array.

        :param elem_DSS:
        :return:
        """
        if self.DSSLoads.First > 0:
            return self.DSSActiveElement.BusNames
        else:
            print('It seems that you have no loads!');

    def BusNames_write(self, elem_DSS: str = None, parameter: str = None):
        """
        (read/write) This property set/get a variant array of strings.
        Get  Bus definitions to which each terminal is connected. 0-based array.

        :param elem_DSS:
        :return:
        """
        if ActiveCktElement(self.DSSObject)._check_element(elem_DSS):
            self.DSSCircuit.SetActiveElement(elem_DSS)
            self.DSSActiveElement.Close(1,0);

    def Close(self, elem_DSS: str = None, parameter: int = None):
        """
        (write only) This method closes the specified terminal and phase, if non-zero.  Else all conductors at terminal.

        """
        if ActiveCktElement(self.DSSObject)._check_element(elem_DSS):
            self.DSSCircuit.SetActiveElement(elem_DSS)
            parameter = self.DSSActiveElement.BusNames

    def _check_element(self, parameter):
        self.DSSActiveClass = self.DSSCircuit.ActiveClass
        class_DSS, name_DSS = self.Base._extract_class_name(parameter)
        self.DSSCircuit.SetActiveClass(class_DSS)
        aux = name_DSS in self.DSSActiveClass.AllNames
        if not aux:
            print(f'Data {parameter}, does not belong to the circuit.')
            return False
        else:
            return True



