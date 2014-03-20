#coding:utf8

print("ding ni de fei")

from socket import AF_INET, SOCK_STREAM, socket
import struct, json

def connect_to_netservice():
    HOST = 'localhost'
    PORT = 22222
    ADDR = (HOST, PORT)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    return client
#end def


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


def send_data(data):
    client = connect_to_netservice()
    client.sendall(sendData(data))
    recvdata = client.recv(1024)
    data = resolveRecvdata(recvdata)
    print("recieve data: %s" % data)
    client.close()
#end def


def test():
    send_data(json.dumps({"username":"test1", "password":"999999"}), 800)
#end def


def login():
    sendData(json.dumps({"user_id":0}), 900)
#end def


if __name__ == "__main__":
    print("i am here")
    login()
#     print("ma la ge bi")
#     login()
#     recvdata = client.recv(1024)
#     print("recvdata :", recvdata)
#     data = resolveRecvdata(recvdata)
#     print(data)
    


