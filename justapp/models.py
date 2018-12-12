from django.db import models
from subprocess import check_output
import subprocess
from threading import Timer
# Create your models here.

def portScanner(ip):
    out = check_output(["perl",'/opt/nikto/nikto.pl',"-host",ip])

    return out


