# -*- coding: utf-8 -*-
# @Time    : 22/10/2021
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm
import numpy as np

from helper_functions import *

def LineCode_DSS(DataFrame_TypLne: pd.DataFrame):
    '''
    :param DataFrame_ElmLne:
    :return:
    '''
    'new LineCode.Sym nphases=3 units=mi r1=0.301 x1=0.766 r0=0.627 x0=1.944 // c1=18.35 c0=7.08'
    'DataFrame creation with OpenDSS keywords'
    df_LineCode_DSS = pd.DataFrame(
        columns=['Id_LineCode', 'nphases','normamps' 'rmatrix', 'xmatrix', 'cmatrix', 'r1', 'x1', 'r0', 'x0', 'C1', 'C0',
                 'units', 'baseFreq', 'emergamps', 'faultrate', 'pctperm', 'repair', 'Kron', 'Rg', 'Xg', 'rho',
                 'neutral', 'B1', 'B0', 'Seasons', 'Ratings', 'LineType', 'like'])

    if DataFrame_TypLne.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_TypLne, 'loc_name(a:40)')

        for index, row in DataFrame_TypLne.iterrows():
            Id_LineCode = DataFrame_TypLne['loc_name(a:40)'][index]
            nphases = DataFrame_TypLne['nlnph(i)'][index]
            units = 'km'
            if DataFrame_TypLne['rline(r)'][index] > 0:
                r1 = DataFrame_TypLne['rline(r)'][index]
            else:
                r1 = ''
            if DataFrame_TypLne['xline(r)'][index] >0:
                x1 = DataFrame_TypLne['xline(r)'][index]
            else:
                x1 = ''

            if DataFrame_TypLne['rline0(r)'][index] > 0:
                r0 = DataFrame_TypLne['rline0(r)'][index]
            else:
                r0 = ''

            if DataFrame_TypLne['xline0(r)'][index] > 0:
                x0 = DataFrame_TypLne['xline0(r)'][index]
            else:
                x0 = ''

            #c1 = DataFrame_TypLne['cline(r)'][index]
            #c0 = DataFrame_TypLne['cline0(r)'][index]
            #b1 = DataFrame_TypLne['bline(r)'][index]
            #b0 = DataFrame_TypLne['bline0(r)'][index]

            normamps = DataFrame_TypLne['sline(r)'][index] * 1000

            df_LineCode_DSS = df_LineCode_DSS.append(
                {'Id_LineCode': Id_LineCode, 'nphases': nphases, 'r1': r1, 'x1': x1, 'r0': r0, 'x0': x0, 'C1': '', 'C0': '', 'units': units, 'rmatrix': '', 'xmatrix': '', 'cmatrix': '',
                 'baseFreq': '', 'normamps': normamps, 'emergamps': '', 'faultrate': '', 'pctperm': '', 'repair': '', 'Kron': '', 'Rg': '', 'Xg': '', 'rho': '',
                 'neutral': '', 'B1': '', 'B0': '', 'Seasons': '', 'Ratings': '', 'LineType': '', 'like': ''}, ignore_index=True)

    return df_LineCode_DSS

def LineGeometry_DSS(DataFrame_TypTow: pd.DataFrame, DataFrame_TypCon: pd.DataFrame) -> pd.DataFrame:
    '''
    :param DataFrame_TypTow:
    :param DataFrame_TypCon:
    :return: df_LineGeometry_DSS
    '''

    'new LineGeometry.Trunk   nconds=4 nphases=3 reduce=yes spacing=500 wires=(336_ACSR_Linnet 336_ACSR_Linnet 336_ACSR_Linnet 4_0_ACSR_Penguin)'
    'new LineGeometry.Lateral nconds=2 nphases=1 reduce=yes spacing=510 wires=(2_ACSR_Sparrow 2_ACSR_Sparrow)'

    df_LineGeometry_DSS = pd.DataFrame(columns=['Id_LineGeometry', 'nconds', 'nphases', 'cond', 'wire', 'x', 'h',
                                                'units', 'normamps', 'emergamps', 'reduce', 'spacing', 'wires',
                                                'cncable', 'tscable', 'cncables', 'tscables', 'Seasons', 'Ratings',
                                                'LineTyp', 'like'])

    if DataFrame_TypTow.empty == True or DataFrame_TypCon.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_TypTow, 'loc_name(a:40)')
        characters_delete(DataFrame_TypCon, 'loc_name(a:40)')

        '''
        list_ver6 = list(DataFrame_TypTow.keys())
        if len([x for x in list_ver6 if x in 'pcond_e:0(p)']) == 1:
            DataFrame_TypTow = DataFrame_TypTow.rename(columns={'pcond_e:0(p)': 'pcond_c:1(p)'})
        '''
        aux = 1 in DataFrame_TypTow['nlear(i)'].values
        if aux == True:

            list_ver6 = list(DataFrame_TypTow.keys())
            if len([x for x in list_ver6 if x in 'pcond_c:1(p)']) == 0:
                DataFrame_TypTow.loc[:, 'pcond_c:1(p)'] = np.NaN

            TypCon = DataFrame_TypCon[['ID(a:40)', 'loc_name(a:40)']]
            TypTow_phase = DataFrame_TypTow[['ID(a:40)', 'pcond_c:0(p)']]
            TypTow_neutral = DataFrame_TypTow[['ID(a:40)', 'pcond_c:1(p)']]
            TypTow_earth = DataFrame_TypTow[['ID(a:40)', 'pcond_e:0(p)']]

            df_TypTow_phase_TypCon = pd.merge(
                TypTow_phase, TypCon, how='left', left_on='pcond_c:0(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
            df_TypTow_phase_TypCon = df_TypTow_phase_TypCon[
                ['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})

            df_TypTow_neutral_TypCon = pd.merge(
                TypTow_neutral, TypCon, how='left', left_on='pcond_c:1(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
            df_TypTow_neutral_TypCon = df_TypTow_neutral_TypCon[
                ['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})

            df_TypTow_earth_TypCon = pd.merge(
                TypTow_earth, TypCon, how='left', left_on='pcond_e:0(p)', right_on='ID(a:40)', suffixes=('_x', '_y'))
            df_TypTow_earth_TypCon = df_TypTow_earth_TypCon[
                ['ID(a:40)_x', 'loc_name(a:40)']].rename(columns={'ID(a:40)_x': 'ID(a:40)'})

            df_phase_neutral_earth_TypCon = df_TypTow_phase_TypCon.merge(
                df_TypTow_neutral_TypCon, on='ID(a:40)').merge(
                df_TypTow_earth_TypCon, on='ID(a:40)').rename(
                columns={'loc_name(a:40)_x': 'phase_TypCon',
                         'loc_name(a:40)_y': 'neutral_TypCon',
                         'loc_name(a:40)': 'earth_TypCon'})

            df_TypTow_TypCon = pd.merge(DataFrame_TypTow, df_phase_neutral_earth_TypCon, on='ID(a:40)')

            for index, row in df_TypTow_TypCon.iterrows():
                Id_LineGeometry = df_TypTow_TypCon['loc_name(a:40)'][index]
                spacing = df_TypTow_TypCon['loc_name(a:40)'][index] + '_Spacing'
                n_phase = df_TypTow_TypCon['nphas:0(r)'][index]
                n_neutral = df_TypTow_TypCon['nphas:1(r)'][index]
                n_earth = df_TypTow_TypCon['nlear(i)'][index]
                nconds = n_phase + n_neutral + n_earth
                reduce = 'yes'

                phase = df_TypTow_TypCon['phase_TypCon'][index]
                neutral = df_TypTow_TypCon['neutral_TypCon'][index]
                earth = df_TypTow_TypCon['earth_TypCon'][index]

                if n_phase == 3:
                    if n_neutral == 1 and n_earth == 1:
                        wires = f'({phase}, {phase}, {phase}, {neutral}, {earth})'
                    if n_neutral == 1 and n_earth == 0:
                        wires = f'({phase}, {phase}, {phase}, {neutral})'
                    if n_neutral == 0 and n_earth == 1:
                        wires = f'({phase}, {phase}, {phase}, {earth})'
                    if n_neutral == 0 and n_earth == 0:
                        wires = f'({phase}, {phase}, {phase})'

                if n_phase == 2:
                    if n_neutral == 1 and n_earth == 1:
                        wires = f'({phase}, {phase}, {neutral}, {earth})'
                    if n_neutral == 1 and n_earth == 0:
                        wires = f'({phase}, {phase}, {neutral})'
                    if n_neutral == 0 and n_earth == 1:
                        wires = f'({phase}, {phase}, {earth})'
                    if n_neutral == 0 and n_earth == 0:
                        wires = f'({phase}, {phase})'

                if n_phase == 1:
                    if n_neutral == 1 and n_earth == 1:
                        wires = f'({phase}, {neutral}, {earth})'
                    if n_neutral == 1 and n_earth == 0:
                        wires = f'({phase}, {neutral})'
                    if n_neutral == 0 and n_earth == 1:
                        wires = f'({phase}, {earth})'
                    if n_neutral == 0 and n_earth == 0:
                        wires = f'({phase})'

                # Append to df_LineGeometry_DSS
                df_LineGeometry_DSS = df_LineGeometry_DSS.append(
                    {'Id_LineGeometry': Id_LineGeometry, 'nconds': nconds, 'nphases': n_phase, 'cond': '',
                     'wire': '', 'x': '', 'h': '', 'units': '', 'normamps': '',
                     'emergamps': '', 'reduce': reduce, 'spacing': spacing, 'wires': wires,
                     'cncable': '', 'tscable': '', 'cncables': '', 'tscables': '',
                     'Seasons': '', 'Ratings': '', 'LineTyp': '', 'like': ''}, ignore_index=True)
        else:

            TypCon = DataFrame_TypCon[['ID(a:40)', 'loc_name(a:40)']]

            TypTow_phase = DataFrame_TypTow[['ID(a:40)', 'pcond_c:0(p)']]
            TypTow_neutral = DataFrame_TypTow[['ID(a:40)', 'pcond_c:1(p)']]

            df_TypTow_phase_TypCon = pd.merge(TypTow_phase, TypCon, how='left', left_on='pcond_c:0(p)',
                                              right_on='ID(a:40)',
                                              suffixes=('_x', '_y'))
            df_TypTow_phase_TypCon = df_TypTow_phase_TypCon[['ID(a:40)_x', 'loc_name(a:40)']].rename(
                columns={'ID(a:40)_x': 'ID(a:40)'})

            df_TypTow_neutral_TypCon = pd.merge(TypTow_neutral, TypCon, how='left', left_on='pcond_c:1(p)',
                                                right_on='ID(a:40)', suffixes=('_x', '_y'))
            df_TypTow_neutral_TypCon = df_TypTow_neutral_TypCon[['ID(a:40)_x', 'loc_name(a:40)']].rename(
                columns={'ID(a:40)_x': 'ID(a:40)'})

            df_phase_neutral_TypCon = pd.merge(df_TypTow_phase_TypCon, df_TypTow_neutral_TypCon, on='ID(a:40)').rename(
                columns={'loc_name(a:40)_x': 'phase_TypCon', 'loc_name(a:40)_y': 'neutral_TypCon'})

            df_TypTow_TypCon = pd.merge(DataFrame_TypTow, df_phase_neutral_TypCon, on='ID(a:40)')

            for index, row in df_TypTow_TypCon.iterrows():
                Id_LineGeometry = df_TypTow_TypCon['loc_name(a:40)'][index]
                spacing = df_TypTow_TypCon['loc_name(a:40)'][index] + '_Spacing'
                reduce = 'yes'
                n_phase = df_TypTow_TypCon['nphas:0(r)'][index]
                n_neutral = df_TypTow_TypCon['nphas:1(r)'][index]
                nconds = n_phase + n_neutral

                phase = df_TypTow_TypCon['phase_TypCon'][index]
                neutral = df_TypTow_TypCon['neutral_TypCon'][index]


                if n_phase == 3:
                    if n_neutral == 1:
                        wires = f'({phase}, {phase}, {phase}, {neutral})'
                    if n_neutral == 0:
                        wires = f'({phase}, {phase}, {phase})'

                if n_phase == 2:
                    if n_neutral == 1:
                        wires = f'({phase}, {phase}, {neutral})'
                    if n_neutral == 0:
                        wires = f'({phase}, {phase})'

                if n_phase == 1:
                    if n_neutral == 1:
                        wires = f'({phase}, {neutral})'
                    if n_neutral == 0:
                        wires = f'({phase})'

                # Append to df_LineGeometry_DSS
                df_LineGeometry_DSS = df_LineGeometry_DSS.append(
                    {'Id_LineGeometry': Id_LineGeometry, 'nconds': nconds, 'nphases': n_phase, 'cond': '',
                     'wire': '', 'x': '', 'h': '', 'units': '', 'normamps': '',
                     'emergamps': '', 'reduce': reduce, 'spacing': spacing, 'wires': wires,
                     'cncable': '', 'tscable': '', 'cncables': '', 'tscables': '',
                     'Seasons': '', 'Ratings': '', 'LineTyp': '', 'like': ''}, ignore_index=True)

    return df_LineGeometry_DSS


def WireData_DSS(DataFrame_TypCon: pd.DataFrame) -> pd.DataFrame:
    '''
    :param DataFrame_TypCon:
    :return: df_WireData_DSS
    '''
    # OpenDSS code
    'new WireData.336_ACSR_Linnet  gmrunits=ft radunits=in runits=mi rac=0.306 diam=0.721 gmrac=0.0244  normamps=530'
    'new WireData.4_0_ACSR_Penguin gmrunits=ft radunits=in runits=mi rac=0.592 diam=0.563 gmrac=0.00814 normamps=340'
    'new WireData.2_ACSR_Sparrow   gmrunits=ft radunits=in runits=mi rac=1.690 diam=0.316 gmrac=0.00418 normamps=180'


    df_WireData_DSS = pd.DataFrame(columns=['Id_WireData', 'DIAM', 'GMRac',  'Rdc', 'Rac', 'Runits', 'GMRunits',
                                            'Radunits', 'radius', 'normamps', 'emergamps', 'Seasons', 'Ratings',
                                            'Capradius', 'like'])

    if DataFrame_TypCon.empty == True:
        pass
    else:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_TypCon, 'loc_name(a:40)')

        'new WireData.ACSR_556_5  DIAM=0.927  GMRac=0.37320  Rdc=0.035227273   Runits=kft Radunits=in gmrunits=in'
        for index, row in DataFrame_TypCon.iterrows():
            id_WireData = DataFrame_TypCon['loc_name(a:40)'][index]
            DIAM = DataFrame_TypCon['diaco(r)'][index]
            GMRac = DataFrame_TypCon['erpha(r)'][index]
            Rdc = DataFrame_TypCon['rpha(r)'][index]
            Runits = 'km'
            Radunits = 'mm'
            GMRunits = 'mm'
            normamps = DataFrame_TypCon['sline(r)'][index] * 1000
            radius = ''

            # Append to df_WireData_DSS
            df_WireData_DSS = df_WireData_DSS.append(
                {'Id_WireData': id_WireData, 'Rdc': Rdc, 'Rac': '', 'Runits': Runits, 'GMRac': GMRac,
                 'GMRunits': GMRunits, 'radius': radius, 'Radunits': Radunits, 'normamps': normamps, 'emergamps': '',
                 'DIAM': DIAM, 'Seasons': '', 'Ratings': '', 'Capradius': '', 'like': ''}, ignore_index=True)

    return df_WireData_DSS


def LineSpacing_DSS(DataFrame_TypTow: pd.DataFrame, DataFrame_TypGeo: pd.DataFrame) -> pd.DataFrame:
    '''
    :param DataFrame_TypTow:
    :return: df_LineSpacing_DSS
    '''
    'new LineSpacing.500 nconds=4 nphases=3 units=ft h=(28 28 28 24) x=(-3.5 -1.0 3.5 0.5)'
    'new LineSpacing.510 nconds=2 nphases=1 units=ft h=(29 24) x=(0 0.5)'

    df_LineSpacing_DSS = pd.DataFrame(columns=['Id_LineSpacing', 'nconds', 'nphases', 'x', 'h', 'units', 'like'])

    if DataFrame_TypTow.empty == False:
        'Function that eliminates empty spaces and special characters that can cause convergence problems in OpenDSS'
        characters_delete(DataFrame_TypTow, 'loc_name(a:40)')
        aux = 1 in DataFrame_TypTow['nlear(i)'].values
        if aux == True:

            list_ver6 = list(DataFrame_TypTow.keys())
            if len([x for x in list_ver6 if x in 'nphas:1(r)']) == 0:
                DataFrame_TypTow.loc[:, 'nphas:1(r)'] = 0
                DataFrame_TypTow.loc[:, 'xy_c:1:0(r)'] = 0
                DataFrame_TypTow.loc[:, 'xy_c:1:3(r)'] = 0

            for index, row in DataFrame_TypTow.iterrows():
                Id_LineSpacing = DataFrame_TypTow['loc_name(a:40)'][index] + '_Spacing'
                n_phase = DataFrame_TypTow['nphas:0(r)'][index]
                n_neutral = DataFrame_TypTow['nphas:1(r)'][index]
                n_earth = DataFrame_TypTow['nlear(i)'][index]
                nconds = n_phase + n_neutral + n_earth

                'phases'
                x1 = DataFrame_TypTow['xy_c:0:0(r)'][index]
                x2 = DataFrame_TypTow['xy_c:0:1(r)'][index]
                x3 = DataFrame_TypTow['xy_c:0:2(r)'][index]
                h1 = DataFrame_TypTow['xy_c:0:3(r)'][index]
                h2 = DataFrame_TypTow['xy_c:0:4(r)'][index]
                h3 = DataFrame_TypTow['xy_c:0:5(r)'][index]
                'neutral'
                x4 = DataFrame_TypTow['xy_c:1:0(r)'][index]
                h4 = DataFrame_TypTow['xy_c:1:3(r)'][index]
                'earth'
                x5 = DataFrame_TypTow['xy_e:0:0(r)'][index]
                h5 = DataFrame_TypTow['xy_e:0:1(r)'][index]

                if n_phase == 3:
                    if n_neutral == 1 and n_earth == 1:
                        x = f'({x1}, {x2}, {x3}, {x4}, {x5})'
                        h = f'({h1}, {h2}, {h3}, {h4}, {h5})'
                    if n_neutral == 1 and n_earth == 0:
                        x = f'({x1}, {x2}, {x3}, {x4})'
                        h = f'({h1}, {h2}, {h3}, {h4})'
                    if n_neutral == 0 and n_earth == 1:
                        x = f'({x1}, {x2}, {x3}, {x5})'
                        h = f'({h1}, {h2}, {h3}, {h5})'
                    if n_neutral == 0 and n_earth == 0:
                        x = f'({x1}, {x2}, {x3})'
                        h = f'({h1}, {h2}, {h3})'

                if n_phase == 2:
                    if n_neutral == 1 and n_earth == 1:
                        x = f'({x1}, {x2}, {x4}, {x5})'
                        h = f'({h1}, {h2}, {h4}, {h5})'
                    if n_neutral == 1 and n_earth == 0:
                        x = f'({x1}, {x2}, {x4})'
                        h = f'({h1}, {h2}, {h4})'
                    if n_neutral == 0 and n_earth == 1:
                        x = f'({x1}, {x2}, {x5})'
                        h = f'({h1}, {h2}, {h5})'
                    if n_neutral == 0 and n_earth == 0:
                        x = f'({x1}, {x2})'
                        h = f'({h1}, {h2})'

                if n_phase == 1:
                    if n_neutral == 1 and n_earth == 1:
                        x = f'({x1}, {x4}, {x5})'
                        h = f'({h1}, {h4}, {h5})'
                    if n_neutral == 1 and n_earth == 0:
                        x = f'({x1}, {x4})'
                        h = f'({h1}, {h4})'
                    if n_neutral == 0 and n_earth == 1:
                        x = f'({x1}, {x5})'
                        h = f'({h1}, {h5})'
                    if n_neutral == 0 and n_earth == 0:
                        x = f'({x1})'
                        h = f'({h1})'
                units = 'm'
                # Append to df_LineSpacing_DSS
                df_LineSpacing_DSS = df_LineSpacing_DSS.append(
                    {'Id_LineSpacing': Id_LineSpacing, 'nconds': nconds, 'nphases': n_phase, 'x': x, 'h': h,
                     'units': units, 'like': ''}, ignore_index=True)
        else:
            for index, row in DataFrame_TypTow.iterrows():
                Id_LineSpacing = DataFrame_TypTow['loc_name(a:40)'][index] + '_Spacing'
                n_phase = DataFrame_TypTow['nphas:0(r)'][index]
                n_neutral = DataFrame_TypTow['nphas:1(r)'][index]
                nconds = n_phase + n_neutral

                'phases'
                x1 = DataFrame_TypTow['xy_c:0:0(r)'][index]
                x2 = DataFrame_TypTow['xy_c:0:1(r)'][index]
                x3 = DataFrame_TypTow['xy_c:0:2(r)'][index]
                h1 = DataFrame_TypTow['xy_c:0:3(r)'][index]
                h2 = DataFrame_TypTow['xy_c:0:4(r)'][index]
                h3 = DataFrame_TypTow['xy_c:0:5(r)'][index]
                'neutral'
                x4 = DataFrame_TypTow['xy_c:1:0(r)'][index]
                h4 = DataFrame_TypTow['xy_c:1:3(r)'][index]
                if n_phase == 3:
                    if n_neutral == 1 :
                        x = f'({x1}, {x2}, {x3}, {x4})'
                        h = f'({h1}, {h2}, {h3}, {h4})'
                    if n_neutral == 0:
                        x = f'({x1}, {x2}, {x3})'
                        h = f'({h1}, {h2}, {h3})'

                if n_phase == 2:
                    if n_neutral == 1:
                        x = f'({x1}, {x2}, {x4})'
                        h = f'({h1}, {h2}, {h4})'
                    if n_neutral == 0:
                        x = f'({x1}, {x2})'
                        h = f'({h1}, {h2})'
                if n_phase == 1:
                    if n_neutral == 1:
                        x = f'({x1}, {x4})'
                        h = f'({h1}, {h4})'
                    if n_neutral == 0:
                        x = f'({x1})'
                        h = f'({h1})'
                units = 'm'
                # Append to df_LineSpacing_DSS
                df_LineSpacing_DSS = df_LineSpacing_DSS.append(
                    {'Id_LineSpacing': Id_LineSpacing, 'nconds': nconds, 'nphases': n_phase, 'x': x, 'h': h,
                     'units': units, 'like': ''}, ignore_index=True)

    if DataFrame_TypGeo.empty == False:
        characters_delete(DataFrame_TypGeo, 'loc_name(a:40)')
        for index, row in DataFrame_TypGeo.iterrows():
            Id_LineSpacing = DataFrame_TypGeo['loc_name(a:40)'][index]
            nphases = DataFrame_TypGeo['xy_c:0:0(r)'][index]
            nconds = DataFrame_TypGeo['xy_c:0:0(r)'][index]
    
            x1 = DataFrame_TypGeo['xy_c:0:1(r)'][index]
            x2 = DataFrame_TypGeo['xy_c:0:2(r)'][index]
            x3 = DataFrame_TypGeo['xy_c:0:3(r)'][index]
    
            h1 = DataFrame_TypGeo['xy_c:0:4(r)'][index]
            h2 = DataFrame_TypGeo['xy_c:0:5(r)'][index]
            h3 = DataFrame_TypGeo['xy_c:0:6(r)'][index]
    
            if nconds == 3:
                x = f'({x1}, {x2}, {x3})'
                h = f'({h1}, {h2}, {h3})'
            elif nconds == 2:
                x = f'({x1}, {x2})'
                h = f'({h1}, {h2})'
            elif nconds == 1:
                x = f'({x1})'
                h = f'({h1})'
            units = 'm'
            df_LineSpacing_DSS = df_LineSpacing_DSS.append({'Id_LineSpacing': Id_LineSpacing, 'nconds': nconds,
                                                            'nphases': nphases, 'x': x, 'h': h, 'units': units,
                                                            'like': ''}, ignore_index=True)
    return df_LineSpacing_DSS


