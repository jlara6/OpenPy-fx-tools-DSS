# -*- coding: utf-8 -*-
# @Time    : 18/05/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Vsource_DSS import DIGS_Vsource_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Rest_of_element_DSS import \
    DIGS_Fault_DSS, DIGS_GICsource_DSS, DIGS_Isource_DSS

def Other_elements_DSS(dict_df_DigS: dict, BBDD_OpenDSS: dict, OpenDSS_element_list: list):

    # from Vsource_DSS
    BBDD_OpenDSS['Vsource'] = DIGS_Vsource_DSS(DataFrame_ElmXnet=dict_df_DigS['ElmXnet'],
                                               DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                               DataFrame_StaCubic=dict_df_DigS['StaCubic'])
    OpenDSS_element_list.append('Vsource')

    # from Rest_of_element_DSS
    BBDD_OpenDSS['Fault'] = DIGS_Fault_DSS()
    OpenDSS_element_list.append('Fault')

    BBDD_OpenDSS['GICsource'] = DIGS_GICsource_DSS()
    OpenDSS_element_list.append('GICsource')

    BBDD_OpenDSS['Isource'] = DIGS_Isource_DSS()
    OpenDSS_element_list.append('Isource')

    return BBDD_OpenDSS, OpenDSS_element_list