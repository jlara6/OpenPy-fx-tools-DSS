# -*- coding: utf-8 -*-
# @Time    : 25/09/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : General_elements_DSS.py
# @Software: PyCharm

import py_dss_interface
import pandas as pd

dss = py_dss_interface.DSSDLL()

def append_LineCode(df_elem: pd.DataFrame):

    dss.linecodes_first()
    for _ in range(dss.linecodes_count()):
        df_elem = df_elem.append(
            {'Id_LineCode': dss.linecodes_read_name(),
             'nphases': dss.linecodes_read_phases(),
             'r1': dss.linecodes_read_r1(),
             'x1': dss.linecodes_read_x1(),
             'r0': dss.linecodes_read_r0(),
             'x0': dss.linecodes_read_x0(),
             'C1': dss.linecodes_read_c1(),
             'C0': dss.linecodes_read_c0(),
             'units': dss.linecodes_read_units(),
             'rmatrix': dss.linecodes_read_rmatrix(),
             'xmatrix': dss.linecodes_read_xmatrix(),
             'cmatrix': dss.linecodes_read_cmatrix(),
             'baseFreq': '',
             'normamps': dss.linecodes_read_norm_amps(),
             'emergamps': dss.linecodes_read_emerg_amps(),
             'faultrate': '',
             'pctperm': '',
             'repair': '',
             'Kron': '', 
             'Rg': '', 
             'Xg': '', 
             'rho': '', 
             'neutral': '', 
             'B1': '',
             'B0': '',
             'Seasons': '', 
             'Ratings': '', 
             'LineType': '', 
             'like': ''}, 
            ignore_index=True)

        dss.linecodes_next()
    return df_elem

def append_LoadShape(df_elem: pd.DataFrame):
    dss.loadshapes_first()
    for _ in range(dss.loadshapes_count()):
        df_elem = df_elem.append(
            {'Id_LoadShape': dss.loadshapes_read_name(),
             'npts': dss.loadshapes_read_npts(),
             'interval': '',
             'mult': dss.loadshapes_read_p_mult(),
             'hour': '',
             'mean': '',
             'stddev': '',
             'csvfile': '',
             'sngfile': '',
             'dblfile': '',
             'action': '',
             'qmult': dss.loadshapes_read_q_mult(),
             'UseActual': '',
             'Pmax': '',
             'Qmax': '',
             'sinterval': dss.loadshapes_read_s_interval(),
             'minterval': dss.loadshapes_read_min_interval(),
             'Pbase': dss.loadshapes_read_p_base(),
             'Qbase': dss.loadshapes_read_q_base(),
             'Pmult': dss.loadshapes_read_p_mult(),
             'PQCSVFile': '',
             'MemoryMapping': '',
             'like': ''},
            ignore_index=True)
        dss.loadshapes_next()
    return df_elem

def append_TShape(df_elem: pd.DataFrame):
    return df_elem

def append_PriceShape(df_elem: pd.DataFrame):
    return df_elem

def append_XYcurve(df_elem: pd.DataFrame):
    return df_elem

def append_GrowthShape(df_elem: pd.DataFrame):
    return df_elem

def append_TCC_Curve(df_elem: pd.DataFrame):
    return df_elem

def append_Spectrum(df_elem: pd.DataFrame):
    return df_elem

def append_WireData(df_elem: pd.DataFrame):
    return df_elem

def append_CNData(df_elem: pd.DataFrame):
    return df_elem

def append_TSData(df_elem: pd.DataFrame):
    return df_elem

def append_LineGeometry(df_elem: pd.DataFrame):
    return df_elem

def append_LineSpacing(df_elem: pd.DataFrame):
    return df_elem

def append_XfmrCode(df_elem: pd.DataFrame):
    return df_elem

def General_DSS(BBDD_DSS: dict, DSS_elem_list: list, name_class: str):

    list_in_class = dss.active_class_all_names()
    n_elem_class = dss.active_class_count()
    list_property = dss.dsselement_all_property_names()

    if name_class == 'LineCode':
        list_aux = ['Id_LineCode']
        list_aux = list_aux + list_property
        df_LineCode = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['LineCode'] = df_LineCode
        else:
            df_LineCode = append_LineCode(df_elem=df_LineCode)
            BBDD_DSS['LineCode'] = df_LineCode

        DSS_elem_list.append('LineCode')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'LoadShape':
        list_aux = ['Id_LoadShape']
        list_aux = list_aux + list_property
        df_LoadShape = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['LoadShape'] = df_LoadShape
        else:
            df_LineCode = append_LoadShape(df_elem=df_LoadShape)
            BBDD_DSS['LoadShape'] = df_LineCode

        DSS_elem_list.append('LoadShape')
        return BBDD_DSS, DSS_elem_list

    elif name_class == 'TShape':
        list_aux = ['Id_TShape']
        list_property = ['npts', 'interval', 'temp', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile',
                         'sinterval', 'minterval', 'action', 'like']
        list_aux = list_aux + list_property
        df_TShape = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['TShape'] = df_TShape
        else:
            df_TShape = append_TShape(df_elem=df_TShape)
            BBDD_DSS['TShape'] = df_TShape

        DSS_elem_list.append('TShape')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'PriceShape':
        list_aux = ['Id_PriceShape']
        list_aux = list_aux + list_property
        df_PriceShape = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['PriceShape'] = df_PriceShape
        else:
            df_PriceShape = append_PriceShape(df_elem=df_PriceShape)
            BBDD_DSS['PriceShape'] = df_PriceShape

        DSS_elem_list.append('PriceShape')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'XYcurve':
        list_aux = ['Id_XYcurve']
        list_aux = list_aux + list_property
        df_XYcurve = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['XYcurve'] = df_XYcurve
        else:
            df_XYcurve = append_XYcurve(df_elem=df_XYcurve)
            BBDD_DSS['XYcurve'] = df_XYcurve

        DSS_elem_list.append('XYcurve')

        return BBDD_DSS, DSS_elem_list
    
    elif name_class == 'GrowthShape':
        list_aux = ['Id_GrowthShape']
        list_aux = list_aux + list_property
        df_GrowthShape = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['GrowthShape'] = df_GrowthShape
        else:
            df_GrowthShape = append_GrowthShape(df_elem=df_GrowthShape)
            BBDD_DSS['GrowthShape'] = df_GrowthShape

        DSS_elem_list.append('GrowthShape')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'TCC_Curve':
        list_aux = ['Id_TCC_Curve']
        list_aux = list_aux + list_property
        df_TCC_Curve = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['TCC_Curve'] = df_TCC_Curve
        else:
            df_TCC_Curve = append_TCC_Curve(df_elem=df_TCC_Curve)
            BBDD_DSS['TCC_Curve'] = df_TCC_Curve

        DSS_elem_list.append('TCC_Curve')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'Spectrum':
        list_aux = ['Id_Spectrum']
        list_aux = list_aux + list_property
        df_Spectrum = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['Spectrum'] = df_Spectrum
        else:
            df_Spectrum = append_Spectrum(df_elem=df_Spectrum)
            BBDD_DSS['Spectrum'] = df_Spectrum

        DSS_elem_list.append('Spectrum')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'WireData':
        list_aux = ['Id_WireData']
        list_aux = list_aux + list_property
        df_WireData = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['WireData'] = df_WireData
        else:
            df_WireData = append_WireData(df_elem=df_WireData)
            BBDD_DSS['WireData'] = df_WireData

        DSS_elem_list.append('WireData')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'CNData':
        list_aux = ['Id_CNData']
        list_aux = list_aux + list_property
        df_CNData = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['CNData'] = df_CNData
        else:
            df_CNData = append_CNData(df_elem=df_CNData)
            BBDD_DSS['CNData'] = df_CNData

        DSS_elem_list.append('CNData')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'TSData':
        list_aux = ['Id_TSData']
        list_aux = list_aux + list_property
        df_TSData = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['TSData'] = df_TSData
        else:
            df_TSData = append_TSData(df_elem=df_TSData)
            BBDD_DSS['TSData'] = df_TSData

        DSS_elem_list.append('TSData')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'LineGeometry':
        list_aux = ['Id_LineGeometry']
        list_aux = list_aux + list_property
        df_LineGeometry = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['LineGeometry'] = df_LineGeometry
        else:
            df_LineGeometry = append_LineGeometry(df_elem=df_LineGeometry)
            BBDD_DSS['LineGeometry'] = df_LineGeometry

        DSS_elem_list.append('LineGeometry')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'LineSpacing':
        list_aux = ['Id_LineSpacing']
        list_aux = list_aux + list_property
        df_LineSpacing = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['LineSpacing'] = df_LineSpacing
        else:
            df_LineSpacing = append_LineSpacing(df_elem=df_LineSpacing)
            BBDD_DSS['LineSpacing'] = df_LineSpacing

        DSS_elem_list.append('LineSpacing')

        return BBDD_DSS, DSS_elem_list

    elif name_class == 'XfmrCode':
        list_aux = ['Id_XfmrCode']
        list_aux = list_aux + list_property
        df_XfmrCode = pd.DataFrame(columns=list_aux)
        if n_elem_class == 0:
            BBDD_DSS['XfmrCode'] = df_XfmrCode
        else:
            df_XfmrCode = append_XfmrCode(df_elem=df_XfmrCode)
            BBDD_DSS['XfmrCode'] = df_XfmrCode

        DSS_elem_list.append('XfmrCode')

        return BBDD_DSS, DSS_elem_list

    else:
        return BBDD_DSS, DSS_elem_list


