#!/usr/local/bin/python

import sys
import time
#from path import Path
import os.path

# if you want to do using Path lib
#d = Path(r'C:\Marcel')
#tot_size = 0

#for files in d.files():
#    if files.isfile():
#        print (files.name , files.size)
#        tot_size += files.size
#
#print tot_size/1024
def converTimeToStr(in_time):
    return time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(in_time))

def visit (arg, dirname, names):
    
    for name in names:
        subname = os.path.join(dirname, name)
        
        if not (os.path.isdir(subname)):
            statDetail = os.stat(subname)
            strmtime = converTimeToStr(statDetail.st_mtime)
            print '%s, %s, %s, %s, %s, %s, %s ' % (now, os.path.dirname( subname), name, (os.path.getsize(subname)) ,strmtime, statDetail.st_uid, statDetail.st_gid )
            
    
def main():
    print 'timenow, dirname, filename, size, mtime, uid, gid'
    os.path.walk(dname, visit, '(User data)')

dname = r'C:\Marcel\temp'
now = converTimeToStr(time.time())

if __name__ == '__main__':
    main()