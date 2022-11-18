# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
from openpy_fx_tools_dss.helper_functions import *

def DIGS_trafo_DSS(DataFrame_ElmTr2: pd.DataFrame, DataFrame_TypTr2: pd.DataFrame,
                   DataFrame_ElmTr3: pd.DataFrame, DataFrame_TypTr3: pd.DataFrame,
                   DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:

    df_trafo_DSS = pd.DataFrame(
        columns=['Id_Transformer', 'Phases', 'Windings', 'Wdg', 'Bus', 'Conn', 'Kv', 'Kva', 'Tap', '%R', 'rneut',
                 'xneut', 'Buses', 'Conns', 'KVs', 'KVAs', 'Taps', '%Rs', 'XHL', 'XLT', 'XHT', 'XscArray', 'Thermal',
                 'n', 'm', 'flrise', 'hsrise', '%Loadloss', '%Noloadloss', '%imag', 'Ppm_Antifloat', 'NormHKVA',
                 'EmergHKVA', 'Sub', 'MaxTap', 'MinTap', 'NumTaps', 'SubName', 'Bank', 'XfmrCode', 'XRConst',
                 'LeadLag', 'Seasons', 'Ratings', 'Inherited Properties', 'Faultrate', 'Basefreq', 'Like'])

    '********************************* 2 winding transformer **********************************************************'
    if DataFrame_ElmTr2.empty == True and DataFrame_TypTr2.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmTr2, 'loc_name(a:40)')
        characters_delete(DataFrame_TypTr2, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)
        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bushv_buslv_conn'
        df_bushv = DataFrame_ElmTr2[['ID(a:40)', 'bushv(p)']]
        df_buslv = DataFrame_ElmTr2[['ID(a:40)', 'buslv(p)']]
        'Bus High Voltage'
        df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='bushv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus Low Voltage'
        df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='buslv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Merge Bus_HV and Bus_LV'
        df_bushv_buslv_conn = pd.merge(df_bushv_conn, df_buslv_conn, on='ID(a:40)').rename(
            columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'buslv_dss'})

        'Part 2: Identify the type of transformer (TypTr2)'
        df_TypTr2_name = DataFrame_TypTr2[['ID(a:40)', 'loc_name(a:40)']]
        merge_Elm_Typ = pd.merge(DataFrame_ElmTr2, df_TypTr2_name,
                                 how='left',
                                 left_on='typ_id(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))

        merge_Elm_Typ_buses_HV_LV = pd.merge(merge_Elm_Typ, df_bushv_buslv_conn,
                                             how='inner',
                                             left_on='ID(a:40)_x', right_on='ID(a:40)',
                                             suffixes=('_x', '_y') )

        merge_Elm_Typ_buses_HV_LV = merge_Elm_Typ_buses_HV_LV[['loc_name(a:40)_x', 'loc_name(a:40)_y',
                                                               'bushv_dss', 'buslv_dss', 'nntap(i)']]

        for index, row in merge_Elm_Typ_buses_HV_LV.iterrows():
            id_trafo = merge_Elm_Typ_buses_HV_LV['loc_name(a:40)_x'][index]
            xfmrcode = merge_Elm_Typ_buses_HV_LV['loc_name(a:40)_y'][index]
            bushv = merge_Elm_Typ_buses_HV_LV['bushv_dss'][index]
            buslv = merge_Elm_Typ_buses_HV_LV['buslv_dss'][index]
            buses = f'[{bushv}, {buslv}]'
            tap = merge_Elm_Typ_buses_HV_LV['nntap(i)'][index]

            df_trafo_DSS = df_trafo_DSS.append({
                'Id_Transformer': id_trafo, 'Phases': '', 'Windings': '', 'Wdg': '', 'Bus': '', 'Conn': '', 'Kv': '',
                'Kva': '', 'Tap': tap, '%R': '', 'rneut': '', 'xneut': '', 'Buses': buses, 'Conns': '', 'KVs': '',
                'KVAs': '', 'Taps': '', '%Rs': '', 'XHL': '', 'XLT': '', 'XHT': '', 'XscArray': '', 'Thermal': '',
                'n': '', 'm': '', 'flrise': '', 'hsrise': '', '%Loadloss': '', '%Noloadloss': '', '%imag': '',
                'Ppm_Antifloat': '', 'NormHKVA': '', 'EmergHKVA': '', 'Sub': '', 'MaxTap': '', 'MinTap': '',
                'NumTaps': '', 'SubName': '', 'Bank': '', 'XfmrCode':xfmrcode, 'XRConst': '', 'LeadLag': '',
                'Seasons': '', 'Ratings': '', 'Inherited Properties': '', 'Faultrate': '', 'Basefreq': '', 'Like': ''},
                ignore_index=True)


    '********************************* 3 winding transformer **********************************************************'
    if DataFrame_ElmTr3.empty == True and DataFrame_TypTr3.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmTr3, 'loc_name(a:40)')
        characters_delete(DataFrame_TypTr3, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)
        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bushv_buslv_conn'
        df_bushv = DataFrame_ElmTr3[['ID(a:40)', 'bushv(p)']]
        df_busmv = DataFrame_ElmTr3[['ID(a:40)', 'busmv(p)']]
        df_buslv = DataFrame_ElmTr3[['ID(a:40)', 'buslv(p)']]
        'Bus High Voltage'
        df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm, how='inner', left_on='bushv(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))
        df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus Medium Voltage'
        df_busmv_conn = pd.merge(df_busmv, df_StaCubic_ElmTerm, how='inner', left_on='busmv(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))
        df_busmv_conn = df_busmv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})

        'Bus Low Voltage'
        df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm, how='inner', left_on='buslv(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))
        df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Merge Bus_HV and Bus_LV'
        df_bus_hv_mv_lv_conn = pd.merge(pd.merge(df_bushv_conn, df_busmv_conn, on='ID(a:40)'),
                                       df_buslv_conn, on='ID(a:40)').rename(
            columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'busmv_dss', 'Bus_name_DSS': 'buslv_dss'})

        'Part 2: Identify the type of transformer (TypTr3)'
        df_TypTr3_name = DataFrame_TypTr3[['ID(a:40)', 'loc_name(a:40)']]
        merge_Elm_Typ = pd.merge(DataFrame_ElmTr3, df_TypTr3_name, how='left', left_on='typ_id(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))

        merge_Elm_Typ_buses_HV_LV = pd.merge(merge_Elm_Typ, df_bus_hv_mv_lv_conn, how='inner', left_on='ID(a:40)_x',
                                             right_on='ID(a:40)', suffixes=('_x', '_y'))
        merge_Elm_Typ_buses_HV_LV = merge_Elm_Typ_buses_HV_LV[
            ['loc_name(a:40)_x', 'loc_name(a:40)_y', 'bushv_dss', 'busmv_dss' ,'buslv_dss' ]]

        for index, row in merge_Elm_Typ_buses_HV_LV.iterrows():
            id_trafo = merge_Elm_Typ_buses_HV_LV['loc_name(a:40)_x'][index]
            xfmrcode = merge_Elm_Typ_buses_HV_LV['loc_name(a:40)_y'][index]
            bushv = merge_Elm_Typ_buses_HV_LV['bushv_dss'][index]
            busmv = merge_Elm_Typ_buses_HV_LV['busmv_dss'][index]
            buslv = merge_Elm_Typ_buses_HV_LV['buslv_dss'][index]
            buses = f'[{bushv}, {busmv}, {buslv}]'

            df_trafo_DSS = df_trafo_DSS.append(
                {'Id_Transformer': id_trafo, 'Phases': '', 'Windings': '', 'Wdg': '', 'Bus': '', 'Conn': '', 'Kv': '',
                 'Kva': '', 'Tap': '', '%R': '', 'rneut': '', 'xneut': '', 'Buses': buses, 'Conns': '', 'KVs': '',
                 'KVAs': '', 'Taps': '', '%Rs': '', 'XHL': '', 'XLT': '', 'XHT': '', 'XscArray': '', 'Thermal': '',
                 'n': '', 'm': '', 'flrise': '', 'hsrise': '', '%Loadloss': '', '%Noloadloss': '', '%imag': '',
                 'Ppm_Antifloat': '', 'NormHKVA': '', 'EmergHKVA': '', 'Sub': '', 'MaxTap': '', 'MinTap': '',
                 'NumTaps': '', 'SubName': '', 'Bank': '', 'XfmrCode': xfmrcode, 'XRConst': '', 'LeadLag': '',
                 'Seasons': '', 'Ratings': '', 'Inherited Properties': '', 'Faultrate': '',
                 'Basefreq': '', 'Like': ''}, ignore_index=True)

    return df_trafo_DSS


def DIGS_trafo_conn_group_DSS(DataFrame_ElmTr2: pd.DataFrame, DataFrame_TypTr2: pd.DataFrame,
                              DataFrame_ElmTr3: pd.DataFrame, DataFrame_TypTr3: pd.DataFrame,
                              DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:


    df_trafo_DSS = pd.DataFrame(
        columns=['Id_Transformer', 'Phases', 'Windings', 'Wdg', 'Bus', 'Conn', 'Kv', 'Kva', 'Tap', '%R', 'rneut',
                 'xneut', 'Buses', 'Conns', 'KVs', 'KVAs', 'Taps', '%Rs', 'XHL', 'XLT', 'XHT', 'XscArray',
                 'Thermal', 'n', 'm', 'flrise', 'hsrise', '%Loadloss', '%Noloadloss', '%imag', 'Ppm_Antifloat',
                 'NormHKVA', 'EmergHKVA', 'Sub', 'MaxTap', 'MinTap', 'NumTaps', 'SubName', 'Bank', 'XfmrCode',
                 'XRConst', 'LeadLag', 'Seasons', 'Ratings', 'Inherited Properties', 'Faultrate', 'Basefreq',
                 'Like'])

    if DataFrame_ElmTr2.empty == True and DataFrame_TypTr2.empty == True:
        pass
    else:

        DataFrame_ElmTr2 = DataFrame_ElmTr2[DataFrame_ElmTr2['ciEnergized(i)'] == 1]  #Filters energized elements
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmTr2, 'loc_name(a:40)')
        characters_delete(DataFrame_TypTr2, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)


        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bushv_buslv_conn'
        df_bushv = DataFrame_ElmTr2[['ID(a:40)', 'bushv(p)']]
        df_buslv = DataFrame_ElmTr2[['ID(a:40)', 'buslv(p)']]
        'Bus High Voltage'
        df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='bushv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus Low Voltage'
        df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='buslv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})

        'Merge Bus_HV and Bus_LV'
        df_bushv_buslv_conn = pd.merge(df_bushv_conn, df_buslv_conn, on='ID(a:40)').rename(
            columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'buslv_dss',
                     'loc_name(a:40)_x': 'name_hv', 'loc_name(a:40)_y': 'name_lv',
                     'nphase(i)_x': 'nphase_hv', 'nphase(i)_y': 'nphase_lv',
                     'phase_DSS_x': 'DSS_hv', 'phase_DSS_y': 'DSS_lv'})

        'Part 2: Identify the type of transformer (TypTr2)'
        df_TypTr2_name = DataFrame_TypTr2[
            ['ID(a:40)', 'loc_name(a:40)', 'nt2ph(i)', 'tr2cn_h(a:2)', 'tr2cn_l(a:2)', 'nt2ag(r)', 'dutap(r)']]
        merge_Elm_Typ = pd.merge(DataFrame_ElmTr2, df_TypTr2_name,
                                 how='left',
                                 left_on='typ_id(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))


        merge_ElmTr2_TypTr2 = pd.merge(merge_Elm_Typ, df_bushv_buslv_conn,
                                       how='inner',
                                       left_on='ID(a:40)_x', right_on='ID(a:40)',
                                       suffixes=('_x', '_y'))

        merge_ElmTr2_TypTr2 = merge_ElmTr2_TypTr2[['loc_name(a:40)_x', 'loc_name(a:40)_y', 'nt2ph(i)',
                                                   'name_hv', 'tr2cn_h(a:2)', 'nphase_hv', 'bushv_dss', 'DSS_hv',
                                                   'name_lv', 'tr2cn_l(a:2)', 'nphase_lv', 'buslv_dss', 'DSS_lv',
                                                   'nt2ag(r)', 'nntap(i)', 'dutap(r)']]

        merge_ElmTr2_TypTr2 = merge_ElmTr2_TypTr2.rename(
            columns={'loc_name(a:40)_x': 'id_trafo', 'loc_name(a:40)_y': 'xfmrcode',
                     'nt2ph(i)': 'type', 'tr2cn_h(a:2)': 'hv_side', 'tr2cn_l(a:2)': 'lv_side', 'nt2ag(r)': 'ph_shift'})

        for index, row in merge_ElmTr2_TypTr2.iterrows():
            id_trafo = merge_ElmTr2_TypTr2['id_trafo'][index]
            xfmrcode = merge_ElmTr2_TypTr2['xfmrcode'][index]

            if merge_ElmTr2_TypTr2['type'][index] == 3 or merge_ElmTr2_TypTr2['type'][index] == 2:
                # HV
                if merge_ElmTr2_TypTr2['hv_side'][index] == 'YN':
                    if len([x for x in merge_ElmTr2_TypTr2['DSS_hv'][index] if x in '4']) > 0:
                        bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index].replace(
                            '.4', '')
                    else:
                        #bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index] + '.4'
                        bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index]

                elif merge_ElmTr2_TypTr2['hv_side'][index] == 'D' or merge_ElmTr2_TypTr2['hv_side'][index] == 'Y':
                    if len([x for x in merge_ElmTr2_TypTr2['DSS_hv'][index] if x in '4']) > 0:
                        bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index].replace(
                            '.4', '')
                    else:
                        bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index]

                else:
                    bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index]

                # LV
                if merge_ElmTr2_TypTr2['lv_side'][index] == 'YN':
                    if len([x for x in merge_ElmTr2_TypTr2['DSS_lv'][index] if x in '4']) > 0:
                        buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index].replace(
                            '.4', '')
                    else:
                        #buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index] + '.4'
                        buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index]

                elif merge_ElmTr2_TypTr2['lv_side'][index] == 'D' or merge_ElmTr2_TypTr2['lv_side'][index] == 'Y':
                    if len([x for x in merge_ElmTr2_TypTr2['DSS_lv'][index] if x in '4']) > 0:
                        buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index].replace(
                            '.4', '')
                    else:
                        buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index]
                else:
                    buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index]

            if merge_ElmTr2_TypTr2['type'][index] == 1:
                bushv = merge_ElmTr2_TypTr2['name_hv'][index] + merge_ElmTr2_TypTr2['DSS_hv'][index] + '.0'
                buslv = merge_ElmTr2_TypTr2['name_lv'][index] + merge_ElmTr2_TypTr2['DSS_lv'][index] + '.0'

            buses = f'[{bushv}, {buslv}]'
            tap = 1 + ((merge_ElmTr2_TypTr2['nntap(i)'][index] * merge_ElmTr2_TypTr2['dutap(r)'][index]) / 100)

            df_trafo_DSS = df_trafo_DSS.append({
                'Id_Transformer': id_trafo, 'Phases': '', 'Windings': '', 'Wdg': '', 'Bus': '', 'Conn': '', 'Kv': '',
                'Kva': '', 'Tap': tap, '%R': '', 'rneut': '', 'xneut': '', 'Buses':buses, 'Conns': '', 'KVs': '',
                'KVAs': '', 'Taps': '', '%Rs': '', 'XHL': '', 'XLT': '', 'XHT': '', 'XscArray': '', 'Thermal': '',
                'n': '', 'm': '', 'flrise': '', 'hsrise': '', '%Loadloss': '', '%Noloadloss': '', '%imag': '',
                'Ppm_Antifloat': '', 'NormHKVA': '', 'EmergHKVA': '', 'Sub': '', 'MaxTap': '', 'MinTap': '',
                'NumTaps': '', 'SubName': '', 'Bank': '', 'XfmrCode': xfmrcode, 'XRConst': '', 'LeadLag': '',
                'Seasons': '', 'Ratings': '', 'Inherited Properties': '', 'Faultrate': '', 'Basefreq': '', 'Like': ''},
                ignore_index=True)

    if DataFrame_ElmTr3.empty == True and DataFrame_TypTr3.empty == True:
        pass
    else:
        DataFrame_ElmTr3 = DataFrame_ElmTr3[DataFrame_ElmTr3['outserv(i)'] == 0]
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmTr3, 'loc_name(a:40)')
        characters_delete(DataFrame_TypTr3, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)

        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bushv_buslv_conn'
        df_bushv = DataFrame_ElmTr3[['ID(a:40)', 'bushv(p)']]
        df_busmv = DataFrame_ElmTr3[['ID(a:40)', 'busmv(p)']]
        df_buslv = DataFrame_ElmTr3[['ID(a:40)', 'buslv(p)']]

        'Bus High Voltage'
        df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='bushv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus Medium Voltage'
        df_busmv_conn = pd.merge(df_busmv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='busmv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_busmv_conn = df_busmv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus Low Voltage'
        df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='buslv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})


        'Merge Bus_HV, Bus_MV and Bus_LV'
        df_bus_hv_mv_lv_conn = pd.merge(pd.merge(df_bushv_conn, df_busmv_conn, on='ID(a:40)'),
                                       df_buslv_conn, on='ID(a:40)').rename(
            columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'busmv_dss', 'Bus_name_DSS': 'buslv_dss',
                     'loc_name(a:40)_x': 'name_hv', 'loc_name(a:40)_y': 'name_mv', 'loc_name(a:40)': 'name_lv',
                     'nphase(i)_x': 'nphase_hv', 'nphase(i)_y': 'nphase_mv', 'nphase(i)': 'nphase_lv',
                     'phase_DSS_x': 'DSS_hv', 'phase_DSS_y': 'DSS_mv', 'phase_DSS': 'DSS_lv'})

        'Part 2: Identify the type of transformer (TypTr3)'
        df_TypTr3_name = DataFrame_TypTr3[['ID(a:40)', 'loc_name(a:40)',
                                           'tr3cn_h(a:2)', 'tr3cn_m(a:2)', 'tr3cn_l(a:2)',
                                           'nt3ag_h(r)', 'nt3ag_m(r)', 'nt3ag_l(r)']].\
            rename(columns={'tr3cn_h(a:2)': 'hv_side', 'tr3cn_m(a:2)': 'mv_side', 'tr3cn_l(a:2)': 'lv_side',
                            'nt3ag_h(r)': 'hv_shift', 'nt3ag_m(r)': 'mv_shift', 'nt3ag_l(r)': 'lv_shift'})

        merge_Elm_Typ = pd.merge(DataFrame_ElmTr3, df_TypTr3_name, how='left', left_on='typ_id(p)', right_on='ID(a:40)',
                                 suffixes=('_x', '_y'))

        Elm_Typ_buses_Tr3 = pd.merge(merge_Elm_Typ, df_bus_hv_mv_lv_conn, how='inner', left_on='ID(a:40)_x',
                                             right_on='ID(a:40)', suffixes=('_x', '_y'))
        
        
        Elm_Typ_buses_Tr3 = Elm_Typ_buses_Tr3[['loc_name(a:40)_x', 'loc_name(a:40)_y',
                                               'name_hv', 'hv_side', 'hv_shift', 'nphase_hv', 'bushv_dss', 'DSS_hv', 'n3tap_h(i)',
                                               'name_mv', 'mv_side', 'mv_shift', 'nphase_mv', 'busmv_dss', 'DSS_mv', 'n3tap_m(i)',
                                               'name_lv', 'lv_side', 'lv_shift', 'nphase_lv', 'buslv_dss', 'DSS_lv', 'n3tap_l(i)']].\
            rename(columns={'loc_name(a:40)_x': 'id_trafo', 'loc_name(a:40)_y': 'xfmrcode',
                            'n3tap_h(i)': 'tap_hv', 'n3tap_m(i)': 'tap_mv', 'n3tap_l(i)': 'tap_lv'})

        for index, row in Elm_Typ_buses_Tr3.iterrows():
            id_trafo = Elm_Typ_buses_Tr3['id_trafo'][index]
            xfmrcode = Elm_Typ_buses_Tr3['xfmrcode'][index]

            # HV
            if Elm_Typ_buses_Tr3['hv_side'][index] == 'YN':
                if len([x for x in Elm_Typ_buses_Tr3['DSS_hv'][index] if x in '4']) > 0:
                    bushv = Elm_Typ_buses_Tr3['name_hv'][index] + Elm_Typ_buses_Tr3['DSS_hv'][index]
                else:
                    bushv = Elm_Typ_buses_Tr3['name_hv'][index] + Elm_Typ_buses_Tr3['DSS_hv'][index] + '.4'
            else:
                bushv = Elm_Typ_buses_Tr3['name_hv'][index] + Elm_Typ_buses_Tr3['DSS_hv'][index]

            # MV
            if Elm_Typ_buses_Tr3['mv_side'][index] == 'YN':
                if len([x for x in Elm_Typ_buses_Tr3['DSS_mv'][index] if x in '4']) > 0:
                    busmv = Elm_Typ_buses_Tr3['name_mv'][index] + Elm_Typ_buses_Tr3['DSS_mv'][index]
                else:
                    busmv = Elm_Typ_buses_Tr3['name_mv'][index] + Elm_Typ_buses_Tr3['DSS_mv'][index] + '.4'
            else:
                busmv = Elm_Typ_buses_Tr3['name_mv'][index] + Elm_Typ_buses_Tr3['DSS_mv'][index]

            # LV
            if Elm_Typ_buses_Tr3['lv_side'][index] == 'YN':
                if len([x for x in Elm_Typ_buses_Tr3['DSS_lv'][index] if x in '4']) > 0:
                    buslv = Elm_Typ_buses_Tr3['name_lv'][index] + Elm_Typ_buses_Tr3['DSS_lv'][index]
                else:
                    buslv = Elm_Typ_buses_Tr3['name_lv'][index] + Elm_Typ_buses_Tr3['DSS_lv'][index] + '.4'
            else:
                buslv = Elm_Typ_buses_Tr3['name_lv'][index] + Elm_Typ_buses_Tr3['DSS_lv'][index]

            buses = f'[{bushv}, {busmv}, {buslv}]'


            df_trafo_DSS = df_trafo_DSS.append(
                {'Id_Transformer': id_trafo, 'Phases': '', 'Windings': '', 'Wdg': '', 'Bus': '', 'Conn': '', 'Kv': '',
                 'Kva': '', 'Tap': '', '%R': '', 'rneut': '', 'xneut': '', 'Buses': buses, 'Conns': '', 'KVs': '',
                 'KVAs': '', 'Taps': '', '%Rs': '', 'XHL': '', 'XLT': '', 'XHT': '', 'XscArray': '', 'Thermal': '',
                 'n': '', 'm': '', 'flrise': '', 'hsrise': '', '%Loadloss': '', '%Noloadloss': '', '%imag': '',
                 'Ppm_Antifloat': '', 'NormHKVA': '', 'EmergHKVA': '', 'Sub': '', 'MaxTap': '', 'MinTap': '',
                 'NumTaps': '', 'SubName': '', 'Bank': '', 'XfmrCode': xfmrcode, 'XRConst': '', 'LeadLag': '',
                 'Seasons': '', 'Ratings': '', 'Inherited Properties': '', 'Faultrate': '',
                 'Basefreq': '', 'Like': ''}, ignore_index=True)

    return df_trafo_DSS


def DIGS_trafo_conn_group_DSS_2(DataFrame_ElmTr2: pd.DataFrame, DataFrame_TypTr2: pd.DataFrame,
                                DataFrame_ElmTr3: pd.DataFrame, DataFrame_TypTr3: pd.DataFrame,
                                DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:


    df_Trafo_DSS = pd.DataFrame(
        columns=['Id_Transformer', 'Phases', 'Windings', 'Wdg', 'Bus', 'Conn', 'Kv', 'Kva', 'Tap', '%R', 'rneut',
                 'xneut', 'Buses', 'Conns', 'KVs', 'KVAs', 'Taps', '%Rs', 'XHL', 'XLT', 'XHT', 'XscArray',
                 'Thermal', 'n', 'm', 'flrise', 'hsrise', '%Loadloss', '%Noloadloss', '%imag', 'Ppm_Antifloat',
                 'NormHKVA', 'EmergHKVA', 'Sub', 'MaxTap', 'MinTap', 'NumTaps', 'SubName', 'Bank', 'XfmrCode',
                 'XRConst', 'LeadLag', 'Seasons', 'Ratings', 'Inherited Properties', 'Faultrate', 'Basefreq',
                 'Like'])

    if DataFrame_ElmTr2.empty == True and DataFrame_TypTr2.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmTr2, 'loc_name(a:40)')
        characters_delete(DataFrame_TypTr2, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)

        'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
        'Result -> df_bushv_buslv_conn'
        df_bushv = DataFrame_ElmTr2[['ID(a:40)', 'bushv(p)']]
        df_buslv = DataFrame_ElmTr2[['ID(a:40)', 'buslv(p)']]
        'Bus High Voltage'
        df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='bushv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})
        'Bus Low Voltage'
        df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm,
                                 how='inner', left_on='buslv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
        df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'loc_name(a:40)', 'nphase(i)', 'Bus_name_DSS', 'phase_DSS']].\
            rename(columns={'ID(a:40)_x': 'ID(a:40)'})

        'Merge Bus_HV and Bus_LV'
        df_bushv_buslv_conn = pd.merge(df_bushv_conn, df_buslv_conn, on='ID(a:40)').rename(
            columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'buslv_dss',
                     'loc_name(a:40)_x': 'name_hv', 'loc_name(a:40)_y': 'name_lv',
                     'nphase(i)_x': 'nphase_hv', 'nphase(i)_y': 'nphase_lv',
                     'phase_DSS_x': 'DSS_hv', 'phase_DSS_y': 'DSS_lv'})

        'Part 2: Identify the type of transformer (TypTr2)'
        df_TypTr2_name = DataFrame_TypTr2[
            ['ID(a:40)', 'loc_name(a:40)', 'nt2ph(i)', 'tr2cn_h(a:2)', 'tr2cn_l(a:2)', 'nt2ag(r)']]
        merge_Elm_Typ = pd.merge(DataFrame_ElmTr2, df_TypTr2_name,
                                 how='left', left_on='typ_id(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))


        merge_ElmTr2_TypTr2 = pd.merge(merge_Elm_Typ, df_bushv_buslv_conn,
                                       how='inner', left_on='ID(a:40)_x', right_on='ID(a:40)', suffixes=('_x', '_y'))

        merge_ElmTr2_TypTr2 = merge_ElmTr2_TypTr2[['loc_name(a:40)_x', 'loc_name(a:40)_y', 'nt2ph(i)',
                                                   'name_hv', 'tr2cn_h(a:2)', 'nphase_hv', 'bushv_dss', 'DSS_hv',
                                                   'name_lv', 'tr2cn_l(a:2)', 'nphase_lv', 'buslv_dss', 'DSS_lv',
                                                   'nt2ag(r)', 'nntap(i)']]

        merge_ElmTr2_TypTr2 = merge_ElmTr2_TypTr2.rename(
            columns={'loc_name(a:40)_x': 'id_trafo', 'loc_name(a:40)_y': 'xfmrcode',
                     'nt2ph(i)': 'type', 'tr2cn_h(a:2)': 'hv_side', 'tr2cn_l(a:2)': 'lv_side', 'nt2ag(r)': 'ph_shift'})

        for index, row in merge_ElmTr2_TypTr2.iterrows():
            ph_shift = merge_ElmTr2_TypTr2['ph_shift'][index]

            if ph_shift == 1 or ph_shift == 11:

                id_trafo = merge_ElmTr2_TypTr2['loc_name(a:40)_x'][index]
                xfmrcode = merge_ElmTr2_TypTr2['loc_name(a:40)_y'][index]
                if ph_shift == 11:
                    LeadLag = 'Lag'
                elif ph_shift == 1:
                    LeadLag = 'Lead'

                bushv = merge_ElmTr2_TypTr2['bushv_dss'][index]

                buslv = merge_ElmTr2_TypTr2['buslv_dss'][index]

                buses = f'[{bushv}, {buslv}]'
                tap = merge_ElmTr2_TypTr2['nntap(i)'][index]

                df_Trafo_DSS = df_Trafo_DSS.append({
                    'Id_Transformer': id_trafo, 'Phases': '', 'Windings': '', 'Wdg': '', 'Bus': '', 'Conn': '',
                    'Kv': '', 'Kva': '', 'Tap': tap, '%R': '', 'rneut': '', 'xneut': '', 'Buses': buses, 'Conns': '',
                    'KVs': '', 'KVAs': '', 'Taps': '', '%Rs': '', 'XHL': '', 'XLT': '', 'XHT': '', 'XscArray': '',
                    'Thermal': '', 'n': '', 'm': '', 'flrise': '', 'hsrise': '', '%Loadloss': '', '%Noloadloss': '',
                    '%imag': '', 'Ppm_Antifloat': '', 'NormHKVA': '', 'EmergHKVA': '', 'Sub': '', 'MaxTap': '',
                    'MinTap': '', 'NumTaps': '', 'SubName': '', 'Bank': '', 'XfmrCode': xfmrcode, 'XRConst': '',
                    'LeadLag': LeadLag, 'Seasons': '', 'Ratings': '', 'Inherited Properties': '', 'Faultrate': '',
                    'Basefreq': '', 'Like': ''}, ignore_index=True)

        print('here')

    return df_Trafo_DSS


def xfmcode_DSS(DataFrame_TypTr2: pd.DataFrame, DataFrame_TypTr3: pd.DataFrame) -> pd.DataFrame:

    '''
    new Xfmrcode.ct10 windings=3 phases=1 xhl=2.040000 xht=2.040000 xlt=1.360000 %imag=0.500 %noloadloss=0.000
    ~ wdg=1 conn=w kv=7.200 kva=10.0 %r=0.600000
    ~ wdg=2 conn=w kv=0.120 kva=10.0 %r=1.200000
    ~ wdg=3 conn=w kv=0.120 kva=10.0 %r=1.200000

    :return:
    '''
    df_xfmcode_DSS = pd.DataFrame(columns=[
        'Id_XfmrCode', 'phases', 'windings', 'wdg', 'conn', 'kV', 'kVA', 'tap', '%R', 'XHL', 'Rneut', 'Xneut', 'conns',
        'thermal', 'n', 'm', 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normhkVA', 'emerghkVA', 'MaxTap',
        'MinTap', 'NumTaps', '%imag', 'ppm_antifloat', 'X12', 'X13', 'X23', 'RdcOhms', 'Seasons', 'Ratings', 'like'])

    '******************************************** 2 winding transformer ***********************************************'
    if DataFrame_TypTr2.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_TypTr2, 'loc_name(a:40)')

        for index, row in DataFrame_TypTr2.iterrows():
            id_xfmrCode = DataFrame_TypTr2['loc_name(a:40)'][index]

            num_phases = identify_number_phases(DataFrame_TypTr2['nt2ph(i)'][index])

            kv_hv = DataFrame_TypTr2['utrn_h(r)'][index]
            kv_lv = DataFrame_TypTr2['utrn_l(r)'][index]
            Kvs = f'[{kv_hv}, {kv_lv}]'

            kva = DataFrame_TypTr2['strn(r)'][index] * 1000
            KVAs = f'[{kva}, {kva}]'

            conn_hv = identify_transformer_connection(DataFrame_TypTr2['tr2cn_h(a:2)'][index])
            conn_lv = identify_transformer_connection(DataFrame_TypTr2['tr2cn_l(a:2)'][index])
            conns = f'[{conn_hv}, {conn_lv}]'

            step = DataFrame_TypTr2['dutap(r)'][index]
            MaxTap = 1 + ((DataFrame_TypTr2['ntpmx(i)'][index] * step) / 100)
            MinTap = 1 + ((DataFrame_TypTr2['ntpmn(i)'][index] * step) / 100)

            R_pu = DataFrame_TypTr2['pcutr(r)'][index] / (DataFrame_TypTr2['strn(r)'][index] * 1000)
            if R_pu == 0:
                R_pu = ''
                loadloss = ''
                loadloss_2 = ''
                XHL_pu = round(DataFrame_TypTr2['uktr(r)'][index] / 100, 6)
                XHL = round(XHL_pu * 100, 6)
                XHT = ''
                XLT = ''
            else:
                R_pu = round(DataFrame_TypTr2['pcutr(r)'][index] / (DataFrame_TypTr2['strn(r)'][index] * 1000), 3)
                loadloss = R_pu * 100
                loadloss_2 = round(loadloss / 2, 3)
                loadloss = ''
                uk_pu = round(DataFrame_TypTr2['uktr(r)'][index] / 100, 3)
                XHL_pu = round(pow(pow(uk_pu, 2) - pow(R_pu, 2), 0.5), 3)
                XHL = XHL_pu * 100
                XHT = XHL/2
                XLT = XHL/2
            Percent_resistance = DataFrame_TypTr2['uktr(r)'][index]
            #per_Rs = ''
            if loadloss_2 == '':
                per_Rs = ''
            else:
                per_Rs = f'[{loadloss_2 }, {loadloss_2 }]'
            #'%R': loadloss_2,

            df_xfmcode_DSS = df_xfmcode_DSS.append({
                'Id_XfmrCode': id_xfmrCode, 'phases': num_phases, 'windings': '2', 'wdg': '', 'conn': '', 'kV': '', 
                'kVA': '', 'tap': '', '%R': '', 'Rneut': '', 'Xneut': '', 'conns': conns, 'kVs': Kvs, 'kVAs': KVAs,
                'taps': '', 'XHL': XHL, 'XHT': XHT, 'XLT': XLT, 'Xscarray': '', 'thermal': '', 'n': '', 'm': '',
                'flrise': '', 'hsrise': '', '%loadloss': loadloss, '%noloadloss': '', 'normhkVA': '', 'emerghkVA': '',
                'MaxTap': MaxTap, 'MinTap': MinTap, 'NumTaps': '', '%imag': '', 'ppm_antifloat': '', '%Rs': per_Rs,
                'X12': '', 'X13': '', 'X23': '', 'RdcOhms': '', 'Seasons': '', 'Ratings': '', 'like': ''},
                ignore_index=True)


    '********************************************************** 3 winding transformer **********************************************************'
    if DataFrame_TypTr3.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_TypTr3, 'loc_name(a:40)')

        for index, row in DataFrame_TypTr3.iterrows():
            id_xfmrCode = DataFrame_TypTr3['loc_name(a:40)'][index]

            num_phases = '3'

            kv_hv = DataFrame_TypTr3['utrn3_h(r)'][index]
            kv_mv = DataFrame_TypTr3['utrn3_m(r)'][index]
            kv_lv = DataFrame_TypTr3['utrn3_l(r)'][index]
            Kvs = f'[{kv_hv}, {kv_mv}, {kv_lv}]'

            kva_hv = DataFrame_TypTr3['strn3_h(r)'][index] * 1000
            kva_mv = DataFrame_TypTr3['strn3_m(r)'][index] * 1000
            kva_lv = DataFrame_TypTr3['strn3_l(r)'][index] * 1000
            KVAs = f'[{kva_hv}, {kva_mv}, {kva_lv}]'

            XHL = DataFrame_TypTr3['uktr3_h(r)'][index] #H-L (winding 1 to winding 2)
            XHT = DataFrame_TypTr3['uktr3_l(r)'][index] #H-T (winding 1 to winding 3)
            XLT = DataFrame_TypTr3['uktr3_m(r)'][index] #L-T (winding 2 to winding 3)


            conn_hv = identify_transformer_connection(DataFrame_TypTr3['tr3cn_h(a:2)'][index])
            conn_mv = identify_transformer_connection(DataFrame_TypTr3['tr3cn_m(a:2)'][index])
            conn_lv = identify_transformer_connection(DataFrame_TypTr3['tr3cn_l(a:2)'][index])
            conns = f'[{conn_hv}, {conn_mv}, {conn_lv}]'

            df_xfmcode_DSS = df_xfmcode_DSS.append(
                {'Id_XfmrCode': id_xfmrCode, 'phases': num_phases, 'windings': '3', 'wdg': '', 'conn': '', 'kV': '',
                 'kVA': '', 'tap': '', '%R': '', 'Rneut': '', 'Xneut': '', 'conns': conns, 'kVs': Kvs, 'kVAs': KVAs,
                 'taps': '', 'Xhl': XHL, 'Xht': XHT, 'Xlt': XLT, 'Xscarray': '', 'thermal': '', 'n': '', 'm': '',
                 'flrise': '', 'hsrise': '', '%loadloss': '', '%noloadloss': '', 'normhkVA': '', 'emerghkVA': '',
                 'MaxTap':  '', 'MinTap':  '', 'NumTaps': '', '%imag': '', 'ppm_antifloat': '', '%Rs':  '', 'X12': '',
                 'X13': '', 'X23': '', 'RdcOhms': '', 'Seasons': '', 'Ratings': '', 'like': ''}, ignore_index=True)


    return df_xfmcode_DSS

def identify_transformer_connection(conn_trafo: str) -> str:
    #Connection of this winding {wye*, Delta, LN, LL}. Default is "wye" with the neutral solidly grounded.
    if conn_trafo == 'Y':
        conn_dss = 'wye'
    elif conn_trafo == 'YN':
        conn_dss = 'wye'
    elif conn_trafo == 'D':
        conn_dss = 'delta'
    elif conn_trafo == 'Z':
        conn_dss = ''
    elif conn_trafo == 'ZN':
        conn_dss = ''

    return conn_dss

def identify_number_phases(technology: str):

    if technology == 1:
        num_phases = 1
    elif technology == 2:
        num_phases = 1
    elif technology == 3:
        num_phases = 3

    return num_phases

