from django.db import models
from subprocess import check_output
# Create your models here.

def portScanner(ip):
    out = check_output(["nikto",'-host',ip])

    return out