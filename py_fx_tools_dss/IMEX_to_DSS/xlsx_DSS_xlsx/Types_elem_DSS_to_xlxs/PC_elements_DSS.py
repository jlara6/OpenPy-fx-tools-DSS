# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PC_elements_MTY.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss
from py_fx_tools_dss.NameClass_columns import dict_PC_elem
from .fx_objects import _COL_ORD, _COL_MTY


list_PC_elements_DSS = ['Load', 'Generator', 'Generic5', 'GICLine', 'IndMach012', 'PVSystem', 'UPFC', 'VCCS', 'Storage',
                        'VSConverter', 'WindGen']

def PC_elements_DV(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'Load':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'Generator':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'Generic5':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'GICLine':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'IndMach012':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'PVSystem':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'UPFC':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'VCCS':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'Storage':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'VSConverter':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'WindGen':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    else:
        return DF_elem_DSS



def PC_elements_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'Load':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'Generator':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'Generic5':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'GICLine':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'IndMach012':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'PVSystem':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'UPFC':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'VCCS':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'Storage':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'VSConverter':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)

    elif name_class == 'WindGen':
        return _COL_ORD(dict_PC_elem, DF_elem_DSS, name_class)
    else:
        return DF_elem_DSS

def PC_elements_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):

    #list_property = dss.dsselement_all_property_names()
    list_property = dict_PC_elem[name_class]

    if name_class == 'Load':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Generator':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Generic5':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GICLine':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'IndMach012':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'PVSystem':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'UPFC':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'VCCS':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Storage':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'VSConverter':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'WindGen':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return BBDD_elem_DSS, DSS_elem_list
