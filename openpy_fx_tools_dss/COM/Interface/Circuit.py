# -*- coding: utf-8 -*-
# @Time    : 08/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Circuit.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import cmath
import math
from .Base import Base

class Circuit(Base):
    """
    This interface can be used to gain access to the features and properties of the active circuit.
    This is one of the most important interfaces since it embeds other interfaces, providing access to them as a
    property declaration. The circuit interface is exposed directly by the OpenDSSEngine.
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
    def ActiveBus(self, myBus: str = None):
        """
        (write only) - This method sets the active bus by name. After setting the active bus, the user can access
        the bus features and values through the ActiveBus interface

        :param myBus:
        :return:
        """
        if self.Base._check_bus(myBus):
            self.DSSCircuit.SetActiveBus(myBus)
    def ActiveCktElement(self):
        """
        (read only) - This property returns a handler to the Active Circuit element interface (same as ActiveElement).

        :return:
        """
        self.DSSCktElement = self.DSSCircuit.ActiveCktElement
    def ActiveClass(self):
        """
        (read only) - This property returns an interface to active class.

        :return:
        """
        self.DSSClass = self.DSSCircuit.ActiveClass
    def ActiveDSSElement(self):
        """
        (read only) - This property returns an Interface to the Active DSS object, which could be either a circuit
        element or a general DSS element.

        :return:
        """
        self.DSSElement = self.DSSCircuit.ActiveDSSElement
    def ActiveElement(self):
        """
        (read only) - This property returns a handler to the active circuit element interface, same as ActiveCktElement.

        :return:
        """
        self.DSSCktElement = self.DSSCircuit.ActiveElement
    def AllBusDistances(self):
        """
        (read only) - This property returns the distance from each bus to parent EnergyMeter.
        Corresponds to sequence in AllBusNames.

        :return:
        """
        return self.DSSCircuit.AllBusDistances
    def AllBusVmag(self):
        """
        (read only) - This property returns an array of magnitudes (doubles) of voltages at all buses.

        :return:
        """
        myNodes = self.DSSCircuit.AllNodeNames
        myVolt = self.DSSCircuit.AllBusVmag
        return pd.DataFrame(list(zip(myNodes, myVolt)), columns=['Bus', 'Vmag(V)'])
    def AllBusVmagPu(self):
        """
        (read only) - This property returns a double Array of all bus voltages (each node) magnitudes in Per unit.

        :return:
        """
        myNodes = self.DSSCircuit.AllNodeNames
        myVolt = self.DSSCircuit.AllBusVmagPu
        return pd.DataFrame(list(zip(myNodes, myVolt)), columns=['Bus', 'Vmag(PU)'])
    def AllBusVolts(self, polar: bool = True):
        """
        (read only) - This property returns a complex array of all bus, node voltages from most recent solution.

        :return:
        """
        myNodes, myVolt = self.DSSCircuit.AllNodeNames, self.DSSCircuit.AllBusVolts
        if polar:
            Vmang, Angle = [], []
            for i in range(0, len(myVolt), 2):
                aux = complex(myVolt[i], myVolt[i + 1])
                Vmang.append(cmath.polar(aux)[0])
                Angle.append(math.degrees(cmath.polar(aux)[1]))
            return pd.DataFrame(list(zip(myNodes, Vmang, Angle)), columns=['Bus', 'Vmag(V)', 'Angle(degrees)'])
        else:
            Real, Imag = [], []
            for i in range(0, len(myVolt), 2):
                Real.append(myVolt[i])
                Imag.append(myVolt[i + 1])
            return pd.DataFrame(list(zip(myNodes, Real, Imag)), columns=['Bus', 'Real', 'Imag'])
    def AllElementLosses(self):
        """
        (read only) - This property returns an array of total losses (complex) in each circuit element.

        :return:
        """
        myElementNames = self.DSSCircuit.AllElementNames
        myELosses = self.DSSCircuit.AllElementLosses
        kW, kVAR = [], []
        for i in range(0, len(myELosses), 2):
            kW.append(myELosses[i])
            kVAR.append(myELosses[i + 1])
        return pd.DataFrame(list(zip(myElementNames, kW, kVAR)), columns=['ElementName', 'kW', 'kVAR'])
    def AllElementNames(self):
        """
        (read only) - This property returns an array of strings containing Full Name of all elements within the model.

        :return:
        """
        return self.DSSCircuit.AllElementNames
    def AllNodeDistances(self):
        """
        (read only) - This property returns an array of distances from parent EnergyMeter for each Node.
        Corresponds to AllBusVMag sequence.

        :return:
        """
        myNodeDistances = self.DSSCircuit.AllNodeDistances
        myNodeNames = self.DSSCircuit.AllNodeNames
        return pd.DataFrame(list(zip(myNodeNames, myNodeDistances)), columns=['NodeName', 'Distance'])
    def AllNodeNames(self):
        """
        (read only) - This property returns an array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc.

        :return:
        """
        return self.DSSCircuit.AllNodeNames
    def Capacitors(self):
        """
        This property returns an interface to the Capacitors class.
        :return:
        """
        self.DSSCapacitor = self.DSSCircuit.Capacitor
    def Capacity(self, Strat: float = 1.0, Increment: float = 0.005):
        """
        (method) - This method computes the maximum load the active circuit can serve in the PRESENT YEAR.
        Uses the EnergyMeter objects with the registers set with the SET UEREGS= (..) command for the AutoAdd functions.
        Returns the metered kW (load + losses - generation) and per unit load multiplier for the loading level at which
        something in the system reports an overload or undervoltage. If no violations, then it returns the metered kW
        for peak load for the year (1.0 multiplier). Aborts and returns 0 if no energymeters.

        :return:
        """
        return self.DSSCircuit.Capacity(Strat, Increment)
    def CapControls(self):
        """
        (read only) - This property returns an interface to the CapControls class.

        :return:
        """
        self.DSSCapCtrls = self.DSSCircuit.CapControls
    def CtrlQueue(self):
        """
        (read only) - TThis property returns an interface to the CtrlQueue.

        :return:
        """
        self.DSSCtrlQueue = self.DSSCircuit.CtrlQueue
    def Disable(self, Element: str = None):
        """
        (method) - This method disables a circuit element by name (removes from circuit but leave in database).

        :return:
        """
        self.DSSCircuit.Disable(self.Base._check_element(Element))
    def Enable(self, Element: str = None):
        """
        (method) - This method Enables a circuit element by name (removes from circuit but leave in database).

        :return:
        """
        self.DSSCircuit.Enable(self.Base._check_element(Element))
    def EndOfTimeStepUpdate(self):
        """
        (method) - This method calls EndOfTimeStepCleanup in SolutionAlgs (Do Cleanup, sample monitors, and increment time).

        :return:
        """
        self.DSSCircuit.EndOfTimeStepUpdate
    def FirstElement(self, ClassName: str = None):
        """
        (read only) - This method sets the first element of active class to be the Active element in the active circuit.
        Returns 0 if none.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSCircuit.FirstElement
    def FirstPCElement(self):
        """
        (read only) - This property sets the first Power Conversion (PC) element to be the active element.

        :return:
        """
        self.DSSElement = self.DSSCircuit.ActiveCktElement
        return self.DSSCircuit.FirstPCElement
    def FirstPDElement(self):
        """
        (read only) - This property sets the first Power Delivery (PD) element to be the active element.

        :return:
        """
        self.DSSElement = self.DSSCircuit.ActiveCktElement
        return self.DSSCircuit.FirstPDElement
    def Fuses(self):
        """
        (read only) - This property returns an interface to the Fuses class.

        :return:
        """
        self.DSSFuses = self.DSSCircuit.Fuses
    def Generators(self):
        """
        (read only) - This property returns an interface to the Generators class.

        :return:
        """
        self.DSSGenerators = self.DSSCircuit.Generators
    def GICSources(self):
        """
        (read only) - This property returns an interface to the GICSources class.

        :return:
        """
        self.DSSGICSources = self.DSSCircuit.GICSources
    def ISources(self):
        """
        (read only) - This property returns an interface to the ISources class.

        :return:
        """
        self.DSSISources =  self.DSSCircuit.ISources
    def LineCodes(self):
        """
        (read only) - This property returns a handler for the LineCodes interface.

        :return:
        """
        self.DSSLineCodes = self.DSSCircuit.LineCodes
    def LineLosses(self):
        """
        (read only) - This property returns an array of doubles containing the complex total line losses in the circuit.

        :return: the Total line losses (P,Q)
        """
        return self.Base._tuple_to_list(self.DSSCircuit.LineLosses)
    def Lines(self):
        """
        (read only) - This property returns a handler for the Lines interface.

        :return: the handler to the Lines interface
        """
        self.DSSLines = self.DSSCircuit.Lines
    def Loads(self):
        """
        (read only) - This property returns a handler for the Loads interface.

        :return: the handler to the Loads interface
        """
        self.DSSLoads = self.DSSCircuit.Loads

    def LoadShapes(self):
        """
        (read only) - This property returns a handler for the LoadShapes interface.

        :return: the handler to the Lines interface
        """
        self.DSSLoadShapes = self.DSSCircuit.LoadShapes
    def Losses(self):
        """
        (read only) - This property returns an array of doubles containing the total losses in active circuit, complex number (two-element array of double).


        :return: the Total line losses (P,Q)
        """
        return self.Base._tuple_to_list(self.DSSCircuit.Losses)
    def Meters(self):
        """
        (read only) - This property returns a handler for the Meters interface.

        :return:
        """
        self.DSSMeters = self.DSSCircuit.Meters
    def Monitors(self):
        """
        (read only) - This property returns a handler for the Monitors interface.

        :return:
        """
        self.DSSMonitors = self.DSSCircuit.Monitors
    def NextElement(self):
        """
        (read only) - This method sets the next element of the active class to be the active element in the active circuit. Returns 0 if no more elements..

        :return:
        """
        return self.DSSCircuit.NextElement
    def NextPCElement(self):
        """
        (read only) - This property gets the next Power Conversion (PC) element to be the active element.

        :return:
        """
        return self.DSSCircuit.NextPCElement
    def NextPDElement(self):
        """
        (read only) - This property gets the next Power Delivery (PD) element to be the active element.

        :return:
        """
        return self.DSSCircuit.NextPDElement
    def NumBuses(self):
        """
        (read only) - This property returns the total number of Buses in the circuit.

        :return:
        """
        return self.DSSCircuit.NumBuses
    def NumCktElements(self):
        """
        (read only) - This property returns the number of Circuit Elements in the model.
        :return:
        """
        return self.DSSCircuit.NumCktElements
    def NumNodes(self):
        """
        (read only) - This property returns the total number of nodes in the circuit.

        :return:
        """
        return self.DSSCircuit.NumNodes
    def Parallel(self):
        """
        (read only) - This property returns a handler for the parallel processing interface

        :return:
        """
        self.DSSParallel = self.DSSCircuit.Parallel
    def ParentPDElement(self):
        """
        (read only) - This property sets Parent PD element, if any, to be the active circuit element and returns index>0; Returns 0 if it fails or not applicable..

        :return:
        """
        return self.DSSCircuit.ParentPDElement
    def PDElements(self):
        """
        (read only) - This property returns a handler for the PDElements interface.

        :return:
        """
        self.DSSPDE = self.DSSCircuit.PDElements
    def PVSystems(self):
        """
        (read only) - This property returns a handler for the PVSystems interface.

        :return:
        """
        self.DSSPVSystems = self.DSSCircuit.PVSystems

    def Reclosers(self):
        """
        (read only) - This property returns a handler for the Reclosers interface.

        :return:
        """
    def ReduceCkt(self):
        """
        (read only) - This property returns a handler for the ReduceCkt interface.

        :return:
        """
        self.DSSRdCkt = self.DSSCircuit.ReduceCkt
    def RegControls(self):
        """
        (read only) - This property returns a handler for the RegControls interface.

        :return:
        """
        self.DSSRegControls = self.DSSCircuit.RegControls
    def Relays(self):
        """
        (read only) - This property returns a handler for the Relays interface.

        :return:
        """
        self.DSSRelays = self.DSSCircuit.Relays
    def Sample(self):
        """
        (method) - This method forces all Meters and Monitors to take a sample.

        :return:
        """
        self.DSSCircuit.Sample()
    def SaveSample(self):
        """
        (method) - This method forces all meters and monitors to save their current buffers.

        :return:
        """
        self.DSSCircuit.SaveSample()
    def Sensors(self):
        """
        (read only) - This property returns a handler for the Sensors interface

        :return:
        """
        self.DSSSensors = self.DSSCircuit.Sensors

    def SetActiveBus(self, myBus: str = None):
        """
        (write only) - This method sets Active bus by name. Ignores node list.  Returns bus index (zero based) compatible with AllBusNames and Buses collection.

        :return:
        """
        self.DSSCircuit.SetActiveBus(self.Base._check_bus(myBus))
    def SetActiveBusi(self, BusIndex: int = 1):
        """
        (write only) - This method sets ActiveBus by Integer value.  0-based index compatible with SetActiveBus return value and AllBusNames indexing.
        Returns 0 if OK

        :return:
        """
        return self.DSSCircuit.SetActiveBusi(BusIndex)
    def SetActiveClass(self, ClassName: str = None):
        """
        (write only) - This method sets the active class by name.  Use FirstElement, NextElement to iterate through the class.
        Returns -1 if fails.

        :return:
        """
        i = self.DSSCircuit.SetActiveClass(ClassName)
        if i < 0:
            print('The class does not exist')
        return i

    def SetActiveElement(self, FullName: str = None):
        """
        (write only) - This method sets the Active Circuit Element using the full object name (e.g. "generator.g1").
        Returns -1 if not found. Else index to be used in CktElements collection or AllElementNames.

        :return:
        """
        i = self.DSSCircuit.SetActiveElement(FullName)
        if i < 0:
            print('The element does not exist')
        return i
    def Settings(self):
        """
        (read only) - This property returns a handler for the Settings interface.

        :return:
        """
        self.DSSSettings = self.DSSCircuit.Settings
    def Solution(self):
        """
        (read only) - This property returns a handler for the Solution interface.

        :return:
        """
        self.DSSSolution = self.DSSCircuit.Solution
    def SubstationLosses(self):
        """
        Returns the substation losses P(kW), Q(kvar)
        :return:
        """
        return self.Base._tuple_to_list(self.DSSCircuit.SubstationLosses)
    def SwtControls(self):
        """
        (read only) - This property returns a handler for the SwtControls interface.

        :return:
        """
        self.DSSSwtControls = self.DSSCircuit.SwtControls
    def SystemY(self):
        """
        (read only) - This property returns the system Y matrix as an DataFrame of doubles representing complex number pairs (dense format- includes 0s - after a solution has been performed)

        :return:
        """
        self.DSSSolution = self.DSSCircuit.Solution
        self.DSSSolution.Solve()
        mySysY = self.DSSCircuit.SystemY
        myNodeList = self.DSSCircuit.AllNodeNames
        YSysSize = len(myNodeList)
        myYMat = np.empty((0, YSysSize), complex)
        myIdx = 0
        for a in range(0, YSysSize):
            myRow = np.empty((0, 0), complex)
            for b in range(0, YSysSize):
                myRow = np.append(myRow , np.array(complex(mySysY[myIdx], mySysY[myIdx + 1]))),
                myIdx += 2
            myYMat = np.append(myYMat, myRow, axis=0)

        myYMat = pd.DataFrame(myYMat, columns=myNodeList, index=myNodeList)
        return myYMat
    def Topology(self):
        """
        (read only) - This property returns a handler for the Topology interface.

        :return:
        """
        self.DSSTopology = self.DSSCircuit.Topology
    def TotalPower(self):
        """
        (read only) - This property returns the total power, watts and vars delivered to the circuit.
        The negative magnitudes (-) indicate that the power is coming out of the substations.

        :return: the total power P(kW),Q(kvar) delivered to the circuit
        """
        return self._tuple_to_list(self.DSSCircuit.TotalPower)
    def Transformers(self):
        """
        (read only) - This property returns a handler for the Transformers interface.

        :return:
        """
        self.DSSTransformers = self.DSSCircuit.Transformers
    def UpdateStorage(self):
        """
        (method) - This method forces update to all storage classes. Typically done after a solution.
        Done automatically in intrinsic solution modes

        :return:
        """
        self.DSSText.Command = 'Solve mode=snap'
        self.DSSCircuit.UpdateStorage()
    def Vsources(self):
        """
        (read only) - This property returns a handler for the Vsources interface.

        :return:
        """
        self.DSSVsources = self.DSSCircuit.Vsources
    def XYCurves(self):
        """
        (read only) - This property returns a handler for the XYCurves interface.

        :return:
        """
        self.DSSXYCurves = self.DSSCircuit.XYCurves
    def YCurrents(self, polar: bool=False):
        """
        (read only) - This property returns a variant array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV.

        :return:
        """
        # Gets the Y currents

        myYCurr = self.DSSCircuit.YCurrents;
        mySize = len(myYCurr)

        if polar:
            Vmang, Angle = [], []
            for i in range(0, len(myYCurr), 2):
                aux = complex(myYCurr[i], myYCurr[i + 1])
                Vmang.append(cmath.polar(aux)[0])
                Angle.append(math.degrees(cmath.polar(aux)[1]))
            return pd.DataFrame(list(zip( Vmang, Angle)), columns=['I(A)', 'Angle(degrees)'])
        else:
            Real, Imag = [], []
            for i in range(0, len(myYCurr), 2):
                Real.append(myYCurr[i])
                Imag.append(myYCurr[i + 1])
            return pd.DataFrame(list(zip( Real, Imag)), columns=['Real', 'Imag'])

    def YNodeOrder(self):
        """
        (read only) - This property returns a variant array of strings containing the names of the nodes in the same order as the Y matrix.

        :return:
        """
        return self._tuple_to_list(self.DSSCircuit.YNodeOrder)

    def YNodeVarray(self, polar: bool=False):
        """
        (read only) - This property returns a variant array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV.

        :return:
        """
        # Gets the Y currents

        myYV = self.DSSCircuit.YNodeVarray;
        mySize = len(myYV)

        if polar:
            Vmang, Angle = [], []
            for i in range(0, len(myYV), 2):
                aux = complex(myYV[i], myYV[i + 1])
                Vmang.append(cmath.polar(aux)[0])
                Angle.append(math.degrees(cmath.polar(aux)[1]))
            return pd.DataFrame(list(zip( Vmang, Angle)), columns=['V', 'Angle(degrees)'])
        else:
            Real, Imag = [], []
            for i in range(0, len(myYV), 2):
                Real.append(myYV[i])
                Imag.append(myYV[i + 1])
            return pd.DataFrame(list(zip( Real, Imag)), columns=['Real', 'Imag'])






















