# -*- coding: utf-8 -*-
# @Time    : 02/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Base.py
# @Software: PyCharm

import numpy as np
import math
import cmath

class Base:
    def __init__(self, DSSObject):
        self.DSSObject = DSSObject

    def _tuple_to_list(self, parameter: tuple):
        return list(parameter)

    def _tuple_to_ndarray(self, parameter: tuple):
        return np.asarray(parameter)

    def _check_str_bus(self, parameter):
        if type(parameter) != 'str':
            if isinstance(parameter, float):
                return str(int(parameter))
            if isinstance(parameter, int):
                return str(parameter)
        return parameter
    def _check_parameter(self, parameter):
        if parameter is None:
            print('The entered parameter is empty ')
        else:
            if isinstance(parameter, str):
                try:
                    parameter = float(parameter)
                except:
                    parameter = 0
        return parameter
    def _polar_or_rectangle(self, data: list, orig: bool, polar: bool, rect: bool):
            data_aux =  list()
            myLen = len(data)
            orig, rect, polar =_check_bool(orig, rect, polar)
            for i in range(0, myLen, 2):
                a = i
                b = i + 1
                if orig:
                    data_aux = data
                if rect:
                    pos_aux = complex(data[i], data[i + 1])
                    data_aux.append(pos_aux)
                if polar:
                    cplx_aux = complex(data[i], data[i + 1])
                    data_aux.append(_polar(cplx_aux))
            return data_aux
    def _extract_class_name(self, element: str):
        pos = element.find('.')
        class_DSS = element[:pos]
        name_DSS = element[pos + 1:]
        return class_DSS, name_DSS

    def _check_element(self, parameter):
        self.DSSActiveClass = self.DSSCircuit.ActiveClass
        class_DSS, name_DSS = Base(self.DSSObject)._extract_class_name(parameter)
        self.DSSCircuit.SetActiveClass(class_DSS)
        aux = name_DSS in self.DSSActiveClass.AllNames
        if not aux:
            print(f'The element {parameter}, do not belong to the circuit.')
            return False
        else:
            return True
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
def _check_bool(orig, rect, polar):
    if orig == True and rect == None and polar == None:
        return orig, rect, polar
    if orig == True and rect == True and polar == None:
        orig, rect, polar = False, True, False
        return orig, rect, polar
    if orig == True and rect == None and polar == True:
        orig, rect, polar = False, False, True
        return orig, rect, polar

def _polar(z):
    a= z.real
    b= z.imag
    r = math.hypot(a,b)
    theta = np.rad2deg(math.atan2(b,a))
    return r,theta

