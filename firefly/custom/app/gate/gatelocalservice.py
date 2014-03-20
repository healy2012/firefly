#coding:utf8

from firefly.utils.services import CommandService
from twisted.internet import defer
from twisted.python import log
import json

from ..data.JSONEncoder import CJsonEncoder
from ..data import datautils

from ..data import commondata



class GateLocalService(CommandService):
    
    def callTargetSingle(self,targetKey,*args,**kw):
        '''call Target by Single
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        
        self._lock.acquire()
        try:
            target = self.getTarget(targetKey)
            if not target:
                log.err('the command '+str(targetKey)+' not Found on service')
                return None
            if targetKey not in self.unDisplay:
                log.msg("call method %s on service[single]"%target.__name__)
            defer_data = target(targetKey,*args,**kw)
            if not defer_data:
                return None
            if isinstance(defer_data,defer.Deferred):
                return defer_data
            d = defer.Deferred()
            d.callback(defer_data)
        finally:
            self._lock.release()
        return d
    #end def
    
#end class

gateLocalService = GateLocalService("gateLocalService")

def gate_localservice_handle(target):
    gateLocalService.mapTarget(target)
#end def


# 用户登陆
@gate_localservice_handle
def gate_localservice_1000(targetKey, clientID, requestData):
    response = {}
    response[commondata.rev_data] = {}
    
    argument = json.loads(requestData)
    name = argument.get("name")
    
    resoult = datautils.check_user(name)
    if not resoult:
        resoult = datautils.create_mcuser(name)
        response[commondata.rev_data] = resoult
    else:
        response[commondata.rev_data] = resoult
    
    response[commondata.command_id] = targetKey
    return json.dumps(response, cls = CJsonEncoder)
#end def


# 所有道具
@gate_localservice_handle
def gate_localservice_2000(targetKey, clientID, requestData):
    argument = json.loads(requestData)
    userId = argument.get("user_id")
    response = {}
    resoult = datautils.get_user_item(userId)
    if resoult:
        response[commondata.state_code] = 0
        response[commondata.rev_data] = resoult
    else:
        response[commondata.state_code] = 1
        response[commondata.rev_data] = {}
    
    response[commondata.command_id] = targetKey
    return json.dumps(response, cls = CJsonEncoder)
#end def


# 买道具
@gate_localservice_handle
def gate_localservice_3000(targetKey, clientID, requestData):
    argument = json.loads(requestData)
    user_id = argument.get("user_id")
    item_id = argument.get("item_id")
    
    response = {}
    response[commondata.rev_data] = {}
    resoult = datautils.buy_item(user_id, item_id)
    if resoult:
        response[commondata.state_code] = 0
    else:
        response[commondata.state_code] = 1
    
    response[commondata.rev_data] = resoult
    response["item_id"] = item_id
    response[commondata.command_id] = targetKey
    return json.dumps(response, cls = CJsonEncoder)
#end def


# 排名
@gate_localservice_handle
def gate_localservice_4000(targetKey, clientID, requestData):
    argument = json.loads(requestData)
    userId = argument.get("user_id")
    response = {}
    resoult = datautils.get_user_ranking(userId)
    if resoult:
        response[commondata.state_code] = 0
        response[commondata.rev_data] = resoult
    else:
        response[commondata.state_code] = 1
        response[commondata.rev_data] = {}
    
    response[commondata.command_id] = targetKey
    return json.dumps(response, cls = CJsonEncoder)
#end def


# 上传战斗结果
@gate_localservice_handle
def gate_localservice_5000(targetKey, clientID, requestData):
    argument = json.loads(requestData)
    userId = argument.get("user_id")
    count = argument.get("count")
    
    response = {}
    resoult = datautils.set_resoult(userId, count)
    if resoult:
        response[commondata.state_code] = 0
        response[commondata.rev_data] = resoult
    else:
        response[commondata.state_code] = 1
        response[commondata.rev_data] = {}
    
    response[commondata.command_id] = targetKey
    return json.dumps(response, cls = CJsonEncoder)
#end def








