#coding:utf8

from firefly.server.globalobject import GlobalObject
from twisted.python import log


from net.netconfig import config_datapack
config_datapack()


from net.netlocalservice import net_localservice_handle
@net_localservice_handle
def call_gate_0(targetKey, conn, requestData):
    '''
    '''    
#     print(requestData)
    d = GlobalObject().remote["gate"].callRemote("reply_net_call", targetKey, conn.transport.sessionno, requestData)
    return d
#end def