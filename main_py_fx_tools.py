import py_fx_tools_dss as fx_dss

xlsx = fx_dss.xlsx_DSS_xlsx()


if __name__ == '__main__':
    #dict_xlsx = fx_dss.load_examples(5)

    data = xlsx.load_examples(1)  # Loads the examples loaded in the library
    #xlsx.create_template_xlsx() # Generates the xlsx template for data entry. In development
    #xlsx.xlsx_to_DSS_scripts(xlsx_path=data['xlsx_path'], path_save=data['path_save']) # Generate OpenDSS files.
    xlsx.DSS_scripts_to_xlsx()


    #fx_dss.create_template_xlsx()

    print('here')







