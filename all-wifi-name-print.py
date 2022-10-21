# importing the subprocess module
import subprocess
  
# using the check_output() for having the network term retrieval
devices = subprocess.check_output(['netsh','wlan','show','network'])
  
# decode it to strings
devices = devices.decode('ascii')
devices= devices.replace("\r","")
  
# displaying the information
print(devices)




#==========================================
#             wifi name list 
#==========================================

import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii") # needed in python 3
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)
