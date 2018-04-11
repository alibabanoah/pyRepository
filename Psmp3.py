import os,re
import time
readini = open('mp3.ini', 'r')
sourcef="."
tartgetf="."
wfile = open("copy.txt",'a')
for line in readini.readlines(): #读取配置文件
    if (re.findall("源文件",line)):
        sourcef=line.split("=")[1].strip()
        print(sourcef)
    if (re.findall("目标文件",line)):
        tartgetf=line.split("=")[1].strip()
        print(tartgetf)

def wfilef(wc):#写文件
    wfile.writelines(wc+"\n")

def renamef(restr):
    fnames = [name for name in os.listdir(sourcef) if name.endswith('.mp3')]
    i = 2492
    for nf in fnames:
        print(sourcef+'\\'+nf,sourcef+'\\'+str(i)+".mp3")
        wfilef(str(i)+"-"+nf.split("-")[1].split(".")[0])
        os.rename(sourcef+'\\'+nf,sourcef+'\\'+str(i)+".mp3")
        i += 1
renamef("e")





