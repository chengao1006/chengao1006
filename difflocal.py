import os
import re
import xlrd
import stat
import pysvn
import shutil
from git import Git
import csv


old_trunk_url = 'https://192.168.1.25:6666/svn/AntMan/trunk/design/X_Data/玩法'
old_rev =  172777    # 0就是默认拉取最新的
new_trunk_url = 'https://192.168.1.25:6666/svn/AntMan/trunk/design/X_Data/玩法'
new_rev =  172778 # 0就是默认拉取最新的
old_dir = './config_dir/old'
new_dir = './config_dir/new'

def svncheckout(trunk_url,rev,dir):
    '''拉取svn'''
    client = pysvn.Client()
    if rev:
        client.checkout(trunk_url,dir,revision = pysvn.Revision(pysvn.opt_revision_kind.number, rev)) 
    else:
        client.checkout(trunk_url,dir)




def exlcezhuanlua(name):
    '''读取xls转lua'''
    workbook = xlrd.open_workbook(name[0])
    sheetNames = workbook.sheet_names()
    #print(sheetNames)
    sheettmp = 0
    for sheet in sheetNames:
        sheet1_object = workbook.sheet_by_index(sheettmp)
        nrows = sheet1_object.nrows
        # print(nrows)   
        # all_row_values = sheet1_object.row_values(rowx=0)
    # print(len(all_row_values))
        sheet = sheet.replace("<", "[").replace(">", "]")
        tmp = []
        for row in range(nrows):
            all_row_valuestmp = sheet1_object.row_values(rowx=row)
            tmp.append(all_row_valuestmp)

        with open("d:\exlce\\tmp\\"+name[1]+"("+sheet+")"+".csv", 'w', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(tmp)
        sheettmp = sheettmp + 1


def readonly_handler(func, path, execinfo):
        os.chmod(path, stat.S_IWRITE)
        func(path)


def getlist(list_file):
    for dirpath, dirnames, filenames in list_file:
        for dir in dirnames:
            all_list.append(os.path.join(dirpath,dir))
        for file in filenames:
            all_list.append(os.path.join(dirpath,file))
    #print(all_list)
    exlcelists = []
    for li in all_list:
        if re.search('\.*.xlsx', str(li)) != None:
            tmpli = []
            newStr = re.sub('\\\\', '-' , li[17:-5])
            tmpli = [li,newStr]
            exlcelists.append(tmpli)           
    #print(exlcelists)
    for strs in exlcelists:
        exlcezhuanlua(strs)


if __name__=="__main__":
    os.removedirs("C:/Users/A/AppData/Local/Programs/Python/Python37/Lib/site-packages/test/config_dir")

    if os.path.exists(old_dir):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(old_dir, onerror=readonly_handler)

    os.makedirs(old_dir)
    svncheckout(old_trunk_url,old_rev,old_dir)
    all_list=[]
    path = os.getcwd()  # 获得当前目录
    list_file = os.walk(old_dir)
    if os.path.exists("D:\exlce\\tmp"):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree("D:\exlce\\tmp", onerror=readonly_handler)
        r = Git("d:\exlce")
        r.execute('git add .')
        r.execute('git commit -m "55"')
    os.makedirs("D:\exlce\\tmp")
    print("拉去旧的svn完成")
    # #print(list_file)
    getlist(list_file)
    print("生成旧的表完成")
    r = Git("d:\exlce")
    r.execute('git add .')
    r.execute('git commit -m "55"')
    if os.path.exists(new_dir):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(new_dir, onerror=readonly_handler)

    os.makedirs(new_dir)
    svncheckout(new_trunk_url,new_rev,new_dir)
    all_list=[]
    path = os.getcwd()  # 获得当前目录
    list_file = os.walk(new_dir)
    if os.path.exists("D:\exlce\\tmp"):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree("D:\exlce\\tmp", onerror=readonly_handler)
    os.makedirs("D:\exlce\\tmp")
    #print(list_file)
    print("拉去新的SVN完成")
    getlist(list_file)
    print("完成")