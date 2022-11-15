# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Other_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss
from py_fx_tools_dss.NameClass_columns import dict_Other
from .fx_objects import _COL_MTY, _COL_ORD

list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']

def Other_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'Vsource':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    elif name_class == 'Fault':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    elif name_class == 'GICsource':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    elif name_class == 'Isource':
        return _COL_ORD(dict_Other, DF_elem_DSS, name_class)

    else:
        return DF_elem_DSS

def Other_DV(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:
    if name_class == 'Vsource':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'Fault':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    elif name_class == 'GICsource':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS

    elif name_class == 'Isource':
        if not DF_elem_DSS.empty:
            pass

        return DF_elem_DSS

    else:
        return DF_elem_DSS

def Other_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    #list_property = dss.dsselement_all_property_names()
    list_property = dict_Other[name_class]

    if name_class == 'Vsource':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Fault':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GICsource':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Isource':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)