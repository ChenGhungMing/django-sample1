# from subprocess import STDOUT,check_output
# # Create your models here.

# out = check_output(["nikto","-host","google.com"])

# print(out)



import subprocess
from threading import Timer

kill = lambda process: process.kill()
cmd = ['nikto', '-h','www.google.com']
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
my_timer = Timer(5, kill, [ping])
try:
    my_timer.start()
    stdout, stderr = ping.communicate()
    print(stdout)
finally:
    my_timer.cancel()