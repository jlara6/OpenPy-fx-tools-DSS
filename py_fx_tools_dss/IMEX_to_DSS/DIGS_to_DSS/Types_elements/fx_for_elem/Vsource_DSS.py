# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from py_fx_tools_dss.helper_functions import *

def DIGS_Vsource_DSS(DataFrame_ElmXnet: pd.DataFrame,
                     DataFrame_ElmTerm: pd.DataFrame,
                     DataFrame_StaCubic: pd.DataFrame) -> pd.DataFrame:

    df_Vsource_DSS = pd.DataFrame(
        columns=['Id_Vsource', 'bus1', 'basekv', 'pu', 'angle', 'frequency', 'phases', 'MVAsc3', 'MVAsc1', 'x1r1',
                 'x0r0', 'Isc3', 'Isc1', 'R1', 'X1', 'R0', 'X0', 'ScanType', 'Sequence', 'bus2', 'Z1', 'Z0', 'Z2',
                 'puZ1', 'puZ0', 'puZ2', 'baseMVA', 'Yearly', 'Daily', 'Duty', 'Model', 'puZideal', 'spectrum',
                 'basefreq', 'enabled', 'like'])

    df_StaCubic_ElmTerm = merge_ElmTerm_StaCubic(DataFrame_StaCubic=DataFrame_StaCubic,
                                                 DataFrame_ElmTerm=DataFrame_ElmTerm)
    df_StaCubic_ElmTerm = df_StaCubic_ElmTerm[['ID(a:40)', 'Bus_name_DSS', 'nphase(i)', 'uknom(r)']]

    'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
    characters_delete(DataFrame_ElmXnet, 'loc_name(a:40)')

    'Identifies the name of the connected bus'
    merge_ElmXnet_StaCubic = pd.merge(DataFrame_ElmXnet, df_StaCubic_ElmTerm, how='inner', left_on='bus1(p)', right_on='ID(a:40)',
                                     suffixes=('_x', '_y'))

    if len([x for x in merge_ElmXnet_StaCubic['bustp(a:2)'] if x in 'SL']) > 0:
        pass
    else:
        message_Vsource = '\n -Vsource: You need to define the SLACK (SL) bus in the Digsilent database. if not, you will have problems in OpenDSS'
        print(message_Vsource)
        file_logging_info(logfilename='BBDD_Digsilent summary', message=message_Vsource)

    for index, row in merge_ElmXnet_StaCubic.iterrows():
        Type_Vsource = merge_ElmXnet_StaCubic['bustp(a:2)'][index]

        if Type_Vsource == 'SL':
            Id_Vsource = 'source'
        else:
            Id_Vsource = merge_ElmXnet_StaCubic['loc_name(a:40)'][index]

        bus1 = merge_ElmXnet_StaCubic['Bus_name_DSS'][index]
        pu = merge_ElmXnet_StaCubic['usetp(r)'][index]
        angle = merge_ElmXnet_StaCubic['phiini(r)'][index]
        #MVAsc3 = merge_ElmXnet_StaCubic['snss(r)'][index]
        MVAsc3 = ''
        #Isc3 = merge_ElmXnet_StaCubic['ikss(r)'][index]
        Isc3 = ''
        basekv = merge_ElmXnet_StaCubic['uknom(r)'][index]
        phases = merge_ElmXnet_StaCubic['nphase(i)'][index]

        df_Vsource_DSS = df_Vsource_DSS.append({'Id_Vsource': Id_Vsource, 'bus1': bus1, 'basekv': basekv, 'pu': pu, 'angle': angle, 'frequency': '', 'phases': phases, 'MVAsc3': MVAsc3,
                                                'MVAsc1': '', 'x1r1': '', 'x0r0': '', 'Isc3': Isc3, 'Isc1': '', 'R1': '', 'X1': '', 'R0': '', 'X0': '',
                                                'ScanType': '', 'Sequence': '', 'bus2': '', 'Z1': '', 'Z0': '', 'Z2': '', 'puZ1': '', 'puZ0': '', 'puZ2': '',
                                                'baseMVA': '', 'Yearly': '', 'Daily': '', 'Duty': '', 'Model': '', 'puZideal': '', 'spectrum': '',
                                                'basefreq': '', 'enabled': '', 'like': ''}, ignore_index=True)

    return df_Vsource_DSS

