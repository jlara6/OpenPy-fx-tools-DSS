# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
from helper_functions import *

def DIGS_load_DSS(DataFrame_ElmLod:pd.DataFrame, DataFrame_TypLod:pd.DataFrame, DataFrame_StaCubic:pd.DataFrame, DataFrame_ElmTerm:pd.DataFrame)->pd.DataFrame:
    df_Load_DSS = pd.DataFrame(columns=['Id_Load', 'bus1', 'phases', 'conn', 'model', 'kV', 'Kw', 'kvar', 'pf',
                                        'yearly', 'daily', 'duty', 'growth', 'Rneut', 'Xneut', 'status', 'class',
                                        'Vminpu', 'Vmaxpu', 'Vminnorm', 'Vminemerg', 'xfkVA', '%mean', '%stddev',
                                        'CVRwatts', 'CVRvars', 'kwh', 'kwhdays', 'kwh.1', 'kwhdays.1', 'Cfactor',
                                        'CVRcurve', 'NumCust', 'ZIPV', '%SeriesRL', 'RelWeigth', 'Vlowpu', 'puXharm',
                                        'Xrharm', 'spectrum', 'basefreq', 'enabled', 'like'])

    if DataFrame_ElmLod.empty == True and DataFrame_TypLod.empty == True:
        pass
    else:
        DataFrame_ElmLod = DataFrame_ElmLod[DataFrame_ElmLod['ciEnergized(i)'] == 1]  # Filters energized elements
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmLod, 'loc_name(a:40)')
        characters_delete(DataFrame_TypLod, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic, DataFrame_ElmTerm=DataFrame_ElmTerm)

        df_ph_vnom = df_StaCubic_ElmTerm[['ID(a:40)', 'nphase(i)', 'uknom(r)', 'loc_name(a:40)', 'phase_DSS', 'Bus_name_DSS']]
        merge_ElmLod_StaCubic = pd.merge(df_ph_vnom, DataFrame_ElmLod, how='inner', left_on='ID(a:40)', right_on='bus1(p)',
                                         suffixes=('_x', '_y'))

        if merge_ElmLod_StaCubic.empty == True:
            pass
        else:
            merge_ElmLod_StaCubic.loc[:, 'nph_load'] = ''
            merge_ElmLod_StaCubic.loc[:, 'bus_load'] = ''
            merge_ElmLod_StaCubic.loc[:, 'conn_load'] = ''

            merge_ElmLod_StaCubic_TyLod = merge_ElmLod_StaCubic[
                ['ID(a:40)_y', 'loc_name(a:40)_y',
                 'nphase(i)', 'uknom(r)', 'loc_name(a:40)_x', 'phase_DSS', 'Bus_name_DSS',
                 'phtech(a)', 'nph_load', 'bus_load', 'conn_load', 'i_sym(i)',
                 'plini(r)', 'qlini(r)',
                 'plinir(r)', 'qlinir(r)', 'plinis(r)', 'qlinis(r)', 'plinit(r)', 'qlinit(r)']].rename(
                columns={'ID(a:40)_y': 'ID(a:40)', 'loc_name(a:40)_y': 'Id_load', 'loc_name(a:40)_x': 'bus_DSS'})

            '''
            if DataFrame_TypLod.empty == True:

                merge_ElmLod_StaCubic_TyLod = merge_ElmLod_StaCubic
                merge_ElmLod_StaCubic_TyLod.loc[:, 'phtech(i)'] = ''
                merge_ElmLod_StaCubic_TyLod = merge_ElmLod_StaCubic_TyLod[
                    ['ID(a:40)_y', 'loc_name(a:40)_y',
                     'nphase(i)', 'uknom(r)', 'loc_name(a:40)_x', 'phase_DSS', 'Bus_name_DSS',
                     'phtech(a)', 'phtech(i)', 'nph_load', 'bus_load', 'conn_load', 'i_sym(i)',
                     'plini(r)', 'qlini(r)',
                     'plinir(r)', 'qlinir(r)', 'plinis(r)', 'qlinis(r)', 'plinit(r)', 'qlinit(r)']].rename(
                    columns={'ID(a:40)_y': 'ID(a:40)', 'loc_name(a:40)_y': 'Id_load', 'loc_name(a:40)_x': 'bus_DSS'})

            else:
                df_TypLod_conn = DataFrame_TypLod[['ID(a:40)', 'phtech(i)']]
                merge_ElmLod_StaCubic_TyLod = pd.merge(merge_ElmLod_StaCubic, df_TypLod_conn, how='inner', left_on='typ_id(p)',
                                                       right_on='ID(a:40)', suffixes=('_x', '_y'))
                merge_ElmLod_StaCubic_TyLod = merge_ElmLod_StaCubic_TyLod[
                    ['ID(a:40)_y', 'loc_name(a:40)_y',
                     'nphase(i)', 'uknom(r)', 'loc_name(a:40)_x', 'phase_DSS', 'Bus_name_DSS',
                     'phtech(a)', 'phtech(i)', 'nph_load', 'bus_load', 'conn_load', 'i_sym(i)',
                     'plini(r)', 'qlini(r)',
                     'plinir(r)', 'qlinir(r)', 'plinis(r)', 'qlinis(r)', 'plinit(r)', 'qlinit(r)']].rename(
                    columns={'ID(a:40)_y': 'ID(a:40)', 'loc_name(a:40)_y': 'Id_load', 'loc_name(a:40)_x': 'bus_DSS'})
            '''
            merge_ElmLod_StaCubic_TyLod = bus_conn_load(DataFrame_elem=merge_ElmLod_StaCubic_TyLod)

            for index, row in merge_ElmLod_StaCubic_TyLod.iterrows():
                # Balanced
                if merge_ElmLod_StaCubic_TyLod['i_sym(i)'][index] == 0:
                    df_Load_DSS, sym = balanced_load(index=index,
                                                     DataFrame_Load_DSS=df_Load_DSS,
                                                     DataFrame_Load_DigS=merge_ElmLod_StaCubic_TyLod)
                # Unbalanced
                elif merge_ElmLod_StaCubic_TyLod['i_sym(i)'][index] == 1:
                    sym = 1
                    phase_1, phase_2, phase_3 = '.1', '.2', '.3'
                    ph_load = merge_ElmLod_StaCubic_TyLod['phase_DSS'][index]
                    nphases = merge_ElmLod_StaCubic_TyLod['nph_load'][index]
                    conn = merge_ElmLod_StaCubic_TyLod['conn_load'][index]

                    if nphases == 3:
                        if (phase_1 in ph_load) == True: #phase 1
                            df_Load_DSS = unbalanced_load(index, phase_1, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                        if (phase_2 in ph_load) == True: #phase 2
                            df_Load_DSS = unbalanced_load(index, phase_2, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                        if (phase_3 in ph_load) == True: #phase 3
                            df_Load_DSS = unbalanced_load(index, phase_3, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                    elif nphases == 2:
                        if sym == 1:
                            if ((phase_1 in ph_load) == True) and ((phase_2 in ph_load) == True) and ((phase_3 in ph_load) == True):
                                df_Load_DSS, sym = balanced_load(index=index,
                                                                 DataFrame_Load_DSS=df_Load_DSS,
                                                                 DataFrame_Load_DigS=merge_ElmLod_StaCubic_TyLod)
                        if sym == 1:
                            if (phase_1 in ph_load) == True:  # phase 1
                                df_Load_DSS = unbalanced_load(index, phase_1, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                            if (phase_2 in ph_load) == True:  # phase 2
                                df_Load_DSS = unbalanced_load(index, phase_2, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                            if (phase_3 in ph_load) == True:  # phase 3
                                df_Load_DSS = unbalanced_load(index, phase_3, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                    elif nphases == 1:
                        if sym == 1:
                            if ((phase_1 in ph_load) == True) and ((phase_2 in ph_load) == True):
                                df_Load_DSS, sym = balanced_load(index=index,
                                                                 DataFrame_Load_DSS=df_Load_DSS,
                                                                 DataFrame_Load_DigS=merge_ElmLod_StaCubic_TyLod)
                            if ((phase_1 in ph_load) == True) and ((phase_3 in ph_load) == True):
                                df_Load_DSS, sym = balanced_load(index=index,
                                                                 DataFrame_Load_DSS=df_Load_DSS,
                                                                 DataFrame_Load_DigS=merge_ElmLod_StaCubic_TyLod)
                            if ((phase_2 in ph_load) == True) and ((phase_3 in ph_load) == True):
                                df_Load_DSS, sym = balanced_load(index=index,
                                                                 DataFrame_Load_DSS=df_Load_DSS,
                                                                 DataFrame_Load_DigS=merge_ElmLod_StaCubic_TyLod)
                        if sym == 1:
                            if (phase_1 in ph_load) == True:  # phase 1
                                df_Load_DSS = unbalanced_load(index, phase_1, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                            if (phase_2 in ph_load) == True:  # phase 2
                                df_Load_DSS = unbalanced_load(index, phase_2, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

                            if (phase_3 in ph_load) == True:  # phase 3
                                df_Load_DSS = unbalanced_load(index, phase_3, df_Load_DSS, merge_ElmLod_StaCubic_TyLod)

            df_Load_DSS.loc[:, 'model'] = '1'
            df_Load_DSS.loc[:, 'Vminpu'] = '0.90'
            df_Load_DSS.loc[:, 'Vmaxpu'] = '1.10'

    return df_Load_DSS


def balanced_load(index: int, DataFrame_Load_DSS: pd.DataFrame, DataFrame_Load_DigS: pd.DataFrame) -> pd.DataFrame:
    balance = 0
    id_load = DataFrame_Load_DigS['Id_load'][index]
    Vnom = round(DataFrame_Load_DigS['uknom(r)'][index], 3)
    conn = DataFrame_Load_DigS['conn_load'][index]
    nphases = DataFrame_Load_DigS['nph_load'][index]
    bus = DataFrame_Load_DigS['bus_load'][index]
    kw = round(DataFrame_Load_DigS['plini(r)'][index] * 1000, 3)
    kvar = round(DataFrame_Load_DigS['qlini(r)'][index] * 1000, 3)
    DataFrame_Load_DSS = DataFrame_Load_DSS.append(
        {'Id_Load': id_load, 'phases': nphases, 'bus1': bus, 'conn': conn, 'kV': Vnom, 'Kw': kw, 'kvar': kvar,
         'pf': '', 'model': '', 'yearly': '', 'daily': '', 'duty': '', 'growth': '', 'Rneut': '', 'Xneut': '',
         'status': '', 'class': '', 'Vminpu': '', 'Vmaxpu': '', 'Vminnorm': '', 'Vminemerg': '', 'xfkVA': '',
         '%mean': '', '%stddev': '', 'CVRwatts': '', 'CVRvars': '', 'kwh': '', 'kwhdays': '', 'kwh.1': '',
         'kwhdays.1': '', 'Cfactor': '', 'CVRcurve': '', 'NumCust': '', 'ZIPV': '', '%SeriesRL': '', 'RelWeigth': '',
         'Vlowpu': '', 'puXharm': '', 'Xrharm': '', 'spectrum': '', 'basefreq': '', 'enabled': '', 'like': ''
         }, ignore_index=True)

    return DataFrame_Load_DSS, balance

def unbalanced_load(index: int, phase: str, DataFrame_Load_DSS: pd.DataFrame,
                    DataFrame_Load_DigS: pd.DataFrame) -> pd.DataFrame:
    nphases = 1
    id_load = DataFrame_Load_DigS['Id_load'][index] + f'_ph{phase}'
    conn = DataFrame_Load_DigS['conn_load'][index]
    if conn == 'LL':
        Vnom = round(DataFrame_Load_DigS['uknom(r)'][index] / pow(3, 0.5), 3)
    elif conn == 'LN':
        Vnom = round(DataFrame_Load_DigS['uknom(r)'][index] / pow(3, 0.5), 3)
    else:
        Vnom = ''

    phtech = DataFrame_Load_DigS['phtech(a)'][index]
    if phtech == "3PH-'D'" or phtech == "1PH PH-PH":
        aux_ph = ''
    elif phtech == "3PH PH-E" or phtech == "2PH PH-E" or phtech == "1PH PH-E":
        aux_ph = '.0'
    elif phtech == "3PH-'YN'" or phtech == "2PH-'YN'" or phtech == "1PH PH-N":
        aux_ph = ''
    elif phtech == "3F-'D'" or phtech == "1F F-F":
        aux_ph = ''
    elif phtech == "3F F-T" or phtech == "2F F-T" or phtech == "1F F-T":
        aux_ph = '.0'
    elif phtech == "3F-'YN'" or phtech == "2F-'YN'" or phtech == "1F F-N":
        aux_ph = ''

    bus = DataFrame_Load_DigS['bus_DSS'][index] + phase + aux_ph

    if phase == '.1':
        kw = round(DataFrame_Load_DigS['plinir(r)'][index] * 1000, 3)
        kvar = round(DataFrame_Load_DigS['qlinir(r)'][index] * 1000, 3)
    elif phase == '.2':
        kw = round(DataFrame_Load_DigS['plinis(r)'][index] * 1000, 3)
        kvar = round(DataFrame_Load_DigS['qlinis(r)'][index] * 1000, 3)
    elif phase == '.3':
        kw = round(DataFrame_Load_DigS['plinit(r)'][index] * 1000, 3)
        kvar = round(DataFrame_Load_DigS['qlinit(r)'][index] * 1000, 3)

    DataFrame_Load_DSS = DataFrame_Load_DSS.append(
        {'Id_Load': id_load, 'phases': nphases, 'bus1': bus, 'conn': conn, 'kV': Vnom, 'Kw': kw,
         'kvar': kvar, 'pf': '', 'model': '', 'yearly': '', 'daily': '', 'duty': '', 'growth': '',
         'Rneut': '', 'Xneut': '', 'status': '', 'class': '', 'Vminpu': '', 'Vmaxpu': '', 'Vminnorm': '',
         'Vminemerg': '', 'xfkVA': '', '%mean': '', '%stddev': '', 'CVRwatts': '', 'CVRvars': '',
         'kwh': '', 'kwhdays': '', 'kwh.1': '', 'kwhdays.1': '', 'Cfactor': '', 'CVRcurve': '',
         'NumCust': '', 'ZIPV': '', '%SeriesRL': '', 'RelWeigth': '', 'Vlowpu': '', 'puXharm': '',
         'Xrharm': '', 'spectrum': '', 'basefreq': '', 'enabled': '', 'like': ''}, ignore_index=True)

    return DataFrame_Load_DSS

def conn_load(technology_DigS:int) -> str:
    # Wye=LN, Delta=LL
    if technology_DigS == 0: #3PH-'D'
        type_conn_load = 'LL'
        conn_nphases = 3
    elif technology_DigS == 2: #3PH-'PH-E'
        type_conn_load = 'LL'
        conn_nphases = 3
    elif technology_DigS == 3: #3PH-'YN'
        type_conn_load = 'LN'
        conn_nphases = 3
    elif technology_DigS == 4: #2PH-'PH-E'
        type_conn_load = 'LL'
        conn_nphases = 2
    elif technology_DigS == 5: #2PH -'YN'
        type_conn_load = 'LN'
        conn_nphases = 2
    elif technology_DigS == 7: #1PH-'PH-PH'
        type_conn_load = 'LL'
        conn_nphases = 2
    elif technology_DigS == 8: #1PH-'PH-N'
        type_conn_load = 'LN'
        conn_nphases = 1
    elif technology_DigS == 9: #1PH-'PH-E'
        type_conn_load = 'LL'
        conn_nphases = 1
    else:
        type_conn_load = ''
        conn_nphases = ''
    return type_conn_load, conn_nphases


def bus_conn_load(DataFrame_elem: pd.DataFrame):
    for index, row in DataFrame_elem.iterrows():

        phtech = DataFrame_elem['phtech(a)'][index]
        'version 5'
        if phtech == "3PH-'D'" or phtech == "3PH PH-E" or phtech == "3PH-'YN'":
            DataFrame_elem['nph_load'][index] = 3
            if phtech == "3PH-'D'":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == "3PH PH-E":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'
            elif phtech == "3PH-'YN'":
                DataFrame_elem['conn_load'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]

        if phtech == "2PH PH-E" or phtech == "2PH-'YN'":
            DataFrame_elem['nph_load'][index] = 2
            if phtech == "2PH PH-E":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'

            elif phtech == "2PH-'YN'":
                DataFrame_elem['conn_load'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]

        if phtech == "1PH PH-PH" or phtech == "1PH PH-N" or phtech == "1PH PH-E":
            DataFrame_elem['nph_load'][index] = 1
            if phtech == "1PH PH-PH":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == "1PH PH-N":
                DataFrame_elem['conn_load'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == "1PH PH-E":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'

        'version 6'
        if phtech == "3F-'D'" or phtech == "3F F-T" or phtech == "3F-'YN'":
            DataFrame_elem['nph_load'][index] = 3
            if phtech == "3F-'D'":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == "3F F-T":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'
            elif phtech == "3F-'YN'":
                DataFrame_elem['conn_load'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]

        if phtech == "2F F-T" or phtech == "2F-'YN'":
            DataFrame_elem['nph_load'][index] = 2
            if phtech == "2F F-T":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'

            elif phtech == "2F-'YN'":
                DataFrame_elem['conn_load'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]

        if phtech == "1F F-F" or phtech == "1F F-N" or phtech == "1F F-T":
            DataFrame_elem['nph_load'][index] = 1
            if phtech == "1F F-F":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == "1F F-N":
                DataFrame_elem['conn_load'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == "1F F-T":
                DataFrame_elem['conn_load'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_load'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'
    return DataFrame_elem