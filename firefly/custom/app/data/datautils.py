#coding:utf8

from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor

from ..data import userdataconfig
from ..data import templatedataconfig

from ..data import commondata



def check_user(name):
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass = DictCursor)
    resoult = {}
    if name:
        sql = u"select * from `tb_user_info` where `name` = '%s'" % (name)
        cursor.execute(sql)
        resoult = cursor.fetchone()

    cursor.close()
    conn.close()
    print("search user_id, resoult = ", resoult)
    return resoult
#end def


def create_mcuser(name):
    dic = {"user_id":0, "name":name}
    mmode1 = userdataconfig.admin_by_tablename("tb_user_info").new(dic)
    mmode1.syncDB()
    
    data = check_user(name)
    user_id = data.get("user_id")
    
    dic["user_id"] = user_id
    mmode2 = userdataconfig.admin_by_tablename("tb_user_ranking").new(dic)
    mmode2.syncDB()
    
    return data
#end def


def get_user_item(user_id):
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass = DictCursor)
    resoult = {}
    if user_id:
        sql = u"select * from `tb_user_item` where `user_id` = '%d'" % (user_id)
        cursor.execute(sql)
        resoult = cursor.fetchall()

    cursor.close()
    conn.close()
#     print("search user_id, resoult = ", resoult)
    return resoult
#end def


def buy_item(user_id, item_id):
    tb_template_item = templatedataconfig.admin_by_tablename("tb_template_item")
    record_item = templatedataconfig.get_static_record(tb_template_item, item_id)
#     print("record_item ===== ", record_item)
    
    tb_user_info = userdataconfig.admin_by_tablename("tb_user_info")
    record_user = userdataconfig.get_user_data(tb_user_info, user_id)
#     print("record_user ====== ", record_user)
    money = record_user.get("money") - record_item.get("money")
    if money < 0:
        return None
    
    props = {}
    props["hitpoints"] = record_user.get("hitpoints") + record_item.get("hitpoints")
    props["damage"] = record_user.get("damage") + record_item.get("damage")
    props["money"] = money
    
    userdataconfig.set_user_value(tb_user_info, user_id, props)
    resoult = userdataconfig.get_user_data(tb_user_info, user_id)
    
    pro = {}
    pro["item_id"] = item_id
    pro["user_id"] = user_id
    mmode = userdataconfig.admin_by_tablename("tb_user_item").new(pro)
    mmode.syncDB()
#     print("mmode.data ==== ", mmode.get("data"))
    
    return resoult
#end def


def create_nickname(user_id, nick_name):
    tb_admin = userdataconfig.admin_by_tablename("tb_user_info")
    props = {}
    props['nick_name'] = nick_name
    return userdataconfig.set_user_value(tb_admin, user_id, props)
#end def


def get_user_ranking(user_id):
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass = DictCursor)
#     u"select `%s` from `%s` order by %s asc" % (pk, tableName, pk)
    sql = u"select * from tb_user_ranking order by score desc"
    
    cursor.execute(sql)
    resoult = cursor.fetchall()
    
    cursor.close()
    conn.close()
#     print("4000 resoult ==== ", resoult)
    return resoult
#end def


def set_resoult(user_id, count):
    
    tb_user_info = userdataconfig.admin_by_tablename("tb_user_info")
    record_user = userdataconfig.get_user_data(tb_user_info, user_id)
    
    props = {}
    props["money"] = count * 50 + record_user["money"]
    userdataconfig.set_user_value(tb_user_info, user_id, props)
    
    pro = {}
    pro["score"] = count * 20
    
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass = DictCursor)
    resoult = 0
    if user_id:
        sql = u'select * from tb_user_ranking where user_id=%d' % (user_id)
        cursor.execute(sql)
        resoult = cursor.fetchone()

    cursor.close()
    conn.close()
    
    tb_user_ranking = userdataconfig.admin_by_tablename("tb_user_ranking")
    index = resoult["index"]
    record_ranking = userdataconfig.get_user_data(tb_user_ranking, index)
    userdataconfig.set_user_value(tb_user_ranking, index, pro)
    
    return userdataconfig.get_user_data(tb_user_info, user_id)
#end def


def set_user_info(pKValue, props):
    userdataconfig.set_user_value(userdataconfig.admin_by_tablename("tb_user_info"), pKValue, props)
#end def








