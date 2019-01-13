#coding=utf-8
import os
import time
import platform
import subprocess
from datetime import datetime
from appJar import gui


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
#     os.system(cmd)
    os.popen(cmd)
    
def Callback_devmgmt():
    cmd = "devmgmt.msc"
#     os.system(cmd)
    os.popen(cmd)
#     out = subprocess.check_output(cmd, stdin=subprocess.DEVNULL, stderr=subprocess.STDOUT).decode('utf-8')
def Callback_multibuttons(btn=None):
    print(btn)
    



