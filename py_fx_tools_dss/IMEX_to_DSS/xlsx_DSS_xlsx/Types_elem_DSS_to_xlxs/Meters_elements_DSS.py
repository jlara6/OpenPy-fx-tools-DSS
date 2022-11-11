# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : PC_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss

list_Meters_DSS = ['EnergyMeter', 'FMonitor', 'Monitor', 'Sensor']

def Meters_DSS(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):
    list_property = dss.dsselement_all_property_names()

    if name_class == 'EnergyMeter':
        list_aux = ['Id_EnergyMeter']
        list_aux = list_aux + list_property
        df_EnergyMeter = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['EnergyMeter'] = df_EnergyMeter
        DSS_elem_list.append('EnergyMeter')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'FMonitor':
        list_aux = ['Id_FMonitor']
        list_aux = list_aux + list_property
        df_FMonitor = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['FMonitor'] = df_FMonitor
        DSS_elem_list.append('FMonitor')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Monitor':
        list_aux = ['Id_Monitor']
        list_aux = list_aux + list_property
        df_Monitor = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Monitor'] = df_Monitor
        DSS_elem_list.append('Monitor')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Sensor':
        list_aux = ['Id_Sensor']
        list_aux = list_aux + list_property
        df_Sensor = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Sensor'] = df_Sensor
        DSS_elem_list.append('Sensor')

        return BBDD_elem_DSS, DSS_elem_list

    else:

        return BBDD_elem_DSS, DSS_elem_list


