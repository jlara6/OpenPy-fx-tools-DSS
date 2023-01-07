
import win32com.client
from openpy_fx_tools_dss.COM.Interface.ActiveBus import ActiveBus
from openpy_fx_tools_dss.COM.Interface.Text import Text

class COM_DLL:

    def __init__(self):
        self.DSSObject = _Check_DSS_Connection()
        self.Text = self.DSSObject.Text
        self.Text.Command = "Clear"

        self.Text = Text(self.DSSObject)
        self.ActiveBus = ActiveBus(self.DSSObject)

def _Check_DSS_Connection(DSSObject=None, version:bool=True):

    DSSObject = win32com.client.Dispatch("OpenDSSEngine.DSS")
    DSSObject.Start("0")

    if DSSObject.Start("0") == False:
        print("DSS Failed to Start")
        exit()
    else:
        if version:
            print(f'{DSSObject.Version}\n')
    return DSSObject
