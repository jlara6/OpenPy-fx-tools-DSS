# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PD_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss

list_PD_elements_DSS = ['Transformer', 'Line', 'Capacitor', 'AutoTrans', 'GICTransformer', 'Reactor']

def PD_elements_DSS(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):

    list_property = dss.dsselement_all_property_names()

    if name_class == 'Transformer':
        list_aux = ['Id_Transformer']
        list_aux = list_aux + list_property
        df_Transformer = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Transformer'] = df_Transformer
        DSS_elem_list.append('Transformer')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Line':
        list_aux = ['Id_Line']
        list_aux = list_aux + list_property
        df_Line = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Line'] = df_Line
        DSS_elem_list.append('Line')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Capacitor':
        list_aux = ['Id_Capacitor']
        list_aux = list_aux + list_property
        df_Capacitor = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Capacitor'] = df_Capacitor
        DSS_elem_list.append('Capacitor')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'AutoTrans':
        list_aux = ['Id_AutoTrans']
        list_aux = list_aux + list_property
        df_AutoTrans = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['AutoTrans'] = df_AutoTrans
        DSS_elem_list.append('AutoTrans')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'GICTransformer':
        list_aux = ['Id_GICTransformer']
        list_aux = list_aux + list_property
        df_GICTransformer = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['GICTransformer'] = df_GICTransformer
        DSS_elem_list.append('GICTransformer')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Reactor':
        list_aux = ['Id_Reactor']
        list_aux = list_aux + list_property
        df_Reactor = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Reactor'] = df_Reactor
        DSS_elem_list.append('Reactor')

        return BBDD_elem_DSS, DSS_elem_list

    else:

        return BBDD_elem_DSS, DSS_elem_list