# -*- coding: utf-8 -*-
# @Time    : 18/05/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.DIGS_to_DSS_elem.Meters_DSS import *

def Meters_elements_DSS(dict_df_DigS: dict, BBDD_OpenDSS: dict, OpenDSS_element_list: list):

    BBDD_OpenDSS['EnergyMeter'] = DIGS_EnergyMeter_DSS()
    OpenDSS_element_list.append('EnergyMeter')

    BBDD_OpenDSS['FMonitor'] = DIGS_FMonitor_DSS()
    OpenDSS_element_list.append('FMonitor')

    BBDD_OpenDSS['Monitor'] = DIGS_Monitor_DSS()
    OpenDSS_element_list.append('Monitor')

    BBDD_OpenDSS['Sensor'] = DIGS_Sensor_DSS()
    OpenDSS_element_list.append('Sensor')

    return BBDD_OpenDSS, OpenDSS_element_list