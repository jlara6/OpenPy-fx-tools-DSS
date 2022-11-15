# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PD_elements_MTY.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss
from py_fx_tools_dss.NameClass_columns import dict_PD_elem
from .fx_objects import _COL_ORD, _COL_MTY

list_PD_elements_DSS = ['Transformer', 'Line', 'Capacitor', 'AutoTrans', 'GICTransformer', 'Reactor']

def PD_elements_DV(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'Transformer':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Line':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Capacitor':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'AutoTrans':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'GICTransformer':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    elif name_class == 'Reactor':
        if not DF_elem_DSS.empty:
            pass
        return DF_elem_DSS
    else:
        return DF_elem_DSS

def PD_elements_ORD(DF_elem_DSS: pd.DataFrame, name_class: str) -> pd.DataFrame:

    if name_class == 'Transformer':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'Line':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'Capacitor':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'AutoTrans':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'GICTransformer':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    elif name_class == 'Reactor':
        return _COL_ORD(dict_PD_elem, DF_elem_DSS, name_class)
    else:
        return DF_elem_DSS

def PD_elements_MTY(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):

    #list_property = dss.dsselement_all_property_names()
    list_property = dict_PD_elem[name_class]

    if name_class == 'Transformer':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Line':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Capacitor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'AutoTrans':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'GICTransformer':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    elif name_class == 'Reactor':
        return _COL_MTY(BBDD_elem_DSS, DSS_elem_list, name_class, list_property)
    else:
        return BBDD_elem_DSS, DSS_elem_list