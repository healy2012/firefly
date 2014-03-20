#coding:utf8

from firefly.server.globalobject import GlobalObject
from firefly.dbentrust.madminanager import MAdminManager

from firefly.dbentrust.memclient import mclient

mclient.flush_all()

def do_when_stop():
    """ before shutdown service
    """
    MAdminManager().checkAdmins()
    
#
GlobalObject().stophandler = do_when_stop



# user data
from data.userdataconfig import registe_user_admin, check_user_admin, DELTA
registe_user_admin()
check_user_admin(DELTA)


