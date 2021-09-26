# -*- encoding: utf-8 -*-
'''
@File    :   exdiff.py
@Time    :   2021/07/14 13:43:23
@Author  :   黄洋
@Version :   1.0
@Contact :   383505002@qq.com
'''
# from threading import Thread
from typing import Text
from PySide2.QtWidgets import (QApplication, QLineEdit, QMainWindow,
                               QMessageBox, QPushButton)
import paramiko
import time

path = 'chengao'

# here put the import lib

class Stats():
    '''图形界面'''
    def __init__(self):
        '''控件'''
        self.wzs = []
        self.sjs = []
        self.xxts = []
        self.window = QMainWindow() #创建一个主窗口
        self.window.resize(900, 400)   #窗口 大小
        self.window.move(300, 300)    #窗口位置
        self.window.setWindowTitle('exceldiff  @黄洋')   #窗口标题

        self.oldsvnurltextEditxxt = QLineEdit(self.window)
        self.oldsvnurltextEditxxt.setPlaceholderText("请输入老版本号SVN地址")
        self.oldsvnurltextEditxxt.setText('https://192.168.1.25:6666/svn/AntMan/trunk/design/X_Data')
        self.oldsvnurltextEditxxt.move(35, 25)
        self.oldsvnurltextEditxxt.resize(700, 25)

        self.oldidtextEditxxt = QLineEdit(self.window)
        self.oldidtextEditxxt.setPlaceholderText("老版本号")
        self.oldidtextEditxxt.move(800, 25)
        self.oldidtextEditxxt.resize(75, 25)


        self.newsvnurltextEditxxt = QLineEdit(self.window)
        self.newsvnurltextEditxxt.setPlaceholderText("请输入新版本号SVN地址")
        self.newsvnurltextEditxxt.setText('https://192.168.1.25:6666/svn/AntMan/trunk/design/X_Data')
        self.newsvnurltextEditxxt.move(35, 75)
        self.newsvnurltextEditxxt.resize(700, 25)

        self.newidtextEditxxt = QLineEdit(self.window)
        self.newidtextEditxxt.setPlaceholderText("新版本号")
        self.newidtextEditxxt.move(800, 75)
        self.newidtextEditxxt.resize(75, 25)

        # self.button = QPushButton('获取userid', self.window)
        # self.button.move(355, 25)

        # self.jbutton = QPushButton('修改cdt', self.window)
        # self.jbutton.move(355, 85)
        # #self.jbutton.setEnabled(False)

        # self.vbutton = QPushButton('修改VIP', self.window)
        # self.vbutton.move(505, 85)

        # self.updateConfigurationbutton = QPushButton('更新配置文件', self.window)
        # self.updateConfigurationbutton.move(655, 85)

        # self.button.clicked.connect(self.jk)
        # self.jbutton.clicked.connect(self.jf)

        # # 获取验证码
        # self.yzmtextEditxxt = QLineEdit(self.window)
        # self.yzmtextEditxxt.setPlaceholderText("等待获取验证码")
        # self.yzmtextEditxxt.move(105, 145)
        # self.yzmtextEditxxt.resize(200, 30)

        self.sjbutton = QPushButton('执行', self.window)
        self.sjbutton.move(320, 145)
        self.sjbutton.resize(150, 30)

        # self.yxbutton = QPushButton('获取邮箱验证码', self.window)
        # self.yxbutton.move(500, 145)        
        # self.yxbutton.resize(150, 30)

        # # 时间
        # self.timetextEditxxt = QLineEdit(self.window)
        # self.timetextEditxxt.setPlaceholderText("请输入修改时间")
        # self.timetextEditxxt.setText('11/23/2020 17:39:18')
        # self.timetextEditxxt.move(105, 205)
        # self.timetextEditxxt.resize(200, 30)
    
        # self.setbutton = QPushButton('修改时间', self.window)
        # self.setbutton.move(355, 205)

        # self.getbutton = QPushButton('获取当前时间', self.window)
        # self.getbutton.move(505, 205)  

        # self.resetButton = QPushButton('重置时间', self.window)
        # self.resetButton.move(655, 205)     

        # # 获取物品item
        # self.itemtextEditxxt = QLineEdit(self.window)
        # self.itemtextEditxxt.setPlaceholderText("请输入物品ID")
        # self.itemtextEditxxt.move(105, 265)
        # self.itemtextEditxxt.resize(100, 30)
    
        # self.itemSumtextEditxxt = QLineEdit(self.window)
        # self.itemSumtextEditxxt.setPlaceholderText("请输入物品数量")
        # self.itemSumtextEditxxt.move(255, 265)
        # self.itemSumtextEditxxt.resize(100, 30)

        # self.setitembutton = QPushButton('修改物品数量', self.window)
        # self.setitembutton.move(405, 265)    
        
        # self.setitembutton.clicked.connect(self.getItems)
        # self.setbutton.clicked.connect(setTime)
        # self.getbutton.clicked.connect(getTime)
        # self.resetButton.clicked.connect(resetTime)

        self.sjbutton.clicked.connect(self.urlinit)
        # self.yxbutton.clicked.connect(yxyzm)
        # self.vbutton.clicked.connect(self.setvip)
        # self.updateConfigurationbutton.clicked.connect(updateConfiguration)
        
    def urlinit(self):
        global oldurl 
        oldurl = self.oldsvnurltextEditxxt.text()
        global newurl 
        newurl= self.newsvnurltextEditxxt.text()
        global oldid
        oldid = self.oldidtextEditxxt.text()
        global newid
        newid = self.newidtextEditxxt.text()
        go()



def go():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.60.64", 22, "test", "123456")
    global path
    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command(f"python3 init.py {path}")
    print(stdout.readlines())
    global oldid
    if oldid == "":
        pass
    else:
        oldid = f"-r{oldid} " 
    stdin, stdout, stderr = ssh.exec_command(f"rm -rf {path}/old")
    stdin, stdout, stderr = ssh.exec_command(f"svn checkout {oldid}{oldurl} {path}/old --username huangyang --password hy123456")
    print(stdout.readlines())
    print(f"svn checkout {oldid}{oldurl} {path}/old --username")
    global newid
    if newid == "":
        pass
    else:
        newid = f"-r{newid} " 
    time.sleep(20)
    stdin, stdout, stderr = ssh.exec_command(f"rm -rf {path}/new")
    stdin, stdout, stderr = ssh.exec_command(f"svn checkout {newid}{newurl} {path}/new --username huangyang --password hy123456")
    print(stdout.readlines())
    print(f"svn checkout {newid}{newurl} {path}/new --username")
    stdin, stdout, stderr = ssh.exec_command(f"cd {path}/tmp/data; rm -rf *")
    stdin, stdout, stderr = ssh.exec_command(f"cd {path}; python3 zhuanlua.py")
    print(stdout.readlines())
    # print(stdout.readlines())  # svn checkout https://192.168.1.25:6666/svn/AntMan/trunk/design/X_Data old --username huangyang --password hy123456
    # # stdin, stdout, stderr = ssh.exec_command("cd tmp/data; rm -rf *")
    stdin, stdout, stderr = ssh.exec_command(f"cd {path}/tmp; git add .; git commit -m '2'")
    stdin, stdout, stderr = ssh.exec_command(f"cd {path}; python3 new.py")
    # stdin, stdout, stderr = ssh.exec_command("git status")cd
    print(stdout.readlines())
    QMessageBox.about(stats.window, '提示',"执行完成")


app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
