from django.db import models
from subprocess import check_output
# Create your models here.

def portScanner(ip):
    
    print(ip)
    out = check_output(["ls", "-al"])

    return out