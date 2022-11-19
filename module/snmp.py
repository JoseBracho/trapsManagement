from pysnmp.entity.rfc3413.oneliner import cmdgen

class SNMP:
    
    def __init__(self) -> None:
        self.SYSNAME = '1.3.6.1.2.1.1.5.0'
        self.PORTDESCRIPTION = '1.3.6.1.2.1.31.1.1.1.18'
        self.COMMUNITY = 'public'
        
    def getPortDetails(self, host, ifIndex = ''):
        if ifIndex != '':
            oid = f'{SNMP.PORTDESCRIPTION}{ifIndex}'
        else:
            oid = self.SYSNAME
        auth = cmdgen.CommunityData(self.COMMUNITY)
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            auth,
            cmdgen.UdpTransportTarget((host, 161)),
            cmdgen.MibVariable(oid),
            lookupMib=False,
        )
        for oid, val in varBinds:
            response = val.prettyPrint()
        return response