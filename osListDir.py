#!/usr/local/bin/python

import sys
import time
import os.path

def converTimeToStr(in_time):
    return time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(in_time))

def visit (arg, dirname, names):
    
    for name in names:
        subname = os.path.join(dirname, name)
        
        if (os.path.isdir(subname)) and os.path.exists(subname):
            statDetail = os.stat(subname)
            # strmtime = converTimeToStr(statDetail.st_mtime)
            print '%s, %s, %s, %s, %s ' % (now, os.path.dirname( subname), name, statDetail.st_uid, statDetail.st_gid )
            
    
def main():
    print 'timenow, basedirname, dirname, uid, gid'
    os.path.walk(dname, visit, '(User data)')

dname = r'C:\Marcel\temp'
now = converTimeToStr(time.time())

if __name__ == '__main__':
    main()