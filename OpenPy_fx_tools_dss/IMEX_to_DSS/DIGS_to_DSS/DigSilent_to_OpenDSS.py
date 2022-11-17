# -*- coding: utf-8 -*-
# @Time    : 18/02/2022
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fx_tools_dss.helper_functions import *
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Bus_Phases_DSS import *
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.file_for_reliability import column_selection_for_reliability
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.Other_DSS import Other_elements_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.General_DSS import General_elements_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.PD_Elements import PD_elements_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.PC_Elements import PC_elements_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.Controls_DSS import Controls_elements_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.Meters_DSS import Meters_elements_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.fx_for_elem.Voltagebases import DIGS_Voltagebases_DSS
from openpy_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.Types_elements.Buscoords import Buscoords_DSS, file_Buscoords_DSS


def DIGS_TO_DSS(workbook_address: str, StaCubic_address: str, projects_name: str, out_path: str, reliability: bool) -> object:
    """
    Function that converts the Digsilent .xls file to an OpenDSS .xls file

    :param workbook_address: Address where the digsilent .xls file is located
    :param projects_name: Project name, this name will be present in the xlsx file as BBDD_DSS_name
    :param out_path: Address where the .xlsx file will be saved with the information for OpenDSS
    :param reliability: It is a boolean, if it is true it generates the .xls file for reliability
    :return: Files: BBDD_DSS_{projects_name}.xlsx, Buscoords_{projects_name}.csv and BBDD_reliability_{projects_name}.xlsx
    """
    
    text_aux = '\n'
    # From helper_functions
    # Read the .xls file. Store the DataFrame in a dictionary and retrieve all the names of the sheets
    BBDD_DigS_to_dic_and_DF, sheets = readAllSheets(workbook_address)
    BBDD_DigS_to_dic_and_DF, sheets = check_version_of_BBDD(BBDD_DigS=BBDD_DigS_to_dic_and_DF, name_sheets=sheets)
    # Function that checks if the element exists in the database. If it exists, it prints: With Data - Empty
    print('___________________________________________________________________________________________________________')
    print('First stage: Database verification')
    text_aux = text_aux + 'Database verification: Ok\n'

    BBDD_DigS_to_dic_and_DF, message_elem_exist = check_if_element_exists(BBDD_elem_DigS=BBDD_DigS_to_dic_and_DF,
                                                                          name_sheets=sheets)
    file_logging_info(logfilename='BBDD_Digsilent summary', message=message_elem_exist)
    name_folders_elements(dict_df_DigS=BBDD_DigS_to_dic_and_DF)

    #BDD_DigS_to_dic_and_DF = name_folders_elements(dict_df_DigS=BBDD_DigS_to_dic_and_DF)

    # From Bus_Phases_DSS
    # Function that converts phase connections from Digsilent format to OpenDSS in the column ['phase_DSS']
    print('___________________________________________________________________________________________________________')
    print('Second stage: Phase identification')
    text_aux = text_aux + 'Phase identification: Ok\n'
    BBDD_DigS_to_dic_and_DF['ElmTerm'] = terminal_name_check(DataFrame_ElmTerm=BBDD_DigS_to_dic_and_DF['ElmTerm'])
    BBDD_DigS_to_dic_and_DF['StaCubic'] = phase_identification(DataFrame_StaCubic=BBDD_DigS_to_dic_and_DF['StaCubic'],
                                                               DataFrame_ElmTerm=BBDD_DigS_to_dic_and_DF['ElmTerm'],
                                                               file_direction=out_path,
                                                               StaCubic_direction=StaCubic_address,
                                                               file_name=projects_name)

    #From functions_to_OpenDSS
    print('___________________________________________________________________________________________________________')
    print('Third stage: OpenDSS Database creation and xlsx_data filling')
    text_aux = text_aux + 'OpenDSS Database creation and xlsx_data filling: Ok\n'

    OpenDSS_element_list, BBDD_OpenDSS = OpenDSS_database_generator(dict_df_DigS=BBDD_DigS_to_dic_and_DF)

    # From helper_functions
    print('___________________________________________________________________________________________________________')
    print('Fourth stage: Export of the file with xlsx_data for OpenDSS')

    text_aux = text_aux + 'Export of the file with xlsx_data for OpenDSS: Ok\n'

    workbook_DSS = f'BBDD_DSS_{projects_name}.xlsx'
    _save_BBDD_xlsx(workbook_DSS=workbook_DSS,
                    elements_OpenDSS=OpenDSS_element_list,
                    BBDD_OpenDSS=BBDD_OpenDSS,
                    out_path=out_path)
    print('___________________________________________________________________________________________________________')
    print('Fifth stage: Export and creation of the geographic coordinate file')

    text_aux = text_aux + 'Export and creation of the geographic coordinate file: Ok\n'

    Buscoords_DSS(name_proyect=projects_name,
                  DataFrame_ElmTerm=BBDD_DigS_to_dic_and_DF['ElmTerm'],
                  DataFrame_ElmSubstat=BBDD_DigS_to_dic_and_DF['ElmSubstat'],
                  out_path=out_path)


    file_Buscoords_DSS(workbook=projects_name,
                       BBDD_OpenDSS=BBDD_OpenDSS,
                       dict_df_DigS=BBDD_DigS_to_dic_and_DF,
                       out_path=out_path)


    print('___________________________________________________________________________________________________________')
    print('The file containing the information to be used to create the OpenDSS scripts was successfully generated.')

    text_aux = text_aux + 'The file containing the information to be used to create the OpenDSS scripts was successfully generated: Ok\n'

    print('___________________________________________________________________________________________________________')
    if reliability == True:

        'Generate files for reliability'
        column_selection_for_reliability(workbook=projects_name,
                                         BBDD_OpenDSS=BBDD_OpenDSS,
                                         dict_df_DigS=BBDD_DigS_to_dic_and_DF,
                                         out_path=out_path)
        print('The file for the reliability analysis were generated successfully')

        text_aux = text_aux + 'The file for the reliability analysis were generated successfully: Ok\n'
    else:
        pass

    text_aux = text_aux + f'The location of the files is:\n'
    text_aux = text_aux + f'{out_path}'


    file_logging_info(logfilename='export summary', message=text_aux)

def OpenDSS_database_generator(dict_df_DigS: dict):
    """
    Fill the dictionary and DataFrame with xlsx_data that OpenDSS reads, use the functions:Other_elements_DSS,
    General_elements_DSS, PD_elements_MTY, PC_elements_MTY, Controls_elements_DSS, Meters_elements_DSS and
    DIGS_Voltagebases_DSS

    :param dict_df_DigS: Dictionary that in each key contains a dataframe with the information exported from Digsilent in .xls format
    :return: OpenDSS_element_list, BBDD_OpenDSS
    """

    OpenDSS_element_list = list()
    BBDD_OpenDSS = dict()

    BBDD_OpenDSS, OpenDSS_element_list = Other_elements_DSS(dict_df_DigS, BBDD_OpenDSS, OpenDSS_element_list)
    BBDD_OpenDSS, OpenDSS_element_list = General_elements_DSS(dict_df_DigS, BBDD_OpenDSS, OpenDSS_element_list)
    BBDD_OpenDSS, OpenDSS_element_list = PD_elements_DSS(dict_df_DigS, BBDD_OpenDSS, OpenDSS_element_list)
    BBDD_OpenDSS, OpenDSS_element_list = PC_elements_DSS(dict_df_DigS, BBDD_OpenDSS, OpenDSS_element_list)
    BBDD_OpenDSS, OpenDSS_element_list = Controls_elements_DSS(dict_df_DigS, BBDD_OpenDSS, OpenDSS_element_list)
    BBDD_OpenDSS, OpenDSS_element_list = Meters_elements_DSS(dict_df_DigS, BBDD_OpenDSS, OpenDSS_element_list)

    # from Voltagebases.py
    BBDD_OpenDSS['Voltagebases'] = DIGS_Voltagebases_DSS(DataFrame_ElmTerm=dict_df_DigS['ElmTerm'])
    OpenDSS_element_list.append('Voltagebases')

    return OpenDSS_element_list, BBDD_OpenDSS
