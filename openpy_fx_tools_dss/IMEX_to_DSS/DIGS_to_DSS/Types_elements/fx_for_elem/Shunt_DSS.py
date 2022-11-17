# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fx_tools_dss.helper_functions import *

def DIGS_Shunt_DSS(DataFrame_ElmShnt: pd.DataFrame, DataFrame_StaCubic: pd.DataFrame, DataFrame_ElmTerm:pd.DataFrame) -> pd.DataFrame:
    '''
    :param DataFrame_ElmShnt:
    :param DataFrame_StaCubic:
    :param DataFrame_ElmTerm:
    :return: df_Shunt_DSS
    '''

    df_Shunt_DSS = pd.DataFrame(columns=['Id_Capacitor', 'bus1', 'bus2', 'phases', 'kvar', 'kv', 'conn', 'cmatrix',
                                         'cuf', 'R', 'XL', 'Harm', 'Numsteps', 'states', 'normamps', 'emergamps',
                                         'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like'])

    if DataFrame_ElmShnt.empty == True:
        pass
    else:
        DataFrame_ElmShnt = DataFrame_ElmShnt[DataFrame_ElmShnt['ciEnergized(i)'] == 1]  # Filters energized elements
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_ElmShnt, 'loc_name(a:40)')

        df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                     DataFrame_ElmTerm=DataFrame_ElmTerm)

        df_StaCubic_ElmTerm = df_StaCubic_ElmTerm[
            ['ID(a:40)', 'nphase(i)', 'uknom(r)', 'loc_name(a:40)', 'phase_DSS', 'Bus_name_DSS']].rename(
                columns={'loc_name(a:40)': 'bus_DSS'})
        df_ElmShnt_Bus_conn = pd.merge(DataFrame_ElmShnt, df_StaCubic_ElmTerm, 
                                       how='inner', left_on='bus1(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))

        if df_ElmShnt_Bus_conn.empty == True:
            pass
        else:
            df_ElmShnt_Bus_conn.loc[:, 'nph_Shnt'] = ''
            df_ElmShnt_Bus_conn.loc[:, 'bus_Shnt'] = ''
            df_ElmShnt_Bus_conn.loc[:, 'conn_Shnt'] = ''
            '''
            New "Capacitor.cap1" bus1=675 phases=3 kvar=[ 600] kv=4.16
            New "Capacitor.cap2" bus1=611.3 phases=1 kvar=[ 100] kv=2.4
            '''
            df_ElmShnt_Bus_conn = bus_conn_Shnt(DataFrame_elem=df_ElmShnt_Bus_conn)
            for index, row in df_ElmShnt_Bus_conn.iterrows():
                Id_Capacitor = df_ElmShnt_Bus_conn['loc_name(a:40)'][index]
                bus1 = df_ElmShnt_Bus_conn['bus_Shnt'][index]
                phases = df_ElmShnt_Bus_conn['nph_Shnt'][index]
                conn = df_ElmShnt_Bus_conn['conn_Shnt'][index]
                kvar = df_ElmShnt_Bus_conn['qcapn(r)'][index] * 1000
                kv = df_ElmShnt_Bus_conn['ushnm(r)'][index]
                if phases == 3:
                    kv = round(df_ElmShnt_Bus_conn['ushnm(r)'][index], 3)
                elif phases == 2:
                    kv = round(df_ElmShnt_Bus_conn['ushnm(r)'][index], 3)
                elif phases == 1:
                    if conn == 'LL':
                        kv = round(df_ElmShnt_Bus_conn['ushnm(r)'][index], 3)
                    elif conn == 'LN':
                        kv = round(df_ElmShnt_Bus_conn['ushnm(r)'][index] / pow(3, 0.5), 3)

                df_Shunt_DSS = df_Shunt_DSS.append(
                    {'Id_Capacitor':Id_Capacitor, 'bus1':bus1, 'bus2':'', 'phases':phases, 'kvar':kvar, 'kv':kv,
                     'conn':'', 'cmatrix':'','cuf':'', 'R':'', 'XL':'', 'Harm':'', 'Numsteps':'', 'states':'',
                     'normamps':'', 'emergamps':'', 'faultrate':'', 'pctperm':'', 'repair':'', 'basefreq':'', 'enabled':'',
                     'like':''}, ignore_index=True)

    return df_Shunt_DSS


def bus_conn_Shnt(DataFrame_elem: pd.DataFrame):
    for index, row in DataFrame_elem.iterrows():
        phtech = DataFrame_elem['ctech(i)'][index]

        #0:  # 3PH-'D', 1: #3PH-'Y', 2: #3PH-'YN'
        if phtech == 0 or phtech == 1 or phtech == 2:
            DataFrame_elem['nph_Shnt'][index] = 3
            if phtech == 0:
                DataFrame_elem['conn_Shnt'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == 1:
                DataFrame_elem['conn_Shnt'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == 2:
                DataFrame_elem['conn_Shnt'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.4'
        # 3: #2PH-'Y', 4: #2PH-'YN'
        elif phtech == 3 or phtech == 4:
            DataFrame_elem['nph_Shnt'][index] = 2
            if phtech == 3:
                DataFrame_elem['conn_Shnt'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]

            elif phtech == 4:
                DataFrame_elem['conn_Shnt'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.4'

        # 5: #1PH-'PH-PH', 6: #1PH-'PH-N', 7: #1PH-'PH-E'
        elif phtech == 5 or phtech == 6 or phtech == 7:
            DataFrame_elem['nph_Shnt'][index] = 1
            if phtech == 5:
                DataFrame_elem['conn_Shnt'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '')
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == 6:
                DataFrame_elem['conn_Shnt'][index] = 'LN'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index]
            elif phtech == 7:
                DataFrame_elem['conn_Shnt'][index] = 'LL'
                if len([x for x in DataFrame_elem['phase_DSS'][index] if x in '4']) > 0:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] +\
                                                        DataFrame_elem['phase_DSS'][index].replace('.4', '') + '.0'
                else:
                    DataFrame_elem['bus_Shnt'][index] = DataFrame_elem['bus_DSS'][index] + \
                                                        DataFrame_elem['phase_DSS'][index] + '.0'
    return DataFrame_elem

def conn_shunt(technology_DigS:int) -> str:
    # Wye=LN, Delta=LL
    if technology_DigS == 0: #3PH-'D'
        type_conn_Shnt = 'LL'
        nphases = 3
    elif technology_DigS == 1: #3PH-'Y'
        type_conn_Shnt = 'LL'
        nphases = 3
    elif technology_DigS == 2: #3PH-'YN'
        type_conn_Shnt = 'LN'
        nphases = 3
    elif technology_DigS == 3: #2PH-'Y'
        type_conn_Shnt = 'LL'
        nphases = 2
    elif technology_DigS == 4: #2PH-'YN'
        type_conn_Shnt = 'LN'
        nphases = 2
    elif technology_DigS == 5: #1PH-'PH-PH'
        type_conn_Shnt = 'LL'
        nphases = 1
    elif technology_DigS == 6: #1PH-'PH-N'
        type_conn_Shnt = 'LN'
        nphases = 1
    elif technology_DigS == 1: #1PH-'PH-E'
        type_conn_Shnt = 'LL'
        nphases = 1
    else:
        type_conn_Shnt = ''
        nphases = ''
    return type_conn_Shnt, nphases