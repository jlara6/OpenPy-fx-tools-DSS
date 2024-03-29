import openpy_fx_tools_dss as fx_tools


dssCOM = fx_tools.COM_DLL()
path = r"C:\Users\tote_\OneDrive\Escritorio\test_lib\IEEE13Node_test.dss"

dssCOM.Text.Command(f'Compile {path}')
dssCOM.Text.Command('solve')

test_ActiveBus = 0
test_ActiveCktElement = 0 #Review
test_ActiveClas = 0
test_ActiveDSSElement = 0
test_Capacitor = 0
test_Circuit = 0
test_Lines = 1

if test_ActiveBus == 1:
    print(f'AllPCEatBus-> {dssCOM.ActiveBus.AllPCEatBus(634)}')
    print(f'AllPDEatBus-> {dssCOM.ActiveBus.AllPDEatBus("634")}')
    print(f'Coorddefined-> {dssCOM.ActiveBus.Coorddefined("650")}')
    print(f'CplxSeqVoltages-> {dssCOM.ActiveBus.CplxSeqVoltages("650", polar=True)} - review')
    print(f'Cust_Duration-> {dssCOM.ActiveBus.Cust_Duration("650")} -> test use')
    print(f'Cust_Interrupts-> {dssCOM.ActiveBus.Cust_Interrupts("650")} -> test use')
    print(f'Distance-> {dssCOM.ActiveBus.Distance("632")} -> test use')
    print(f'GetUniqueNodeNumber-> {dssCOM.ActiveBus.GetUniqueNodeNumber("633")}')
    print(f'Int_Duration-> {dssCOM.ActiveBus.Int_Duration("611")} -> test use')
    print(f'Isc-> {dssCOM.ActiveBus.Isc("633")} - need test use')
    print(f'kvBase-> {dssCOM.ActiveBus.kVBase("611")}')
    print(f'Lambda-> {dssCOM.ActiveBus.Lambda("611")} - need test use')
    print(f'Latitude_read-> {dssCOM.ActiveBus.Latitude_read("633")}')
    print(f'Longitude_write')
    dssCOM.ActiveBus.Latitude_write("633", data="55.00")
    print(f'dss.Latitude_read-> {dssCOM.ActiveBus.Latitude_read("633")}')
    print(f'LineList-> {dssCOM.ActiveBus.LineList("632")}')
    print(f'LoadList-> {dssCOM.ActiveBus.LoadList("634")}')
    print(f'Latitude_read-> {dssCOM.ActiveBus.Longitude_read("633")}')
    print(f'Longitude_write')
    dssCOM.ActiveBus.Longitude_write("633", data="4355.00")
    print(f'dss.Latitude_read-> {dssCOM.ActiveBus.Longitude_read("633")}')
    print(f'N_Customers-> {dssCOM.ActiveBus.N_Customers("650")} - need test use')
    print(f'N_Interrupts-> {dssCOM.ActiveBus.N_interrupts("634")} - need test use')
    print(f'Name-> {dssCOM.ActiveBus.Name("633")}')
    print(f'Nodes-> {dssCOM.ActiveBus.Nodes("633")}')
    print(f'Nodes-> {dssCOM.ActiveBus.Nodes("611")}')
    print(f'NumNodes-> {dssCOM.ActiveBus.NumNodes("633")}')
    print(f'NumNodes-> {dssCOM.ActiveBus.NumNodes("611")}')
    print(f'puVLL-> {dssCOM.ActiveBus.puVLL("645")} - review')
    print(f'puVmagAngle-> {dssCOM.ActiveBus.puVmagAngle("645")} - review')
    print(f'puVoltages-> {dssCOM.ActiveBus.puVoltages("645")} - review')
    print(f'SectionID-> {dssCOM.ActiveBus.SectionID("633")} - need test use')
    print(f'SeqVoltages-> {dssCOM.ActiveBus.SeqVoltages("650")} - review')
    print(f'TotalMiles-> {dssCOM.ActiveBus.TotalMiles("611")} - need test use')
    print(f'VLL-> {dssCOM.ActiveBus.VLL("633")} - review')
    print(f'VMagAngle-> {dssCOM.ActiveBus.VMagAngle("634")} - review')
    print(f'Voc-> {dssCOM.ActiveBus.Voc("632")} - need test use')
    print(f'Voltages-> {dssCOM.ActiveBus.Voltages("634")} - review')
    print(f'x_read-> {dssCOM.ActiveBus.x_read("632")}')
    print(f'x_write')
    dssCOM.ActiveBus.x_write("632", data="55.00")
    print(f'x_read-> {dssCOM.ActiveBus.x_read("632")}')
    print(f'y_read-> {dssCOM.ActiveBus.y_read("632")}')
    print(f'y_write')
    dssCOM.ActiveBus.y_write("632", data="155.00")
    print(f'y_read-> {dssCOM.ActiveBus.y_read("632")}')
    print(f'YscMatrix-> {dssCOM.ActiveBus.YscMatrix("650")} - need test use (create Matrix)')
    print(f'Zsc0-> {dssCOM.ActiveBus.Zsc0("633")} - need test use')
    print(f'ZSC012Matrix-> {dssCOM.ActiveBus.ZSC012Matrix("632")} - need test use (create Matrix)')
    print(f'Zsc1-> {dssCOM.ActiveBus.Zsc1("633")} - need test use')
    print(f'ZscMatrix-> {dssCOM.ActiveBus.ZscMatrix("632")} - need test use (create Matrix)')
    print(f'ZscRefresh-> {dssCOM.ActiveBus.ZscRefresh("632")} - need test use')
if test_ActiveCktElement == 1:
    #need review
    print(f'AllPropertyNames-> {dssCOM.ActiveCktElement.AllPropertyNames("Load.634a")}')
    print(f'AllVariableNames-> {dssCOM.ActiveCktElement.AllVariableNames("Load.634a")} - need test use')
    print(f'AllVariableValues-> {dssCOM.ActiveCktElement.AllVariableValues("Load.634a")} - need test use')
    print(f'BusNames_read-> {dssCOM.ActiveCktElement.BusNames_read()} - review')
    dssCOM.ActiveCktElement.BusNames_write("Load.671", "632.1" ) #REVIEW
    print(f'BusNames_read-> {dssCOM.ActiveCktElement.BusNames_read()} - review')
    print(f'Close-> {dssCOM.ActiveCktElement.Close("Line.645646")} - review need test using')
if test_ActiveClas == 1:
    print(f'AllBusNames-> {dssCOM.ActiveClass.AllNames("load")}')
    print(f'First-> {dssCOM.ActiveClass.First("load")}')
    print(f'Next-> {dssCOM.ActiveClass.Next("load")}')
    print(f'Name-> {dssCOM.ActiveClass.Name_read("load")}')
    print(f'NumElements-> {dssCOM.ActiveClass.NumElements("load")}')
    print(f'ActiveClassName-> {dssCOM.ActiveClass.ActiveClassName()}')
    print(f'Count-> {dssCOM.ActiveClass.Count("load")}')
    print(f'ActiveClassParent-> {dssCOM.ActiveClass.ActiveClassParent("vsource")}')
if test_ActiveDSSElement == 1:
    print(f'AllPropertyNames-> {dssCOM.ActiveDSSElement.AllPropertyNames("Line")}')
    print(f'Name-> {dssCOM.ActiveDSSElement.Name()}')
    print(f'NumProperties-> {dssCOM.ActiveDSSElement.NumProperties()}')
    print(f'Properties_read-> {dssCOM.ActiveDSSElement.Properties_read("element")}')
    print(f'Properties_write-> {dssCOM.ActiveDSSElement.Properties_write("element", "Line.671680")} - review')
    print(f'Properties_read-> {dssCOM.ActiveDSSElement.Properties_read("element")}')
if test_Capacitor == 1:
    print(f'AllNames-> {dssCOM.Capacitor.AllNames()}')
    print(f'AvailableSteps-> {dssCOM.Capacitor.AvailableSteps()} - need used test')
    print(f'Close-> {dssCOM.Capacitor.Close()} - need used test')
    print(f'Count-> {dssCOM.Capacitor.Count()}')
    print(f'First-> {dssCOM.Capacitor.First()}')
    print(f'IsDelta-> {dssCOM.Capacitor.IsDelta()}')
    print(f'kV-> {dssCOM.Capacitor.kV()} - (read/write)')
    print(f'Name-> {dssCOM.Capacitor.Name()} - (read/write)')
    print(f'Next-> {dssCOM.Capacitor.Next()}')
    print(f'NumSteps-> {dssCOM.Capacitor.NumSteps()} - (read/write)')
    #print(f'Open-> {dssCOM.Capacitor.Open()}')
    print(f'States-> {dssCOM.Capacitor.States()} - (read/write)')

if test_Circuit == 1:
    print(f'ActiveBus-> {dssCOM.Circuit.ActiveBus("650")}')
    print(f'ActiveCktElement-> {dssCOM.Circuit.ActiveCktElement()}')
    print(f'AllBusDistances-> {dssCOM.Circuit.AllBusDistances()}')
    #print(f'AllBusVmag->\n {dssCOM.Circuit.AllBusVmag()}')
    #print(f'AllBusVmagPU->\n {dssCOM.Circuit.AllBusVmagPu()}')
    #print(f'AllBusVolts->\n {dssCOM.Circuit.AllBusVolts()}')
    #print(f'AllElementLosses->\n {dssCOM.Circuit.AllElementLosses()}')
    #print(f'AllNodeDistances->\n {dssCOM.Circuit.AllNodeDistances()}')
    print(f'Capacity-> {dssCOM.Circuit.Capacity()} - need test using')
    print(f'Disable-> {dssCOM.Circuit.Disable("Load.634a")}')
    print(f'Ebable-> {dssCOM.Circuit.Enable("Load.634a")}')
    print(f'LineLosses->{dssCOM.Circuit.LineLosses()}' )
    print(f'Losses->{dssCOM.Circuit.Losses()}')
    print(f'NumBuses->{dssCOM.Circuit.NumBuses()}')
    print(f'NumCktElements->{dssCOM.Circuit.NumCktElements()}')
    print(f'NumNodes->{dssCOM.Circuit.NumNodes()}')
    print(f'SetActiveBusi->{dssCOM.Circuit.SetActiveBusi(55)}')
    print(f'SubstationLosses->{dssCOM.Circuit.SubstationLosses()}')
    #print(f'SystemY\n->{dssCOM.Circuit.SystemY()}')
    print(f'TotalPower->{dssCOM.Circuit.TotalPower()}')
    print(f'Ycurrents\n->{dssCOM.Circuit.YCurrents(polar=True)}')
    print(f'YNodeOrder\n->{dssCOM.Circuit.YNodeOrder()}')
    print(f'YNodeVarray\n->{dssCOM.Circuit.YNodeVarray()}')
if test_Lines == 1:
    print(f'Lines->{dssCOM.Lines.AllNames()}')
    dssCOM.Lines.First()
    print(f'Name->{dssCOM.Lines.Name()}')
    print(f'Lines->{dssCOM.Lines.AllNames()}')
    print(f'Bus1_read->{dssCOM.Lines.Bus1_read()}')
    #print(f'Bus1_write->{dssCOM.Lines.Bus1_write("671")}')
    #print(f'Bus1_read->{dssCOM.Lines.Bus1_read()}')

    print(f'Bus2_read->{dssCOM.Lines.Bus2_read()}')
    #print(f'Bus2_write->{dssCOM.Lines.Bus2_write("670")}')
    #print(f'Bus2_read->{dssCOM.Lines.Bus2_read()}')

    print(f'C0_read->{dssCOM.Lines.C0_read()}')
    print(f'C0_write->{dssCOM.Lines.C0_write(0.005)}')
    print(f'C0_read->{dssCOM.Lines.C0_read()}')

    print(f'C1_read->{dssCOM.Lines.C1_read()}')
    print(f'C1_write->{dssCOM.Lines.C1_write(0.005)}')
    print(f'C1_read->{dssCOM.Lines.C1_read()}')

    print(f'CMatrix->{dssCOM.Lines.Cmatrix()}')
    print(f'Count->{dssCOM.Lines.Count()}')
    print(f'EmergAmps->{dssCOM.Lines.EmergAmps_read()}')
    print(f'EmergAmps Write->{dssCOM.Lines.EmergAmps_write()}')
    print(f'EmergAmps->{dssCOM.Lines.EmergAmps_read()}')
    print(f'Geometry->{dssCOM.Lines.Geometry()} - need test used read/write')
    print(f'Length->{dssCOM.Lines.Length_read()}')
    print(f'Length_write->{dssCOM.Lines.Length_write(5000)}')
    print(f'Length->{dssCOM.Lines.Length_read()}')
    print(f'LineCode->{dssCOM.Lines.LineCode()} - need test used read/write')
    print(f'NormAmps->{dssCOM.Lines.NormAmps_read()}')
    print(f'NormAmps Write->{dssCOM.Lines.NormAmps_write()}')
    print(f'NormAmps->{dssCOM.Lines.NormAmps_read()}')
    print(f'NumCust->{dssCOM.Lines.NumCust()} - need test using')
    print(f'Parent->{dssCOM.Lines.Parent()} - need test using')
    print(f'Phases->{dssCOM.Lines.Phases_read()}')
    #print(f'Phases Write->{dssCOM.Lines.Phases_write(4)}')
    #print(f'Phases->{dssCOM.Lines.Phases_read()}')
    print(f'Rmatrix_read\n->{dssCOM.Lines.Rmatrix_read()}')
    print(f'Rmatrix_write\n->{dssCOM.Lines.Rmatrix_write(dssCOM.Lines.Rmatrix_read())}')
    print(f'Rmatrix_read\n->{dssCOM.Lines.Rmatrix_read()}')
    print(f'SeasonRating->{dssCOM.Lines.SeasonRating()}')
    print(f'Spacing_read->{dssCOM.Lines.Spacing_read()} - need test using')
    print(f'TotalCust->{dssCOM.Lines.TotalCust()} - need test using')
    print(f'Units_read->{dssCOM.Lines.Units_read()}')
    dssCOM.Lines.Units_write(4)
    print(f'Units_read->{dssCOM.Lines.Units_read()}')
    print(f'Yprim\n->{dssCOM.Lines.Yprim()}')



#dssCOM.Text.Command("plot circuit Power max=2000 n n C1=$00FF0000")
#dss.Text.Command('Show Voltage')













