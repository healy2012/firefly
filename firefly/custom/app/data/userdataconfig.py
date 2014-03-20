#coding:utf8

from firefly.dbentrust.mmode import MAdmin
from firefly.dbentrust.madminanager import MAdminManager
from commondata import arr_tb_name_user 


arrUserTable = []

def init_globals():
    print("init_globals()")
    for i in xrange(0, len(arr_tb_name_user)):
        key = ""
        if i == 0:
            key = "user_id"
        else:
            key = "index"
        tb_admin = MAdmin(arr_tb_name_user[i], key, incrky = key)
        tb_admin.insert()
        arrUserTable.append(tb_admin)
#end def

init_globals()



def registe_user_admin():
    for tb_admin in arrUserTable:
        MAdminManager().registe(tb_admin)
#end def


DELTA = 1800

from twisted.internet import reactor
reactor = reactor


def admin_by_tablename(tableName):
    for tb in arr_tb_name_user:
        if tb == tableName:
            index = arr_tb_name_user.index(tb)
            return arrUserTable[index]
#end def


def check_user_admin(DELTA):
    MAdminManager().checkAdmins()
    reactor.callLater(DELTA, check_user_admin, DELTA)
#end def


def get_user_data(tb_admin, pkValue):
    if tb_admin == None:
        print("get_user_data  ***  not found table")
        return None
#     print("pKey === ", pkValue)
    
    dicData = tb_admin.getObjData(pkValue)
#     print("dicData ==== ", dicData)
    return dicData
#end def


def get_user_value(tb_admin, pKey, key):
    values = get_user_data(tb_admin, pKey)
#     print("values ========== \n", values)
    if values:
        return values.get(key)
    
    return
#end def


def set_user_value(tb_admin, pKValue, props):
    if not tb_admin:
        return False
    
    mmode = tb_admin.getObj(pKValue)
    mmode.update_multi(props)
    mmode.syncDB()
    return True
#end def







