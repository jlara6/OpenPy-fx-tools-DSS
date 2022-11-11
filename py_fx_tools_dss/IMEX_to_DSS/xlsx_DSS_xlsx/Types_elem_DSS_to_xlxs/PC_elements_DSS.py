# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PC_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss

list_PC_elements_DSS = ['Load', 'Generator', 'Generic5', 'GICLine', 'IndMach012', 'PVSystem', 'UPFC', 'VCCS', 'Storage',
                        'VSConverter', 'WindGen']

def PC_elements_DSS(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    list_property = dss.dsselement_all_property_names()

    if name_class == 'Load':
        list_aux = ['Id_Load']
        list_aux = list_aux + list_property
        df_Load = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Load'] = df_Load
        DSS_elem_list.append('Load')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Generator':
        list_aux = ['Id_Generator']
        list_aux = list_aux + list_property
        df_Generator = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Generator'] = df_Generator
        DSS_elem_list.append('Generator')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Generic5':
        list_aux = ['Id_Generic5']
        list_aux = list_aux + list_property
        df_Generic5 = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Generic5'] = df_Generic5
        DSS_elem_list.append('Generic5')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'GICLine':
        list_aux = ['Id_GICLine']
        list_aux = list_aux + list_property
        df_GICLine = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['GICLine'] = df_GICLine
        DSS_elem_list.append('GICLine')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'IndMach012':
        list_aux = ['Id_IndMach012']
        list_aux = list_aux + list_property
        df_IndMach012 = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['IndMach012'] = df_IndMach012
        DSS_elem_list.append('IndMach012')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'PVSystem':
        list_aux = ['Id_PVSystem']
        list_aux = list_aux + list_property
        df_PVSystem = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['PVSystem'] = df_PVSystem
        DSS_elem_list.append('PVSystem')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'UPFC':
        list_aux = ['Id_UPFC']
        list_aux = list_aux + list_property
        df_UPFC = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['UPFC'] = df_UPFC
        DSS_elem_list.append('UPFC')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'VCCS':
        list_aux = ['Id_VCCS']
        list_aux = list_aux + list_property
        df_VCCS = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['VCCS'] = df_VCCS
        DSS_elem_list.append('VCCS')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Storage':
        list_aux = ['Id_Storage']
        list_aux = list_aux + list_property
        df_Storage = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Storage'] = df_Storage
        DSS_elem_list.append('Storage')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'VSConverter':
        list_aux = ['Id_VSConverter']
        list_aux = list_aux + list_property
        df_VSConverter = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['VSConverter'] = df_VSConverter
        DSS_elem_list.append('VSConverter')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'WindGen':
        list_aux = ['Id_WindGen']
        list_aux = list_aux + list_property
        df_WindGen = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['WindGen'] = df_WindGen
        DSS_elem_list.append('WindGen')

        return BBDD_elem_DSS, DSS_elem_list

    else:

        return BBDD_elem_DSS, DSS_elem_list
