# -*- coding: utf-8 -*-
# @Time    : 18/05/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Line_modeling_DSS import \
    WireData_DSS, LineSpacing_DSS, LineGeometry_DSS, LineCode_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Trafo_DSS import xfmcode_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Rest_of_element_DSS import \
    DIGS_CNData_DSS, DIGS_GrowthShape_DSS, DIGS_LoadShape_DSS, DIGS_PriceShape_DSS, DIGS_Spectrum_DSS, \
    DIGS_TCC_Curve_DSS, DIGS_TSData_DSS, DIGS_TShape_DSS, DIGS_XYcurve_DSS

def General_elements_DSS(dict_df_DigS:dict, BBDD_OpenDSS:dict, OpenDSS_element_list:list):

    # from Line_modeling_DSS.py
    # WireData
    BBDD_OpenDSS['WireData'] = WireData_DSS(DataFrame_TypCon=dict_df_DigS['TypCon'])
    OpenDSS_element_list.append('WireData')

    # LineSpacing
    BBDD_OpenDSS['LineSpacing'] = LineSpacing_DSS(DataFrame_TypTow=dict_df_DigS['TypTow'],
                                                  DataFrame_TypGeo=dict_df_DigS['TypGeo'])
    OpenDSS_element_list.append('LineSpacing')

    # LineGeometry
    BBDD_OpenDSS['LineGeometry'] = LineGeometry_DSS(DataFrame_TypTow=dict_df_DigS['TypTow'],
                                                    DataFrame_TypCon=dict_df_DigS['TypCon'])
    OpenDSS_element_list.append('LineGeometry')

    BBDD_OpenDSS['LineCode'] = LineCode_DSS(DataFrame_TypLne=dict_df_DigS['TypLne'])
    OpenDSS_element_list.append('LineCode')

    # from Trafo_DSS
    # 2 winding transformer
    BBDD_OpenDSS['XfmrCode'] = xfmcode_DSS(DataFrame_TypTr2=dict_df_DigS['TypTr2'],
                                           DataFrame_TypTr3=dict_df_DigS['TypTr3'])
    OpenDSS_element_list.append('XfmrCode')

    BBDD_OpenDSS['CNData'] = DIGS_CNData_DSS()
    OpenDSS_element_list.append('CNData')

    BBDD_OpenDSS['GrowthShape'] = DIGS_GrowthShape_DSS()
    OpenDSS_element_list.append('GrowthShape')

    BBDD_OpenDSS['LoadShape'] = DIGS_LoadShape_DSS()
    OpenDSS_element_list.append('LoadShape')

    BBDD_OpenDSS['PriceShape'] = DIGS_PriceShape_DSS()
    OpenDSS_element_list.append('PriceShape')

    BBDD_OpenDSS['Spectrum'] = DIGS_Spectrum_DSS()
    OpenDSS_element_list.append('Spectrum')

    BBDD_OpenDSS['TCC_Curve'] = DIGS_TCC_Curve_DSS()
    OpenDSS_element_list.append('TCC_Curve')

    BBDD_OpenDSS['TSData'] = DIGS_TSData_DSS()
    OpenDSS_element_list.append('TSData')

    BBDD_OpenDSS['TShape'] = DIGS_TShape_DSS()
    OpenDSS_element_list.append('TShape')

    BBDD_OpenDSS['XYcurve'] = DIGS_XYcurve_DSS()
    OpenDSS_element_list.append('XYcurve')

    return BBDD_OpenDSS, OpenDSS_element_list