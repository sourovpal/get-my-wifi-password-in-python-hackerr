# first we will import the subprocess module
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profile = []
for i in data:
    if "All User Profile" in i:
        profile.append(i.split(":")[1][1:-1])

for i in profile:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    profile_password = [b.split(':')[1][1:-1] for b in result if "Key Content" in b]

    try:
        print("{:<30} | {:<}".format("Username", "Password"))
        print("{:<28}   {:<}".format("---------", "-----------"))
        print("{:<30} | {:<}".format(i, profile_password[0]))
    except IndexError:
        print("{:<30} | {:<}".format(i, ""))
        
        
        
#========================================= 2 =============================================

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
                        'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
