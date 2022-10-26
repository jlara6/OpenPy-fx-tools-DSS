# -*- coding: utf-8 -*-
# @Time    : 18/05/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from Types_elem_DIGS_to_DSS.DigS_to_OpenDSS_elem.Load_DSS import DIGS_load_DSS
from Types_elem_DIGS_to_DSS.DigS_to_OpenDSS_elem.Rest_of_element_DSS import DIGS_Generator_DSS, DIGS_Generic5_DSS, DIGS_GICLine_DSS, \
    DIGS_IndMach012_DSS, DIGS_PVSystem_DSS, DIGS_Storage_DSS, DIGS_UPFC_DSS, DIGS_VCCS_DSS, DIGS_WindGen_DSS, DIGS_VSConverter_DSS


def PC_elements_DSS(dict_df_DigS:dict, BBDD_OpenDSS:dict, OpenDSS_element_list:list):

    # from Load_DSS.py
    BBDD_OpenDSS['Load'] = DIGS_load_DSS(DataFrame_ElmLod=dict_df_DigS['ElmLod'],
                                         DataFrame_TypLod=dict_df_DigS['TypLod'],
                                         DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                         DataFrame_StaCubic=dict_df_DigS['StaCubic'])
    OpenDSS_element_list.append('Load')

    # From Rest_of_element_DSS.py
    BBDD_OpenDSS['Generator'] = DIGS_Generator_DSS()
    OpenDSS_element_list.append('Generator')

    BBDD_OpenDSS['Generic5'] = DIGS_Generic5_DSS()
    OpenDSS_element_list.append('Generic5')

    BBDD_OpenDSS['GICLine'] = DIGS_GICLine_DSS()
    OpenDSS_element_list.append('GICLine')

    BBDD_OpenDSS['IndMach012'] = DIGS_IndMach012_DSS()
    OpenDSS_element_list.append('IndMach012')

    BBDD_OpenDSS['PVSystem'] = DIGS_PVSystem_DSS()
    OpenDSS_element_list.append('PVSystem')

    BBDD_OpenDSS['UPFC'] = DIGS_UPFC_DSS()
    OpenDSS_element_list.append('UPFC')

    BBDD_OpenDSS['VCCS'] = DIGS_VCCS_DSS()
    OpenDSS_element_list.append('VCCS')

    BBDD_OpenDSS['Storage'] = DIGS_Storage_DSS()
    OpenDSS_element_list.append('Storage')

    BBDD_OpenDSS['VSConverter'] = DIGS_VSConverter_DSS()
    OpenDSS_element_list.append('VSConverter')

    BBDD_OpenDSS['WindGen'] = DIGS_WindGen_DSS()
    OpenDSS_element_list.append('WindGen')

    return BBDD_OpenDSS, OpenDSS_element_list