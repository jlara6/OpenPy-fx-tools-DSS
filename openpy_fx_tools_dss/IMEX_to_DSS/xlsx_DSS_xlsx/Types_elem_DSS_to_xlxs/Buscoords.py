# -*- coding: utf-8 -*-
# @Time    : 18/11/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm
from typing import Dict, Any, Union

import pandas as pd
from numpy import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray

from openpy_fx_tools_dss.helper_functions import *
from openpy_fx_tools_dss.interface_dss import dss, drt

def Buscoords_DSS(name_proyect: str, path_save: str):

    coord = dict()
    all_bus_names = dss.circuit_all_bus_names()

    for name in all_bus_names:
        coord[name] = dict()

        dss.circuit_set_active_bus(name)
        coord[name]['Y'] = dss.bus_read_y()
        coord[name]['X'] = dss.bus_read_x()

    df_Buscoords_DSS = pd.DataFrame(pd.DataFrame(coord).T).reset_index().rename(columns={'index': f'Bus name'})
    df_Buscoords_DSS.to_csv(f'{path_save}\Buscoords_{name_proyect}.csv', index=False, header=False)

