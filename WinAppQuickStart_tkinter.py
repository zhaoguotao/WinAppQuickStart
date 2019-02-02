#coding=utf-8
'''
os.popen(cmd) vs os.system(cmd):
os.popen(cmd)无法再纯GUI程序中使用，就是说只能用pyinstaller -F -c 生成exe，如果用-w，则os.popen(cmd)命令无法执行。而os.system(cmd)可以使用-w编译成exe。
'''
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
    cmd = "start /b taskmgr.exe"
#     os.popen(cmd)
    os.system(cmd)

def Callback_devmgmt():
    cmd = "start /b devmgmt.msc"
#     os.popen(cmd)
    os.system(cmd)
    
def Callback_calc():
    cmd = "start /b calc"
#     os.popen(cmd)
    os.system(cmd)

def Callback_control():
    cmd = "start /b control"
#     os.popen(cmd)
    os.system(cmd)

def Callback_explorer():
    cmd = "start /b explorer"
#     os.popen(cmd)
    os.system(cmd)

def Callback_inetcpl():
    cmd = "start /b inetcpl.cpl"
#     os.popen(cmd)
    os.system(cmd)

def Callback_Mouse():
    cmd = "start /b main.cpl"
#     os.popen(cmd)
    os.system(cmd)

def Callback_msinfo32():
    cmd = "start /b msinfo32"
#     os.popen(cmd)
    os.system(cmd)

def Callback_mspaint():
    cmd = "start /b mspaint"
#     os.popen(cmd)
    os.system(cmd)

def Callback_mstsc():
    cmd = "start /b mstsc"
#     os.popen(cmd)
    os.system(cmd)

def Callback_networkLink():
    cmd = "start /b ncpa.cpl"
#     os.popen(cmd)
    os.system(cmd)

def Callback_notepad():
    cmd = "start /b notepad"
#     os.popen(cmd)
    os.system(cmd)

def Callback_regedit():
    cmd = "start /b regedit.exe"
#     os.popen(cmd)
    os.system(cmd)

def Callback_systemAttr():
    cmd = "start /b sysdm.cpl"
#     os.popen(cmd)
    os.system(cmd)

def Callback_winver():
    cmd = "start /b winver"
#     os.popen(cmd)
    os.system(cmd)

def Callback_mmsys():
    cmd = "start /b mmsys.cpl"#sound
#     os.popen(cmd)
    os.system(cmd)
    
def Callback_attributes():
    global flag
    if flag == 0:
        flag = 1
        top.attributes("-topmost", 0)#not on top
        BTN1['bg'] = "light gray"
    else:
        flag = 0
        top.attributes("-topmost", 1)#on top
        BTN1['bg'] = "light green"

def Callback_overrideredirect():
    global flag
    if top.wm_overrideredirect() == True:
        top.overrideredirect(0)
    else:
        top.overrideredirect(1)
        
def Callback_info():
    print(top.wm_overrideredirect())
        
def Callback_OpenAppFolder():
#     print(sys.path[0])
#     c_d = os.getcwd()
    c_d = os.path.split(os.path.realpath(__file__))[0]
#     c_d = sys.path[0]
    os.startfile(c_d)

def movewindow(event):
    top.geometry('+{0}+{1}'.format(event.x_root,event.y_root))#'%dx%d+%d+%d'

  
flag = 0
btn_names =[]
btn_names_1 = ["设备管理器","任务管理器","计算器"]
btn_names_2 = ["控制面板","资源管理器 ","Internet属性 "]
btn_names_3 = ["鼠标属性","系统信息 ","画图 "]
btn_names_4 = ["远程桌面连接","网络连接 ","打开记事本 "]
btn_names_5 = ["注册表 ","系统属性 ","关于Windows"]
btn_names_6 = ["声音","reserved1","reserved2"]
btn_names.append(btn_names_1)
btn_names.append(btn_names_2)
btn_names.append(btn_names_3)
btn_names.append(btn_names_4)
btn_names.append(btn_names_5)
btn_names.append(btn_names_6)

btn_func=[]
btn_func_1  = [Callback_devmgmt,Callback_taskmgr,Callback_calc]
btn_func_2  = [Callback_control,Callback_explorer,Callback_inetcpl]
btn_func_3  = [Callback_Mouse,Callback_msinfo32,Callback_mspaint]
btn_func_4  = [Callback_mstsc,Callback_networkLink,Callback_notepad]
btn_func_5  = [Callback_regedit,Callback_systemAttr,Callback_winver]
btn_func_6  = [Callback_mmsys,None,None]
btn_func.append(btn_func_1)
btn_func.append(btn_func_2)
btn_func.append(btn_func_3)
btn_func.append(btn_func_4)
btn_func.append(btn_func_5)
btn_func.append(btn_func_6)

if __name__ == '__main__':
    top = Tk()
    top.overrideredirect(0)
    top.resizable(height=False,width=False)
    top.title(string=u'QuickRun')
    if 1 == UsePlatform():
    	top.attributes("-toolwindow", 1)#Toolbar style，this Property is only for windows，linux can not use
    top.attributes("-topmost", 1)#top
    top.attributes("-alpha",1)#transparency

    for i in range(len(btn_names)):#row
        for j in range(len(btn_names[i])):#column
            Button(top, text =btn_names[i][j], command = btn_func[i][j],width=13).grid(row=i,column=j)
    BTN1 = Button(top, text ="置顶", command = Callback_attributes,width=13,bg="light green")
    BTN1.grid(row=6,column=0)
    Button(top, text ="本程序路径", command = Callback_OpenAppFolder,width=13).grid(row=6,column=1)
    Button(top, text ="显示标题", command = Callback_overrideredirect,width=13).grid(row=6,column=2)
    top.bind('<B3-Motion>',movewindow)
    top.mainloop()
