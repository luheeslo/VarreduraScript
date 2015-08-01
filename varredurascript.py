#!/usr/bin/python

import subprocess
import sys
import re

if len(sys.argv) == 0:
    print "Usage: varredurascript.py <ipformat> or <inetnum>"
    sys.exit(2)

input = sys.argv[1]
if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", input):
    output = subprocess.check_output(['whois', input])
    inetnum = ''

    for line in output.splitlines():
        line_split = line.split()
        if (len(line_split) != 0) and (line_split[0] == 'inetnum:'):
            inetnum = line_split[1]
            break
    if not inetnum:
        print "Error: inetnum not found"
        sys.exit(2)
    input = inetnum

print "Varrendo ips... "
output = subprocess.check_output(['nmap', '-sS', '-sV', input])

try:
    f = open('hosts_data.txt', 'w')
    f.write(output)
    f.close
except IOError, e:
    print 'Erro ao escrever no arquivo: %s' % (e.message)
