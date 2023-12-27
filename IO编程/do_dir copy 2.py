import os
import time
path = r'.'
filenum, filesize, dirnum = 0, 0, 0
for name in os.listdir(path):

    # listdir(dir)返回dir路径下所有的文件和目录

    if os.path.isfile(name):
        print('%s\t\t%d\t%s' % (time.strftime('%Y/%m/%d %H:%M',
              time.localtime(os.path.getmtime(name))), os.path.getsize(name), name))
        # \t是制表符 使得对齐,一个\t,8个位置
        # os.path.getmtime(name) 获得name文件的最后修改的时间（时间戳）
        # time.localtime() 将Timestamp对象转换为struct_time对象
        # strftime()将struct_time对象转换为格式化时间 2009/01/07 23:54
        filenum = filenum+1
        filesize += os.path.getsize(name)

    if os.path.isdir(name):
        print('%s\t<DIR>\t\t%s' % (time.strftime('%Y/%m/%d %H:%M',
              time.localtime(os.path.getmtime(name))), name))
        dirnum += 1
print('\t\t%d个文件\t\t%d个字节' % (filenum, filesize))
print('\t\t%d个目录' % dirnum)
