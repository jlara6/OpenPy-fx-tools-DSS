# -*- coding: utf-8 -*-
# @Time    : 11/11/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : NameClass_columns.py
# @Software: PyCharm


list_General_DSS = ['WireData', 'LineSpacing', 'LineGeometry', 'LineCode', 'XfmrCode', 'CNData', 'GrowthShape',
                    'LoadShape', 'PriceShape', 'Spectrum', 'TCC_Curve', 'TSData', 'TShape', 'XYcurve']

dict_General = dict()
dict_General['LineCode'] = [
    'nphases', 'r1', 'x1', 'r0', 'x0', 'C1', 'C0', 'units', 'rmatrix', 'xmatrix', 'cmatrix', 'baseFreq', 'normamps',
    'emergamps', 'faultrate', 'pctperm', 'repair', 'Kron', 'Rg', 'Xg', 'rho', 'neutral', 'B1', 'B0', 'Seasons',
    'Ratings', 'LineType', 'like']
dict_General['LoadShape'] = [
    'npts', 'interval', 'mult', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile', 'action', 'qmult',
    'UseActual', 'Pmax', 'Qmax', 'sinterval', 'minterval', 'Pbase', 'Qbase', 'Pmult', 'PQCSVFile', 'MemoryMapping',
    'like']
dict_General['TShape'] = [
    'npts', 'interval', 'temp', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile', 'sinterval', 'minterval',
    'action', 'like']
dict_General['PriceShape'] = [
    'npts', 'interval', 'price', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile', 'sinterval', 'minterval',
    'action', 'like']
dict_General['XYcurve'] = ['npts', 'Points', 'Yarray', 'Xarray', 'csvfile', 'sngfile', 'dblfile', 'x', 'y', 'Xshift',
                           'Yshift', 'Xscale', 'Yscale', 'like']
dict_General['GrowthShape'] = ['npts', 'year', 'mult', 'csvfile', 'sngfile', 'dblfile', 'like']
dict_General['TCC_Curve'] = ['npts', 'C_array', 'T_array', 'like']
dict_General['Spectrum'] = ['NumHarm', 'harmonic', '%mag', 'angle', 'CSVFile', 'like']
dict_General['WireData'] = ['Rdc', 'Rac', 'Runits', 'GMRac', 'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps',
                            'diam', 'Seasons', 'Ratings', 'Capradius', 'like']
dict_General['CNData'] = [
    'k', 'DiaStrand', 'GmrStrand', 'Rstrand', 'EpsR', 'InsLayer', 'DiaIns', 'DiaCable', 'Rdc', 'Rac', 'Runits', 'GMRac',
    'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons', 'Ratings', 'Capradius', 'like']
dict_General['TSData'] = [
    'DiaShield', 'TapeLayer', 'TapeLap', 'EpsR', 'InsLayer', 'DiaIns', 'DiaCable', 'Rdc', 'Rac', 'Runits', 'GMRac',
    'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons', 'Ratings', 'Capradius', 'like']
dict_General['LineGeometry'] = [
    'nconds', 'nphases', 'cond', 'wire', 'x', 'h', 'units', 'normamps', 'emergamps', 'reduce', 'spacing', 'wires',
    'cncable', 'tscable', 'cncables', 'tscables', 'Seasons', 'Ratings', 'LineType', 'like']
dict_General['LineSpacing'] = ['nconds', 'nphases', 'x', 'h', 'units', 'like']
dict_General['XfmrCode'] = [
    'phases', 'windings', 'wdg', 'conn', 'kV', 'kVA', 'tap', '%R', 'Rneut', 'Xneut', 'conns', 'kVs', 'kVAs', 'taps',
    'Xhl', 'Xht', 'Xlt', 'Xscarray', 'thermal', 'n', 'm', 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normhkVA',
    'emerghkVA', 'MaxTap', 'MinTap', 'NumTaps', '%imag', 'ppm_antifloat', '%Rs', 'X12', 'X13', 'X23', 'RdcOhms',
    'Seasons', 'Ratings', 'like']


list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']
dict_Other = dict()

dict_Other['Vsource'] = [
    'bus1', 'basekv', 'pu', 'angle', 'frequency', 'phases', 'MVAsc3', 'MVAsc1', 'x1r1', 'x0r0', 'Isc3', 'Isc1', 'R1',
    'X1', 'R0', 'X0', 'ScanType', 'Sequence', 'bus2', 'Z1', 'Z0', 'Z2', 'puZ1', 'puZ0', 'puZ2', 'baseMVA', 'Yearly',
    'Daily', 'Duty', 'Model', 'puZideal', 'spectrum', 'basefreq', 'enabled', 'like']
dict_Other['Fault'] = [
    'bus1', 'bus2', 'phases', 'r', '%stddev', 'Gmatrix', 'ONtime', 'temporary', 'MinAmps', 'normamps', 'emergamps',
    'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like']
dict_Other['GICsource'] = [
    'Description', 'Volts', 'angle', 'frequency', 'phases', 'EN', 'EE', 'Lat1', 'Lon1', 'Lat2', 'Lon2', 'spectrum',
    'basefreq', 'enabled', 'like']
dict_Other['Isource'] = [
    'bus1', 'amps', 'angle', 'frequency', 'phases', 'scantype', 'sequence', 'Yearly', 'Daily', 'Duty', 'Bus2',
    'spectrum', 'basefreq', 'enabled', 'like']



