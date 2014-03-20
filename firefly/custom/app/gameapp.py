#coding:utf8

from firefly.server.globalobject import remoteserviceHandle, GlobalObject


def game1_command(conn, data):
    print("game1  ***  game1_command(), data = %s" % data)
    return "ni yong yuan bu dong wo shang bei"

    

@remoteserviceHandle("gate")
def game1_side(conn, data):
    return game1_command(conn, data)