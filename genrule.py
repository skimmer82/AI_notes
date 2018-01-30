# encoding:UTF-8

import sys, os, time, optparse
import re
from difflib import *


def main():
    sys.stdout.writelines("hello\n")
    a = "qabxcd"
    b = "abycdf"
    s = SequenceMatcher(None, a, b)
    e = s.get_opcodes()
    for i in range(0, e.__len__()-1):
        tag, i1, i2, j1, j2 = e[i]
        print ("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %
               (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))
        if tag == 'replace':
            print ("%s %s" %
                   (a[i1:i2], b[j1:j2]))
            s1 = "if 1:\n\
                    output_line = '%s'\n\
                    match = re.match(r'.*(%s).*', output_line)\n\
                    if match:\n\
                            pattern_replace = re.sub(r'%s', r'%s', output_line, flags=re.I)\n\
                            print pattern_replace\n\
                 " % (a, a[i1:i2], a[i1:i2], b[j1:j2])
            print s1
            exec s1

# match = re.match(r'.*(Amy).*', output_line)
# if match:
#     pattern_replace = re.sub(r'Amy', r'艾米', output_line, flags=re.I)
#     output_line = pattern_replace
#     print >> log_file, output_line

if __name__ == '__main__':
    main()
