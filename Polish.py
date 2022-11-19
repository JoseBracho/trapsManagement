from module.snmp import SNMP
from module.telegramBot import Message

class Polish: 
    
    def cleanUP(oid, device, event):
        #Port event
        if(event == 'linkUp' or event == 'linkDown'):
            oi = f'{oid}'.rstrip('\n').split('\n')[-1].strip().split('=')
            if oi[0] == 'string':
                if not ('.' in oi[1]):
                    getOid = f'{oid}'.rstrip('\n').split('\n')[1].split('=')[1]
                    position = getOid.rindex('.')
                    ifIndex = getOid[position:]
                    snmp1 = SNMP()
                    snmp2 = SNMP()
                    portDescription = snmp1.getPortDetails(device, ifIndex)
                    hostname = snmp2.getPortDetails(device)
                    if(oi[1][0] == 'a'):
                        msj = f'IP: {device}\nHostname: {hostname}\nPortChannel: {oi[1]}\nDescripcion: {portDescription}\nEstado: {event}'
                        Message.sendMessage(msj)
                    else:
                        msj = f'IP: {device}\nHostname: {hostname}\nPuerto: {oi[1]}\nDescripcion: {portDescription}\nEstado: {event}'
                        Message.sendMessage(msj)