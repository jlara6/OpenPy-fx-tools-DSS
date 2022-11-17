# -*- coding: utf-8 -*-
# @Time    : 16/11/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : Voltagebases_DSS.py
# @Software: PyCharm


import warnings
warnings.simplefilter(action='ignore', category=Warning)
import pandas as pd
from openpy_fx_tools_dss.interface_dss import dss

def Voltagebases_DSS() -> pd.DataFrame:
    list_aux = dss.settings_read_voltage_bases()
    data = str(list_aux).replace("[", "").replace("]", "")
    dic = {'Id_Voltagebases': data}
    df_Voltagebases_DSS = pd.DataFrame(columns=['Id_Voltagebases'])
    df_Voltagebases_DSS = df_Voltagebases_DSS.append({'Id_Voltagebases': list_aux}, ignore_index=True)

    return df_Voltagebases_DSS

