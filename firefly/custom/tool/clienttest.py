#coding:utf8

from socket import AF_INET, SOCK_STREAM, socket
import struct, json

def connect_to_netservice():
    HOST = 'localhost'
    PORT = 22222
    ADDR = (HOST, PORT)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    return client
#end connect_to_netservice


def sendData(send_str, command_ID):
    HEAD_0 = chr(55)
    HEAD_1 = chr(66)
    HEAD_2 = chr(77)
    HEAD_3 = chr(88)
    ProtoVersion = chr(99)
    ServerVersion = 1

    send_str = send_str
    data = struct.pack("!sssss3I",
                        HEAD_0,
                        HEAD_1,
                        HEAD_2,
                        HEAD_3,
                        ProtoVersion,
                        ServerVersion,
                        len(send_str) + 4,
                        command_ID) 
    send_data = data + send_str
    return send_data
#end sendData


def resolveRecvdata(data):
    head = struct.unpack("!sssss3I", data[:17])
    length = head[6]
    _data = data[17:17 + length]
    return _data
#end resolveRecvdata


def request_data(data, command_ID):
    client = connect_to_netservice()
    client.sendall(sendData(data, command_ID))
    recvdata = client.recv(2048)
    data = resolveRecvdata(recvdata)
    print("recieve data: %s" % data)
    client.close()
#end def

# -----------------------------------------------

def login():
    print("....login()")
    request_data(json.dumps({"name":"hhhsaf"}), 1000)
#end def


def getproperties():
    print("....getproperties()")
    request_data(json.dumps({"user_id":104}), 2000)
#end def


def gettask():
    print("....gettask()")
    request_data(json.dumps({"user_id":104, "count":20}), 5000)
#end def
 
 
def gethair():
    print("....gethair()")
    request_data(json.dumps({"tableName":"tb_static_hair", "pk":"hair_id"}), 800)
#end def   


def taketask():
    print("....taketask()")
    request_data(json.dumps({"user_id":10002, "miss_id":1}), 801)
#end def


def taskdone():
    print("....taskdone()")
    request_data(json.dumps({"user_id":10002, "miss_id":1}), 802)
#end def


def taskreward():
    print("....taskreward()")
    request_data(json.dumps({"user_id":10002}), 702)
#end def   



if __name__ == "__main__":
    gettask()
#     print("ma la ge bi")
#     login()
#     recvdata = client.recv(1024)
#     print("recvdata :", recvdata)
#     data = resolveRecvdata(recvdata)
#     print(data)
    

