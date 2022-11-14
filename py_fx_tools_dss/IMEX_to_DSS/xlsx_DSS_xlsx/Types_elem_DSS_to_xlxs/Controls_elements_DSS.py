# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PC_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss
from py_fx_tools_dss.NameClass_columns import dict_Control

list_Controls_DSS = ['CapControl', 'ESPVLControl', 'ExpControl', 'Fuse', 'GenDispatcher', 'InvControl', 'Recloser',
                     'RegControl', 'Relay', 'StorageController', 'SwtControl', 'UPFCControl']

def Controls_DSS(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    # list_property = dss.dsselement_all_property_names()
    list_property = dict_Control[name_class]

    if name_class == 'CapControl':
        list_aux = ['Id_CapControl']
        list_aux = list_aux + list_property
        df_CapControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['CapControl'] = df_CapControl
        DSS_elem_list.append('CapControl')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'ESPVLControl':
        list_aux = ['Id_ESPVLControl']
        list_aux = list_aux + list_property
        df_ESPVLControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['ESPVLControl'] = df_ESPVLControl
        DSS_elem_list.append('ESPVLControl')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'ExpControl':
        list_aux = ['Id_ExpControl']
        list_aux = list_aux + list_property
        df_ExpControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['ExpControl'] = df_ExpControl
        DSS_elem_list.append('ExpControl')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Fuse':
        list_aux = ['Id_Fuse']
        list_aux = list_aux + list_property
        df_Fuse = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Fuse'] = df_Fuse
        DSS_elem_list.append('Fuse')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'GenDispatcher':
        list_aux = ['Id_GenDispatcher']
        list_aux = list_aux + list_property
        df_GenDispatcher = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['GenDispatcher'] = df_GenDispatcher
        DSS_elem_list.append('GenDispatcher')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'InvControl':
        list_aux = ['Id_InvControl']
        list_aux = list_aux + list_property
        df_InvControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['InvControl'] = df_InvControl
        DSS_elem_list.append('InvControl')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Recloser':
        list_aux = ['Id_Recloser']
        list_aux = list_aux + list_property
        df_Recloser = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Recloser'] = df_Recloser
        DSS_elem_list.append('Recloser')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'RegControl':
        list_aux = ['Id_RegControl']
        list_aux = list_aux + list_property
        df_RegControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['RegControl'] = df_RegControl
        DSS_elem_list.append('RegControl')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Relay':
        list_aux = ['Id_Relay']
        list_aux = list_aux + list_property
        df_Relay = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Relay'] = df_Relay
        DSS_elem_list.append('Relay')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'StorageController':
        list_aux = ['Id_StorageController']
        list_aux = list_aux + list_property
        df_StorageController = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['StorageController'] = df_StorageController
        DSS_elem_list.append('StorageController')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'SwtControl':
        list_aux = ['Id_SwtControl']
        list_aux = list_aux + list_property
        df_SwtControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['SwtControl'] = df_SwtControl
        DSS_elem_list.append('SwtControl')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'UPFCControl':
        list_aux = ['Id_UPFCControl']
        list_aux = list_aux + list_property
        df_UPFCControl = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['UPFCControl'] = df_UPFCControl
        DSS_elem_list.append('UPFCControl')

        return BBDD_elem_DSS, DSS_elem_list

    else:

        return BBDD_elem_DSS, DSS_elem_list


