#!/usr/local/bin/python

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

dname = r'C:\Marcel\temp'

def visit (arg, dirname, names):
    
    for name in names:
        subname = os.path.join(dirname, name)
        
        if not (os.path.isdir(subname)):
        #    print '  %s/' % name
        #else:
            print '%s, %s, %s ' % (os.path.dirname( subname), name, (os.path.getsize(subname)))
            #print 'parent directory %s ' % os.path.dirname( subname)
    #print
    
def main():
    print 'dirname, filename, size'
    os.path.walk(dname, visit, '(User data)')


if __name__ == '__main__':
#    sys.exit(main())
    main()