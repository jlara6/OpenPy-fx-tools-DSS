# -*- coding: utf-8 -*-
# @Time    : 17/06/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm
from typing import Dict, Any, Union

import pandas as pd
from numpy import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray

from helper_functions import *


def Buscoords_DSS(name_proyect: str, DataFrame_ElmTerm: pd.DataFrame, DataFrame_ElmSubstat: pd.DataFrame, out_path: str):
    """
    :param DataFrame_ElmTerm:
    :return: Buscoords_{name_proyect}.csv
    """
    df_ElmSubstat = DataFrame_ElmSubstat

    df_Buscoords_DSS = pd.DataFrame(
        columns=['Id_node', 'GPSlat(r)', 'GPSlon(r)'])

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTerm, 'loc_name(a:40)')
    DataFrame_ElmTerm = DataFrame_ElmTerm[DataFrame_ElmTerm['ciEnergized(i)'] == 1]

    for index, row in DataFrame_ElmTerm.iterrows():
        # name = DataFrame_ElmTerm['loc_name(a:40)'][index]
        lat = DataFrame_ElmTerm['GPSlat(r)'][index]
        lon = DataFrame_ElmTerm['GPSlon(r)'][index]

        if lat == 0 and lon == 0:

            if df_ElmSubstat.empty == True:
                pass
            else:
                id_node = DataFrame_ElmTerm['loc_name(a:40)'][index]
                df_ElmSubstat_aux = df_ElmSubstat[
                    df_ElmSubstat['ID(a:40)'] == DataFrame_ElmTerm['fold_id(p)'][index]].reset_index()
                if df_ElmSubstat_aux.empty == True:
                    GPSlat = 0
                    GPSlon = 0
                else:
                    GPSlat = df_ElmSubstat_aux.iloc[0]['GPSlat(r)']
                    GPSlon = df_ElmSubstat_aux.iloc[0]['GPSlon(r)']

                if GPSlat == 0 and GPSlon == 0:
                    pass
                else:
                    df_Buscoords_DSS = df_Buscoords_DSS.append(
                        {'Id_node': id_node, 'GPSlat(r)': GPSlat, 'GPSlon(r)': GPSlon}, ignore_index=True)

        else:
            id_node = DataFrame_ElmTerm['loc_name(a:40)'][index]
            GPSlat = DataFrame_ElmTerm['GPSlat(r)'][index]
            GPSlon = DataFrame_ElmTerm['GPSlon(r)'][index]

            df_Buscoords_DSS = df_Buscoords_DSS.append(
                {'Id_node': id_node, 'GPSlat(r)': GPSlat, 'GPSlon(r)': GPSlon}, ignore_index=True)

    df_Buscoords_DSS.to_csv(f'{out_path}\Buscoords_{name_proyect}.csv', index=False, header=False)

def BBDD_Buscoords_DSS(DataFrame_ElmTerm: pd.DataFrame, DataFrame_ElmSubstat: pd.DataFrame):
    """
    :param DataFrame_ElmTerm:
    :return: Buscoords_{name_proyect}.csv
    """
    df_ElmSubstat = DataFrame_ElmSubstat

    df_Buscoords_DSS = pd.DataFrame(
        columns=['Id_node', 'GPSlat(r)', 'GPSlon(r)'])

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTerm, 'loc_name(a:40)')
    DataFrame_ElmTerm = DataFrame_ElmTerm[DataFrame_ElmTerm['ciEnergized(i)'] == 1]

    for index, row in DataFrame_ElmTerm.iterrows():
        # name = DataFrame_ElmTerm['loc_name(a:40)'][index]
        lat = DataFrame_ElmTerm['GPSlat(r)'][index]
        lon = DataFrame_ElmTerm['GPSlon(r)'][index]

        if lat == 0 and lon == 0:

            if df_ElmSubstat.empty == True:
                id_node = DataFrame_ElmTerm['loc_name(a:40)'][index]
                GPSlat = ''
                GPSlon = ''

                df_Buscoords_DSS = df_Buscoords_DSS.append(
                    {'Id_node': id_node, 'GPSlat(r)': GPSlat, 'GPSlon(r)': GPSlon}, ignore_index=True)
            else:
                id_node = DataFrame_ElmTerm['loc_name(a:40)'][index]
                df_ElmSubstat_aux = df_ElmSubstat[
                    df_ElmSubstat['ID(a:40)'] == DataFrame_ElmTerm['fold_id(p)'][index]].reset_index()

                if df_ElmSubstat_aux.empty == True:
                    GPSlat = 0
                    GPSlon = 0
                else:
                    GPSlat = df_ElmSubstat_aux.iloc[0]['GPSlat(r)']
                    GPSlon = df_ElmSubstat_aux.iloc[0]['GPSlon(r)']

                if GPSlat == 0 and GPSlon == 0:
                    GPSlat = ''
                    GPSlon = ''
                    df_Buscoords_DSS = df_Buscoords_DSS.append(
                        {'Id_node': id_node, 'GPSlat(r)': GPSlat, 'GPSlon(r)': GPSlon}, ignore_index=True)
                    # pass
                else:
                    df_Buscoords_DSS = df_Buscoords_DSS.append(
                        {'Id_node': id_node, 'GPSlat(r)': GPSlat, 'GPSlon(r)': GPSlon}, ignore_index=True)

        else:
            id_node = DataFrame_ElmTerm['loc_name(a:40)'][index]
            GPSlat = DataFrame_ElmTerm['GPSlat(r)'][index]
            GPSlon = DataFrame_ElmTerm['GPSlon(r)'][index]

            df_Buscoords_DSS = df_Buscoords_DSS.append(
                {'Id_node': id_node, 'GPSlat(r)': GPSlat, 'GPSlon(r)': GPSlon}, ignore_index=True)

    return df_Buscoords_DSS


def Buscoords_trafo_Tr2(DataFrame_ElmTr2:pd.DataFrame, DataFrame_ElmTerm:pd.DataFrame,
                       DataFrame_StaCubic:pd.DataFrame )->pd.DataFrame:

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

    df_trafo_Tr2_DSS = df_trafo_Tr2_DSS.rename(columns={'Bus_hv': 'bus1', 'Bus_lv': 'bus2'})
    return df_trafo_Tr2_DSS


def Buscoords_Bus1(name_element: str, name_column: list, BBDD_OpenDSS: pd.DataFrame, df_Buscoords_DSS: pd.DataFrame,
                  df_StaCubic_ElmTerm: pd.DataFrame):

    BBDD_Buscoords = dict()

    BBDD_Buscoords[name_element] = BBDD_OpenDSS[name_element][name_column]
    BBDD_Buscoords[name_element].loc[:, 'GPSlat(r)_bus1'] = ''
    BBDD_Buscoords[name_element].loc[:, 'GPSlon(r)_bus1'] = ''

    for index, row in BBDD_Buscoords[name_element].iterrows():
        name_elem = BBDD_Buscoords[name_element]['bus1'][index]
        df_name = df_StaCubic_ElmTerm[df_StaCubic_ElmTerm['Bus_name_DSS'] == name_elem].reset_index()
        name_ph_no = df_name['loc_name(a:40)'][0]
        BBDD_Buscoords[name_element]['bus1'][index] = name_ph_no
        df_aux = df_Buscoords_DSS[df_Buscoords_DSS['Id_node'] == name_ph_no].reset_index()
        if df_aux.empty == True:
            pass
        else:
            BBDD_Buscoords[name_element]['GPSlat(r)_bus1'][index] = df_aux.loc[0, 'GPSlat(r)']
            BBDD_Buscoords[name_element]['GPSlon(r)_bus1'][index] = df_aux.loc[0, 'GPSlon(r)']

    return BBDD_Buscoords[name_element]

def Buscoords_Load_Bus1(name_element: str, name_column: list, BBDD_OpenDSS: pd.DataFrame, df_Buscoords_DSS: pd.DataFrame,
                  df_StaCubic_ElmTerm: pd.DataFrame):

    BBDD_Buscoords = dict()

    BBDD_Buscoords[name_element] = BBDD_OpenDSS[name_element][name_column]
    BBDD_Buscoords[name_element].loc[:, 'GPSlat(r)_bus1'] = ''
    BBDD_Buscoords[name_element].loc[:, 'GPSlon(r)_bus1'] = ''

    for index, row in BBDD_Buscoords[name_element].iterrows():
        name_elem = BBDD_Buscoords[name_element]['bus1'][index]
        df_name = df_StaCubic_ElmTerm[df_StaCubic_ElmTerm['Bus_name_DSS'] == name_elem].reset_index()
        name_ph_no = df_name['loc_name(a:40)'][0]
        BBDD_Buscoords[name_element]['bus1'][index] = name_ph_no
        df_aux = df_Buscoords_DSS[df_Buscoords_DSS['Id_node'] == name_ph_no].reset_index()
        if df_aux.empty == True:
            pass
        else:
            BBDD_Buscoords[name_element]['GPSlat(r)_bus1'][index] = df_aux.loc[0, 'GPSlat(r)']
            BBDD_Buscoords[name_element]['GPSlon(r)_bus1'][index] = df_aux.loc[0, 'GPSlon(r)']

    return BBDD_Buscoords[name_element]

def Buscoords_Bus1_Bus2(name_element:str, name_column:list, BBDD_OpenDSS: pd.DataFrame, df_Buscoords_DSS: pd.DataFrame,
                       df_StaCubic_ElmTerm: pd.DataFrame):

    BBDD_Buscoords = dict()

    BBDD_Buscoords[name_element] = BBDD_OpenDSS[name_element][name_column]

    BBDD_Buscoords[name_element].loc[:, 'GPSlat(r)_bus1'] = ''
    BBDD_Buscoords[name_element].loc[:, 'GPSlon(r)_bus1'] = ''

    BBDD_Buscoords[name_element].loc[:, 'GPSlat(r)_bus2'] = ''
    BBDD_Buscoords[name_element].loc[:, 'GPSlon(r)_bus2'] = ''

    for index, row in BBDD_Buscoords[name_element].iterrows():
        name_elem_b1 = BBDD_Buscoords[name_element]['bus1'][index]
        df_name_b1 = df_StaCubic_ElmTerm[df_StaCubic_ElmTerm['Bus_name_DSS'] == name_elem_b1].reset_index()
        name_ph_no_b1 = df_name_b1['loc_name(a:40)'][0]
        BBDD_Buscoords[name_element]['bus1'][index] = name_ph_no_b1
        df_aux_b1 = df_Buscoords_DSS[df_Buscoords_DSS['Id_node'] == name_ph_no_b1].reset_index()

        name_elem_b2 = BBDD_Buscoords[name_element]['bus2'][index]
        df_name_b2 = df_StaCubic_ElmTerm[df_StaCubic_ElmTerm['Bus_name_DSS'] == name_elem_b2].reset_index()
        name_ph_no_b2 = df_name_b2['loc_name(a:40)'][0]
        BBDD_Buscoords[name_element]['bus2'][index] = name_ph_no_b2
        df_aux_b2 = df_Buscoords_DSS[df_Buscoords_DSS['Id_node'] == name_ph_no_b2].reset_index()

        if df_aux_b1.empty == True and df_aux_b2.empty == True:
            pass

        elif df_aux_b1.empty == True and df_aux_b2.empty == False:
            BBDD_Buscoords[name_element]['GPSlat(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlat(r)']
            BBDD_Buscoords[name_element]['GPSlon(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlon(r)']

        elif df_aux_b1.empty == False and df_aux_b2.empty == True:
            BBDD_Buscoords[name_element]['GPSlat(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlat(r)']
            BBDD_Buscoords[name_element]['GPSlon(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlon(r)']

        else:
            BBDD_Buscoords[name_element]['GPSlat(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlat(r)']
            BBDD_Buscoords[name_element]['GPSlon(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlon(r)']

            BBDD_Buscoords[name_element]['GPSlat(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlat(r)']
            BBDD_Buscoords[name_element]['GPSlon(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlon(r)']

    return BBDD_Buscoords[name_element]


def Buscoords_trafo_Tr2_Bus1_Bus2(df_trafo_Tr2_Buscoords: pd.DataFrame, df_Buscoords_DSS: pd.DataFrame,
                                 df_StaCubic_ElmTerm: pd.DataFrame):

    df_trafo_Tr2_Buscoords.loc[:, 'GPSlat(r)_bus1'] = ''
    df_trafo_Tr2_Buscoords.loc[:, 'GPSlon(r)_bus1'] = ''

    df_trafo_Tr2_Buscoords.loc[:, 'GPSlat(r)_bus2'] = ''
    df_trafo_Tr2_Buscoords.loc[:, 'GPSlon(r)_bus2'] = ''

    for index, row in df_trafo_Tr2_Buscoords.iterrows():
        name_elem_b1 = df_trafo_Tr2_Buscoords['bus1'][index]
        df_name_b1 = df_StaCubic_ElmTerm[df_StaCubic_ElmTerm['Bus_name_DSS'] == name_elem_b1].reset_index()
        name_ph_no_b1 = df_name_b1['loc_name(a:40)'][0]
        df_trafo_Tr2_Buscoords['bus1'][index] = name_ph_no_b1
        df_aux_b1 = df_Buscoords_DSS[df_Buscoords_DSS['Id_node'] == name_ph_no_b1].reset_index()

        name_elem_b2 = df_trafo_Tr2_Buscoords['bus2'][index]
        df_name_b2 = df_StaCubic_ElmTerm[df_StaCubic_ElmTerm['Bus_name_DSS'] == name_elem_b2].reset_index()
        name_ph_no_b2 = df_name_b2['loc_name(a:40)'][0]
        df_trafo_Tr2_Buscoords['bus2'][index] = name_ph_no_b2
        df_aux_b2 = df_Buscoords_DSS[df_Buscoords_DSS['Id_node'] == name_ph_no_b2].reset_index()

        if df_aux_b1.empty == True and df_aux_b2.empty == True:
            pass

        elif df_aux_b1.empty == True and df_aux_b2.empty == False:
            df_trafo_Tr2_Buscoords['GPSlat(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlat(r)']
            df_trafo_Tr2_Buscoords['GPSlon(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlon(r)']

        elif df_aux_b1.empty == False and df_aux_b2.empty == True:
            df_trafo_Tr2_Buscoords['GPSlat(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlat(r)']
            df_trafo_Tr2_Buscoords['GPSlon(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlon(r)']

        else:
            df_trafo_Tr2_Buscoords['GPSlat(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlat(r)']
            df_trafo_Tr2_Buscoords['GPSlon(r)_bus1'][index] = df_aux_b1.loc[0, 'GPSlon(r)']

            df_trafo_Tr2_Buscoords['GPSlat(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlat(r)']
            df_trafo_Tr2_Buscoords['GPSlon(r)_bus2'][index] = df_aux_b2.loc[0, 'GPSlon(r)']

    return df_trafo_Tr2_Buscoords


def file_Buscoords_DSS_orig(workbook:str, BBDD_OpenDSS:dict, dict_df_DigS:dict, out_path:str):

    element_list = list()
    BBDD_Buscoords = dict()

    df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=dict_df_DigS['StaCubic'],
                                                 DataFrame_ElmTerm=dict_df_DigS['ElmTerm'])

    df_trafo_Tr2 = Buscoords_trafo_Tr2(DataFrame_ElmTr2=dict_df_DigS['ElmTr2'],
                                      DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                      DataFrame_StaCubic=dict_df_DigS['StaCubic'])

    df_Buscoords_DSS = BBDD_Buscoords_DSS(DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                        DataFrame_ElmSubstat=dict_df_DigS['ElmSubstat'])

    if df_Buscoords_DSS.empty == True:
        pass
    else:
        BBDD_Buscoords['Buscoords'] = df_Buscoords_DSS
        element_list.append('Buscoords')

    if BBDD_OpenDSS['Vsource'].empty == True :
        pass
    else:
        BBDD_Buscoords['Vsource'] = Buscoords_Bus1(name_element='Vsource', name_column=['Id_Vsource', 'bus1'],
                                                 BBDD_OpenDSS=BBDD_OpenDSS, df_Buscoords_DSS=df_Buscoords_DSS,
                                                 df_StaCubic_ElmTerm=df_StaCubic_ElmTerm)
        element_list.append('Vsource')

    if BBDD_OpenDSS['Line'].empty == True :
        pass
    else:
        BBDD_Buscoords['Line'] = Buscoords_Bus1_Bus2(name_element='Line', name_column=['Id_Line', 'bus1', 'bus2'],
                                                   BBDD_OpenDSS=BBDD_OpenDSS, df_Buscoords_DSS=df_Buscoords_DSS,
                                                   df_StaCubic_ElmTerm=df_StaCubic_ElmTerm)
        element_list.append('Line')

    if BBDD_OpenDSS['Switch'].empty == True:
        pass
    else:
        BBDD_Buscoords['Switch'] = Buscoords_Bus1_Bus2(name_element='Switch', name_column=['Id_Switch', 'bus1', 'bus2'],
                                                     BBDD_OpenDSS=BBDD_OpenDSS, df_Buscoords_DSS=df_Buscoords_DSS,
                                                     df_StaCubic_ElmTerm=df_StaCubic_ElmTerm)
        element_list.append('Switch')

    if BBDD_OpenDSS['Transformer'].empty == True:
        pass
    else:
        BBDD_Buscoords['Transformer'] = Buscoords_trafo_Tr2_Bus1_Bus2(df_trafo_Tr2_Buscoords=df_trafo_Tr2,
                                                                    df_Buscoords_DSS=df_Buscoords_DSS,
                                                                    df_StaCubic_ElmTerm=df_StaCubic_ElmTerm)
        element_list.append('Transformer')

    if BBDD_OpenDSS['Load'].empty == True:
        pass
    else:
        BBDD_Buscoords['Load'] = Buscoords_Bus1(name_element='Load', name_column=['Id_Load', 'bus1'],
                                              BBDD_OpenDSS=BBDD_OpenDSS, df_Buscoords_DSS=df_Buscoords_DSS,
                                              df_StaCubic_ElmTerm=df_StaCubic_ElmTerm)
        element_list.append('Load')

    workbook_aux = f'BBDD_Buscoords_{workbook}.xlsx'
    save_BBDD_xlsx(workbook_DSS=workbook_aux, elements_OpenDSS=element_list, BBDD_OpenDSS=BBDD_Buscoords, out_path=out_path)

    '**********'
    #workbook_DSS = f'BBDD_DSS_{projects_name}.xlsx'
    #save_BBDD_xlsx(workbook_DSS=workbook_DSS, elements_OpenDSS=OpenDSS_element_list, BBDD_OpenDSS=BBDD_OpenDSS, out_path=out_path)

    return BBDD_Buscoords, element_list


def file_Buscoords_DSS(workbook: str, BBDD_OpenDSS:dict, dict_df_DigS:dict, out_path:str):

    element_list = list()
    BBDD_Buscoords = dict()

    df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=dict_df_DigS['StaCubic'],
                                                 DataFrame_ElmTerm=dict_df_DigS['ElmTerm'])


    df_Buscoords_DSS = BBDD_Buscoords_DSS(DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                          DataFrame_ElmSubstat=dict_df_DigS['ElmSubstat'])

    BBDD_Buscoords['Buscoords'] = df_Buscoords_DSS
    element_list.append('Buscoords')

    BBDD_Buscoords['Vsource'] = Buscoords_Vsource(DataFrame_ElmXnet=dict_df_DigS['ElmXnet'],
                                                  df_StaCubic_ElmTerm=df_StaCubic_ElmTerm,
                                                  DataFrame_Buscoords=df_Buscoords_DSS)
    element_list.append('Vsource')

    BBDD_Buscoords['Line'] = Buscoords_Line(DataFrame_ElmLne=dict_df_DigS['ElmLne'],
                                            df_StaCubic_ElmTerm=df_StaCubic_ElmTerm,
                                            DataFrame_Buscoords=df_Buscoords_DSS)
    element_list.append('Line')

    BBDD_Buscoords['Switch'] = Buscoords_Switch(DataFrame_ElmCoup=dict_df_DigS['ElmCoup'],
                                                DataFrame_RelFuse=dict_df_DigS['RelFuse'],
                                                df_StaCubic_ElmTerm=df_StaCubic_ElmTerm,
                                                DataFrame_Buscoords=df_Buscoords_DSS)

    element_list.append('Switch')

    BBDD_Buscoords['Transformer'] = Buscoords_Transformer(DataFrame_ElmTr2=dict_df_DigS['ElmTr2'],
                                                          df_StaCubic_ElmTerm=df_StaCubic_ElmTerm,
                                                          DataFrame_Buscoords=df_Buscoords_DSS)
    element_list.append('Transformer')

    BBDD_Buscoords['Load'] = Buscoords_Load(DataFrame_ElmLod=dict_df_DigS['ElmLod'],
                                            df_StaCubic_ElmTerm=df_StaCubic_ElmTerm,
                                            DataFrame_Buscoords=df_Buscoords_DSS)
    element_list.append('Load')

    BBDD_Buscoords['Capacitor'] = Buscoords_Capacitor(DataFrame_ElmShnt=dict_df_DigS['ElmShnt'],
                                                      df_StaCubic_ElmTerm=df_StaCubic_ElmTerm,
                                                      DataFrame_Buscoords=df_Buscoords_DSS)
    element_list.append('Capacitor')


    workbook_aux = f'BBDD_Buscoords_{workbook}.xlsx'
    save_BBDD_xlsx(workbook_DSS=workbook_aux, elements_OpenDSS=element_list,
                   BBDD_OpenDSS=BBDD_Buscoords, out_path=out_path)

    '**********'
    #workbook_DSS = f'BBDD_DSS_{projects_name}.xlsx'
    #save_BBDD_xlsx(workbook_DSS=workbook_DSS, elements_OpenDSS=OpenDSS_element_list, BBDD_OpenDSS=BBDD_OpenDSS, out_path=out_path)

    return BBDD_Buscoords, element_list

def Buscoords_Vsource(DataFrame_ElmXnet: pd.DataFrame, df_StaCubic_ElmTerm: pd.DataFrame, DataFrame_Buscoords: pd.DataFrame):

    df_Vsource_DSS = pd.DataFrame(columns=['Id_Vsource', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1'])

    if DataFrame_ElmXnet.empty == True:
        ElmXnet_Buscoords = df_Vsource_DSS

    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmXnet, 'loc_name(a:40)')
        DataFrame_ElmXnet = DataFrame_ElmXnet[['loc_name(a:40)', 'bus1(p)']]

        merge_ElmXnet_StaCubic = pd.merge(DataFrame_ElmXnet, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                         suffixes=('_x', '_y'))

        DataFrame_ElmXnet = merge_ElmXnet_StaCubic[['loc_name(a:40)_x', 'loc_name(a:40)_y']].rename(
            columns={'loc_name(a:40)_x': 'Id_Vsource', 'loc_name(a:40)_y': 'bus1'})

        ElmXnet_Buscoords = pd.merge(DataFrame_ElmXnet, DataFrame_Buscoords, how='inner', left_on='bus1', right_on='Id_node',
                                         suffixes=('_x', '_y')).rename(
            columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})

        ElmXnet_Buscoords = ElmXnet_Buscoords[['Id_Vsource', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    return ElmXnet_Buscoords

def Buscoords_Line(DataFrame_ElmLne: pd.DataFrame, df_StaCubic_ElmTerm: pd.DataFrame, DataFrame_Buscoords: pd.DataFrame):

    df_Line_DSS = pd.DataFrame(columns=['Id_Line',
                                        'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                        'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2'])

    if DataFrame_ElmLne.empty == True:
        Line_Buscoords = df_Line_DSS

    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmLne, 'loc_name(a:40)')

        df_name = DataFrame_ElmLne[['ID(a:40)', 'loc_name(a:40)']]
        df_bus1 = DataFrame_ElmLne[['ID(a:40)', 'bus1(p)']]
        df_bus2 = DataFrame_ElmLne[['ID(a:40)', 'bus2(p)']]
        'Bus 1'
        df_bus1_conn = pd.merge(df_bus1, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                suffixes=('_x', '_y'))
        df_bus1_conn = df_bus1_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bus1'})
        df_bus1_conn_coords = pd.merge(df_bus1_conn, DataFrame_Buscoords, how='inner', left_on='bus1', right_on='Id_node',
                                suffixes=('_x', '_y')).rename(columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})

        df_bus1_conn_coords = df_bus1_conn_coords[['ID(a:40)', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

        'Bus 2'
        df_bus2_conn = pd.merge(df_bus2, df_StaCubic_ElmTerm, how='inner', left_on='bus2(p)', right_on='ID(a:40)',
                                suffixes=('_x', '_y'))
        df_bus2_conn = df_bus2_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(
            columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bus2'})
        df_bus2_conn_coords = pd.merge(df_bus2_conn, DataFrame_Buscoords, how='inner', left_on='bus2',
                                       right_on='Id_node',
                                       suffixes=('_x', '_y')).rename(
            columns={'GPSlat(r)': 'GPSlat(r)_bus2', 'GPSlon(r)': 'GPSlon(r)_bus2'})

        df_bus2_conn_coords = df_bus2_conn_coords[['ID(a:40)', 'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]
        'Merge Bus 1 and Bus 2'

        df_bus1_bus2_coords = pd.merge(df_bus1_conn_coords, df_bus2_conn_coords, on='ID(a:40)')

        Line_Buscoords = pd.merge(df_name, df_bus1_bus2_coords, on='ID(a:40)').rename(columns={'loc_name(a:40)': 'Id_Line'})
        Line_Buscoords = Line_Buscoords[['Id_Line',
                                        'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                        'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]

    return Line_Buscoords

def Buscoords_Switch(DataFrame_ElmCoup: pd.DataFrame, DataFrame_RelFuse: pd.DataFrame,
                     df_StaCubic_ElmTerm: pd.DataFrame, DataFrame_Buscoords: pd.DataFrame):

    df_Switch_DSS = pd.DataFrame(columns=['Id_Switch',
                                          'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                          'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2'])

    if DataFrame_ElmCoup.empty == True and DataFrame_RelFuse.empty == True:
        Switch_Buscoords = df_Switch_DSS
    else:

        if DataFrame_ElmCoup.empty == True:
            ElmCoup_Buscoords = pd.DataFrame(columns=['Id_Switch',
                                                      'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                                      'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2'])
        else:
            characters_delete(DataFrame_ElmCoup, 'loc_name(a:40)')
            df_name = DataFrame_ElmCoup[['ID(a:40)', 'loc_name(a:40)']]
            df_bus1 = DataFrame_ElmCoup[['ID(a:40)', 'bus1(p)']]
            df_bus2 = DataFrame_ElmCoup[['ID(a:40)', 'bus2(p)']]
            'Bus 1'
            df_bus1_conn = pd.merge(df_bus1, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                    suffixes=('_x', '_y'))
            df_bus1_conn = df_bus1_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bus1'})
            df_bus1_conn_coords = pd.merge(df_bus1_conn, DataFrame_Buscoords, how='inner', left_on='bus1', right_on='Id_node',
                                    suffixes=('_x', '_y')).rename(columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})

            df_bus1_conn_coords = df_bus1_conn_coords[['ID(a:40)', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

            'Bus 2'
            df_bus2_conn = pd.merge(df_bus2, df_StaCubic_ElmTerm, how='inner', left_on='bus2(p)', right_on='ID(a:40)',
                                    suffixes=('_x', '_y'))
            df_bus2_conn = df_bus2_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(
                columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bus2'})
            df_bus2_conn_coords = pd.merge(df_bus2_conn, DataFrame_Buscoords, how='inner', left_on='bus2',
                                           right_on='Id_node',
                                           suffixes=('_x', '_y')).rename(
                columns={'GPSlat(r)': 'GPSlat(r)_bus2', 'GPSlon(r)': 'GPSlon(r)_bus2'})

            df_bus2_conn_coords = df_bus2_conn_coords[['ID(a:40)', 'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]
            'Merge Bus 1 and Bus 2'

            df_bus1_bus2_coords = pd.merge(df_bus1_conn_coords, df_bus2_conn_coords, on='ID(a:40)')

            ElmCoup_Buscoords = pd.merge(df_name, df_bus1_bus2_coords, on='ID(a:40)').rename(columns={'loc_name(a:40)': 'Id_Switch'})
            ElmCoup_Buscoords = ElmCoup_Buscoords[['Id_Switch',
                                                   'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                                   'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]

        if DataFrame_RelFuse.empty == True:
            RelFuse_Buscoords = pd.DataFrame(columns=['Id_Switch',
                                                      'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                                      'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2'])
        else:

            characters_delete(DataFrame_RelFuse, 'loc_name(a:40)')
            df_name = DataFrame_RelFuse[['ID(a:40)', 'loc_name(a:40)']]
            df_bus1 = DataFrame_RelFuse[['ID(a:40)', 'bus1(p)']]
            df_bus2 = DataFrame_RelFuse[['ID(a:40)', 'bus2(p)']]
            'Bus 1'
            df_bus1_conn = pd.merge(df_bus1, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                    suffixes=('_x', '_y'))
            df_bus1_conn = df_bus1_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bus1'})
            df_bus1_conn_coords = pd.merge(df_bus1_conn, DataFrame_Buscoords, how='inner', left_on='bus1', right_on='Id_node',
                                    suffixes=('_x', '_y')).rename(columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})

            df_bus1_conn_coords = df_bus1_conn_coords[['ID(a:40)', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

            'Bus 2'
            df_bus2_conn = pd.merge(df_bus2, df_StaCubic_ElmTerm, how='inner', left_on='bus2(p)', right_on='ID(a:40)',
                                    suffixes=('_x', '_y'))
            df_bus2_conn = df_bus2_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(
                columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bus2'})
            df_bus2_conn_coords = pd.merge(df_bus2_conn, DataFrame_Buscoords, how='inner', left_on='bus2',
                                           right_on='Id_node',
                                           suffixes=('_x', '_y')).rename(
                columns={'GPSlat(r)': 'GPSlat(r)_bus2', 'GPSlon(r)': 'GPSlon(r)_bus2'})

            df_bus2_conn_coords = df_bus2_conn_coords[['ID(a:40)', 'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]
            'Merge Bus 1 and Bus 2'

            df_bus1_bus2_coords = pd.merge(df_bus1_conn_coords, df_bus2_conn_coords, on='ID(a:40)')

            RelFuse_Buscoords = pd.merge(df_name, df_bus1_bus2_coords, on='ID(a:40)').rename(columns={'loc_name(a:40)': 'Id_Switch'})
            RelFuse_Buscoords = RelFuse_Buscoords[['Id_Switch',
                                                 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1',
                                                 'bus2', 'GPSlat(r)_bus2', 'GPSlon(r)_bus2']]

        Switch_Buscoords = pd.concat([ElmCoup_Buscoords, RelFuse_Buscoords])

    return Switch_Buscoords

def Buscoords_Transformer(DataFrame_ElmTr2: pd.DataFrame, df_StaCubic_ElmTerm: pd.DataFrame, DataFrame_Buscoords: pd.DataFrame):

    df_Transformer_DSS = pd.DataFrame(columns=['Id_Transformer',
                                               'bushv', 'GPSlat(r)_bushv', 'GPSlon(r)_bushv',
                                               'buslv', 'GPSlat(r)_buslv', 'GPSlon(r)_buslv'])

    if DataFrame_ElmTr2.empty == True:
        Transformer_Buscoords = df_Transformer_DSS

    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmTr2, 'loc_name(a:40)')

        df_name = DataFrame_ElmTr2[['ID(a:40)', 'loc_name(a:40)']]
        df_bushv = DataFrame_ElmTr2[['ID(a:40)', 'bushv(p)']]
        df_buslv = DataFrame_ElmTr2[['ID(a:40)', 'buslv(p)']]
        'Bus 1'
        df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm, how='inner', left_on='bushv(p)', right_on='ID(a:40)',
                                suffixes=('_x', '_y'))
        df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'bushv'})
        df_bushv_conn_coords = pd.merge(df_bushv_conn, DataFrame_Buscoords, how='inner', left_on='bushv', right_on='Id_node',
                                suffixes=('_x', '_y')).rename(columns={'GPSlat(r)': 'GPSlat(r)_bushv', 'GPSlon(r)': 'GPSlon(r)_bushv'})

        df_bushv_conn_coords = df_bushv_conn_coords[['ID(a:40)', 'bushv', 'GPSlat(r)_bushv', 'GPSlon(r)_bushv']]

        'Bus 2'
        df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm, how='inner', left_on='buslv(p)', right_on='ID(a:40)',
                                suffixes=('_x', '_y'))
        df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'loc_name(a:40)']].rename(
            columns={'ID(a:40)_x': 'ID(a:40)', 'loc_name(a:40)': 'buslv'})
        df_buslv_conn_coords = pd.merge(df_buslv_conn, DataFrame_Buscoords, how='inner', left_on='buslv',
                                       right_on='Id_node',
                                       suffixes=('_x', '_y')).rename(
            columns={'GPSlat(r)': 'GPSlat(r)_buslv', 'GPSlon(r)': 'GPSlon(r)_buslv'})

        df_buslv_conn_coords = df_buslv_conn_coords[['ID(a:40)', 'buslv', 'GPSlat(r)_buslv', 'GPSlon(r)_buslv']]
        'Merge Bus 1 and Bus 2'

        df_bushv_buslv_coords = pd.merge(df_bushv_conn_coords, df_buslv_conn_coords, on='ID(a:40)')

        Transformer_Buscoords = pd.merge(df_name, df_bushv_buslv_coords, on='ID(a:40)').rename(columns={'loc_name(a:40)': 'Id_Transformer'})
        Transformer_Buscoords = Transformer_Buscoords[['Id_Transformer',
                                                       'bushv', 'GPSlat(r)_bushv', 'GPSlon(r)_bushv',
                                                       'buslv', 'GPSlat(r)_buslv', 'GPSlon(r)_buslv']]


    return Transformer_Buscoords

def Buscoords_Load(DataFrame_ElmLod: pd.DataFrame, df_StaCubic_ElmTerm: pd.DataFrame, DataFrame_Buscoords: pd.DataFrame):

    df_Load_DSS = pd.DataFrame(columns=['Id_Load', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1'])

    if DataFrame_ElmLod.empty == True:
        ElmLod_Buscoords = df_Load_DSS

    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmLod, 'loc_name(a:40)')
        DataFrame_ElmLod = DataFrame_ElmLod[['loc_name(a:40)', 'bus1(p)']]

        merge_ElmLod_StaCubic = pd.merge(DataFrame_ElmLod, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                         suffixes=('_x', '_y'))

        DataFrame_ElmLod = merge_ElmLod_StaCubic[['loc_name(a:40)_x', 'loc_name(a:40)_y']].rename(
            columns={'loc_name(a:40)_x': 'Id_Load', 'loc_name(a:40)_y': 'bus1'})

        ElmLod_Buscoords = pd.merge(DataFrame_ElmLod, DataFrame_Buscoords, how='inner', left_on='bus1', right_on='Id_node',
                                         suffixes=('_x', '_y')).rename(
            columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})

        ElmLod_Buscoords = ElmLod_Buscoords[['Id_Load', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    return ElmLod_Buscoords

def Buscoords_Capacitor(DataFrame_ElmShnt: pd.DataFrame, df_StaCubic_ElmTerm: pd.DataFrame, DataFrame_Buscoords: pd.DataFrame):

    df_Capacitor_DSS = pd.DataFrame(columns=['Id_Capacitor', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1'])

    if DataFrame_ElmShnt.empty == True:
        ElmShnt_Buscoords = df_Capacitor_DSS

    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmShnt, 'loc_name(a:40)')
        DataFrame_ElmShnt = DataFrame_ElmShnt[['loc_name(a:40)', 'bus1(p)']]

        merge_ElmShnt_StaCubic = pd.merge(DataFrame_ElmShnt, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)',
                                         right_on='ID(a:40)', suffixes=('_x', '_y'))

        DataFrame_ElmShnt = merge_ElmShnt_StaCubic[['loc_name(a:40)_x', 'loc_name(a:40)_y']].rename(
            columns={'loc_name(a:40)_x': 'Id_Capacitor', 'loc_name(a:40)_y': 'bus1'})

        ElmShnt_Buscoords = pd.merge(DataFrame_ElmShnt, DataFrame_Buscoords, how='inner', left_on='bus1',
                                    right_on='Id_node', suffixes=('_x', '_y')).rename(
            columns={'GPSlat(r)': 'GPSlat(r)_bus1', 'GPSlon(r)': 'GPSlon(r)_bus1'})

        ElmShnt_Buscoords = ElmShnt_Buscoords[['Id_Capacitor', 'bus1', 'GPSlat(r)_bus1', 'GPSlon(r)_bus1']]

    return ElmShnt_Buscoords