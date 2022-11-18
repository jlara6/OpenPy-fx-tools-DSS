# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
from py_fx_tools_dss.helper_functions import *

def DIGS_trafo_Tr2_DSS(DataFrame_ElmTr2: pd.DataFrame, DataFrame_TypTr2: pd.DataFrame,
                       DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:


    df_trafo_Tr2_DSS = pd.DataFrame(columns= ['Id_Transformer', 'Phases', 'Windings', 'Wdg', 'Bus', 'Conn', 'Kv', 'Kva', 'Tap',
                                              '%R', 'rneut', 'xneut', 'Buses', 'Conns', 'KVs', 'KVAs', 'Taps', '%Rs', 'XHL (or X12)',
                                              'XLT (or X23)', 'XHT (or X13)', 'XscArray', 'Thermal', 'n', 'm', 'flrise', 'hsrise',
                                              '%Loadloss', '%Noloadloss', '%imag', 'Ppm_Antifloat', 'NormHKVA', 'EmergHKVA',
                                              'Sub', 'MaxTap', 'MinTap', 'NumTaps', 'SubName', 'Bank', 'XfmrCode', 'XRConst',
                                              'LeadLag', 'Seasons', 'Ratings', 'Inherited Properties', 'Faultrate', 'Basefreq',
                                              'Like'])

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTr2, 'loc_name(a:40)')
    characters_delete(DataFrame_TypTr2, 'loc_name(a:40)')

    df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic, DataFrame_ElmTerm=DataFrame_ElmTerm)
    'Part 1: Identify bus and node connection in DigSilent to OpenDSS '
    'Result -> df_bushv_buslv_conn'
    df_bushv = DataFrame_ElmTr2[['ID(a:40)', 'bushv(p)']]
    df_buslv = DataFrame_ElmTr2[['ID(a:40)', 'buslv(p)']]
    'Bus High Voltage'
    df_bushv_conn = pd.merge(df_bushv, df_StaCubic_ElmTerm, how='left', left_on='bushv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
    df_bushv_conn = df_bushv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
    'Bus Low Voltage'
    df_buslv_conn = pd.merge(df_buslv, df_StaCubic_ElmTerm, how='left', left_on='buslv(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
    df_buslv_conn = df_buslv_conn[['ID(a:40)_x', 'Bus_name_DSS']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})
    'Merge Bus_HV and Bus_LV'
    df_bushv_buslv_conn = pd.merge(df_bushv_conn, df_buslv_conn, on='ID(a:40)').rename(columns={'Bus_name_DSS_x': 'bushv_dss', 'Bus_name_DSS_y': 'buslv_dss'})

    'Part 2: Identify the type of transformer (TypTr2)'
    df_TypTr2_name = DataFrame_TypTr2[['ID(a:40)', 'loc_name(a:40)']]
    merge_Elm_Typ_Tr2 = pd.merge(DataFrame_ElmTr2, df_TypTr2_name, how='left', left_on='typ_id(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
    merge_Elm_Typ_Tr2_buses_HV_LV = pd.merge(merge_Elm_Typ_Tr2, df_bushv_buslv_conn, how='left', left_on='ID(a:40)_x', right_on='ID(a:40)', suffixes=('_x', '_y') )
    merge_Elm_Typ_Tr2_buses_HV_LV = merge_Elm_Typ_Tr2_buses_HV_LV[['loc_name(a:40)_x', 'loc_name(a:40)_y', 'bushv_dss', 'buslv_dss', 'nntap(i)']]

    for index, row in merge_Elm_Typ_Tr2_buses_HV_LV.iterrows():
        id_trafo = merge_Elm_Typ_Tr2_buses_HV_LV['loc_name(a:40)_x'][index]
        xfmrcode = merge_Elm_Typ_Tr2_buses_HV_LV['loc_name(a:40)_y'][index]
        bushv = merge_Elm_Typ_Tr2_buses_HV_LV['bushv_dss'][index]
        buslv = merge_Elm_Typ_Tr2_buses_HV_LV['buslv_dss'][index]
        buses = f'[{bushv}, {buslv}]'
        tap = merge_Elm_Typ_Tr2_buses_HV_LV['nntap(i)'][index]

        df_trafo_Tr2_DSS = df_trafo_Tr2_DSS.append({'Id_Transformer':id_trafo, 'Phases':'', 'Windings':'', 'Wdg':'', 'Bus':'', 'Conn':'', 'Kv':'', 'Kva':'', 'Tap':tap,
                                                    '%R':'', 'rneut':'', 'xneut':'', 'Buses':buses, 'Conns':'', 'KVs':'', 'KVAs':'', 'Taps':'', '%Rs':'', 'XHL (or X12)':'',
                                                    'XLT (or X23)':'', 'XHT (or X13)':'', 'XscArray':'', 'Thermal':'', 'n':'', 'm':'', 'flrise':'', 'hsrise':'',
                                                    '%Loadloss':'', '%Noloadloss':'', '%imag':'', 'Ppm_Antifloat':'', 'NormHKVA':'', 'EmergHKVA':'',
                                                    'Sub':'', 'MaxTap':'', 'MinTap':'', 'NumTaps':'', 'SubName':'', 'Bank':'', 'XfmrCode':xfmrcode, 'XRConst':'',
                                                    'LeadLag':'', 'Seasons':'', 'Ratings':'', 'Inherited Properties':'', 'Faultrate':'', 'Basefreq':'',
                                                    'Like':''}, ignore_index=True)

    return df_trafo_Tr2_DSS

def DIGS_trafo_Tr3_DSS(DataFrame_ElmTr3: pd.DataFrame, DataFrame_TypTr3: pd.DataFrame,
                          DataFrame_ElmTerm: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:
    '''
    New Transformer.Service50kVA Xfmrcode=1-ph50kVA-2 Buses=[Source_Bus.1.0  UPFC_Input.1]
    '''
    df_trafo_DSS = pd.DataFrame(
        columns=['Id_Transformer', 'Phases', 'Windings', 'Wdg', 'Bus', 'Conn', 'Kv', 'Kva', 'Tap',
                 '%R', 'rneut', 'xneut', 'Buses', 'Conns', 'KVs', 'KVAs', 'Taps', '%Rs', 'XHL (or X12)',
                 'XLT (or X23)', 'XHT (or X13)', 'XscArray', 'Thermal', 'n', 'm', 'flrise', 'hsrise',
                 '%Loadloss', '%Noloadloss', '%imag', 'Ppm_Antifloat', 'NormHKVA', 'EmergHKVA',
                 'Sub', 'MaxTap', 'MinTap', 'NumTaps', 'SubName', 'Bank', 'XfmrCode', 'XRConst',
                 'LeadLag', 'Seasons', 'Ratings', 'Inherited Properties', 'Faultrate', 'Basefreq',
                 'Like'])

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmTr3, 'loc_name(a:40)')
    characters_delete(DataFrame_TypTr3, 'loc_name(a:40)')

    df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                 DataFrame_ElmTerm=DataFrame_ElmTerm)
    df_ph_vnom = df_StaCubic_ElmTerm[['ID(a:40)', 'nphase(i)', 'uknom(r)', 'loc_name(a:40)', 'Bus_name_DSS']]
    merge_ElmLod_StaCubic = pd.merge(df_ph_vnom, DataFrame_ElmLod, how='right', left_on='ID(a:40)',
                                     right_on='bushv(p)',
                                     suffixes=('_x', '_y'))


def xfmcode_Tr2_DSS(DataFrame_TypTr2:pd.DataFrame)->pd.DataFrame:

        '''
        new Xfmrcode.ct10 windings=3 phases=1 xhl=2.040000 xht=2.040000 xlt=1.360000 %imag=0.500 %noloadloss=0.000
        ~ wdg=1 conn=w kv=7.200 kva=10.0 %r=0.600000
        ~ wdg=2 conn=w kv=0.120 kva=10.0 %r=1.200000
        ~ wdg=3 conn=w kv=0.120 kva=10.0 %r=1.200000

        :return:
        '''
        df_xfmcode_Tr2_DSS= pd.DataFrame(columns= ['Id_XfmrCode', 'phases', 'windings', 'wdg', 'conn', 'kV', 'kVA', 'tap', '%R',
                                                   'Rneut', 'Xneut', 'conns', 'kVs', 'kVAs', 'taps', 'Xhl', 'Xht', 'Xlt', 'Xscarray',
                                                   'thermal', 'n', 'm', 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normhkVA',
                                                   'emerghkVA', 'MaxTap', 'MinTap', 'NumTaps', '%imag', 'ppm_antifloat', '%Rs',
                                                   'X12', 'X13', 'X23', 'RdcOhms', 'Seasons', 'Ratings', 'like'])


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
            conns= f'[{conn_hv}, {conn_lv}]'

            MaxTap = DataFrame_TypTr2['ntpmx(i)'][index]
            MinTap = DataFrame_TypTr2['ntpmn(i)'][index]

            Percent_resistance = DataFrame_TypTr2['uktr(r)'][index]
            per_Rs = f'[{Percent_resistance}, {Percent_resistance}]'

            Xhl = DataFrame_TypTr2['x0pu_hls(r)'][index] * 100

            df_xfmcode_Tr2_DSS = df_xfmcode_Tr2_DSS.append({'Id_XfmrCode':id_xfmrCode, 'phases':num_phases, 'windings':'2', 'wdg':'', 'conn':'', 'kV':'', 'kVA':'', 'tap':'', '%R':'',
                                                            'Rneut':'', 'Xneut':'', 'conns':conns, 'kVs':Kvs, 'kVAs':KVAs, 'taps':'', 'Xhl':Xhl, 'Xht':'', 'Xlt':'', 'Xscarray':'',
                                                            'thermal':'', 'n':'', 'm':'', 'flrise':'', 'hsrise':'', '%loadloss':'', '%noloadloss':'', 'normhkVA':'',
                                                            'emerghkVA':'', 'MaxTap':MaxTap, 'MinTap':MinTap, 'NumTaps':'', '%imag':'', 'ppm_antifloat':'', '%Rs':per_Rs,
                                                            'X12':'', 'X13':'', 'X23':'', 'RdcOhms':'', 'Seasons':'', 'Ratings':'', 'like':''}, ignore_index=True)


        return df_xfmcode_Tr2_DSS

def xfmcode_Tr3_DSS(DataFrame_TypTr3: pd.DataFrame) -> pd.DataFrame:
    '''
    new Xfmrcode.ct10 windings=3 phases=1 xhl=2.040000 xht=2.040000 xlt=1.360000 %imag=0.500 %noloadloss=0.000
    ~ wdg=1 conn=w kv=7.200 kva=10.0 %r=0.600000
    ~ wdg=2 conn=w kv=0.120 kva=10.0 %r=1.200000
    ~ wdg=3 conn=w kv=0.120 kva=10.0 %r=1.200000

    :return:
    '''
    df_xfmcode_DSS = pd.DataFrame(columns=['Id_XfmrCode', 'phases', 'windings', 'wdg', 'conn', 'kV', 'kVA', 'tap', '%R',
                                           'Rneut', 'Xneut', 'conns', 'kVs', 'kVAs', 'taps', 'Xhl', 'Xht', 'Xlt', 'Xscarray',
                                           'thermal', 'n', 'm', 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normhkVA',
                                           'emerghkVA', 'MaxTap', 'MinTap', 'NumTaps', '%imag', 'ppm_antifloat', '%Rs',
                                           'X12', 'X13', 'X23', 'RdcOhms', 'Seasons', 'Ratings', 'like'])

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_TypTr3, 'loc_name(a:40)')

    '''
        New  XfmrCode.1-ph50kVA  phases=1  Windings=3 ppm=0	
        ~ Xhl=2.04   Xht=2.04   Xlt=1.36  %noloadloss=.02
        ~ kVs=[7.2  0.12  0.12] ! ratings of windings
        ~ kVAs=[50 50 50]
        ~ %Rs = [0.6  1.2  1.2]
        ~ conns=[wye wye wye] ! default

        // 2 winding model
        New  XfmrCode.1-ph50kVA-2  phases=1  Windings=2 ppm=0
        ~ Xhl=2.04   %noloadloss=.02
        ~ kVs=[7.2  0.24]     ! ratings of windings
        ~ kVAs=[50 50 ]
        ~ %Rs = [0.9 0.9]
        ~ conns=[wye  wye]    ! default


        //  low-impedance transformer for interconnecting the UPFC to the system
        New  XfmrCode.UPFCInterface  phases=1  Windings=3 ppm=0	
        ~ Xhl=.0204   Xht=.0204   Xlt=.0136  %noloadloss=.01
        ~ kVs=[0.24 0.12  0.12]     ! ratings of windings
        ~ kVAs=[50 50 50]
        ~ %Rs = [0.006  .012  .012]
        ~ conns=[wye wye wye]    ! default
        '''

def identify_transformer_connection(conn_trafo:str)->str:
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

def identify_number_phases(tecnology:str):

    if tecnology == 1:
        num_phases = 1
    elif tecnology == 2:
        num_phases = 2
    elif tecnology == 3:
        num_phases = 3

    return  num_phases
