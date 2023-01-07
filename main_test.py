import openpy_fx_tools_dss as fx_dss

xlsx = fx_dss.xlsx_DSS_xlsx()

DSS_xlsx = 1
xlsx_DSS = 1

DSS_path = r"C:\Users\tote_\OneDrive\Escritorio\Files_DSS\Master_Caso_Base.dss"
xlsx_path = r"C:\Users\tote_\OneDrive\Escritorio\Files_DSS\Test_DSS"

if __name__ == "__main__":
    if DSS_xlsx == 1:
        xlsx.OpenDSS_to_xlsx(
            DSS_path=DSS_path,
            path_save=xlsx_path,
            prj_name='test'
        )
    if xlsx_DSS == 1:
        xlsx.xlsx_to_OpenDSS(
            xlsx_path=r"C:\Users\tote_\OneDrive\Escritorio\Files_DSS\Test_DSS\BBDD_DSS_test.xlsx",
            path_save=r"C:\Users\tote_\OneDrive\Escritorio\Files_DSS\Test_DSS",
            prj_name='test'
        )
