import sys
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

dname = r'C:\Marcel\python\projects\FileSpace'

def visit (arg, dirname, names):
    print dirname, arg
    for name in names:
        subname = os.path.join(dirname, name)
        
        if os.path.isdir(subname):
            print '  %s/' % name
        else:
            print ' %s \t %s ' % (name, (os.path.getsize(subname)))
    print
    
os.path.walk(dname, visit, '(User data)')