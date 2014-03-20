#coding:utf8

from firefly.server.globalobject import GlobalObject
from firefly.netconnect.datapack import DataPackProtoc

HEAD_0 = 55
HEAD_1 = 66
HEAD_2 = 77
HEAD_3 = 88
ProtoVersion = 99
ServerVersion = 1

def config_datapack():
    datapack = DataPackProtoc(HEAD_0, HEAD_1, HEAD_2, HEAD_3, ProtoVersion, ServerVersion)
    GlobalObject().netfactory.setDataProtocl(datapack)
