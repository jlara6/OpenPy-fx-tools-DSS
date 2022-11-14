# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd

def DIGS_EnergyMeter_DSS() -> pd.DataFrame:
    '''
    :return: df_EnergyMeter_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_EnergyMeter_DSS = pd.DataFrame(
        columns=['Id_EnergyMeter', 'element', 'terminal', 'action', 'option', 'kVAnormal', 'kVAemerg', 'peakcurrent',
                 'Zonelist', 'LocalOnly', 'Mask', 'Losses', 'LineLosses', 'XfmrLosses', 'SeqLosses', '3phaseLosses',
                 'VbaseLosses', 'PhaseVoltageReport', 'Int_Rate', 'Int_Duration', 'SAIFI', 'SAIFIkW', 'SAIDI', 'CAIDI',
                 'CustInterrupts', 'basefreq', 'enabled', 'like'])

    return df_EnergyMeter_DSS

def DIGS_FMonitor_DSS() -> pd.DataFrame:
    '''
    :return: df_FMonitor_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_FMonitor_DSS = pd.DataFrame(
        columns=['Id_FMonitor', 'element', 'terminal', 'mode', 'action', 'residual', 'VIPolar', 'PPolar', 'P_trans_ref',
                 'V_Sensor', 'P_Sensor', 'Node_num', 'Cluster_num', 'Total_Clusters', 'Nodes', 'CommVector',
                 'ElemTableLine', 'P_Mode', 'CommDelayVector', 'T_intvl_smpl', 'MaxLocalMem', 'Volt_limits_pu',
                 'b_Curt_Ctrl', 'up_dly', 'virtual_ld_node', 'EGen', 'attack_defense', 'Comm_hide', 'Comm_node_hide',
                 'basefreq', 'enabled', 'like'])

    return df_FMonitor_DSS

def DIGS_Monitor_DSS() -> pd.DataFrame:
    '''
    :return: df_Monitor_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Monitor_DSS = pd.DataFrame(
        columns=['Id_Monitor', 'element', 'terminal', 'mode', 'action', 'residual', 'VIPolar', 'PPolar', 'basefreq',
                 'enabled', 'like'])

    return df_Monitor_DSS

def DIGS_Sensor_DSS() -> pd.DataFrame:
    '''
    :return: df_Sensor_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Sensor_DSS = pd.DataFrame(
        columns=['Id_Sensor', 'element', 'terminal', 'kvbase', 'clear', 'kVs', 'currents', 'kWs', 'kvars', 'conn',
                 'Deltadirection', '%Error', 'Weight', 'action', 'basefreq', 'enabled', 'like'])

    return df_Sensor_DSS



