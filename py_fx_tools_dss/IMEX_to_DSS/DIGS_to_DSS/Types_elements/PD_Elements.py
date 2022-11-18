# -*- coding: utf-8 -*-
# @Time    : 18/05/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Line_DSS import DIGS_line_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Trafo_DSS import DIGS_trafo_DSS, DIGS_trafo_conn_group_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Switch_DSS import DIGS_switch_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Rest_of_element_DSS import DIGS_AutoTrans_DSS, DIGS_GICTransformer_DSS, DIGS_Reactor_DSS
from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Shunt_DSS import DIGS_Shunt_DSS

def PD_elements_DSS(dict_df_DigS:dict, BBDD_OpenDSS:dict, OpenDSS_element_list:list):


    # from Trafo_DSS.py (2 winding transformer)
    BBDD_OpenDSS['Transformer'] = DIGS_trafo_conn_group_DSS(DataFrame_ElmTr2=dict_df_DigS['ElmTr2'],
                                                            DataFrame_ElmTr3=dict_df_DigS['ElmTr3'],
                                                            DataFrame_TypTr2=dict_df_DigS['TypTr2'],
                                                            DataFrame_TypTr3=dict_df_DigS['TypTr3'],
                                                            DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                                            DataFrame_StaCubic=dict_df_DigS['StaCubic'])

    OpenDSS_element_list.append('Transformer')

    # from Line_DSS
    BBDD_OpenDSS['Line'] = DIGS_line_DSS(DataFrame_ElmLne=dict_df_DigS['ElmLne'],
                                         DataFrame_TypTow=dict_df_DigS['TypTow'],
                                         DataFrame_TypLne=dict_df_DigS['TypLne'],
                                         DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                         DataFrame_StaCubic=dict_df_DigS['StaCubic'],
                                         DataFrame_TypGeo=dict_df_DigS['TypGeo'],
                                         DataFrame_TypCon=dict_df_DigS['TypCon'])
    OpenDSS_element_list.append('Line')

    # From Switch_DSS
    BBDD_OpenDSS['Switch'] = DIGS_switch_DSS(DataFrame_ElmCoup=dict_df_DigS['ElmCoup'],
                                             DataFrame_RelFuse=dict_df_DigS['RelFuse'],
                                             DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                             DataFrame_StaCubic=dict_df_DigS['StaCubic'])
    OpenDSS_element_list.append('Switch')

    # From Shunt_DSS.py
    BBDD_OpenDSS['Capacitor'] = DIGS_Shunt_DSS(DataFrame_ElmShnt=dict_df_DigS['ElmShnt'],
                                               DataFrame_ElmTerm=dict_df_DigS['ElmTerm'],
                                               DataFrame_StaCubic=dict_df_DigS['StaCubic'])
    OpenDSS_element_list.append('Capacitor')

    # From Rest_of_element_DSS
    BBDD_OpenDSS['AutoTrans'] = DIGS_AutoTrans_DSS()
    OpenDSS_element_list.append('AutoTrans')

    BBDD_OpenDSS['GICTransformer'] = DIGS_GICTransformer_DSS()
    OpenDSS_element_list.append('GICTransformer')

    BBDD_OpenDSS['Reactor'] = DIGS_Reactor_DSS()
    OpenDSS_element_list.append('Reactor')

    return BBDD_OpenDSS, OpenDSS_element_list