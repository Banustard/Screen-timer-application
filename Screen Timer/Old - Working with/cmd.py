import subprocess

p = subprocess.Popen('net user', shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print (line) 
retval = p.wait()
