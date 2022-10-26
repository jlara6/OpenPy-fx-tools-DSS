# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

import pandas as pd

def DIGS_AutoTrans_DSS()->pd.DataFrame:
    '''
    :return: df_AutoTrans_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_AutoTrans_DSS = pd.DataFrame(
        columns=['Id_AutoTrans', 'phases', 'windings', 'wdg', 'bus', 'conn', 'kV', 'KVA', 'tap', '%R', 'Rdcohms',
                 'Core', 'buses', 'conns', 'kVs', 'KVAs', 'taps', 'XHX', 'XHT', 'XXT', 'XSCarray', 'thermal', 'n', 'm',
                 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normkVA', 'emergkVA', 'sub', 'MaxTap', 'MinTap',
                 'NumTaps', 'subname', '%imag', 'pp', '_amtifloat', '%Rs', 'bank', 'XfmrCode', 'XRConst', 'LeadLag',
                 'WdgCurrents', 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled',
                 'like'])

    return df_AutoTrans_DSS

def DIGS_GICTransformer_DSS()->pd.DataFrame:
    '''
    :return: df_GICTransformer_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_GICTransformer_DSS = pd.DataFrame(
        columns=['Id_AutoTrans', 'phases', 'windings', 'wdg', 'bus', 'conn', 'kV', 'KVA', 'tap', '%R', 'Rdcohms',
                 'Core', 'buses', 'conns', 'kVs', 'KVAs', 'taps', 'XHX', 'XHT', 'XXT', 'XSCarray', 'thermal', 'n', 'm',
                 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normkVA', 'emergkVA', 'sub', 'MaxTap', 'MinTap',
                 'NumTaps', 'subname', '%imag', 'pp', '_amtifloat', '%Rs', 'bank', 'XfmrCode', 'XRConst', 'LeadLag',
                 'WdgCurrents', 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled',
                 'like'])

    return df_GICTransformer_DSS

def DIGS_Reactor_DSS()->pd.DataFrame:
    '''
    :return: df_Reactor_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Reactor_DSS = pd.DataFrame(
        columns=['Id_Reactor', 'bus1', 'bus2', 'phases', 'kvar', 'kv', 'conn', 'Rmatrix', 'Xmatrix', 'Parallel', 'R',
                 'X', 'Rp', 'Z1', 'Z2', 'Z0', 'Z', 'Rcurve', 'LCurve', 'LmH', 'normamps', 'emergamps', 'faultrate',
                 'pctperm', 'repair', 'basefreq', 'enabled', 'like'])

    return df_Reactor_DSS

def DIGS_Generator_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_Generator_DSS = pd.DataFrame(
        columns=['Id_Generator', 'phases', 'bus1', 'kv', 'kW', 'pf', 'kvar', 'model', 'Vminpu', 'Vmaxpu', 'yearly',
                 'daily', 'duty', 'dispmode', 'dispvalue', 'conn', 'Rneut', 'Xneut', 'status', 'class', 'Vpu',
                 'maxkvar', 'minkvar', 'pvfactor', 'forceon', 'KVA', 'MVA', 'Xd', 'Xdp', 'Xdpp', 'H', 'D', 'UserModel',
                 'UserData', 'ShaftModel', 'ShaftData', 'DutyStart', 'debugtrace', 'Balanced', 'XRdp', 'UseFuel',
                 'FuelWh', '%Fuel', '%Reserve', 'Refuel', 'spectrum', 'Basefreq', 'enabled', 'like'])

    return df_Generator_DSS

def DIGS_Generic5_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_Generic5_DSS = pd.DataFrame(
        columns=['Id_Generic5', 'phases', 'bus1', 'kv', 'kW', 'pf', 'conn', 'kVA', 'H', 'D', 'P_ref1kW', 'P_ref2kW',
                 'P_ref3kW', 'P_ref1kVLN', 'P_ref2VLN', 'P_ref3VLN', 'MaxSlip', 'SlipOption', 'Yearly', 'Daily', 'Duty',
                 'Debugtrace', 'P_refkW', 'Q_refkVAr', 'Cluster_num', 'V_refkVLN', 'ctrl_mode', 'QV_flag', 'kcd', 'kcq',
                 'kqi', 'Q_ref1kW', 'Q_ref2kW', 'Q_ref3kW', 'PmaxkW', 'PminkW', 'PQpriority', 'PmppkW', 'Pfctr1',
                 'Pfctr2', 'Pfctr3', 'Pfctr4', 'Pfctr5', 'Pfctr6', 'PbiaskW', 'CC_Switch', 'kcp_drp2', 'Volt_trhd',
                 'droop', 'spectrum', 'basefreq', 'enable', 'like'])

    return df_Generic5_DSS

def DIGS_GICLine_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_GICLine_DSS = pd.DataFrame(
        columns=['Id_GICLine', 'bus1', 'bus2', 'Volts', 'Angle', 'frecuency', 'phases', 'R', 'X', 'C', 'EN', 'EE',
                 'Lat1', 'Lon1', 'Lat2', 'Lon2', 'spectrum', 'basefreq', 'enabled', 'like'])

    return df_GICLine_DSS


def DIGS_IndMach012_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_IndMach012_DSS = pd.DataFrame(
        columns=['Id_IndMach012', 'phases', 'bus1', 'kv', 'kW', 'pf', 'conn', 'KVA', 'H', 'D', 'puRs', 'puXs', 'puRr',
                 'puXr', 'puXm', 'Slip', 'MaxSlip', 'SlipOption', 'Yearly', 'Daily', 'Duty', 'Debugtrace', 'spectrum',
                 'basefreq', 'enabled', 'like'])

    return df_IndMach012_DSS

def DIGS_PVSystem_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_PVSystem_DSS = pd.DataFrame(
        columns=['Id_PVSystem', 'phases', 'bus1', 'kv', 'irradiance', 'Pmpp', '%Pmpp', 'Temperature', 'pf', 'conn',
                 'kvar', 'KVA', '%Cutin', '%Cutout', 'EffCurve', 'P-TCurve', '%R', '%X', 'model', 'Vminpu', 'Vmaxpu',
                 'Balanced', 'LimitCurrent', 'yearly', 'daily', 'duty', 'Tyearly', 'Tdaily', 'Tduty', 'class',
                 'UserModel', 'UserData', 'debugtrace', 'VarFollowInverted', 'DutyStart', 'WattPriority', 'PFPriority',
                 '%PminNoVars', '%PminkvarMax', 'kvarMax', 'kvarMaxAbs', 'spectrum', 'basefreq', 'enabled', 'like'])

    return df_PVSystem_DSS

def DIGS_UPFC_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_UPFC_DSS = pd.DataFrame(
        columns= ['Id_UPFC', 'bus1', 'bus2', 'refkv', 'pf', 'frecuency', 'phases', 'Xs', 'Tol1', 'Mode', 'VpqMax',
                  'LossCurve', 'VHLimit', 'VLLimit', 'Climit', 'refkv2', 'kvarLimit', 'spectrum', 'basefreq',
                  'enabled', 'like'])

    return df_UPFC_DSS

def DIGS_VCCS_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_VCCS_DSS = pd.DataFrame(
        columns= ['Id_UPFC', 'bus1', 'bus2', 'refkv', 'pf', 'frecuency', 'phases', 'Xs', 'Tol1', 'Mode', 'VpqMax',
                  'LossCurve', 'VHLimit', 'VLLimit', 'Climit', 'refkv2', 'kvarLimit', 'spectrum', 'basefreq',
                  'enabled', 'like'])

    return df_VCCS_DSS

def DIGS_Storage_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_Storage_DSS = pd.DataFrame(
        columns=['Id_Storage', 'phases', 'bus1', 'kv', 'conn', 'kW', 'kvar', 'pf', 'kVA', '%Cutin', '%Cutout',
                 'EffCurve', 'VarFollowInverter', 'kvarMax', 'kvarMaxAbs', 'WattPriority', 'PFPriority', '%PminNoVars',
                 '%PminkvarMax', 'KWrated', '%kWrated', 'kWhrated', 'kWhstrored', '%stored', '%reserve', 'State',
                 '%Discharge', '%Charge', '%EffCharge', '%EffDischarge', '%IdlingkW', '%Idlingkvar', '%R', '%X',
                 'model', 'Vminpu', 'Vmaxpu', 'Balanced', 'LimitCurrent', 'yearly', 'daily', 'duty', 'DispMode',
                 'DischargeTrigger', 'TimeChargeTrig', 'class', 'DynaDLL', 'DynaData', 'DynaData.1', 'UserModel',
                 'UserData', 'debugtrace', 'spectrum', 'basefreq', 'enabled', 'like'])

    return df_Storage_DSS

def DIGS_VSConverter_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_VSConverter_DSS = pd.DataFrame(
        columns=['Id_VSConverter', 'phases', 'Bus1', 'kVac', 'kVdc', 'kW', 'Ndc', 'Rac', 'Xac', 'm0', 'd0', 'Mmin',
                 'Mmax', 'Iacmax', 'Idcmax', 'Vacref', 'Pacref', 'Qacref', 'Vdcref', 'VscMode', 'spectrum', 'basefreq',
                 'enabled', 'like'])

    return df_VSConverter_DSS

def DIGS_WindGen_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_WindGen_DSS = pd.DataFrame(
        columns=['Id_WindGen', 'phases', 'bus1', 'kv', 'kW', 'PF', 'model', 'yearly', 'daily', 'duty', 'conn', 'kvar',
                 'status', 'class', 'Vpu', 'maxkvar', 'minkvar', 'pvfactor', 'debugtrace', 'Vminpu', 'Vmaxpu',
                 'forceon', 'kVA', 'MVA', 'Xd', 'Xdp', 'Xdpp', 'H', 'D', 'UserModel', 'UserData', 'ShaftModel',
                 'ShaftModel.1', 'DutyStart', 'Balanced', 'XRdp', 'spectrum', 'basefreq', 'enabled', 'like'])

    return df_WindGen_DSS

def DIGS_CapControl_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_CapControl_DSS = pd.DataFrame(
        columns=['Id_CapControl', 'element', 'terminal', 'capacitor', 'type', 'PTratio', 'CTratio', 'Onsetting',
                 'OFFsentting', 'Delay', 'VoltOverride', 'Vmax', 'Vmin', 'DelayOFF', 'DeadTime', 'CTPhase', 'PTPhase',
                 'Vbus', 'Eventlog', 'UserModel', 'UserData', 'pctMinkvar', 'Reset', 'basefreq', 'enabled', 'like'])

    return df_CapControl_DSS

def DIGS_ESPVLControl_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_ESPVLControl_DSS = pd.DataFrame(
        columns=['Id_ESPVLControl', 'Element', 'Terminal', 'Type', 'kWBand', 'kvarlimit', 'LocalControlList',
                 'LocalControlWeight', 'PVSystemList', 'PVSystemWeight', 'StorageList', 'StorageWeight', 'Forecast',
                 'basefreq', 'enabled', 'like'])

    return df_ESPVLControl_DSS

def DIGS_ExpControl_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_ExpControl_DSS = pd.DataFrame(
        columns=['Id_ExpControl', 'PVSystemList', 'Vreg', 'Slope', 'VregTau', 'Qbias', 'VregMin', 'VregMax', 'QmaxLead',
                 'QmaxLag', 'EventLog', 'DeltaQ_factor', 'PreferQ', 'Tresponse', 'basefreq', 'enabled', 'like'])

    return df_ExpControl_DSS

def DIGS_Fuse_DSS()->pd.DataFrame:

    'DataFrame creation with OpenDSS keywords'
    df_Fuse_DSS = pd.DataFrame(
        columns=['Id_Fuse', 'MonitoredObj', 'MonitoredTerm', 'SwitchedObj', 'SwitchedTerm', 'FaseCurve', 'RatedCurrent',
                 'Delay', 'Action', 'Normal', 'State', 'basefreq', 'enabled', 'like'])

    return df_Fuse_DSS

def DIGS_GenDispatcher_DSS()->pd.DataFrame:
    '''

    :return: df_GenDispatcher_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_GenDispatcher_DSS = pd.DataFrame(
        columns=['Id_GenDispatcher', 'Element', 'Terminal', 'kWLimit', 'kWBand', 'kvarLimit', 'GenList', 'basefreq',
                 'enabled', 'like'])

    return df_GenDispatcher_DSS

def DIGS_InvControl_DSS()->pd.DataFrame:
    '''

    :return: df_InvControl_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_InvControl_DSS = pd.DataFrame(
        columns=['Id_InvControl', 'DERList', 'Mode', 'CombiMode', 'vvc_curve1', 'hysteresis_offset',
                 'voltage_curve_ref', 'avgwindowlen', 'volt_watt_curve', 'DbVMin', 'DbVMax', 'ArGraLowV', 'ArGraHiV',
                 'DynReacavgwindowlen', 'deltaQ_Factor', 'VoltageChangeTolerance', 'VarChangeTolerance',
                 'VoltwattYAxis', 'RateofChangeMode', 'LPFTau', 'RiseFallLimit', 'deltaP_Factor', 'EventLog',
                 'RefReactivePower', 'ActivePChangeTolerance', 'monVoltageCalc', 'monBus', 'MonBusesVbase',
                 'voltwattCH_curve', 'wattpf_curve', 'wattvar_curve', 'VV_RefReactivePower', 'PVSystemList',
                 'Vsetpoint', 'basefreq', 'enabled', 'like'])

    return df_InvControl_DSS

def DIGS_Recloser_DSS()->pd.DataFrame:
    '''
    :return: df_Recloser_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Recloser_DSS = pd.DataFrame(
        columns=['Id_Recloser', 'MonitoredObj', 'MonitoredTerm', 'SwitchedObj', 'SwitchedTerm', 'NumFast', 'PhaseFast',
                 'PhaseDelayed', 'GroundFast', 'GroundDelayed', 'PhaseTrip', 'GroundTrip', 'PhaseInst', 'GroundInst',
                 'Reset', 'Shots', 'RecloseIntervals', 'Delay', 'Action', 'TDPhFast', 'TDGrFast', 'TDPhDelayed',
                 'TDGrDelayed', 'Normal', 'State', 'basefreq', 'enabled', 'like'])

    return df_Recloser_DSS

def DIGS_RegControl_DSS(DataFrame_ElmTr2:pd.DataFrame)->pd.DataFrame:
    '''
    :return: df_RegControl_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_RegControl_DSS = pd.DataFrame(
        columns=['Id_RegControl', 'transformer', 'winding', 'vreg', 'band', 'ptratio', 'Ctprim', 'R', 'X', 'bus',
                 'delay', 'reversible', 'revvreg', 'revband', 'revR', 'revX', 'tapdelay', 'debugtrace', 'maxtapchange',
                 'inversetime', 'tapwinding', 'vlimit', 'Ptphase', 'revThreshold', 'revDelay', 'revNeutral', 'EventLog',
                 'RemotePTRatio', 'TapNum', 'Reset', 'LDC_Z', 'rev_Z', 'Cogen', 'basefreq', 'enabled', 'like'])

    DataFrame_ElmTr2 = DataFrame_ElmTr2[DataFrame_ElmTr2['ciEnergized(i)'] == 1]  # Filters energized elements
    DataFrame_ElmTr2 = DataFrame_ElmTr2[DataFrame_ElmTr2['i_auto(i)'] == 1]  # Filters energized elements

    if DataFrame_ElmTr2.empty == False:
        
        for index,  row in DataFrame_ElmTr2.iterrows():
            Id_RegControl = DataFrame_ElmTr2['loc_name(a:40)'][index]
            transformer = DataFrame_ElmTr2['loc_name(a:40)'][index]
            winding = '2'
            vreg = '122'
            band = '2'
            ptratio = '20'
            Ctprim = '700'
            R = '3'
            X = '9'

            df_RegControl_DSS = df_RegControl_DSS.append(
                {'Id_RegControl': Id_RegControl, 'transformer': transformer, 'winding': winding, 'vreg': vreg, 'band': band, 'ptratio': ptratio, 'Ctprim': Ctprim, 'R': R, 'X': X, 'bus': '',
                 'delay': '', 'reversible': '', 'revvreg': '', 'revband': '', 'revR': '', 'revX': '', 'tapdelay': '', 'debugtrace': '', 'maxtapchange': '',
                 'inversetime': '', 'tapwinding': '', 'vlimit': '', 'Ptphase': '', 'revThreshold': '', 'revDelay': '', 'revNeutral': '', 'EventLog': '',
                 'RemotePTRatio': '', 'TapNum': '', 'Reset': '', 'LDC_Z': '', 'rev_Z': '', 'Cogen': '', 'basefreq': '', 'enabled': '', 'like': ''}, ignore_index=True)

    return df_RegControl_DSS

def DIGS_Relay_DSS()->pd.DataFrame:
    '''
    :return: df_Relay_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Relay_DSS = pd.DataFrame(
        columns=['Id_Relay', 'MonitoredObj', 'MonitoredTerm', 'SwitchedObj', 'SwitchedTerm', 'type', 'Phasecurve',
                 'Groundcurve', 'PhaseTrip', 'GroundTrip', 'TDPhase', 'TDGround', 'PhaseInst', 'GroundInst ', 'Reset',
                 'Shots', 'RecloseIntervals', 'Delay', 'Overvoltcurve', 'Undervoltcurve', 'kvbase', '47%Pickup',
                 '46BaseAmps', '46%Pickup', '46isqt', 'Variable', 'overtrip', 'undertrip', 'Breakertime', 'action', 'Z1mag',
                 'Z1ang', 'Z0mag', 'Z0ang', 'Mphase', 'Mground', 'EventLog', 'DebugTrace', 'DistReverse', 'Normal', 'State',
                 'basefreq', 'enabled', 'like'])

    return df_Relay_DSS


def DIGS_StorageController_DSS()->pd.DataFrame:
    '''
    :return: df_StorageController_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_StorageController_DSS = pd.DataFrame(
        columns=['Id_StorageController', 'Element', 'Terminal', 'MonPhase', 'kWTarget', 'kWTargetLow', '%kWBand', 'kWBand',
                 '%kWBandLow', 'kWBandLow', 'ElementList', 'Weights', 'ModeDischarge', 'ModeCharge', 'TimeDischargeTrigger',
                 'TimeChargeTrigger', '%RatekW', '%RateCharge', '%Reserve', 'kWhTotal', 'kWTotal', 'kWhActual', 'kWActual',
                 'kWneed', 'Yearly', 'Daily', 'Duty', 'EventLog', 'InhibitTime', 'Tup', 'TFlat', 'Tdn', 'kWThreshold',
                 'DispFactor', 'ResetLevel', 'Seasons', 'SeasonTargets', 'SeasonTargetsLow', 'basefreq', 'enabled', 'like'])

    return df_StorageController_DSS

def DIGS_SwtControl_DSS()->pd.DataFrame:
    '''
    :return: df_SwtControlv_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_SwtControl_DSS = pd.DataFrame(
        columns=['Id_SwtControl', 'SwitchedObj', 'SwitchedTerm', 'Action', 'Lock', 'Delay', 'Normal', 'State', 'Reset',
                 'basefreq', 'enabled', 'like'])

    return df_SwtControl_DSS

def DIGS_UPFCControl_DSS()->pd.DataFrame:
    '''
    :return: df_UPFCControl_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_UPFCControl_DSS = pd.DataFrame(
        columns= ['Id_UPFCControl', 'Element', 'Terminal', 'kWLimit', 'kWBand', 'kvarlimit', 'GenList', 'basefreq',
                  'enabled', 'like'])

    return df_UPFCControl_DSS

def DIGS_CNData_DSS()->pd.DataFrame:
    '''
    :return: df_CNData_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_CNData_DSS = pd.DataFrame(
        columns=['Id_CNData', 'k', 'DiaStrand', 'GmrStrand', 'Rstrand', 'EpsR', 'InsLayer', 'DiaIns', 'DiaCable', 'Rdc',
                 'Rac', 'Runits', 'GMRac', 'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons',
                 'Ratings', 'Capradius', 'like'])

    return df_CNData_DSS


def DIGS_GrowthShape_DSS()->pd.DataFrame:
    '''
    :return: df_GrowthShape_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_GrowthShape_DSS = pd.DataFrame(
        columns= ['Id_GrowthShape', 'npts', 'year', 'mult', 'csvfile', 'sngfile', 'dblfile', 'like'])

    return df_GrowthShape_DSS

def DIGS_LoadShape_DSS()->pd.DataFrame:
    '''
    :return: df_LoadShape_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_LoadShape_DSS = pd.DataFrame(
        columns=['Id_LoadShape', 'npts', 'interval', 'mult', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile',
                 'action', 'qmult', 'UseActual', 'Pmax', 'Qmax', 'sinterval', 'minterval', 'Pbase', 'Qbase', 'Pmult',
                 'PQCSVFile', 'MemoryMapping', 'like'])

    return df_LoadShape_DSS

def DIGS_PriceShape_DSS()->pd.DataFrame:
    '''
    :return: df_PriceShape_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_PriceShape_DSS = pd.DataFrame(
        columns=['Id_PriceShape', 'npts', 'interval', 'price', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile',
                 'dblfile', 'sinterval', 'minterval', 'action', 'like'])

    return df_PriceShape_DSS

def DIGS_Spectrum_DSS()->pd.DataFrame:
    '''
    :return: df_Spectrum_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Spectrum_DSS = pd.DataFrame(
        columns=['Id_Spectrum', 'NumHarm', 'harmonic', '%mag', 'angle', 'CSVFile', 'like'])

    return df_Spectrum_DSS

def DIGS_TCC_Curve_DSS()->pd.DataFrame:
    '''
    :return: df_TCC_Curve_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_TCC_Curve_DSS = pd.DataFrame(
        columns=['Id_TCC_Curve', 'npts', 'C_array', 'T_array', 'like'])

    return df_TCC_Curve_DSS

def DIGS_TSData_DSS() -> pd.DataFrame:
    '''
    :return: df_TSData_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_TSData_DSS = pd.DataFrame(
        columns=['Id_TSData', 'DiaShield', 'TapeLayer', 'TapeLap', 'EpsR', 'InsLayer', 'DiaIns', 'DiaCable', 'Rdc',
                 'Rac', 'Runits', 'GMRac', 'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons',
                 'Ratings', 'Capradius', 'like'])

    return df_TSData_DSS

def DIGS_TShape_DSS() -> pd.DataFrame:
    '''
    :return: df_TShape_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_TShape_DSS = pd.DataFrame(
        columns=['Id_TShape', 'npts', 'interval', 'temp', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile',
                 'sinterval', 'minterval', 'action', 'like'])

    return df_TShape_DSS

def DIGS_XYcurve_DSS() -> pd.DataFrame:
    '''
    :return: df_XYcurve_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_XYcurve_DSS = pd.DataFrame(
        columns=['Id_XYcurve', 'npts', 'Points', 'Yarray', 'Xarray', 'csvfile', 'sngfile', 'dblfile', 'x', 'y',
                 'Xshift', 'Yshift', 'Xscale', 'Yscale', 'like'])

    return df_XYcurve_DSS

def DIGS_Fault_DSS() -> pd.DataFrame:
    '''
    :return: df_Fault_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Fault_DSS = pd.DataFrame(
        columns=['Id_Fault', 'bus1', 'bus2', 'phases', 'r', '%stddev', 'Gmatrix', 'ONtime', 'temporary', 'MinAmps',
                 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like'])

    return df_Fault_DSS

def DIGS_GICsource_DSS()->pd.DataFrame:
    '''
    :return: df_GICsource_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_GICsource_DSS = pd.DataFrame(
        columns=['Id_GICsource', 'Volts', 'angle', 'frequency', 'phases', 'EN', 'EE', 'Lat1', 'Lon1', 'Lat2', 'Lon2',
                  'spectrum', 'basefreq', 'enabled', 'like'])

    return df_GICsource_DSS

def DIGS_Isource_DSS()->pd.DataFrame:
    '''
    :return: df_Isouce_DSS
    '''
    'DataFrame creation with OpenDSS keywords'
    df_Isouce_DSS = pd.DataFrame(
        columns=['Id_Isource', 'bus1', 'amps', 'angle', 'frequency', 'phases', 'scantype', 'sequence', 'Yearly',
                 'Daily', 'Duty', 'Bus2', 'spectrum', 'basefreq', 'enabled', 'like'])

    return df_Isouce_DSS

