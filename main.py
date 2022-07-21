import shutil
import socket
import smtplib
from email.message import EmailMessage

total, used, free = shutil.disk_usage("/")

total = total // (2**30)

free = free // (2**30)
free = round(free / total * 100, 2)
