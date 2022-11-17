import openpy_fx_tools_dss as fx_dss

xlsx = fx_dss.xlsx_DSS_xlsx()

run_DSS_to_xlxs = 1
run_xlsx_to_DSS = 1



if __name__ == '__main__':
    #dict_xlsx = fx_dss.load_examples_xlsx(5)

    #xlsx_data = xlsx.load_examples_xlsx(1)  # Loads the examples loaded in the library
    #xlsx.create_template_xlsx() # Generates the xlsx template for xlsx_data entry. In development
    #xlsx.xlsx_to_OpenDSS(xlsx_path=xlsx_data['xlsx_path'], path_save=xlsx_data['path_save']) # Generate OpenDSS files.

    if run_DSS_to_xlxs == 1:
        DSS_data = xlsx.load_examples_DSS(2)
        xlsx.OpenDSS_to_xlsx(DSS_path=DSS_data['DSS_path'],
                             path_save=DSS_data['path_save'],
                             prj_name=DSS_data['prj_name'])

    if run_xlsx_to_DSS == 1:
        xlsx_data = xlsx.load_examples_xlsx(1)  # Loads the examples loaded in the library
        #xlsx.create_template_xlsx() # Generates the xlsx template for xlsx_data entry. In development
        xlsx.xlsx_to_OpenDSS(xlsx_path=xlsx_data['xlsx_path'],
                             path_save=xlsx_data['path_save'],
                             prj_name=xlsx_data['prj_name']) # Generate OpenDSS files.

    #fx_dss.create_template_xlsx()

    print('here')







