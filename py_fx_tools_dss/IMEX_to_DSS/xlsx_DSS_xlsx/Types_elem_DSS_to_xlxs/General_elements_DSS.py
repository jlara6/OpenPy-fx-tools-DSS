# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : General_elements_DSS.py
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.interface_dss import dss, drt

list_General_DSS = ['WireData', 'LineSpacing', 'LineGeometry', 'LineCode', 'XfmrCode', 'CNData', 'GrowthShape',
                    'LoadShape', 'PriceShape', 'Spectrum', 'TCC_Curve', 'TSData', 'TShape', 'XYcurve']

def General_DSS(BBDD_elem_DSS: dict, DSS_elem_list: list, name_class: str):

    list_property = dss.dsselement_all_property_names()

    if name_class == 'LineCode':
        list_aux = ['Id_LineCode']
        list_aux = list_aux + list_property
        df_LineCode = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['LineCode'] = df_LineCode
        DSS_elem_list.append('LineCode')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'LoadShape':
        list_aux = ['Id_LoadShape']
        list_aux = list_aux + list_property
        df_LoadShape = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['LoadShape'] = df_LoadShape
        DSS_elem_list.append('LoadShape')
        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'TShape':
        list_aux = ['Id_TShape']
        list_aux = list_aux + list_property
        df_TShape = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['TShape'] = df_TShape
        DSS_elem_list.append('TShape')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'PriceShape':
        list_aux = ['Id_PriceShape']
        list_aux = list_aux + list_property
        df_PriceShape = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['PriceShape'] = df_PriceShape
        DSS_elem_list.append('PriceShape')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'XYcurve':
        list_aux = ['Id_XYcurve']
        list_aux = list_aux + list_property
        df_XYcurve = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['XYcurve'] = df_XYcurve
        DSS_elem_list.append('XYcurve')

        return BBDD_elem_DSS, DSS_elem_list
    
    elif name_class == 'GrowthShape':
        list_aux = ['Id_GrowthShape']
        list_aux = list_aux + list_property
        df_GrowthShape = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['GrowthShape'] = df_GrowthShape
        DSS_elem_list.append('GrowthShape')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'TCC_Curve':
        list_aux = ['Id_TCC_Curve']
        list_aux = list_aux + list_property
        df_TCC_Curve = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['TCC_Curve'] = df_TCC_Curve
        DSS_elem_list.append('TCC_Curve')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'Spectrum':
        list_aux = ['Id_Spectrum']
        list_aux = list_aux + list_property
        df_Spectrum = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['Spectrum'] = df_Spectrum
        DSS_elem_list.append('Spectrum')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'WireData':
        list_aux = ['Id_WireData']
        list_aux = list_aux + list_property
        df_WireData = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['WireData'] = df_WireData
        DSS_elem_list.append('WireData')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'CNData':
        list_aux = ['Id_CNData']
        list_aux = list_aux + list_property
        df_CNData = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['CNData'] = df_CNData
        DSS_elem_list.append('CNData')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'TSData':
        list_aux = ['Id_TSData']
        list_aux = list_aux + list_property
        df_TSData = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['TSData'] = df_TSData
        DSS_elem_list.append('TSData')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'LineGeometry':
        list_aux = ['Id_LineGeometry']
        list_aux = list_aux + list_property
        df_LineGeometry = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['LineGeometry'] = df_LineGeometry
        DSS_elem_list.append('LineGeometry')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'LineSpacing':
        list_aux = ['Id_LineSpacing']
        list_aux = list_aux + list_property
        df_LineSpacing = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['LineSpacing'] = df_LineSpacing
        DSS_elem_list.append('LineSpacing')

        return BBDD_elem_DSS, DSS_elem_list

    elif name_class == 'XfmrCode':
        list_aux = ['Id_XfmrCode']
        list_aux = list_aux + list_property
        df_XfmrCode = pd.DataFrame(columns=list_aux)
        BBDD_elem_DSS['XfmrCode'] = df_XfmrCode
        DSS_elem_list.append('XfmrCode')

        return BBDD_elem_DSS, DSS_elem_list

    else:
        return BBDD_elem_DSS, DSS_elem_list


