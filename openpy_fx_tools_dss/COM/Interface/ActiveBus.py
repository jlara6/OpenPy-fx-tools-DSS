# -*- coding: utf-8 -*-
# @Time    : 02/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ActiveBus.py
# @Software: PyCharm

from .Base import Base

def check_bus(myBus):
    DSSText = dss_engine.Text
    DSSCircuit = dss_engine.ActiveCircuit

    myBusNames = DSSCircuit.AllBusNames
    aux = myBus in myBusNames
    if not aux:
        print('The Bus entered is not in the circuit.')
        exit()

class ActiveBus(Base):

    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSActiveBus = self.DSSCircuit.ActiveBus

    def AllPCEatBus(self, myBus: str) -> list:
        """
        (read only) - This property returns the names of all power conversion elements (PCE) connected to the active bus. The names are returned as list of string.

        :param myBus: Bus name of interest
        :return: list[str]
        """
        self.Base._tuple_to_list(myBus)
        if ActiveBus(self.DSSObject)._check_bus(myBus):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.AllPCEatBus)
        else:
            return None

    def AllPDEatBus(self, myBus: str):
        """
        (read only) - This property returns the names of all power delivery elements (PDE) connected to the active bus. The names are returned as list of string.

        :return:
        :param myBus: Bus name of interest
        :return: list[str]
        """
        if ActiveBus(self.DSSObject)._check_bus(myBus):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.AllPDEatBus)
        else:
            return None

    def Coorddefined(self, myBus: str) -> bool:
        """
        (read only) - This property returns False=0 else True. Indicates whether a coordinate has been defined for this bus.

        :param myBus: Bus name of interest
        :return: bool
        """
        if ActiveBus(self.DSSObject)._check_bus(myBus):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Coorddefined
        else:
            return None

    def CplxSeqVoltages(self, myBus: str, rect: bool = False, polar: bool = True):
        """
        (read only) - This property returns a complex or polar of Sequence Voltages (0, 1, 2) at this Bus.

        :param myBus: Bus name of interest
        :param rect: For complex. The default is False
        :param polar: For polar. The default is True
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(myBus):
            self.DSSCircuit.SetActiveBus(myBus)

        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        mySeqVolt = self.DSSActiveBus.CplxSeqVoltages
        return data_rect_polar(mySeqVolt, rect, polar)

    def cust_duration(self, myBus: str):
        """
        (read only) - This property returns the accumulated customer outage duration for the active bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Cust_Duration

    def cust_interrupts(self, myBus: str):
        """
        (read only) - This property returns the accumulated number of customer-interruptions from the active bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Cust_Interrupts

    def distance(self, myBus: str):
        """
        (read only) - This property returns the distance to the active bus from energymeter (if non-zero).

        :param myBus:
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Distance

    def get_unique_node_number(self, myBus, StartNumber: int = 1):
        """
        (read only) - This method returns a unique node number at the active bus to avoid node collisions and adds it to the node list for the bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.GetUniqueNodeNumber(StartNumber)

    def int_duration(self, myBus: str):
        """
        (read only) - This property returns the average interruption duration in hours.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Int_Duration

    def Isc_Icc(self, myBus, rect: bool = False, polar: bool = True):
        """
        (read only) - This property returns the short circuit currents at the active bus. The values are returned as a complex or polar list.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        myIsc = self.DSSActiveBus.Isc
        return data_rect_polar(myIsc, rect, polar)

    def kVBase(self, myBus):
        """
        (read only) - This property returns the Base voltage at the active bus in kV.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.kVBase

    def Lambda(self, myBus):
        """
        (read only) - This property returns the accumulated failure rate downstream from this bus; faults per year.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Lambda

    def latitude(self, myBus):
        """
        (read/write) - This property allows to read/write the latitude in GIS coordinates for the active bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return print('development')

    def longitude(self, myBus):
        """
        (read/write) - This property allows to read/write the longitude in GIS coordinates for the active bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return print('development')

    def line_list(self, myBus):
        """
        (read only) - This property returns a Variant Array of Strings containing the list of LINE elements connected to the active bus. Complete name Line.xxxx.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.LineList

    def load_list(self, myBus):
        """
        (read only) - Tis property returns the names of all power conversion elements (PCE) connected to the active bus. The names are returned as an array of string.


        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.LoadList

    def n_customers(self, myBus):
        """
        (read only) - This property returns the total numbers of customers served down-line from the active bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.N_Customers

    def n_interrupts(self, myBus):
        """
        (read only) - This property returns the Number of interruptions per year for the active bus.

        :param myBus: Bus name of interest
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.N_interrupts

    def name(self, myBus):
        """
        (read only) - This property returns the name of the active bus.

        :param myBus:
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Name

    def nodes(self, myBus):
        """
        (read only) - This property returns an Integer Array of Node Numbers defined at the active bus in same order as the voltages.

        :param myBus:
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Nodes

    def num_nodes(self, myBus):
        """
        (read only) - This property returns number of nodes at the active bus.

        :param myBus:
        :return:
        """
        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.NumNodes

    def pu_VLL(self, myBus):
        """
        (read only) - This property returns a Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.

        :param myBus:
        :return:
        """

    def Latitude_read(self, myBus):
        self.DSSCircuit.SetActiveBus(myBus)
        return self.DSSActiveBus.Latitude

    def Latitude_write(self, myBus, data: float = 0.0):
        self.DSSCircuit.SetActiveBus(myBus)
        self.DSSActiveBus.Latitude = data

    def _check_bus(self, myBus):
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        myBusNames = self.DSSCircuit.AllBusNames
        aux = myBus in myBusNames
        if not aux:
            print(f'The Bus: {myBus} entered is not in the circuit.')
            return False
        else:
            return True







