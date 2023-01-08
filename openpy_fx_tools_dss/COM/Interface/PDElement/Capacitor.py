# -*- coding: utf-8 -*-
# @Time    : 08/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Capacitor.py
# @Software: PyCharm

from openpy_fx_tools_dss.COM.Interface.Base import Base

class Capacitor(Base):
    """
    This interface can be used to gain access to the features and properties of all the capacitors deployed across the model.
    Because it is embedded within the ActiveCircuit interface, requires the definition of this interface before getting
    access the to Capacitors interface.
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSCapacitors = self.DSSCircuit.Capacitors
    def AllNames(self):
        """
        (read only) - This property returns the names for all the capacitors defined within the model.
        The names are returned as an array of string.

        :return:
        """
        return self.Base._tuple_to_list(self.DSSCapacitors.AllNames)
    def AvailableSteps(self):
        """
        (read only) - This property returns the number of Steps available in the active cap bank to be switched ON.

        :return:
        """
        return self.DSSCapacitors.AvailableSteps
    def Close(self):
        """
        (method) - Close all steps, all phases of the active Capacitor

        :return:
        """
        return self.DSSCapacitors.Close()
    def Count(self):
        """
        (read only) - This property returns the number capacitors defined within the circuit.

        :return:
        """
        return self.DSSCapacitors.Count
    def First(self):
        return self.DSSCapacitors.First
    def IsDelta(self):
        return self.DSSCapacitors.IsDelta
    def kV(self):
        return self.DSSCapacitors.kV
    def Name(self):
        return self.DSSCapacitors.Name
    def Next(self):
        return self.DSSCapacitors.Next
    def NumSteps(self):
        return self.DSSCapacitors.NumSteps
    def Open(self):
        return self.DSSCapacitors.Open()
    def States(self):
        return self.DSSCapacitors.States