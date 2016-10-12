#!/usr/bin/env python

#
# Usage: makecuts.py inaudio destpath offset0 > cutfile

import sys
import re

inaudio  = sys.argv[1]
destpath = sys.argv[2]
curtime = float(sys.argv[3])

linere = re.compile('\s*(\S+)\s+([0-9.]+)\s*')
for line in sys.stdin:
    mo = re.match(linere, line)
    if not mo:
        sys.stderr.write("Bad line:\n%s\n"%(line))
        sys.exit(1)
    fname = mo.group(1)
    fname = fname.replace('_trim', '')
    dur = float(mo.group(2))
    print "%s %f %f %s/%s"%(inaudio, curtime, curtime+dur, destpath, fname)
    curtime += dur

