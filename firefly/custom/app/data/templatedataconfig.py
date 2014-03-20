#coding:utf8

from firefly.dbentrust.mmode import MAdmin
from commondata import arr_tb_name_template, arr_key_name_template


arr_id_list = []
arr_tb_static = []

def init_globals():
    for i in xrange(0, len(arr_tb_name_template)):
        arr_id_list.append(())
        #
        tb_admin = MAdmin(arr_tb_name_template[i], arr_key_name_template[i], incrky = arr_key_name_template[i])
        tb_admin.insert()
        arr_tb_static.append(tb_admin)
#end def

init_globals()



from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor


def admin_by_tablename(tableName):
    for tb in arr_tb_name_template:
        if tb == tableName:
            index = arr_tb_name_template.index(tb)
            return arr_tb_static[index]
#end def


def get_static_data_pklist(tableName, pk):
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass = DictCursor)
#     pkList = []
    if tableName:
        sql = u"select `%s` from `%s` order by %s asc" % (pk, tableName, pk)
    
    cursor.execute(sql)
    pkList = cursor.fetchall()
#     print("pkList = ", pkList)
    cursor.close()
    conn.close()
    return pkList
#end def


def get_static_wholetable(tableName):
#     global arr_tb_staticName
#     global arrPkName
#     global arr_id_list
    index = -1
    table = None
    rtnData = []
    
    for tbName in arr_tb_name_template:
        if tbName == tableName:
            try:
                index = arr_tb_name_template.index(tableName)
            finally:
                break
    
    if index >= 0:
        if not arr_id_list[index]:
            pk_list = get_static_data_pklist(tableName, arr_key_name_template[index])
            arr_id_list[index] = pk_list
#         table = admin_by_tableName(tableName)
        table = arr_tb_static[index]
    
    for dicPK in arr_id_list[index]:
        pkValue = dicPK.get(arr_key_name_template[index])
        if pkValue:
            record = table.getObjData(pkValue)
#             print("pkValue ============= ", pkValue)
            if record:
                rtnData.append(record)
    return rtnData
#end def


def get_static_record(tb_admin, pkValue):
#     print("pkValue ===== ", pkValue)
    if not tb_admin:
#         print("get_static_record ****** tb_admin is None")
        return None
    
    record = tb_admin.getObjData(pkValue)
#     print("get_static_record ****** record === ", record)

    return record
#end def

















