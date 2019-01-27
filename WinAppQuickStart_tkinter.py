#coding=utf-8
import os
import time
import platform
import subprocess
from tkinter import *
from datetime import datetime


def UsePlatform():
  sysstr = platform.system()
  if(sysstr =="Windows"):
    return 1
  elif(sysstr == "Linux"):
    return 2
  else:
    return 3#other system

def Callback_taskmgr():
    cmd = "taskmgr.exe"
    os.popen(cmd)

def Callback_devmgmt():
    cmd = "devmgmt.msc"
    os.popen(cmd)
def Callback_calc():
    cmd = "calc"
    os.popen(cmd)

def Callback_control():
    cmd = "control"
    os.popen(cmd)

def Callback_explorer():
    cmd = "explorer"
    os.popen(cmd)

def Callback_inetcpl():
    cmd = "inetcpl.cpl"
    os.popen(cmd)

def Callback_Mouse():
    cmd = "main.cpl"
    os.popen(cmd)

def Callback_msinfo32():
    cmd = "msinfo32"
    os.popen(cmd)

def Callback_mspaint():
    cmd = "mspaint"
    os.popen(cmd)

def Callback_mstsc():
    cmd = "mstsc"
    os.popen(cmd)

def Callback_networkLink():
    cmd = "ncpa.cpl"
    os.popen(cmd)

def Callback_notepad():
    cmd = "notepad"
    os.popen(cmd)

def Callback_regedit():
    cmd = "regedit.exe"
    os.popen(cmd)

def Callback_systemAttr():
    cmd = "sysdm.cpl"
    os.popen(cmd)

def Callback_winver():
    cmd = "winver"
    os.popen(cmd)

def Callback_attributes():
    global flag
    if flag == 0:
        flag = 1
        top.attributes("-topmost", 0)#top
    else:
        flag = 0
        top.attributes("-topmost", 1)#top


flag = 0
btn_names =[]
btn_names_1 = ["设备管理器","任务管理器","计算器"]
btn_names_2 = ["控制面板","资源管理器 ","Internet属性 "]
btn_names_3 = ["鼠标属性","系统信息 ","画图 "]
btn_names_4 = ["远程桌面连接","网络连接 ","打开记事本 "]
btn_names_5 = ["注册表 ","系统属性 ","关于Windows"]

btn_names_6 = ["鼠标属性","系统信息 ","画图 "]
btn_names_7 = ["鼠标属性","系统信息 ","画图 "]
btn_names.append(btn_names_1)
btn_names.append(btn_names_2)
btn_names.append(btn_names_3)
btn_names.append(btn_names_4)
btn_names.append(btn_names_5)
#     print(btn_names)

btn_func=[]
btn_func_1  = [Callback_devmgmt,Callback_taskmgr,Callback_calc]
btn_func_2  = [Callback_control,Callback_explorer,Callback_inetcpl]
btn_func_3  = [Callback_Mouse,Callback_msinfo32,Callback_mspaint]
btn_func_4  = [Callback_mstsc,Callback_networkLink,Callback_notepad]
btn_func_5  = [Callback_regedit,Callback_systemAttr,Callback_winver]
btn_func.append(btn_func_1)
btn_func.append(btn_func_2)
btn_func.append(btn_func_3)
btn_func.append(btn_func_4)
btn_func.append(btn_func_5)
#     print(btn_func)

if __name__ == '__main__':
    top = Tk()
    #~ top.geometry('305x300')
    top.resizable(height=False,width=False)
    top.title(string=u'QuickRun')
    if 1 == UsePlatform():
    	top.attributes("-toolwindow", 1)#Toolbar style，this Property is only for windows，linux can not use
    top.attributes("-topmost", 1)#top
    top.attributes("-alpha",1)#transparency

    for i in range(len(btn_names)):#row
        for j in range(len(btn_names[i])):#column
            Button(top, text =btn_names[i][j], command = btn_func[i][j],width=13).grid(row=i,column=j)
    Button(top, text ="置顶", command = Callback_attributes,width=13).grid(row=5,column=0)
    top.mainloop()
