# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm


import pandas as pd

def DIGS_Voltagebases_DSS(DataFrame_ElmTerm:pd.DataFrame) -> pd.DataFrame:
    df_Voltagebases_DSS = pd.DataFrame(columns=['Id_Voltagebases'])

    DataFrame_ElmTerm = DataFrame_ElmTerm.loc[:, ['ID(a:40)', 'loc_name(a:40)', 'uknom(r)', 'ciEnergized(i)']]
    DataFrame_ElmTerm = DataFrame_ElmTerm[DataFrame_ElmTerm['ciEnergized(i)'] == 1]  # Filters energized elements

    Voltagebases = DataFrame_ElmTerm['uknom(r)'].unique()
    Voltagebases_list = Voltagebases.tolist()
    df_Voltagebases_DSS = df_Voltagebases_DSS.append({'Id_Voltagebases': Voltagebases_list}, ignore_index=True)

    return df_Voltagebases_DSS