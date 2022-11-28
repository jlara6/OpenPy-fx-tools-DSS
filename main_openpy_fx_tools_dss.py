import openpy_fx_tools_dss as fx_dss

xlsx = fx_dss.xlsx_DSS_xlsx()
test = fx_dss.examples_lib()

run_DSS_to_xlxs = 1
run_xlsx_to_DSS = 1
opt_crt = 3

if __name__ == '__main__':
    # dict_xlsx = fx_dss.load_examples_xlsx(5)

    # xlsx_data = xlsx.load_examples_xlsx(1)  # Loads the examples loaded in the library
    # xlsx.create_template_xlsx() # Generates the xlsx template for xlsx_data entry. In development
    # xlsx.xlsx_to_OpenDSS(xlsx_path=xlsx_data['xlsx_path'], path_save=xlsx_data['path_save']) # Generate OpenDSS files.

    # xlsx.create_template_xlsx() # Generates the xlsx template for xlsx_data entry. In development

    # Loads the examples loaded in the library
    DSS_path = test.load_examples_DSS(opt_crt, 'xlsx')
    xlsx_path = test.load_examples_xlsx(opt_crt)

    # fx_dss.create_template_xlsx()

    if run_DSS_to_xlxs == 1:
        # Generate xlsx file.
        xlsx.OpenDSS_to_xlsx(
            DSS_path=DSS_path['DSS_path'],
            path_save=DSS_path['path_save'],
            prj_name=DSS_path['prj_name']
        )

    if run_xlsx_to_DSS == 1:
        # Generate OpenDSS files.
        xlsx.xlsx_to_OpenDSS(
            xlsx_path=xlsx_path['xlsx_path'],
            path_save=xlsx_path['path_save'],
            prj_name=DSS_path['prj_name']
        )
