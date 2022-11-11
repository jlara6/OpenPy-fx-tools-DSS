# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:41 PM
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : create_file_xlsx.py
# @Software: PyCharm
import pandas as pd

from ...interface_dss import dss, drt
from ...helper_functions import _save_BBDD_xlsx
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Other_elements_DSS import Other_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.General_elements_DSS import General_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.PD_elements_DSS import PD_elements_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.PC_elements_DSS import PC_elements_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Controls_elements_DSS import Controls_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Meters_elements_DSS import Meters_DSS

list_General_DSS = ['WireData', 'LineSpacing', 'LineGeometry', 'LineCode', 'XfmrCode', 'CNData', 'GrowthShape',
                    'LoadShape', 'PriceShape', 'Spectrum', 'TCC_Curve', 'TSData', 'TShape', 'XYcurve']

list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']

list_PD_elements_DSS = ['Transformer', 'Line', 'Capacitor', 'AutoTrans', 'GICTransformer', 'Reactor']

list_PC_elements_DSS = ['Generator', 'Generic5', 'GICLine', 'IndMach012', 'Load', 'PVSystem', 'Storage', 'UPFC', 'VCCS',
                        'VSConverter', 'WindGen']

list_Controls_DSS = ['CapControl', 'ESPVLControl', 'ExpControl', 'Fuse', 'GenDispatcher', 'InvControl', 'Recloser',
                     'RegControl', 'Relay', 'StorageController', 'SwtControl', 'UPFCControl']

list_Meters_DSS = ['EnergyMeter', 'FMonitor', 'Monitor', 'Sensor']

list_General = list()
list_Other = list()
list_PD_elements = list()
list_PC_elements = list()
list_Controls = list()
list_Meters = list()

def _Create_DSS_to_xlsx_files(DSS_file: str, path_save: str, prj_name: str):
    n_elem_dss = {
        "General": len(list_General_DSS), "Other": len(list_Other_DSS), "PD_elem": len(list_PD_elements_DSS),
        "PC_elem": len(list_PC_elements_DSS), "Controls": len(list_Controls_DSS), "Meters": len(list_Meters_DSS)}


    n_elem_add = {"General": 0, "Other": 0, "PD_elem": 0, "PC_elem": 0, "Controls": 0, "Meters": 0}

    DSS_elem_list = list()
    BBDD_OpenDSS = dict()
    list_no_class = list()

    dss.text("ClearAll")
    dss.text(f"compile [{DSS_file}]")


    drt.run_command(f"compile [{DSS_file}]")
    drt.ActiveClass.First()

    list_no = ['Solution']
    for ClassName in dss.dss_classes():
        if len([x for x in [ClassName] if x in list_no]) != 1:
            BBDD_OpenDSS, DSS_elem_list, n_elem_add = _Add_BBDD_list_DSS(
                BBDD_OpenDSS=BBDD_OpenDSS,
                DSS_elem_list=DSS_elem_list,
                ClassName=ClassName,
                dict_class=n_elem_add)
        else:
            pass

    workbook_DSS = f'BBDD_DSS_{prj_name}.xlsx'
    _save_BBDD_xlsx(workbook_DSS=workbook_DSS,
                    elements_OpenDSS=DSS_elem_list,
                    BBDD_OpenDSS=BBDD_OpenDSS,
                    out_path=path_save)






def _class_to_DataFrame(ClassName: str, transform_string=None, clean_data=None):

    if transform_string is None:
        transform_string = _evaluate_expression

    if clean_data is None:
        clean_data = _clean_data


    data = dict()
    drt.Circuit.SetActiveClass("{class_name}".format(class_name=ClassName))
    for element in drt.ActiveClass.AllNames():
        name = "{element}".format(element=element)
        drt.ActiveClass.Name(element)

        data[name] = dict()
        for i, n in enumerate(drt.Element.AllPropertyNames()):
            # use 1-based index for compatibility with previous versions
            string = drt.Properties.Value(str(i + 1))

            data[name][n] = transform_string(string)

    data = clean_data(data, ClassName)
    df_class = pd.DataFrame(pd.DataFrame(data).T).reset_index().rename(columns={'index': f'Id_{ClassName}'})

    return df_class

    #df_class = drt.utils.class_to_dataframe(ClassName)

    #BBDD_OpenDSS[ClassName] = df_class
    #DSS_elem_list.append(ClassName)

    #return BBDD_OpenDSS, DSS_elem_list


def _Add_BBDD_list_DSS(BBDD_OpenDSS: dict, DSS_elem_list: list, ClassName: str, dict_class: dict):

    elem_no_drt = ['WindGen', 'Generic5', 'FMonitor']
    PC_elem_no_drt = ['WindGen', 'Generic5']

    if len([x for x in [ClassName] if x in elem_no_drt]) == 1:
        dss.circuit_set_active_class(ClassName)
        if len([x for x in [ClassName] if x in PC_elem_no_drt]) == 1:
            BBDD_OpenDSS, DSS_elem_list = PC_elements_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                          DSS_elem_list=DSS_elem_list,
                                                          name_class=ClassName)
            list_PC_elements.append(ClassName)
            dict_class['PC_elem'] += 1

        if ClassName == 'FMonitor':
            BBDD_OpenDSS, DSS_elem_list = Meters_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                     DSS_elem_list=DSS_elem_list,
                                                     name_class=ClassName)
            list_Meters.append(ClassName)
            dict_class['Meters'] += 1

    else:
        df_class = _class_to_DataFrame(ClassName)
        if len([x for x in [ClassName] if x in list_General_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = General_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                          DSS_elem_list=DSS_elem_list,
                                                          name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = df_class
                DSS_elem_list.append(ClassName)

            list_General.append(ClassName)
            dict_class['General'] += 1

        if len([x for x in [ClassName] if x in list_Other_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = Other_DSS(BBDD_DSS=BBDD_OpenDSS,
                                                        DSS_elem_list=DSS_elem_list,
                                                        name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = df_class
                DSS_elem_list.append(ClassName)

            list_Other.append(ClassName)
            dict_class['Other'] += 1

        if len([x for x in [ClassName] if x in list_PD_elements_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = PD_elements_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                              DSS_elem_list=DSS_elem_list,
                                                              name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = df_class
                DSS_elem_list.append(ClassName)

            list_PD_elements.append(ClassName)
            dict_class['PD_elem'] += 1

        if len([x for x in [ClassName] if x in list_PC_elements_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = PC_elements_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                              DSS_elem_list=DSS_elem_list,
                                                              name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = df_class
                DSS_elem_list.append(ClassName)

            list_PC_elements.append(ClassName)
            dict_class['PC_elem'] += 1

        if len([x for x in [ClassName] if x in list_Controls_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = Controls_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                           DSS_elem_list=DSS_elem_list,
                                                           name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = df_class
                DSS_elem_list.append(ClassName)

            list_Controls.append(ClassName)
            dict_class['Controls'] += 1

        if len([x for x in [ClassName] if x in list_Meters_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = Meters_DSS(BBDD_elem_DSS=BBDD_OpenDSS,
                                                         DSS_elem_list=DSS_elem_list,
                                                         name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = df_class
                DSS_elem_list.append(ClassName)

            list_Meters.append(ClassName)
            dict_class['Meters'] += 1

    return BBDD_OpenDSS, DSS_elem_list, dict_class

def _evaluate_expression(string):

    if "[" in string and "]" in string:
        e = [
            _evaluate_expression(x.strip())
            for x in string.replace("[", "").replace("]", "").split(",")
            if x.strip() != ""
        ]

        return e

    elif string.startswith("(") and string.endswith(")"):
        e = tuple(
            _evaluate_expression(x.strip())
            for x in string.replace("(", "").replace(")", "").split(",")
            if x.strip() != ""
        )
        return e

    elif string.lower() == "true":
        return True

    elif string.lower() == "false":
        return False

    else:
        return string

def _clean_data(data, class_name):
    for element in drt.ActiveClass.AllNames():
        name = "{class_name}.{element}".format(class_name=class_name, element=element)
        drt.ActiveClass.Name(element)

        if "nconds" in drt.Element.AllPropertyNames():
            nconds = int(data[name]["nconds"])
            x = []
            h = []
            units = []

            for cond in range(1, nconds + 1):
                drt.run_command("{name}.cond={cond}".format(name=name, cond=cond))
                x.append(float(drt.run_command("? {name}.x".format(name=name))))
                h.append(float(drt.run_command("? {name}.h".format(name=name))))
                units.append(drt.run_command("? {name}.units".format(name=name)))

            data[name]["x"] = x
            data[name]["h"] = h
            data[name]["units"] = units

    return data