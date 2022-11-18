# -*- coding: utf-8 -*-
# @Time    : 18/05/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Rest_of_element_DSS import \
    DIGS_CapControl_DSS, DIGS_ESPVLControl_DSS, DIGS_ExpControl_DSS, DIGS_Fuse_DSS, DIGS_GenDispatcher_DSS, \
    DIGS_InvControl_DSS, DIGS_Recloser_DSS, DIGS_RegControl_DSS, DIGS_Relay_DSS, DIGS_StorageController_DSS, \
    DIGS_UPFCControl_DSS, DIGS_SwtControl_DSS


def Controls_elements_DSS(dict_df_DigS: dict, BBDD_OpenDSS: dict, OpenDSS_element_list: list):

    BBDD_OpenDSS['CapControl'] = DIGS_CapControl_DSS()
    OpenDSS_element_list.append('CapControl')

    BBDD_OpenDSS['ESPVLControl'] = DIGS_ESPVLControl_DSS()
    OpenDSS_element_list.append('ESPVLControl')

    BBDD_OpenDSS['ExpControl'] = DIGS_ExpControl_DSS()
    OpenDSS_element_list.append('ExpControl')

    BBDD_OpenDSS['Fuse'] = DIGS_Fuse_DSS()
    OpenDSS_element_list.append('Fuse')

    BBDD_OpenDSS['GenDispatcher'] = DIGS_GenDispatcher_DSS()
    OpenDSS_element_list.append('GenDispatcher')

    BBDD_OpenDSS['InvControl'] = DIGS_InvControl_DSS()
    OpenDSS_element_list.append('InvControl')

    BBDD_OpenDSS['Recloser'] = DIGS_Recloser_DSS()
    OpenDSS_element_list.append('Recloser')

    BBDD_OpenDSS['RegControl'] = DIGS_RegControl_DSS(DataFrame_ElmTr2=dict_df_DigS['ElmTr2'])
    OpenDSS_element_list.append('RegControl')

    BBDD_OpenDSS['Relay'] = DIGS_Relay_DSS()
    OpenDSS_element_list.append('Relay')

    BBDD_OpenDSS['StorageController'] = DIGS_StorageController_DSS()
    OpenDSS_element_list.append('StorageController')

    BBDD_OpenDSS['SwtControl'] = DIGS_SwtControl_DSS()
    OpenDSS_element_list.append('SwtControl')

    BBDD_OpenDSS['UPFCControl'] = DIGS_UPFCControl_DSS()
    OpenDSS_element_list.append('UPFCControl')

    return BBDD_OpenDSS, OpenDSS_element_list