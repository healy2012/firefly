#coding:utf8

from firefly.utils.singleton import Singleton


class VTUsersManager:
    '''
    虚拟角色管理器
    '''
    __metaclass__ = Singleton    

    def __init__(self):
        '''记录角色ID与客户端id的关系'''
        self.vtUsers = {}
    #end def
    
    
    def add_vtuser(self, vtUser):
        if not vtUser:
            print("vtuser must have legal value.")
            return
        
        userID = vtUser.get_userID()
        self.vtUsers[str(userID)] = vtUser
    #end def
    
    
    def get_vtUser_by_userID(self, userID):
        return self.vtUsers[userID]
    #end def
        
    
    def get_vtUser_by_clientID(self, clientID):
        for vtUser in self.vtUsers.values():
            if vtUser.get_clientID == clientID:
                return vtUser
        
        return
    #end def
    
    
    def drop_vtUser_by_userID(self, userID):
        try:
            del self.vtUsers[userID]
        finally:
            pass
    #end def
    
    
    def drop_vtUser_by_clientID(self, clientID):
        try:
            vtUser = self.get_vtUser_by_clientID(clientID)
            if vtUser:
                userID = vtUser.get_userID
                del self.vtUsers[userID]
        finally:
            pass
    #end def
    
    
    def get_node_by_userID(self, userID):
        vtUser = self.vtUsers[userID]
        return vtUser.get_node()
    #end def
    
    
    def get_node_by_clientID(self, clientID):
        vtUser = self.get_vtUser_by_clientID(clientID)
        if vtUser:
            return vtUser.get_node()
        
        return
    #end def
    
    
    def get_clientID_by_userID(self, userID):
        vtUser = self.get_vtUser_by_userID(userID)
        if vtUser:
            return vtUser.get_clientID()
        
        return -1
    #end def
    
    
    def get_userID_by_clientID(self, clientID):
        vtUser = self.get_vtUser_by_clientID(clientID)
        if vtUser:
            return vtUser.get_userID()
        
        return -1
    #end def
    
    
    
    