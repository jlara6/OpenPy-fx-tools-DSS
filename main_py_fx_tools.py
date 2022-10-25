import py_fx_tools_dss as fx_dss

xlsx_dss = fx_dss.base_xlsx_DSS


if __name__ == '__main__':
    dict_xlsx = xlsx_dss.Load_examples_xlsx_files(option=1)
    xlsx_dss.xlsx_DSS()

    print('here')







