#!/usr/bin/python3
import os, sys

print(os.getpid())

if sys.platform == 'Linux':
    print(os.getloadavg())

loadavg = os.getloadavg()
print("5 min loadavg",loadavg)

cpu_core_count = os.cpu_count()
print(cpu_core_count)

def A():
  cpu_core_count = 0.1*os.cpu_count()
  '''
  loadavg5min = os.getloadavg()
  '''
  load1, load5, load15 = os.getloadavg()
  if cpu_core_count - load5<1:
    sys.exit()
