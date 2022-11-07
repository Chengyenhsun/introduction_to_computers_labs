import os

path = os.getcwd()  #讀取當前工作目錄
p = path.replace(os.sep, ",")  #將目錄用","隔開
listp = list(p.split(","))  #將目錄存成list
while '' in listp:  #刪除list中的空格
    listp.remove('')
print(listp)  #顯示出當前工作目錄的list


listdir = os.listdir('/home/F14106155') #讀取 ‘/home/學號’ 目錄下所有檔案和資料夾
print(listdir)  #顯示目錄下所有檔案和資料夾

path = 'f14106155.txt'  #建立f14106155.txt文字檔
with open('f14106155.txt', 'w') as t:  #開啟檔案
    for i in range(len(listp)):  #將目錄list寫入檔案
        t.write(str(listp[i]) + os.linesep)
    t.write(os.linesep)
    for i in range(len(listdir)):  #將listdir寫入檔案
        t.write(str(listdir[i]) + os.linesep)

path = 'f14106155.txt'
f = open(path, 'r')  #讀取f14106155.txt文字檔並輸出
f.close()