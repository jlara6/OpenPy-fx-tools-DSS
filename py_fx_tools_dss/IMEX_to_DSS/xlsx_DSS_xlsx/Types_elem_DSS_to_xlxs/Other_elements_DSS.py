# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Other_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss, drt

list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']

def Other_DSS(BBDD_DSS: dict, DSS_elem_list: list, name_class: str):
    list_property = dss.dsselement_all_property_names()

    if name_class == 'Vsource':
        list_aux = ['Id_Vsource']
        list_aux = list_aux + list_property
        df_Vsource = pd.DataFrame(columns=list_aux)
        BBDD_DSS['Vsource'] = df_Vsource
        DSS_elem_list.append('Vsource')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'Fault':
        list_aux = ['Id_Fault']
        list_aux = list_aux + list_property
        df_Fault = pd.DataFrame(columns=list_aux)
        BBDD_DSS['Fault'] = df_Fault
        DSS_elem_list.append('Fault')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'GICsource':
        list_aux = ['Id_GICsource']
        list_aux = list_aux + list_property
        df_GICsource = pd.DataFrame(columns=list_aux)
        BBDD_DSS['GICsource'] = df_GICsource
        DSS_elem_list.append('GICsource')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'Isource':
        list_aux = ['Id_Isource']
        list_aux = list_aux + list_property
        df_Isource = pd.DataFrame(columns=list_aux)
        BBDD_DSS['Isource'] = df_Isource
        DSS_elem_list.append('Isource')

        return BBDD_DSS, DSS_elem_list

    else:
        return BBDD_DSS, DSS_elem_list