# -*- coding: utf-8 -*-
# @Time    : 8/23/2022 3:41 PM
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : create_file_xlsx.py
# @Software: PyCharm

import logging
import pandas as pd

from ...interface_dss import dss, drt
from ...helper_functions import _save_BBDD_xlsx
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Other_elem_DSS import Other_MTY, Other_Def_Value, Other_ORD
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.General_elem_DSS import General_MTY, General_Def_Value, General_ORD
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.PD_elem_DSS import PD_elements_MTY, PD_elem_Def_Value, PD_elements_ORD
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.PC_elem_DSS import PC_elements_MTY, PC_elem_Def_Value, PC_elements_ORD
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Controls_elem_DSS import Controls_MTY, Controls_Def_Value, Controls_ORD
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Meters_elem_DSS import Meters_MTY, Meters_Def_Value, Meters_ORD
from openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs.Voltagebases_DSS import Voltagebases_DSS

from openpy_fx_tools_dss.logg_print_alert import logg_alert

log_py = logging.getLogger(__name__)

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

    BBDD_OpenDSS = _check_DSS_default_values(BBDD_OpenDSS=BBDD_OpenDSS)

    xlsx_name_DSS = f'BBDD_DSS_{prj_name}.xlsx'
    _save_BBDD_xlsx(workbook_DSS=xlsx_name_DSS,
                    elements_OpenDSS=DSS_elem_list,
                    BBDD_OpenDSS=BBDD_OpenDSS,
                    out_path=path_save)

    logg_alert.update_logg_file(f'Created and saved the {xlsx_name_DSS} file in the path:\n{path_save}', 2, log_py)


def _check_DSS_default_values(BBDD_OpenDSS: dict):

    for ClassName in BBDD_OpenDSS.keys():

        if len([x for x in [ClassName] if x in list_General_DSS]) == 1:
            BBDD_OpenDSS[ClassName] = General_Def_Value(DF_elem_DSS=BBDD_OpenDSS[ClassName], name_class=ClassName)

        if len([x for x in [ClassName] if x in list_Other_DSS]) == 1:
            BBDD_OpenDSS[ClassName] = Other_Def_Value(DF_elem_DSS=BBDD_OpenDSS[ClassName], name_class=ClassName)

        if len([x for x in [ClassName] if x in list_PD_elements_DSS]) == 1:
            BBDD_OpenDSS[ClassName] = PD_elem_Def_Value(DF_elem_DSS=BBDD_OpenDSS[ClassName], name_class=ClassName)

        if len([x for x in [ClassName] if x in list_PC_elements_DSS]) == 1:
            BBDD_OpenDSS[ClassName] = PC_elem_Def_Value(DF_elem_DSS=BBDD_OpenDSS[ClassName], name_class=ClassName)

        if len([x for x in [ClassName] if x in list_Controls_DSS]) == 1:
            BBDD_OpenDSS[ClassName] = Controls_Def_Value(DF_elem_DSS=BBDD_OpenDSS[ClassName], name_class=ClassName)

        if len([x for x in [ClassName] if x in list_Meters_DSS]) == 1:
            BBDD_OpenDSS[ClassName] = Meters_Def_Value(DF_elem_DSS=BBDD_OpenDSS[ClassName], name_class=ClassName)

    return BBDD_OpenDSS



def ClassName_to_DataFrame_inter(ClassName: str, transform_string=None, clean_data=None):
    data = dict()

    if transform_string is None:
        transform_string = _evaluate_expression

    if clean_data is None:
        clean_data = _clean_data

    dss.circuit_set_active_class(ClassName)
    for element in dss.active_class_all_names():
        name = "{element}".format(element=element)
        name_elem = ClassName+'.'+element
        dss.circuit_set_active_element(name_elem)

        data[name] = dict()

        for i, n in enumerate(dss.cktelement_all_property_names()):
            # use 1-based index for compatibility with previous versions
            PropertyName = dss.cktelement_all_property_names()[i]
            if PropertyName == 'WdgCurrents':
                string = ''
            else:
                string = dss.dssproperties_read_value(str(i + 1))
            string = transform_string(string)
            if type(string) == list:
                string = str(string).replace("'", "")
                if string == "[]":
                    string = ""

            if type(string) == tuple:
                string = str(list(string)).replace("'", "")
                if string == "[]":
                    string = ""


            if PropertyName == 'bus1':
                string = str(string)
            if PropertyName == 'bus2':
                string = str(string)

            data[name][n] = string

    data = clean_data(data, ClassName)
    df_class = pd.DataFrame(pd.DataFrame(data).T).reset_index().rename(columns={'index': f'Id_{ClassName}'})

    return df_class


def ClassName_to_DataFrame(ClassName: str, transform_string=None, clean_data=None):

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

        if ClassName == 'Transformer':
            print('here')

        for i, n in enumerate(drt.Element.AllPropertyNames()):
            # use 1-based index for compatibility with previous versions
            PropertyName = drt.Element.AllPropertyNames()[i]

            if PropertyName == 'WdgCurrents':
                string = ''
            else:
                string = drt.Properties.Value(str(i + 1))
            string = transform_string(string)
            if type(string) == list:
                string = str(string).replace("'", "")
                if string == "[]":
                    string = ""

                """
                if "[" in string and "]" in string and " " in string:
                    pass
                else:
                    string = str(string).replace("[", "")
                    string = str(string).replace("]", "")
                """
            if type(string) == tuple:
                string = str(list(string)).replace("'", "")
                if string == "[]":
                    string = ""

            if PropertyName == 'bus1':
                string = str(string)
            if PropertyName == 'bus2':
                string = str(string)

            data[name][n] = string



    data = clean_data(data, ClassName)
    df_class = pd.DataFrame(pd.DataFrame(data).T).reset_index().rename(columns={'index': f'Id_{ClassName}'})

    return df_class



def _Add_BBDD_list_DSS(BBDD_OpenDSS: dict, DSS_elem_list: list, ClassName: str, dict_class: dict):

    elem_no_drt = ['WindGen', 'Generic5', 'FMonitor']
    PC_elem_no_drt = ['WindGen', 'Generic5']

    if len([x for x in [ClassName] if x in elem_no_drt]) == 1:
        dss.circuit_set_active_class(ClassName)
        if len([x for x in [ClassName] if x in PC_elem_no_drt]) == 1:
            BBDD_OpenDSS, DSS_elem_list = PC_elements_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                          DSS_elem_list=DSS_elem_list,
                                                          name_class=ClassName)
            list_PC_elements.append(ClassName)
            dict_class['PC_elem'] += 1

        if ClassName == 'FMonitor':
            BBDD_OpenDSS, DSS_elem_list = Meters_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                     DSS_elem_list=DSS_elem_list,
                                                     name_class=ClassName)
            list_Meters.append(ClassName)
            dict_class['Meters'] += 1

    else:
        #df_class_2 = ClassName_to_DataFrame_inter(ClassName)
        df_class = ClassName_to_DataFrame(ClassName)
        if len([x for x in [ClassName] if x in list_General_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = General_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                          DSS_elem_list=DSS_elem_list,
                                                          name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = General_ORD(DF_elem_DSS=df_class, name_class=ClassName)
                DSS_elem_list.append(ClassName)

            list_General.append(ClassName)
            dict_class['General'] += 1

        if len([x for x in [ClassName] if x in list_Other_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = Other_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                        DSS_elem_list=DSS_elem_list,
                                                        name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = Other_ORD(DF_elem_DSS=df_class, name_class=ClassName)
                DSS_elem_list.append(ClassName)

            list_Other.append(ClassName)
            dict_class['Other'] += 1

        if len([x for x in [ClassName] if x in list_PD_elements_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = PD_elements_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                              DSS_elem_list=DSS_elem_list,
                                                              name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = PD_elements_ORD(DF_elem_DSS=df_class, name_class=ClassName)
                DSS_elem_list.append(ClassName)

            list_PD_elements.append(ClassName)
            dict_class['PD_elem'] += 1

        if len([x for x in [ClassName] if x in list_PC_elements_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = PC_elements_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                              DSS_elem_list=DSS_elem_list,
                                                              name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = PC_elements_ORD(DF_elem_DSS=df_class, name_class=ClassName)
                DSS_elem_list.append(ClassName)

            list_PC_elements.append(ClassName)
            dict_class['PC_elem'] += 1

        if len([x for x in [ClassName] if x in list_Controls_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = Controls_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                           DSS_elem_list=DSS_elem_list,
                                                           name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = Controls_ORD(DF_elem_DSS=df_class, name_class=ClassName)
                DSS_elem_list.append(ClassName)

            list_Controls.append(ClassName)
            dict_class['Controls'] += 1

        if len([x for x in [ClassName] if x in list_Meters_DSS]) == 1:
            if df_class.empty:
                BBDD_OpenDSS, DSS_elem_list = Meters_MTY(BBDD_elem_DSS=BBDD_OpenDSS,
                                                         DSS_elem_list=DSS_elem_list,
                                                         name_class=ClassName)
            else:
                BBDD_OpenDSS[ClassName] = Meters_ORD(DF_elem_DSS=df_class, name_class=ClassName)
                DSS_elem_list.append(ClassName)

            list_Meters.append(ClassName)
            dict_class['Meters'] += 1

        BBDD_OpenDSS['Voltagebases'] = Voltagebases_DSS()
        DSS_elem_list.append('Voltagebases')

    return BBDD_OpenDSS, DSS_elem_list, dict_class

def _evaluate_expression(string):

    list_except = ['none', '----', 'No', 'oh', '', '0', "-1", "shell"]
    list_units = ['mi', 'kft', 'km', 'm', 'Ft', 'in', 'cm']

    if "[" in string and "]" in string:
        str_mdf = [
            _evaluate_expression(x.strip())
            for x in string.replace("[", "").replace("]", "").split(",")
            if x.strip() != ""
        ]
        return str_mdf

    elif len([x for x in [string] if x in list_except]) == 1:
        str_mdf = ''
        return str_mdf

    elif len([x for x in [string] if x in list_units]) == 1:
        return string


    elif string.startswith("(") and string.endswith(")"):
        str_mdf = tuple(
            _evaluate_expression(x.strip())
            for x in string.replace("(", "").replace(")", "").split(",")
            if x.strip() != ""
        )
        return str_mdf

    elif string.lower() == "true":
        return True

    elif string.lower() == "false":
        return False

    elif "|" in string:
        return string


    elif string.startswith("'") and string.endswith("'"):
        print('here')


    elif type(string) == list:
        return string

    else:
        try:
            string = float(string)
            return string
        except ValueError:
            return string

def _clean_data(data, class_name):
    for element in drt.ActiveClass.AllNames():
        name = "{element}".format(element=element)
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

        if class_name == 'Vsource':
            pass
        else:
            list_AllPropertyNames = drt.Element.AllPropertyNames()
            ph_aux = ['nphases', 'phases']

            for k in ph_aux:
                if len([x for x in [k] if x in list_AllPropertyNames]) == 1:
                    if 'bus1' in drt.Element.AllPropertyNames():
                        pos = data[name]['bus1'].find('.')
                        ph_1 = data[name]['bus1'][pos:]
                        if ph_1.find('0') == -1:
                            pass
                        else:
                            if int(data[name][k]) == 3:
                                data[name]["bus1"] = data[name]["bus1"][:pos] + '.1.2.3' + ph_1


                    if 'bus2' in drt.Element.AllPropertyNames():
                        pos = data[name]['bus2'].find('.')
                        ph_2 = data[name]['bus2'][pos:]
                        if ph_2.find('0') == -1:
                            pass
                        else:
                            if int(data[name][k]) == 3:
                                data[name]["bus2"] = data[name]["bus2"][:pos] + '.1.2.3' + ph_2

                    if 'conns' in drt.Element.AllPropertyNames():
                        pos = data[name]['buses']
                        aux1 = pos.find('[')
                        aux2 = pos.find(',')
                        aux3 = pos.find(']')

                        list_buses = [pos[aux1 + 1:aux2], pos[aux2 + 1:aux3]]

                        list_nbus = list()

                        for bus in list_buses:
                            pos = bus.find('.')
                            ph_1 = bus[pos:]
                            if ph_1.find('0') == -1:
                                list_nbus.append(bus)
                            else:
                                if int(data[name]['phases']) == 3:
                                    list_nbus.append(bus[:pos] + '.1.2.3' + ph_1)

                        data[name]['buses'] = f'[{list_nbus[0]}, {list_nbus[1]}]'




    return data