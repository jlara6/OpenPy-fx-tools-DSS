# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm
import pandas as pd
import numpy as np

from openpy_fx_tools_dss.helper_functions import *

def DIGS_line_DSS(DataFrame_ElmLne:pd.DataFrame, DataFrame_TypTow:pd.DataFrame, DataFrame_TypLne:pd.DataFrame, DataFrame_ElmTerm:pd.DataFrame, DataFrame_StaCubic:pd.DataFrame,
                  DataFrame_TypGeo: pd.DataFrame, DataFrame_TypCon: pd.DataFrame )->pd.DataFrame:
    '''
    :param DataFrame_ElmLne:
    :param DataFrame_TypTow:
    :return: df_Line_DSS
    '''

    'DataFrame creation with OpenDSS keywords'
    df_Line_DSS = pd.DataFrame(columns=['Id_Line', 'phases', 'bus1', 'bus2', 'linecode', 'geometry', 'spacing',
                                        'wires', 'length', 'units', 'r1', 'x1', 'r0', 'x0', 'C1', 'C0', 'B1', 'B0',
                                        'rmatrix', 'xmatrix', 'cmatrix', 'Switch', 'Rg', 'Xg', 'rho', 'EathModel',
                                        'cncables', 'tscables', 'Seasons', 'Ratings', 'LineType', 'normamps',
                                        'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like'])

    if DataFrame_ElmLne.empty == True:
        pass
    else:
        DataFrame_ElmLne = DataFrame_ElmLne[DataFrame_ElmLne['ciEnergized(i)'] == 1]  # Filters energized elements
        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)

        df_StaCubic_ElmTerm = df_StaCubic_ElmTerm[['ID(a:40)', 'Bus_name_DSS']]

        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmLne, 'loc_name(a:40)')
        characters_delete(DataFrame_TypTow, 'loc_name(a:40)')
        characters_delete(DataFrame_TypLne, 'loc_name(a:40)')
        characters_delete(DataFrame_TypGeo, 'loc_name(a:40)')
        characters_delete(DataFrame_TypCon, 'loc_name(a:40)')


        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bus1_bus2_conn'
        df_bus1 = DataFrame_ElmLne[['ID(a:40)', 'bus1(p)']]
        df_bus2 = DataFrame_ElmLne[['ID(a:40)', 'bus2(p)']]
        'Bus 1'
        df_bus1_conn = pd.merge(df_bus1, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bus1_conn = df_bus1_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x':'ID(a:40)'})
        'Bus 2'
        df_bus2_conn = pd.merge(df_bus2, df_StaCubic_ElmTerm, how='inner', left_on='bus2(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bus2_conn = df_bus2_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x':'ID(a:40)'})
        'Merge Bus 1 and Bus 2'
        df_bus1_bus2_conn = pd.merge(df_bus1_conn, df_bus2_conn, on='ID(a:40)').rename(columns={'Bus_name_DSS_x': 'bus1_dss', 'Bus_name_DSS_y': 'bus2_dss'})
        'phases'
        df_bus = DataFrame_ElmLne[['ID(a:40)', 'bus1(p)']]
        df_cubic = DataFrame_StaCubic[['ID(a:40)', 'nphase(i)']]
        df_bus_phase = pd.merge(df_bus, df_cubic, how='inner', left_on='bus1(p)', right_on='ID(a:40)', suffixes=('_x', '_y')).rename(columns={'ID(a:40)_x': 'ID(a:40)'})

        df_busconn_phase = pd.merge(df_bus1_bus2_conn, df_bus_phase, on='ID(a:40)')
        df_busconn_phase = df_busconn_phase[['ID(a:40)', 'nphase(i)', 'bus1_dss', 'bus2_dss']]

        df_ElmLne_busconn_phase = pd.merge(DataFrame_ElmLne, df_busconn_phase, on='ID(a:40)')

        'Part 2: Identify the type of line modeling'
        'TypTow or TypLne'
        for index,  row in df_ElmLne_busconn_phase.iterrows():
            id_line = df_ElmLne_busconn_phase['loc_name(a:40)'][index]
            phases = df_ElmLne_busconn_phase['nphase(i)'][index]
            bus1 = df_ElmLne_busconn_phase['bus1_dss'][index]
            bus2 = df_ElmLne_busconn_phase['bus2_dss'][index]
            normamps = df_ElmLne_busconn_phase['Inom(r)'][index] * 1000
            geometry, LineCode, R1, X1, R0, X0, C1, C0, B1, B0, G1, G0, spacing, wires = Identify_line_modeling(index, df_ElmLne_busconn_phase, DataFrame_TypTow, DataFrame_TypLne, DataFrame_TypGeo, DataFrame_TypCon)
            if geometry == '' and LineCode == '' and spacing == '' and wires == '':
                length = 1
            else:
                length = df_ElmLne_busconn_phase['dline(r)'][index]

            #Append to df_Line_DSS
            df_Line_DSS = df_Line_DSS.append({'Id_Line':id_line, 'phases':phases, 'bus1':bus1, 'bus2':bus2, 'linecode':LineCode,
                                               'geometry':geometry, 'length':length, 'units':'km','r1':R1, 'x1':X1, 'r0':R0, 'x0':X0,
                                               'C1':C1, 'C0':C0, 'B1':B1, 'B0':B0, 'rmatrix':'', 'xmatrix':'',
                                               'cmatrix':'', 'Switch':'', 'Rg':'', 'Xg':'', 'rho':'', 'spacing':spacing,
                                               'wires':wires, 'EathModel':'', 'cncables':'', 'tscables':'', 'Seasons':'',
                                               'Ratings':'', 'LineType':'', 'normamps':normamps, 'emergamps':'', 'faultrate':'',
                                               'pctperm':'', 'repair':'', 'basefreq':'', 'enabled':'', 'like':''}, ignore_index=True)

    return df_Line_DSS

def Identify_line_modeling(index: int, DataFrame_ElmLne: pd.DataFrame, DataFrame_TypTow: pd.DataFrame,
                           DataFrame_TypLne: pd.DataFrame, DataFrame_TypGeo: pd.DataFrame, DataFrame_TypCon: pd.DataFrame):
    '''
    :param index:
    :param DataFrame_ElmLne:
    :param DataFrame_TypTow:
    :param DataFrame_TypLne:
    :return:
    '''

    'TypLne'
    id_TypLne_max = DataFrame_TypLne['ID(a:40)'].max()
    id_TypLne_min = DataFrame_TypLne['ID(a:40)'].min()
    'TypTow'
    id_TypTow_max = DataFrame_TypTow['ID(a:40)'].max()
    id_TypTow_min = DataFrame_TypTow['ID(a:40)'].min()

    'TypGeo'
    id_TypGeo_max = DataFrame_TypGeo['ID(a:40)'].max()
    id_TypGeo_min = DataFrame_TypGeo['ID(a:40)'].min()

    'TypCon'
    id_TypCon_max = DataFrame_TypCon['ID(a:40)'].max()
    id_TypCon_min = DataFrame_TypCon['ID(a:40)'].min()


    aux_Cir_TyCon = DataFrame_ElmLne['pCondCir(p)'][index]
    aux_Gnd_TyCon = DataFrame_ElmLne['pCondGnd(p)'][index]

    aux_type = DataFrame_ElmLne['typ_id(p)'][index]

    if pd.isnull(aux_type) == True:
        R1, X1, R0, X0, C1, C0, B1, B0, G1, G0 = DataFrame_ElmLne['R1(r)'][index], DataFrame_ElmLne['X1(r)'][index], \
                                                 DataFrame_ElmLne['R0(r)'][index], DataFrame_ElmLne['X0(r)'][index], \
                                                 DataFrame_ElmLne['C1(r)'][index], DataFrame_ElmLne['C0(r)'][index], \
                                                 DataFrame_ElmLne['B1(r)'][index], DataFrame_ElmLne['B0(r)'][index], \
                                                 DataFrame_ElmLne['G1(r)'][index], DataFrame_ElmLne['G0(r)'][index]
        geometry = ''
        LineCode = ''
        spacing = ''
        wires = ''
    else:
        if pd.isnull(id_TypTow_min) == False and pd.isnull(id_TypTow_max) == False:
            if aux_type >= id_TypTow_min and aux_type <= id_TypTow_max:
                R1, X1, R0, X0, C1, C0, B1, B0, G1, G0 = '', '', '', '', '', '', '', '', '', ''
                geometry = DataFrame_TypTow[DataFrame_TypTow['ID(a:40)'] == aux_type]['loc_name(a:40)'].tolist()[0]
                LineCode = ''
                spacing = ''
                wires = ''
        if pd.isnull(id_TypLne_min) == False and pd.isnull(id_TypLne_max) == False:
            if aux_type >= id_TypLne_min and aux_type <= id_TypLne_max:
                R1, X1, R0, X0, C1, C0, B1, B0, G1, G0 = '', '', '', '', '', '', '', '', '', ''
                geometry = ''
                LineCode = DataFrame_TypLne[DataFrame_TypLne['ID(a:40)'] == aux_type]['loc_name(a:40)'].tolist()[0]
                spacing = ''
                wires = ''
        if pd.isnull(id_TypGeo_min) == False and pd.isnull(id_TypGeo_max) == False:
            if aux_type >= id_TypGeo_min and aux_type <= id_TypGeo_max:
                R1, X1, R0, X0, C1, C0, B1, B0, G1, G0 = '', '', '', '', '', '', '', '', '', ''
                geometry = ''
                LineCode = ''
                TypGeo_filter = DataFrame_TypGeo[DataFrame_TypGeo['ID(a:40)'] == aux_type].reset_index()
                spacing = TypGeo_filter.iloc[0]['loc_name(a:40)']
                ncond = TypGeo_filter.iloc[0]['xy_c:0:0(r)']
                wires = wires_DSS(DataFrame_TypCon, aux_Cir_TyCon, aux_Gnd_TyCon, ncond)

        if pd.isnull(id_TypCon_min) == False and pd.isnull(id_TypCon_max) == False:
            if aux_type >= id_TypCon_min and aux_type <= id_TypCon_max:
                R1, X1, R0, X0, C1, C0, B1, B0, G1, G0 = '', '', '', '', '', '', '', '', '', ''
                geometry = ''
                LineCode = DataFrame_TypCon[DataFrame_TypCon['ID(a:40)'] == aux_type]['loc_name(a:40)'].tolist()[0]
                spacing = ''
                wires = ''
        else:
            R1, X1, R0, X0, C1, C0, B1, B0, G1, G0 = '', '', '', '', '', '', '', '', '', ''
            geometry = ''
            LineCode = ''
            spacing = ''
            wires = ''

    return geometry, LineCode, R1, X1, R0, X0, C1, C0, B1, B0, G1, G0, spacing, wires

def wires_DSS(DataFrame_TypCon:pd.DataFrame, aux_Cir_TyCon:str, aux_Gnd_TyCon:str, ncond:int):

    if pd.isnull(aux_Cir_TyCon) == False and pd.isnull(aux_Gnd_TyCon) == True:
        aux_phase = DataFrame_TypCon[DataFrame_TypCon['ID(a:40)'] == aux_Cir_TyCon].reset_index()
        phase = aux_phase.iloc[0]['loc_name(a:40)']
        if int(ncond) == 3:
            wires = f'({phase}, {phase}, {phase})'
        if int(ncond) == 2:
            wires = f'({phase}, {phase})'
        if int(ncond) == 1:
            wires = f'({phase})'

    elif pd.isnull(aux_Cir_TyCon) == False and pd.isnull(aux_Gnd_TyCon) == False:
        aux_phase = DataFrame_TypCon[DataFrame_TypCon['ID(a:40)'] == aux_Cir_TyCon].reset_index()
        phase = aux_phase.iloc[0]['loc_name(a:40)']
        aux_neutral = DataFrame_TypCon[DataFrame_TypCon['ID(a:40)'] == aux_Gnd_TyCon].reset_index()
        neutral = aux_neutral.iloc[0]['loc_name(a:40)']
        if int(ncond) == 4:
            wires = f'({phase}, {phase}, {phase}, {neutral})'
        if int(ncond) == 3:
            wires = f'({phase}, {phase}, {neutral})'
        if int(ncond) == 2:
            wires = f'({phase}, {neutral})'
        if int(ncond) == 1:
            wires = f'({neutral})'

    return wires