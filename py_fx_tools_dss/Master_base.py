# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------.py
# @Software: PyCharm

from py_fx_tools_dss.IMEX_to_DSS.DIGS_to_DSS.DigSilent_to_OpenDSS import DIGS_TO_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.create_scpit_base_DSS import create_DSS
from py_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.create_file_xlsx import Create_DSS_to_xlsx_files


def select_import(case_nro: int):

    if case_nro == 1:
        export_name = 'Hidrandina_TOE_V6'
        xls_file_address = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\11. Hidrandina\Hidrandina_TOE105.xls"
        xls_file_StaCubic = r""
        address_saves = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\11. Hidrandina"

    elif case_nro == 3:
        export_name = 'Elor_V6'
        xls_file_address = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\13. Elor V6\ELOR_Iquitos_v6.xls"
        xls_file_StaCubic = r""
        address_saves = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\13. Elor V6"

    elif case_nro == 4:
        export_name = 'SEAL'
        xls_file_address = r"C:....\SEAL_CiudadMunicipal_Max2021_RedEq_V2.xls"
        xls_file_StaCubic = r""
        address_saves = r"....\8. SEAL"

    elif case_nro == 5:
        export_name = '13ieee_V6'
        xls_file_address = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\12. 13ieee_V6\IEEE 13 Node Feeder.xls"
        xls_file_StaCubic = r""
        address_saves = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\12. 13ieee_V6"

    elif case_nro == 6:
        export_name = '15node'
        xls_file_address = r"C:\Users\tote_\Google Drive\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\Casos_de_estudio\12. 13ieee_V6\IEEE 13 Node Feeder.xls"
        xls_file_StaCubic = r""
        address_saves = r"G:\Mi unidad\UNSJ-IEE\Investigación RID\Avances de Tesis PhD\1. Estimador de estado del SD\DSSE_Punto_Interior"

    return export_name, xls_file_address, xls_file_StaCubic, address_saves



#export_name, xls_file_address, xls_file_StaCubic, address_saves = select_import(6)

'Part 1'
'Function that converts the Digsilent .xls file to an OpenDSS .xlsx file.'
reliability = True
DIGS_TO_DSS(workbook_address=xls_file_address, StaCubic_address=xls_file_StaCubic, projects_name=export_name, out_path=address_saves, reliability=reliability)

'Part 2'
'Create the OpenDSS scripts in the folder where the xlsx file is located: BBDD_DSS_{name_project}'
#create_DSS(name_dss=export_name, address_saves=address_saves)

DSS_path = r"G:\Mi unidad\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\feeders\13Bus\IEEE13Nodeckt.dss"
path_save = r"G:\Mi unidad\UNSJ-IEE\PROYECTOS EN CURSO\OpenDSS_red_real\1. PyQGIS\Codigo_PyQGIS\DigSilent_to_openDSS\feeders\13Bus"

Create_DSS_to_xlsx_files(DSS_file=DSS_path, out_path=path_save)

'Part 3'
'Create the OpenDSS scripts in the folder where the xlsx file is located: BBDD_DSS_{name_project}'
create_DSS(name_dss=export_name_edit, address_saves=address_saves_edit)
