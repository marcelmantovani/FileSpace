#!/usr/bin/python
"""Script to serve as utility for tracking types of files consuming the most disk space in a given filesystem."""
import sys
import logging
from path import Path

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


fh = logging.FileHandler('log_filename.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(fh)
logger.addHandler(ch)


def main():
    """ Main entry point for the script"""
    logger.debug("Python version: {}".format(sys.version))
    logger.debug('Entering main')
    getCountOfFiles(r'C:\Marcel\python\projects\FileSpace')
    
    pass

def getCountOfFiles(directory):
    """ For a given path, lists all files in the directory"""
    logger.debug('getFiles with input {}'.format(directory))
    try:
        d = Path(directory)
    except IOError:
        logger.warning('Error reading files your path' )
    else:
        num_files = len(d.files())

    print num_files
    pass


if __name__ == '__main__':
#    sys.exit(main())
    main()
    