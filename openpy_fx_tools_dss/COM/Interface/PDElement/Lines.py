# -*- coding: utf-8 -*-
# @Time    : 10/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Base.py
# @Software: PyCharm

import numpy as np
from openpy_fx_tools_dss.COM.Interface.Base import Base

class Lines(Base):
    """
    This interface can be used to gain access to the features of the Lines deployed across the circuit model in OpenDSS.
    This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before
    getting access the to Lines interface.
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSLines = self.DSSCircuit.Lines
    def AllNames(self):
        """
        (read only) - This property returns a variant array of strings containing names of all Line elements.

        :return:
        """
        return self._tuple_to_list(self.DSSLines.AllNames)
    def First(self):
        """
        (read only) - Invoking this property sets the first line element active.  Returns 0 if no lines.
        Otherwise, index of the line element.

        :return:
        """
        return self.DSSLines.First
    def Name(self):
        """
        (read) - This property gets the active line by name.

        :return:
        """
        return self.DSSLines.Name

    def Bus1_read(self):
        """
        (read/write) - This property sets/gets the name of bus for terminal 1 for the active line.

        :return:
        """
        return self.DSSLines.Bus1

    def Bus1_write(self, Value: str = None):
        """
        (read/write) - This property sets/gets the name of bus for terminal 1 for the active line.

        :return:
        """
        self.DSSLines.Bus1 = Value
    def Bus2_read(self):
        """
        (read/write) - This property sets/gets the name of bus for terminal 2 for the active line.

        :return:
        """
        return self.DSSLines.Bus1

    def Bus2_write(self, Value: str = None):
        """
        (read/write) - This property sets/gets the name of bus for terminal 2 for the active line.

        :return:
        """
        self.DSSLines.Bus2 = Value

    def C0_read(self):
        """
        (read/write) - This property sets/gets the Zero Sequence capacitance of the active line, nanofarads per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        return self.DSSLines.C0
    def C0_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Zero Sequence capacitance of the active line, nanofarads per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        self.DSSLines.C0 = Value

    def C1_read(self):
        """
        (read/write) - This property sets/gets the Zero Sequence capacitance of the active line, nanofarads per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        return self.DSSLines.C1
    def C1_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Zero Sequence capacitance of the active line, nanofarads per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        self.DSSLines.C1 = Value
    def Cmatrix(self):
        """
        (read/write) - This property sets/gets the nodal Capacitance matrix, lower triangle, nf per unit length for the active line.
        Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration.
        Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.
        For balanced line models, you may use the standard symmetrical component data definition instead.

        :return:
        """
        myCmatrix = np.reshape(np.array(self.DSSLines.Cmatrix), (self.DSSLines.Phases, self.DSSLines.Phases))
        return myCmatrix
    def Count(self):
        """
        (read only) - This property returns the number of Line objects in Active Circuit.

        :return: Gets the number of line objects in the model
        """
        return self.DSSLines.Count
    def EmergAmps_read(self):
        """
        (read/write) - This property sets/gets the Emergency (maximum) ampere rating of the active Line.

        :return: Gets emergency amps for the active line
        """
        return self.DSSLines.EmergAmps
    def EmergAmps_write(self, Value: float = 400.0):
        """
        (read/write) - This property sets/gets the Emergency (maximum) ampere rating of the active Line.

        :return: Gets emergency amps for the active line
        """
        self.DSSLines.EmergAmps = Value
    def Geometry(self):
        """
        (read/write) - This property sets/gets the line geometry code of the active Line.

        :return:
        """
        myCode = self.DSSLines.Geometry
        myPreFx = 'Geometry='
        if myCode == "":
            myCode = self.DSSLines.LineCode
            myPreFx = 'LineCode='
        return myPreFx+myCode
    def Length_read(self):
        """
        (read/write) - This property sets/gets the Length of active line section in units compatible with the LineCode definition.

        :return: Gets the line length
        """
        return self.DSSLines.Length
    def Length_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Length of active line section in units compatible with the LineCode definition.

        :return: Sets the line length
        """
        self.DSSLines.Length = Value
    def LineCode(self):
        """
        (read/write) - This property sets/gets the line LineCode of the active Line.

        :return:
        """
        myCode = self.DSSLines.Geometry
        myPreFx = 'Geometry='
        if myCode == "":
            myCode = self.DSSLines.LineCode
            myPreFx = 'LineCode='
        return myPreFx + myCode
    def NormAmps_read(self):
        """
        (read/write) - This property sets/gets the normal ampere rating of the active Line.

        :return: Gets normal amps for the active line
        """
        return self.DSSLines.NormAmps
    def NormAmps_write(self, Value: float = 300.0):
        """
        (read/write) - This property sets/gets the normal ampere rating of the active Line.

        :return: Gets normal amps for the active line
        """
        self.DSSLines.NormAmps = Value
    def NumCust(self):
        """
        (read only) - This property returns the number of customers in the active line section.

        :return:
        """
        return self.DSSLines.NumCust
    def Parent(self):
        """
        (read only) - This property sets Parent of the active Line to be the active line.
        Returns 0 if no parent or action fails..

        :return: sets Parent of the active Line to be the active line
        """
        i = self.DSSLines.Parent
        if i == 0:
            i = None
            print('No parent upstream Line')
        return i
    def Phases_read(self):
        """
        (read/write) - This property sets/gets the number of phases of the active Line.

        :return: Gets the number of phases of the active line object
        """
        return self.DSSLines.Phases
    def Phases_write(self, Value: int = 3):
        """
        (read/write) - This property sets/gets the number of phases of the active Line.

        :return: Sets the number of phases of the active line object
        """
        self.DSSLines.Phases = Value
    def R0_read(self):
        """
        (read/write) - This property sets/gets the Zero Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        return self.DSSLines.R0
    def R0_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Zero Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        self.DSSLines.R0 = Value
    def R1_read(self):
        """
        (read/write) - This property sets/gets the Positive Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        return self.DSSLines.R1
    def R1_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Positive Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        self.DSSLines.R1 = Value
    def Rg_read(self):
        """
        (read/write) - This property sets/gets the earth return resistance value used to compute line impedance at power frequency.

        :return:
        """
        return self.DSSLines.Rg
    def Rg_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the earth return resistance value used to compute line impedance at power frequency.

        :return:
        """
        self.DSSLines.Rg = Value
    def Rho_read(self):
        """
        (read/write) - This property sets/gets the earth resistivity used to compute earth correction factor.
        Overrides Line geometry definition if specified. Default=100 meter ohms.

        :return: Gets earth resistivity for the active line
        """
        return self.DSSLines.Rho
    def Rho_write(self, Value: float = 100.0):
        """
        (read/write) - This property sets/gets the earth resistivity used to compute earth correction factor.
        Overrides Line geometry definition if specified. Default=100 meter ohms.

        :param Value: New Value
        :return: Sets earth resistivity for the active line
        """
        self.DSSLines.Rho = Value
    def Rmatrix_read(self):
        """
        (read/write) - This property sets/gets the Resistance matrix, lower triangle, ohms per unit length.
        Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.
        Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.
        For balanced line models, you may use the standard symmetrical component data definition instead.

        :return: Gets Cmatrix for the active line
        """
        myRmatrix = np.reshape(np.array(self.DSSLines.Rmatrix), (self.DSSLines.Phases, self.DSSLines.Phases))
        return myRmatrix
    def Rmatrix_write(self, Rmatrix: np.ndarray):
        """
        (read/write) - This property sets/gets the Resistance matrix, lower triangle, ohms per unit length.
        Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.
        Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.
        For balanced line models, you may use the standard symmetrical component data definition instead.

        :return: Gets Cmatrix for the active line
        """
        nphases = self.DSSLines.Phases
        if len(tuple(Rmatrix.ravel())) == (nphases * nphases):
            self.DSSLines.Rmatrix = tuple(Rmatrix.ravel())
        else:
            print(f'Rmatrix must have dimensions {Rmatrix.shape}')
    def SeasonRating(self):
        """
        (read only) - This property returns the rating for the current season (in Amps) if the SeasonalRatings option is active.

        :return: gets the rating for the current season that applies to the active line
        """
        return self.DSSLines.SeasonRating
    def Spacing_read(self):
        """
        (read/write) - This property sets/gets the line spacing code of the active Line.

        :return: Gets the line spacing assigned to the active line
        """
        return self.DSSLines.Spacing
    def Spacing_write(self, Value):
        """
        (read/write) - This property sets/gets the line spacing code of the active Line.

        :return: Gets the line spacing assigned to the active line
        """
        self.DSSLines.Spacing = Value
    def TotalCust(self):
        """
        (read only) - This property returns the total Number of customers served from the active line section downstream.

        :return:
        """
        return self.DSSLines.TotalCust
    def Units_read(self):
        """
        (read/write) - This property sets/gets the Length Units = {none | mi(1)|kft(2)|km(3)|m(4)|Ft(5)|in(6)|cm(7) } for the active line.
        Default is None - assumes length units match impedance units.

        :return: Gets length units of the active line
        """
        return self.DSSLines.Units
    def Units_write(self, Value: int = 0):
        """
        (read/write) - This property sets/gets the Length Units = {none | mi(1)|kft(2)|km(3)|m(4)|Ft(5)|in(6)|cm(7) } for the active line.
        Default is None - assumes length units match impedance units.

        :return: Sets length units of the active line
        """
        self.DSSLines.Units = Value
    def X0_read(self):
        """
        (read/write) - This property sets/gets the Zero Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        return self.DSSLines.X0
    def X0_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Zero Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        self.DSSLines.X0 = Value
    def X1_read(self):
        """
        (read/write) - This property sets/gets the Positive Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        return self.DSSLines.X1
    def X1_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Positive Sequence resistance of the active line, ohms per unit length.
        Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        :return:
        """
        self.DSSLines.X1 = Value
    def Xg_read(self):
        """
        (read/write) - This property sets/gets the Carson earth return reactance per unit length used to compute impedance values at base frequency.
        For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedance).
        This value is required for harmonic solutions if you wish to adjust the earth return impedance for frequency. If not, set both Rg and Xg = 0.

        :return: Gets Xg for the active line
        """
        return self.DSSLines.Xg
    def Xg_write(self, Value: float = 0.0):
        """
        (read/write) - This property sets/gets the Carson earth return reactance per unit length used to compute impedance values at base frequency.
        For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedance).
        This value is required for harmonic solutions if you wish to adjust the earth return impedance for frequency. If not, set both Rg and Xg = 0.

        :return: Sets Xg for the active line
        """
        self.DSSLines.Xg = Value
    def Xmatrix_read(self):
        """
        (read/write) - This property sets/gets the Reactance matrix, lower triangle, ohms per unit length.
        Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.
        Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.
        For balanced line models, you may use the standard symmetrical component data definition instead.

        :return: Gets Xmatrix for the active line
        """
        myXmatrix = np.reshape(np.array(self.DSSLines.Xmatrix), (self.DSSLines.Phases, self.DSSLines.Phases))
        return myXmatrix
    def Xmatrix_write(self, Xmatrix: np.ndarray):
        """
        (read/write) - This property sets/gets the Reactance matrix, lower triangle, ohms per unit length.
        Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration.
        Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.
        For balanced line models, you may use the standard symmetrical component data definition instead.

        :return: Sets Xmatrix for the active line
        """
        nphases = self.DSSLines.Phases
        if len(tuple(Rmatrix.ravel())) == (nphases * nphases):
            self.DSSLines.Xmatrix = tuple(Rmatrix.ravel())
        else:
            print(f'Rmatrix must have dimensions {Xmatrix.shape}')
    def Yprim(self):
        """
        (read only) - This property returns the primitive Y bus matrix for the active line.

        :return: Gets the Y prim matrix
        """
        myYPrim = self.DSSLines.Yprim
        mySize = len(myYPrim)
        myYMat = np.empty((0, (self.DSSLines.Phases * 2)), complex)
        myIdx = 0
        for a in range(0, (self.DSSLines.Phases * 2)):
            myRow = np.empty((0, 0), complex)
            for b in range(0, (self.DSSLines.Phases * 2)):
                myRow = np.append(myRow, np.array(complex(myYPrim[myIdx], myYPrim[myIdx + 1]))),
                myIdx += 2
            myYMat = np.append(myYMat, myRow, axis=0)

        return myYMat









