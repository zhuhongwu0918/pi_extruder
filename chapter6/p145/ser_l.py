import socket as sk
import multiprocessing as mp
import time as t
import os

#https://www.cnblogs.com/hardfood/p/14263412.html
def c_s_c(sock_in, addr,sock_list):             #进程出来函数
    for sock_c in sock_list.items():            #遍历字典元组
        sock_c[1].send(("user"+str(addr)+"---in---\n").encode()) #遍历通知所有在聊天室的用户有新用户进入

    while True:
        readdata = sock_in.recv(1024) #recv函数有阻塞左作用，若连接断开或者sock被关闭，返回空
        if readdata:            
            #print(readdata)       #服务端看信息调试用
            for sock_c in sock_list.items():    
                sock_c[1].send(str(addr).encode()+readdata) #转发给所用用户
        else:
            for sock_c in sock_list.items():
                sock_c[1].send(("user"+str(addr)+"---out---").encode())  #encode编码为字节序
            del sock_list[addr]#将退出的用户从字典中删除
            sock_in.close()
            os._exit(0)#终止进程
            break#摆设用
            
def main():
    s = sk.socket(sk.AF_INET ,sk.SOCK_STREAM)
    s.bind(('',2333))
    s.listen()
    sock_list=mp.Manager().dict() #共享内存字典--------------------------------
    while True:
        sock,addr = s.accept()
        sock_list[addr]=sock    #将地址作为索引--------------------------------
        t1 = mp.Process(target=c_s_c, args=(sock, addr,sock_list)) #多进程------
        t1.start()

if __name__ == '__main__':
    main()