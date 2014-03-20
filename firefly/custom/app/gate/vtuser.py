#coding:utf8


class VTUser(object):
    '''
    虚拟角色类，只是记录角色当前所在的节点
    '''
    def __init__(self, clientID, userID, node = "gate"):
        '''初始化
        @param characterId: int 角色的id
        @param dynamicId: int 角色的客户端ID
        @param node: int 角色所在节点服务的id
        @param locked: bool 角色的锁定状态
        @param fubenID: 所在副本
        '''
        self.clientID = clientID
        self.userID = userID
        self.node = node
        self.locked = False
        self.fubenID = 0
    #end def
    
    
    def get_clientID(self):
        return self.clientID
    #end def
    
    
    def set_clientID(self, clientID):
        self.clientID = clientID
    #end def
    
    
    def get_userID(self):
        return self.userID
    #end def
    
    
    def set_userID(self, userID):
        self.userID = userID
    #end def
    
    
    def get_locked(self):
        return self.locked
    #end def
    
    
    def lock(self):
        self.locked = True
    #end def
    
    
    def release(self):
        self.locked = False
    #end def
    
    
    def get_node(self):
        return self.node
    #end def
    
    
    def set_node(self, node):
        '''
        设置角色的节点服务ID
        '''
        self.node = node
    #end def
    
    
    def get_fubenID(self):
        return self.fubenID
    #end def
    
    
    def set_fubenID(self, fubenID):
        self.fubenID = fubenID
    #end def
    
        
    def init_data(self):
        pass
    #end def

#end class

# from data.userdataconfig import get_user_info
from ..data.datautils import check_user
def create_user(mac_addr, custom_id, clientID = -1):
#     dicInfo = get_user_info()
#     macAddr = dicInfo.get("mac_addr")
#     customID = dicInfo.get("custom_id")
    checkResoult = check_user(mac_addr, custom_id)
    print(checkResoult)
    if not checkResoult:
        vtuser = VTUser(clientID,)
    else:
        pass
#     return checkResoult
#end def

