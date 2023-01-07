import openpy_fx_tools_dss as fx_tools


dss = fx_tools.COM_DLL()

path = r"C:\Users\tote_\OneDrive\Escritorio\test_lib\IEEE13Node.dss"


dss.Text.Command(f'Compile {path}')
dss.Text.Command('solve')

test_ActiveBus = 1

if test_ActiveBus == 1:
    print(f'AllPCEatBus={dss.ActiveBus.AllPCEatBus("634")}')
    print(f'AllPDEatBus={dss.ActiveBus.AllPDEatBus("634")}')
    print(f'Coorddefined={dss.ActiveBus.Coorddefined("650")}')
    print(f'CplxSeqVoltages={dss.ActiveBus.CplxSeqVoltages("650", rect=True)}')
    print(f'Cust_Duration={dss.ActiveBus.cust_duration("650")} -> test use')
    print(f'Cust_Interrupts={dss.ActiveBus.cust_interrupts("650")} -> test use')
    print(f'Distance={dss.ActiveBus.distance("632")} -> test use')
    print(f'GetUniqueNodeNumber={dss.ActiveBus.get_unique_node_number("633")}')
    print(f'Int_Duration={dss.ActiveBus.int_duration("611")} -> test use')
    print(f'Isc={dss.ActiveBus.Isc_Icc("633")} - need test use')
    print(f'kvBase={dss.ActiveBus.kVBase("611")}')
    print(f'Lambda={dss.ActiveBus.Lambda("611")} - need test use')
    print(f'Latitude={dss.ActiveBus.latitude("650")} - development')
    print(f'LineList={dss.ActiveBus.line_list("632")}')
    print(f'LoadList={dss.ActiveBus.load_list("634")}')
    print(f'N_Customers={dss.ActiveBus.n_customers("650")} - need test use')
    print(f'N_Interrupts={dss.ActiveBus.n_interrupts("634")} - need test use')
    print(f'Name={dss.ActiveBus.name("633")}')
    print(f'Nodes={dss.ActiveBus.nodes("633")}')
    print(f'Nodes={dss.ActiveBus.nodes("611")}')
    print(f'NumNodes={dss.ActiveBus.num_nodes("633")}')
    print(f'NumNodes={dss.ActiveBus.num_nodes("611")}')

    print(f'dss.Latitude_read={dss.ActiveBus.Latitude_read("633")}')
    dss.ActiveBus.Latitude_write("633", data="0.1")
    print(f'dss.Latitude_read={dss.ActiveBus.Latitude_read("633")}')
    print(f'dss.Latitude_read={dss.ActiveBus.Latitude_read("633")}')

    print(a)


#dss.Text.Command('Show Voltage')













