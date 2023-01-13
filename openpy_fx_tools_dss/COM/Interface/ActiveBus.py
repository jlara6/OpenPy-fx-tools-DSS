# -*- coding: utf-8 -*-
# @Time    : 02/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ActiveBus.py
# @Software: PyCharm

from .Base import Base

class ActiveBus(Base):
    """
    This interface can be used to gain access to the features of the active Bus.
    Since buses are not objects, this interface provides access to the bus properties and values.
    The active bus needs to be specified by using the Active Circuit interface.
    The ActiveBus interface is embedded within the ActiveCircuit interface,
    requiring the definition of this interface before getting access the to ActiveBus interface
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSActiveBus = self.DSSCircuit.ActiveBus
    def AllPCEatBus(self, myBus: str = None) -> list:
        """
        (read only) - This property returns the names of all power conversion elements (PCE) connected to the active bus. The names are returned as list of string.

        :param myBus: Bus name of interest. Default is None
        :return: list[str]
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.AllPCEatBus)
        else:
            return None
    def AllPDEatBus(self, myBus: str = None):
        """
        (read only) - This property returns the names of all power delivery elements (PDE) connected to the active bus. The names are returned as list of string.

        :return:
        :param myBus: Bus name of interest. Default is None
        :return: list[str]
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.AllPDEatBus)
        else:
            return None
    def Coorddefined(self, myBus: str = None) -> bool:
        """
        (read only) - This property returns False=0 else True. Indicates whether a coordinate has been defined for this bus.

        :param myBus: Bus name of interest. Default is None
        :return: bool
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Coorddefined
        else:
            return None
    def CplxSeqVoltages(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a complex or polar of Sequence Voltages (0, 1, 2) at this Bus.

        :param myBus: Bus name of interest. Default is None
        :param rect: For complex. The default is False
        :param polar: For polar. The default is True
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.CplxSeqVoltages
                ),
                orig, polar, rect)
        else:
            return None
    def Cust_Duration(self, myBus: str = None):
        """
        (read only) - This property returns the accumulated customer outage duration for the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Cust_Duration
        else:
            return None
    def Cust_Interrupts(self, myBus: str = None):
        """
        (read only) - This property returns the accumulated number of customer-interruptions from the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Cust_Interrupts
        else:
            return None
    def Distance(self, myBus: str = None):
        """
        (read only) - This property returns the distance to the active bus from energymeter (if non-zero).

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Distance
        else:
            return None
    def GetUniqueNodeNumber(self, myBus: str = None, StartNumber: int = 1):
        """
        (read only) - This method returns a unique node number at the active bus to avoid node collisions and adds it to the node list for the bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.GetUniqueNodeNumber(StartNumber)
        else:
            return None
    def Int_Duration(self, myBus: str = None):
        """
        (read only) - This property returns the average interruption duration in hours.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Int_Duration
        else:
            return None
    def Isc(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns the short circuit currents at the active bus. The values are returned as a complex or polar list.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.Isc
                ),
                orig, polar, rect)
        else:
            return None

        check_bus(myBus)
        self.DSSCircuit.SetActiveBus(myBus)
        myIsc = self.DSSActiveBus.Isc
        return data_rect_polar(myIsc, rect, polar)

    def kVBase(self, myBus: str = None):
        """
        (read only) - This property returns the Base voltage at the active bus in kV.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.kVBase
        else:
            return None
    def Lambda(self, myBus: str = None):
        """
        (read only) - This property returns the accumulated failure rate downstream from this bus; faults per year.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Lambda
        else:
            return None
        
    def Latitude_read(self, myBus: str = None):
        """
        (read) - This property allows to read the latitude in GIS coordinates for the active bus.

        :param myBus: Bus name of interest. Default is None
        :return: 
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Latitude
        else:
            return None
    def Latitude_write(self, myBus, NewData: float = None):
        """
        (write) - This property allows to write the latitude in GIS coordinates for the active bus.

        :param myBus:
        :param data:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            self.DSSActiveBus.Latitude = self.Base._check_parameter(data)
        else:
            return None
    def LineList(self, myBus: str = None):
        """
        (read only) - This property returns a Variant Array of Strings containing the list of LINE elements connected to the active bus. Complete name Line.xxxx.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.LineList)
        else:
            return None

    def LoadList(self, myBus: str = None):
        """
        (read only) - Tis property returns the names of all power conversion elements (PCE) connected to the active bus. The names are returned as an array of string.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.LoadList)
        else:
            return None
    def Longitude_read(self, myBus: str = None):
        """
        (read) - This property allows to read the latitude in GIS coordinates for the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Longitude
        else:
            return None
    def Longitude_write(self, myBus, data: float = None):
        """
        (write) - This property allows to write the latitude in GIS coordinates for the active bus.

        :param myBus:
        :param data:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            self.DSSActiveBus.Longitude = self.Base._check_parameter(data)
        else:
            return None
    def N_Customers(self, myBus: str = None):
        """
        (read only) - This property returns the total numbers of customers served down-line from the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.N_Customers
        else:
            return None
    def N_interrupts(self, myBus: str = None):
        """
        (read only) - This property returns the Number of interruptions per year for the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.N_interrupts
        else:
            return None
    def Name(self, myBus: str = None):
        """
        (read only) - This property returns the name of the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Name
        else:
            return None
    def Nodes(self, myBus: str = None):
        """
        (read only) - This property returns an Integer Array of Node Numbers defined at the active bus in same order as the voltages.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._tuple_to_list(self.DSSActiveBus.Nodes)
        else:
            return None
    def NumNodes(self, myBus: str = None):
        """
        (read only) - This property returns number of nodes at the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.NumNodes
        else:
            return None
    def puVLL(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Complex array of pu L-L voltages for 2- and 3-phase buses. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only 3 phases.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.puVLL
                ),
                orig, polar, rect)
        else:
            return None
    def puVmagAngle(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Variant array of doubles containing voltage magnitude, angle pairs in per unit.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.puVmagAngle
                ),
                orig, polar, rect)
        else:
            return None
    def puVoltages(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Complex Array of pu voltages at the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.puVoltages
                ),
                orig, polar, rect)
        else:
            return None
    def SectionID(self, myBus: str = None):
        """
        (read only) - This property returns an Integer ID of the feeder section in which this bus is located.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.SectionID
        else:
            return None
    def SeqVoltages(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Double Array of sequence voltages at the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.SeqVoltages
                ),
                orig, polar, rect)
        else:
            return None
    def TotalMiles(self, myBus: str = None):
        """
        (read only) - This property returns the total length of line down-line from the active bus, in miles. For recloser siting algorithm.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.TotalMiles
        else:
            return None
    def VLL(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns for 2- and 3-phase buses, a variant array of complex numbers representing L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.VLL
                ),
                orig, polar, rect)
        else:
            return None
    def VMagAngle(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Variant Array of doubles containing voltages in Magnitude (VLN), angle (deg).


        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.VMagAngle
                ),
                orig, polar, rect)
        else:
            return None
    def Voc(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Complex Array of doubles containing the Open circuit voltage at the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.Voc
                ),
                orig, polar, rect)
        else:
            return None
    def Voltages(self, myBus: str = None, orig: bool = True, rect: bool = None, polar: bool = None):
        """
        (read only) - This property returns a Complex array of voltages at the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.Base._polar_or_rectangle(
                self.Base._tuple_to_list(
                    self.DSSActiveBus.Voltages
                ),
                orig, polar, rect)
        else:
            return None
    def x_read(self, myBus: str = None):
        """
        (read) - This property allows to read the X Coordinate (double) for the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.x
        else:
            return None
    def x_write(self, myBus, data: float = None):
        """
        (write) - This property allows to write the X Coordinate (double) for the active bus.

        :param myBus:
        :param data:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            self.DSSActiveBus.x = self.Base._check_parameter(data)
        else:
            return None
    def y_read(self, myBus: str = None):
        """
        (read) - This property allows to read the Y Coordinate (double) for the active bus.

        :param myBus: Bus name of interest. Default is None
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.y
        else:
            return None
    def y_write(self, myBus, data: float = None):
        """
        (write) - This property allows to write the Y Coordinate (double) for the active bus.

        :param myBus:
        :param data:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            self.DSSActiveBus.y = self.Base._check_parameter(data)
        else:
            return None
    def YscMatrix(self, myBus: str = None):
        """
        (read only) - This property returns a complex array of Ysc matrix column by column for the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.YscMatrix
        else:
            return None
    def Zsc0(self, myBus: str = None):
        """
        (read only) - This property returns the Complex Zero-Sequence short circuit impedance at bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSText.Command = "Solve mode=fault"
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Zsc0
        else:
            return None
    def ZSC012Matrix(self, myBus: str = None):
        """
        (read only) - This property returns an array of doubles (complex) containing the complete 012 Zsc matrix for the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSText.Command = "Solve mode=fault"
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.ZSC012Matrix
        else:
            return None
    def Zsc1(self, myBus: str = None):
        """
        (read only) - This property returns the Complex Positive-Sequence short circuit impedance at bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSText.Command = "Solve mode=fault"
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.Zsc1
        else:
            return None
    def ZscMatrix(self, myBus: str = None):
        """
        (read only) - This property returns a complex array of Zsc matrix column by column for the active bus.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSText.Command = "Solve mode=fault"
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.ZSC012Matrix
        else:
            return None
    def ZscRefresh(self, myBus: str = None):
        """
        (method) - This method recomputes Zsc for active bus for present circuit configuration.

        :param myBus:
        :return:
        """
        if ActiveBus(self.DSSObject)._check_bus(self.Base._check_str_bus(myBus)):
            self.DSSCircuit.SetActiveBus(myBus)
            return self.DSSActiveBus.ZscRefresh()
        else:
            return None
    def _check_bus(self, myBus: str = None):
        if myBus is None:
            print('You must enter a correct bus name')
        else:
            self.DSSCircuit = self.DSSObject.ActiveCircuit
            myBusNames = self.DSSCircuit.AllBusNames
            aux = myBus in myBusNames
            if not aux:
                print(f'The Bus: {myBus} entered is not in the circuit.')
                return False
            else:
                return True

