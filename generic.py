#!/usr/bin/env/python
#
# Generic python wrapper.
# Arg handling, logging, Global, etc.

from __future__ import print_function

from six.moves import input
import six

import argparse
import logging
import sys

VERSION = 0.1

class Global:
    '''Stores globals. There should be no instances of Global.'''

    # Command line arguments
    args = None

# end class Global

def main(argv):
    parse_arguments(argv[1:])
    setup_logging()
# end main()

def parse_arguments(strs):
    parser = argparse.ArgumentParser(description='Description. Version %s.'%(VERSION))
    parser.add_argument('-loglevel', 
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='WARNING',
                        help='Logging level (default %(default)s)')
    parser.add_argument('-version', '--version', action='version', version=str(VERSION))
    Global.args = parser.parse_args(strs)
# end parse_arguments()

def setup_logging():
    numeric_level = getattr(logging, Global.args.loglevel, None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level, format="%(module)s:%(levelname)s: %(message)s")
# end setup_logging()

if __name__ == "__main__":
    main(sys.argv)

