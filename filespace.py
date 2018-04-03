#!/usr/bin/python
"""Script to serve as utility for tracking types of files consuming the most disk space in a given filesystem."""
import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


fh = logging.FileHandler('log_filename.log')
fh.setLevel(logger.getEffectiveLevel)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logger.getEffectiveLevel)
ch.setFormatter(fh)
logger.addHandler(ch)


def main():
    """ Main entry point for the script"""
    logger.debug('Entering main')
    pass

if __name__ == '__main__':
    sys.exit(main())
