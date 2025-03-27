import socket

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip_add  ="192.168.217.191"
port = 1228
complete = (ip_add, port)
message = input ("love's yaa")
encode_mgs=message.encode('ascii')
s.sendto(encode_mgs,complete )

