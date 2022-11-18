# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from py_fx_tools_dss.helper_functions import *
import pandas as pd

def reliability_trafo_Tr2(DataFrame_ElmTr2:pd.DataFrame, DataFrame_ElmTerm:pd.DataFrame, DataFrame_StaCubic:pd.DataFrame )->pd.DataFrame:


    df_trafo_Tr2_DSS = pd.DataFrame(columns= ['Id_Transformer', 'Bus_hv', 'Bus_lv'])

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTr2, 'loc_name(a:40)')

    df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic, DataFrame_ElmTerm=DataFrame_ElmTerm)
    'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
    'Result -> df_bushv_buslv_conn'
    df_bushv = DataFrame_ElmTr2[['ID(a:40)', 'bushv(p)']]
    df_buslv = DataFrame_ElmTr2[['ID(a:40)', 'buslv(p)']]
    'Bus High Voltage'
    df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm, how='inner', left_on='bushv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
    df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
    'Bus Low Voltage'
    df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm, how='inner', left_on='buslv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
    df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
    'Merge Bus_HV and Bus_LV'
    df_bushv_buslv_conn = pd.merge(df_bushv_conn, df_buslv_conn, on='ID(a:40)').rename(columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'buslv_dss'})

    merge_Elm_Typ_Tr2_buses_HV_LV = pd.merge(DataFrame_ElmTr2, df_bushv_buslv_conn, how='inner', left_on='ID(a:40)', right_on='ID(a:40)', suffixes=('_x', '_y') )
    merge_Elm_Typ_Tr2_buses_HV_LV = merge_Elm_Typ_Tr2_buses_HV_LV[['loc_name(a:40)', 'bushv_dss', 'buslv_dss']]

    for index, row in merge_Elm_Typ_Tr2_buses_HV_LV.iterrows():
        id_trafo = merge_Elm_Typ_Tr2_buses_HV_LV['loc_name(a:40)'][index]
        bushv = merge_Elm_Typ_Tr2_buses_HV_LV['bushv_dss'][index]
        buslv = merge_Elm_Typ_Tr2_buses_HV_LV['buslv_dss'][index]

        df_trafo_Tr2_DSS = df_trafo_Tr2_DSS.append({'Id_Transformer':id_trafo, 'Bus_hv':bushv, 'Bus_lv':buslv}, ignore_index=True)

    return df_trafo_Tr2_DSS

def column_selection_for_reliability(workbook:str, BBDD_OpenDSS:dict, dict_df_DigS:dict, out_path:str):

    element_list = list()
    BBDD_reliability = dict()

    BBDD_reliability['Vsource'] = BBDD_OpenDSS['Vsource'][['Id_Vsource', 'bus1']]
    element_list.append('Vsource')

    BBDD_reliability['Transformer'] = reliability_trafo_Tr2(DataFrame_ElmTr2=dict_df_DigS['ElmTr2'],
                                                            DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                                            DataFrame_StaCubic=dict_df_DigS['StaCubic'])
    element_list.append('Transformer')

    BBDD_reliability['Line'] = BBDD_OpenDSS['Line'][['Id_Line', 'bus1', 'bus2', 'length', 'units']]
    element_list.append('Line')

    BBDD_reliability['Switch'] = BBDD_OpenDSS['Switch'][['Id_Switch', 'bus1', 'bus2', 'length', 'units']]
    element_list.append('Switch')

    BBDD_reliability['Load'] = BBDD_OpenDSS['Load'][['Id_Load', 'bus1', 'kvar', 'Kw', 'NumCust']]
    element_list.append('Load')

    workbook_aux = f'BBDD_reliability_{workbook}.xlsx'
    _save_BBDD_xlsx(workbook_DSS=workbook_aux, elements_OpenDSS=element_list, BBDD_OpenDSS=BBDD_reliability, out_path=out_path)

    '**********'
    #workbook_DSS = f'BBDD_DSS_{projects_name}.xlsx'
    #_save_BBDD_xlsx(workbook_DSS=workbook_DSS, elements_OpenDSS=OpenDSS_element_list, BBDD_OpenDSS=BBDD_OpenDSS, path_save=path_save)

    return BBDD_reliability, element_list