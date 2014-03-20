#coding:utf8


from firefly.server.globalobject import GlobalObject, rootserviceHandle
from gate.gatelocalservice import gateLocalService

# @rootserviceHandle
def gate_side(conn, data):
    print("gateapp  ***  send_to_game1()")
    d = GlobalObject().root.callChild("game1", "game1_side", conn, data)
#     d = GlobalObject().remote["game1"].callRemote("game1_side", conn, data)
    return d
#end def


@rootserviceHandle
def reply_net_call(targetKey, clientID, requestData):
    print("gateapp  ***  reply_net_call()")
    if gateLocalService._targets.has_key(targetKey):
        return gateLocalService.callTarget(targetKey, clientID, requestData)
    else:
        print("not found the target with key:%s" % targetKey)
#end def



