# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from helper_functions import *

def DIGS_switch_DSS(DataFrame_ElmCoup:pd.DataFrame, DataFrame_RelFuse:pd.DataFrame, DataFrame_ElmTerm:pd.DataFrame, DataFrame_StaCubic:pd.DataFrame )->pd.DataFrame:
    '''
    :param DataFrame_ElmCoup:
    :param DataFrame_RelFuse:
    :param DataFrame_ElmTerm:
    :param DataFrame_StaCubic:
    :return:
    '''

    'DataFrame creation with OpenDSS keywords'
    df_switch_DSS = pd.DataFrame(columns=
                                 ['Id_Switch', 'phases', 'bus1', 'bus2', 'linecode', 'geometry','length', 'units',
                                  'r1', 'x1', 'r0', 'x0', 'C1', 'C0', 'B1', 'B0', 'rmatrix', 'xmatrix', 'cmatrix',
                                  'Switch', 'Rg', 'Xg', 'rho', 'spacing', 'wires', 'EathModel', 'cncables', 'tscables',
                                  'Seasons', 'Ratings', 'LineType', 'normamps', 'emergamps', 'faultrate', 'pctperm',
                                  'repair', 'basefreq', 'enabled', 'like'])

    if DataFrame_ElmCoup.empty == False:

        DataFrame_ElmCoup = DataFrame_ElmCoup[DataFrame_ElmCoup['ciEnergized(i)'] == 1] # Filters energized elements
        DataFrame_ElmCoup.reset_index(inplace=True)
        '********************************************Sectionalizer/Switch**************************************************************'
        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)

        df_StaCubic_ElmTerm = df_StaCubic_ElmTerm[['ID(a:40)', 'Bus_name_DSS']]

        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmCoup, 'loc_name(a:40)')

        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bus1_bus2_conn'
        df_bus1 = DataFrame_ElmCoup[['ID(a:40)', 'bus1(p)']]
        df_bus2 = DataFrame_ElmCoup[['ID(a:40)', 'bus2(p)']]
        'Bus 1'
        df_bus1_conn = pd.merge(df_bus1, df_StaCubic_ElmTerm, how='left', left_on='bus1(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bus1_conn = df_bus1_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x':'ID(a:40)'})
        'Bus 2'
        df_bus2_conn = pd.merge(df_bus2, df_StaCubic_ElmTerm, how='left', left_on='bus2(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bus2_conn = df_bus2_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x':'ID(a:40)'})
        'Merge Bus 1 and Bus 2'
        df_bus1_bus2_conn = pd.merge(df_bus1_conn, df_bus2_conn, on='ID(a:40)').rename(columns={'Bus_name_DSS_x': 'bus1_dss', 'Bus_name_DSS_y': 'bus2_dss'})
        df_bus1_bus2_conn.reset_index(inplace=True)
        'Part 2: Identify the type of switch modeling'
        for index,  row in DataFrame_ElmCoup.iterrows():
            id_switch = DataFrame_ElmCoup['loc_name(a:40)'][index]
            state = DataFrame_ElmCoup['isclosed(i)'][index]
            if state == 1:
                switch = 'y'
            else:
                switch = 'n'
            phases = DataFrame_ElmCoup['nphase(i)'][index]
            bus1 = df_bus1_bus2_conn['bus1_dss'][index]
            bus2 = df_bus1_bus2_conn['bus2_dss'][index]

            #Append to df_switch_DSS
            df_switch_DSS = df_switch_DSS.append({'Id_Switch':id_switch, 'phases':phases, 'bus1':bus1, 'bus2':bus2, 'linecode':'', 'geometry':'','length': 0.001, 'units':'',
                                                  'r1':1e-4, 'x1':0, 'r0':1e-4, 'x0':0, 'C1':0, 'C0':0, 'B1':'', 'B0':'', 'rmatrix':'', 'xmatrix':'', 'cmatrix':'',
                                                  'Switch':switch, 'Rg':'', 'Xg':'', 'rho':'', 'spacing':'', 'wires':'', 'EathModel':'', 'cncables':'', 'tscables':'',
                                                  'Seasons':'', 'Ratings':'', 'LineType':'', 'normamps':'', 'emergamps':'', 'faultrate':'', 'pctperm':'',
                                                  'repair':'', 'basefreq':'', 'enabled':'', 'like':''}, ignore_index=True)

    if DataFrame_RelFuse.empty == False:

        '***********************************************************Fuse***********************************************************'

        DataFrame_RelFuse = DataFrame_RelFuse[DataFrame_RelFuse['ciEnergized(i)'] == 1]  # Filters energized elements
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_RelFuse, 'loc_name(a:40)')
        DataFrame_RelFuse = DataFrame_RelFuse[DataFrame_RelFuse['ciEnergized(i)'] == 1].reset_index(drop=True) # Filters energized elements
        DataFrame_RelFuse = DataFrame_RelFuse.dropna(subset=["bus1(p)"]).reset_index(drop=True)
        DataFrame_RelFuse = DataFrame_RelFuse.dropna(subset=["bus2(p)"]).reset_index(drop=True)

        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bus1_bus2_conn'
        df_bus1 = DataFrame_RelFuse[['ID(a:40)', 'bus1(p)']]
        df_bus2 = DataFrame_RelFuse[['ID(a:40)', 'bus2(p)']]
        'Bus 1'
        df_bus1_conn = pd.merge(df_bus1, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                suffixes=('_x', '_y'))
        df_bus1_conn = df_bus1_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus 2'
        df_bus2_conn = pd.merge(df_bus2, df_StaCubic_ElmTerm, how='inner', left_on='bus2(p)', right_on='ID(a:40)',
                                suffixes=('_x', '_y'))
        df_bus2_conn = df_bus2_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Merge Bus 1 and Bus 2'
        df_bus1_bus2_conn = pd.merge(df_bus1_conn, df_bus2_conn, on='ID(a:40)').rename(
            columns={'Bus_name_DSS_x': 'bus1_dss', 'Bus_name_DSS_y': 'bus2_dss'})

        'Part 2: Identify the type of switch modeling'
        for index, row in DataFrame_RelFuse.iterrows():
            id_switch = DataFrame_RelFuse['loc_name(a:40)'][index]
            state = DataFrame_RelFuse['ciEnergized(i)'][index]
            if state == 1:
                switch = 'y'
            else:
                switch = 'n'
            phases = DataFrame_RelFuse['nphase(i)'][index]
            bus1 = df_bus1_bus2_conn['bus1_dss'][index]
            bus2 = df_bus1_bus2_conn['bus2_dss'][index]

            # Append to df_switch_DSS
            df_switch_DSS = df_switch_DSS.append(
                {'Id_Switch': id_switch, 'phases': phases, 'bus1': bus1, 'bus2': bus2, 'linecode': '', 'geometry': '',
                 'length':  0.001, 'units': '', 'r1': 1e-4, 'x1': 0, 'r0': 1e-4, 'x0': 0, 'C1': 0, 'C0': 0, 'B1': '',
                 'B0': '', 'rmatrix': '', 'xmatrix': '', 'cmatrix': '', 'Switch': switch, 'Rg': '', 'Xg': '', 'rho': '',
                 'spacing': '', 'wires': '', 'EathModel': '', 'cncables': '', 'tscables': '', 'Seasons': '', 'Ratings': '',
                 'LineType': '', 'normamps': '', 'emergamps': '', 'faultrate': '', 'pctperm': '', 'repair': '',
                 'basefreq': '', 'enabled': '', 'like': ''}, ignore_index=True)

    return df_switch_DSS