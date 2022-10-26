# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:41 PM
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : create_file_xlsx.py
# @Software: PyCharm

import py_dss_interface
from helper_functions import save_BBDD_xlsx
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx_mod.Types_elem_DSS_to_xlxs.Other_elements_DSS import Other_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx_mod.Types_elem_DSS_to_xlxs.General_elements_DSS import General_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx_mod.Types_elem_DSS_to_xlxs.PD_elements_DSS import PD_elements_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx_mod.Types_elem_DSS_to_xlxs.PC_elements_DSS import PC_elements_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx_mod.Types_elem_DSS_to_xlxs.Controls_elements_DSS import Controls_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx_mod.Types_elem_DSS_to_xlxs.Meters_elements_DSS import Meters_DSS

dss = py_dss_interface.DSSDLL()


def Create_DSS_to_xlsx_files(DSS_file: str, out_path: str, project_name: str ='default'):

    dss.text("ClearAll")
    dss.text(f"compile [{DSS_file}]")

    OpenDSS_element_list = list()
    BBDD_OpenDSS = dict()

    list_class = dss.dss_classes()

    list_Other = list()
    list_General = list()
    list_PD_elements = list()
    list_PC_elements = list()
    list_Controls = list()
    list_Meters = list()

    list_no_class = list()

    list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']
    list_General_DSS = ['WireData', 'LineSpacing', 'LineGeometry', 'LineCode', 'XfmrCode', 'CNData', 'GrowthShape',
                        'LoadShape', 'PriceShape', 'Spectrum', 'TCC_Curve', 'TSData', 'TShape', 'XYcurve']
    list_PD_elements_DSS = ['Transformer', 'Line', 'Switch', 'Capacitor', 'AutoTrans', 'GICTransformer', 'Reactor']
    list_PC_elements_DSS = ['Load', 'Generator', 'Generic5', 'GICLine', 'IndMach012', 'PVSystem', 'UPFC', 'VCCS',
                            'Storage', 'VSConverter', 'WindGen']
    list_Controls_DSS = ['CapControl', 'ESPVLControl', 'ExpControl', 'Fuse', 'GenDispatcher', 'InvControl', 'Recloser',
                         'RegControl', 'Relay', 'StorageController', 'SwtControl', 'UPFCControl']
    list_Meters_DSS = ['EnergyMeter', 'FMonitor', 'Monitor', 'Sensor']

    for name_class in list_class:
        nclss = name_class
        dss.circuit_set_active_class(name_class)
        if len([x for x in [name_class] if x in list_Other_DSS]) == 1:
            BBDD_OpenDSS, OpenDSS_element_list = Other_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                           DSS_elem_list=OpenDSS_element_list,
                                                           name_class=name_class)
            list_Other.append(name_class)
        elif len([x for x in [name_class] if x in list_General_DSS]) == 1:
            BBDD_OpenDSS, OpenDSS_element_list = General_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                             DSS_elem_list=OpenDSS_element_list,
                                                             name_class=name_class)
            list_General.append(name_class)
        elif len([x for x in [name_class] if x in list_PD_elements_DSS]) == 1:
            BBDD_OpenDSS, OpenDSS_element_list = PD_elements_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                                 DSS_elem_list=OpenDSS_element_list,
                                                                 name_class=name_class)
            list_PD_elements.append(name_class)
        elif len([x for x in [name_class] if x in list_PC_elements_DSS]) == 1:
            BBDD_OpenDSS, OpenDSS_element_list = PC_elements_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                                 DSS_elem_list=OpenDSS_element_list,
                                                                 name_class=name_class)
            list_PC_elements.append(name_class)
        elif len([x for x in [name_class] if x in list_Controls_DSS]) == 1:
            BBDD_OpenDSS, OpenDSS_element_list = Controls_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                              DSS_elem_list=OpenDSS_element_list,
                                                              name_class=name_class)
            list_Controls.append(name_class)
        elif len([x for x in [name_class] if x in list_Meters_DSS]) == 1:
            BBDD_OpenDSS, OpenDSS_element_list = Meters_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                            DSS_elem_list=OpenDSS_element_list,
                                                            name_class=name_class)
            list_Meters.append(name_class)
        else:
            list_no_class.append(name_class)

    workbook_DSS = f'BBDD_DSS_{project_name}.xlsx'
    save_BBDD_xlsx(workbook_DSS=workbook_DSS,
                   elements_OpenDSS=OpenDSS_element_list,
                   BBDD_OpenDSS=BBDD_OpenDSS,
                   out_path=out_path)

    print('here')







