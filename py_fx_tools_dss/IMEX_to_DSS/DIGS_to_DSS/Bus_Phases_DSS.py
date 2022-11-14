# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd
from collections import defaultdict
from py_fx_tools_dss.helper_functions import *

pd.options.mode.chained_assignment = None

def terminal_name_check(DataFrame_ElmTerm: pd.DataFrame):
    '''
    check that there are no terminals with the same name

    :param DataFrame_ElmTerm:
    :return:
    '''

    df_ElmTerm = DataFrame_ElmTerm
    df_duplicate_ElmTerm = DataFrame_ElmTerm[DataFrame_ElmTerm['loc_name(a:40)'].duplicated() == True]
    value_unique = list(df_duplicate_ElmTerm['loc_name(a:40)'].unique())
    df_ElmTerm['aux'] = df_ElmTerm['loc_name(a:40)'].apply(lambda x: 1 if (x in value_unique) else 0)
    for index, row in df_ElmTerm.iterrows():
        if df_ElmTerm['aux'][index] == 1:
            df_ElmTerm['loc_name(a:40)'][index] = df_ElmTerm['loc_name(a:40)'][index] + '_' + str(
                df_ElmTerm['fold_id(p)'][index])
        else:
            pass

    return df_ElmTerm


def phase_identification(DataFrame_StaCubic:pd.DataFrame, DataFrame_ElmTerm: pd.DataFrame,
                         file_direction: str, StaCubic_direction:str, file_name: str) -> pd.DataFrame:
    #print('___________________________________________________________________________________________________________')
    #print('Start phase identification from DigSilent to OpenDSS')
    df_StaCubic = DataFrame_StaCubic[['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)',  'obj_id(p)',
                                     'it2p1(i)', 'it2p2(i)', 'it2p3(i)', 'nphase(i)', 'cPhInfo(a)']]
    num_aux = 10000
    count_1 = 0
    count_2 = 0
    stop_while = 20
    #print(f'{count_2}, {count_1}')

    keys_DataFrame_ElmTerm = DataFrame_ElmTerm.loc[:, ['ID(a:40)', 'ciEnergized(i)']]
    keys_DataFrame_ElmTerm = keys_DataFrame_ElmTerm[keys_DataFrame_ElmTerm['ciEnergized(i)'] == 1] #Filters energized elements

    df_StaCubic_ElmTerm = pd.merge(
        DataFrame_StaCubic, keys_DataFrame_ElmTerm,
        how='inner', left_on='cterm(p)', right_on='ID(a:40)').rename(columns={'ID(a:40)_x':'ID(a:40)'})

    df_StaCubic = df_StaCubic_ElmTerm[['ID(a:40)', 'loc_name(a:40)', 'fold_id(p)', 'obj_id(p)',
                                      'it2p1(i)', 'it2p2(i)', 'it2p3(i)', 'nphase(i)', 'cPhInfo(a)']]
    #df_StaCubic.loc[:, 'dss_aux'] = df_StaCubic['cPhInfo(a)']
    df_StaCubic.loc[:, 'dss_aux'] = df_StaCubic.loc[:, 'cPhInfo(a)']

    if StaCubic_direction != '':
        df_StaCubic = pd.read_excel(io=f'{file_direction}\StaCubic_{file_name}.xlsx')
    else:
        pass

    aux_2ph = num_aux
    cod_2ph_digs = ['DP1DP2', 'DP2DP1', 'DP1DP2N', 'DP2DP1N']


    while aux_2ph != 0:
        count_2 += 1
        if len([x for x in df_StaCubic['dss_aux'] if x in cod_2ph_digs]) == 0:
            break
        if len([x for x in df_StaCubic['dss_aux'] if x in cod_2ph_digs]) > 0:
            df_StaCubic = phase_2ph_identification(df_StaCubic)
            aux_2ph = len([x for x in df_StaCubic['dss_aux'] if x in cod_2ph_digs])
            #print(aux_2ph)
        if count_2 == stop_while:
            message_2ph = '\n -biphasic phase cannot be identified, you must do it manually by identifying the phases in the df_StaCubic.xlsx file'
            print(message_2ph)
            file_logging_info(logfilename='BBDD_Digsilent summary', message=message_2ph)
            df_StaCubic.to_excel(f'{file_direction}\StaCubic_{file_name}.xlsx', index=False)
            exit()

    aux_1ph = num_aux
    cod_1ph_digs = ['SP', 'SPN']
    while aux_1ph != 0:
        count_1 += 1
        if len([x for x in df_StaCubic['dss_aux'] if x in cod_1ph_digs]) == 0:
            break
        if len([x for x in df_StaCubic['dss_aux'] if x in cod_1ph_digs]) > 0:
            df_StaCubic = phase_1ph_identification(df_StaCubic)
            aux_1ph = len([x for x in df_StaCubic['dss_aux'] if x in cod_1ph_digs])
        if count_1 == stop_while:
            message_1ph = '\n -monophasic phase cannot be identified, you must do it manually by identifying the phases in the df_StaCubic.xlsx file'
            print(message_1ph)
            file_logging_info(logfilename='BBDD_Digsilent summary', message=message_1ph)
            df_StaCubic.to_excel(f'{file_direction}\StaCubic_{file_name}.xlsx', index=False)
            exit()

    #Create the auxiliary column of OpenDSS and conditionals according to the connection of the phase
    df_StaCubic.loc[:, 'phase_DSS'] = ''
    for index, row in df_StaCubic.iterrows():
        #three phase
        if row['dss_aux'] == 'abc':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.2.3'
        elif row['dss_aux'] == 'abcN':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.2.3.4'

        #biphasic
        if row['dss_aux'] == 'ab':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.2'
        elif row['dss_aux'] == 'abN':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.2.4'
        elif row['dss_aux'] == 'ac':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.3'
        elif row['dss_aux'] == 'acN':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.3.4'
        elif row['dss_aux'] == 'ba':
            df_StaCubic.at[index, 'phase_DSS'] = '.2.1'
        elif row['dss_aux'] == 'baN':
            df_StaCubic.at[index, 'phase_DSS'] = '.2.1.4'
        elif row['dss_aux'] == 'bc':
            df_StaCubic.at[index, 'phase_DSS'] = '.2.3'
        elif row['dss_aux'] == 'bcN':
            df_StaCubic.at[index, 'phase_DSS'] = '.2.3.4'
        elif row['dss_aux'] == 'ca':
            df_StaCubic.at[index, 'phase_DSS'] = '.3.1'
        elif row['dss_aux'] == 'caN':
            df_StaCubic.at[index, 'phase_DSS'] = '.3.1.4'
        elif row['dss_aux'] == 'cb':
            df_StaCubic.at[index, 'phase_DSS'] = '.3.2'
        elif row['dss_aux'] == 'cbN':
            df_StaCubic.at[index, 'phase_DSS'] = '.3.2.4'
        #monophasic
        if row['dss_aux'] == 'a':
            df_StaCubic.at[index, 'phase_DSS'] = '.1'
        elif row['dss_aux'] == 'aN':
            df_StaCubic.at[index, 'phase_DSS'] = '.1.4'
        elif row['dss_aux'] == 'b':
            df_StaCubic.at[index, 'phase_DSS'] = '.2'
        elif row['dss_aux'] == 'bN':
            df_StaCubic.at[index, 'phase_DSS'] = '.2.4'
        elif row['dss_aux'] == 'c':
            df_StaCubic.at[index, 'phase_DSS'] = '.3'
        elif row['dss_aux'] == 'cN':
            df_StaCubic.at[index, 'phase_DSS'] = '.3.4'
        elif row['dss_aux'] == 'N':
            df_StaCubic.at[index, 'phase_DSS'] = '.4'

    #df_StaCubic_2 = df_StaCubic[['ID(a:40)', 'fold_id(p)', 'obj_id(p)', 'nphase(i)', 'cPhInfo(a)', 'dss_aux', 'phase_DSS']]

    #print('Finished phase identification from DigSilent to OpenDSS')
    #print('___________________________________________________________________________________________________________')
    return df_StaCubic

def phase_2ph_identification(df_StaCubic: pd.DataFrame) -> pd.DataFrame:
    bus_max, bus_min = df_StaCubic['fold_id(p)'].max(), df_StaCubic['fold_id(p)'].min()
    #Creation of dictionaries with elements that have the phase connection
    dic_2ph_data = defaultdict(list)
    dic_2ph_no_data = defaultdict(list)
    for bus in range(bus_min, bus_max + 1, 1):
        for index, row in df_StaCubic.iterrows():
            if bus == row['fold_id(p)']:
                if row['nphase(i)'] == 2:
                    if row['dss_aux'] == 'aN' or row['dss_aux'] =='cN' or row['dss_aux'] == 'bN':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'ab' or row['dss_aux'] =='ac':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'ba' or row['dss_aux'] == 'bc':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'ca' or row['dss_aux'] == 'cb':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'abN' or row['dss_aux'] =='acN':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'baN' or row['dss_aux'] == 'bcN':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'caN' or row['dss_aux'] == 'cbN':
                        dic_2ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'DP1DP2' or row['dss_aux'] == 'DP1DP2N':
                        dic_2ph_no_data[row['fold_id(p)']].append(row['obj_id(p)'])

    #Traversal of the elements in common between the dictionaries with and without phase information
    for key_1, value_1 in dic_2ph_data.items():
        for mm in value_1:
            for key_2, value_2 in dic_2ph_no_data.items():
                for kk in value_2:
                    if mm == kk:
                        index_data = df_StaCubic[(df_StaCubic['fold_id(p)'] == key_1) & (df_StaCubic['obj_id(p)'] == mm)].index
                        index_no_data = df_StaCubic[(df_StaCubic['fold_id(p)'] == key_2) & (df_StaCubic['obj_id(p)'] == kk)].index
                        #df_StaCubic['dss_aux'][int(index_data[0])] = df_StaCubic['dss_aux'][int(index_data[0])]
                        #df_StaCubic['dss_aux'][int(index_no_data[0])] = df_StaCubic['dss_aux'][int(index_data[0])]

                        df_StaCubic.loc[int(index_data[0]), 'dss_aux'] = df_StaCubic.loc[int(index_data[0]), 'dss_aux']
                        df_StaCubic.loc[int(index_no_data[0]), 'dss_aux'] = df_StaCubic.loc[int(index_data[0]), 'dss_aux']

    #Identifies the inheritance of names based on the elements connected to each bar
    Bus_elem = defaultdict(list)
    Bus_conn = defaultdict(list)
    for bus in range(bus_min, bus_max + 1, 1):
        for index, row in df_StaCubic.iterrows():
            if bus == row['fold_id(p)']:
                if row['nphase(i)'] == 2 or row['nphase(i)'] == 1:
                    Bus_elem[row['fold_id(p)']].append(row['obj_id(p)'])
                    Bus_conn[row['fold_id(p)']].append(row['dss_aux'])

    cod_disg = ['SPN', 'SP', 'DP1', 'DP2', 'DP1N', 'DP2N', 'DP1DP2', 'DP2DP1', 'DP1DP2N', 'DP2DP1N']
    cod_phase_dig = ['a', 'b', 'c', 'aN', 'bN', 'cN',
                     'ab', 'ac', 'abN', 'acN',
                     'ba', 'bc', 'baN', 'bcN',
                     'ca', 'cb', 'caN', 'cbN']

    for key_bus, value_elem in Bus_elem.items():
        node_conn = Bus_conn[key_bus]
        if len([x for x in Bus_conn[key_bus] if x in cod_phase_dig]) > 0:
            if len([x for x in Bus_conn[key_bus] if x in cod_disg]) == 0:
                pass
            else:
                phase_data = [x for x in Bus_conn[key_bus] if x in cod_phase_dig]
                len_phase = 0
                for phase in phase_data:
                    phase_aux = phase.replace('N', '')
                    if len(phase_aux) > len_phase:
                        sin_N = phase_aux
                if len(sin_N) == 2:
                    DP1 = sin_N[0]
                    DP2 = sin_N[1]
                elif len(sin_N) == 1:
                    DP1 = sin_N[0]

                for x, k in enumerate(node_conn):
                    try:
                        node_conn[x] = node_conn[x].replace('DP1', DP1)
                        node_conn[x] = node_conn[x].replace('DP2', DP2)
                    except UnboundLocalError:
                        pass

                'comentario: debe haber una funcion que discrimine el elemento conectado entre dos nodos,'
                'ya que si es un transformador la herencia (HV->DP2N a LV->DP1DP2N), se pierde la conexion' \
                'cuando hace la herencia del los otras elementos agua abajo (DP1)'

    for key_3, value_3 in Bus_elem.items():
        for index, elem in enumerate(value_3):
            try:
                index_dss = df_StaCubic[(df_StaCubic['fold_id(p)'] == key_3) & (df_StaCubic['obj_id(p)'] == elem)].index
                df_StaCubic.loc[int(index_dss[0]), 'dss_aux'] = Bus_conn[key_3][index]
                #df_StaCubic['dss_aux'][int(index_dss[0])] = Bus_conn[key_3][index]
                #df_StaCubic['dss_aux'][int(index_dss[0])] = Bus_conn[key_3][index]
            except IndexError:
                pass
    return df_StaCubic

def phase_1ph_identification(df_StaCubic:pd.DataFrame)->pd.DataFrame:
    bus_max, bus_min = df_StaCubic['fold_id(p)'].max(), df_StaCubic['fold_id(p)'].min()
    dic_1ph_data = defaultdict(list)
    dic_1ph_no_data = defaultdict(list)
    for bus in range(bus_min, bus_max + 1, 1):
        for index, row in df_StaCubic.iterrows():
            if bus == row['fold_id(p)']:
                if row['nphase(i)'] == 1:
                    if row['dss_aux'] == 'aN' or row['dss_aux'] =='cN' or row['dss_aux'] == 'bN':
                        dic_1ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'a' or row['dss_aux'] =='b' or  row['dss_aux'] =='c':
                        dic_1ph_data[row['fold_id(p)']].append(row['obj_id(p)'])
                    elif row['dss_aux'] == 'SP' or row['dss_aux'] == 'SPN':
                        dic_1ph_no_data[row['fold_id(p)']].append(row['obj_id(p)'])
    for key_1, value_1 in dic_1ph_data.items():
        for mm in value_1:
            for key_2, value_2 in dic_1ph_no_data.items():
                for kk in value_2:
                    if mm == kk:
                        index_data = df_StaCubic[(df_StaCubic['fold_id(p)'] == key_1) & (df_StaCubic['obj_id(p)'] == mm)].index
                        index_no_data = df_StaCubic[(df_StaCubic['fold_id(p)'] == key_2) & (df_StaCubic['obj_id(p)'] == kk)].index
                        #df_StaCubic['dss_aux'][int(index_data[0])] = df_StaCubic['dss_aux'][int(index_data[0])]
                        #df_StaCubic['dss_aux'][int(index_no_data[0])] = df_StaCubic['dss_aux'][int(index_data[0])]

                        df_StaCubic.loc[int(index_data[0]), 'dss_aux'] = df_StaCubic.loc[int(index_data[0]), 'dss_aux']
                        df_StaCubic.loc[int(index_no_data[0]), 'dss_aux'] = df_StaCubic.loc[int(index_data[0]), 'dss_aux']

    #Identifica la herencia de nombres en funcion de los elementos conetados a cada barra
    Bus_elem = defaultdict(list)
    Bus_conn = defaultdict(list)
    for bus in range(bus_min, bus_max + 1, 1):
        for index, row in df_StaCubic.iterrows():
            if bus == row['fold_id(p)']:
                if row['nphase(i)'] == 2 or row['nphase(i)'] == 1:
                    Bus_elem[row['fold_id(p)']].append(row['obj_id(p)'])
                    Bus_conn[row['fold_id(p)']].append(row['dss_aux'])

    cod_disg = ['SPN', 'SP','DP1', 'DP2', 'DP1N', 'DP2N', 'DP1DP2', 'DP2DP1', 'DP1DP2N', 'DP2DP1N']
    cod_phase_dig = ['a', 'b', 'c', 'aN', 'bN', 'cN',
                     'ab', 'ac', 'abN', 'acN',
                     'ba', 'bc', 'baN', 'bcN',
                     'ca', 'cb', 'caN', 'cbN']
    for key_bus, value_elem in Bus_elem.items():
        node_conn = Bus_conn[key_bus]
        if len([x for x in Bus_conn[key_bus] if x in cod_phase_dig]) > 0:
            if len([x for x in Bus_conn[key_bus] if x in cod_disg]) == 0:
                pass
            else:
                phase_data = [x for x in Bus_conn[key_bus] if x in cod_phase_dig]
                len_phase = 0
                for phase in phase_data:
                    phase_aux = phase.replace('N', '')
                    if len(phase_aux) > len_phase:
                        sin_N = phase_aux
                if len(sin_N) == 2:
                    DP1 = sin_N[0]
                    DP2 = sin_N[1]
                elif len(sin_N) == 1:
                    DP1 = sin_N[0]
                for x, k in enumerate(node_conn):
                    node_conn[x] = node_conn[x].replace('SP', DP1)

    for key_3, value_3 in Bus_elem.items():
        for index, elem in enumerate(value_3):
            try:
                index_dss = df_StaCubic[(df_StaCubic['fold_id(p)'] == key_3) & (df_StaCubic['obj_id(p)'] == elem)].index
                #df_StaCubic['dss_aux'][int(index_dss[0])] = Bus_conn[key_3][index]
                df_StaCubic.loc[int(index_dss[0]), 'dss_aux'] = Bus_conn[key_3][index]
            except IndexError:
                pass

    return df_StaCubic