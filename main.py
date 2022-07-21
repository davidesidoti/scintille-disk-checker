import shutil
import socket
import smtplib
from email.message import EmailMessage

total, used, free = shutil.disk_usage("/")

total = total // (2**30)

free = free // (2**30)
free = round(free / total * 100, 2)

if (free > 65):
    msg = EmailMessage()
    msg.set_content(
        f'Lo spazio del disco in `{socket.gethostname()}` è al {free}%')
    msg['Subject'] = f'Spazio del disco in {socket.gethostname()} basso'
    msg['From'] = 'disk-checker@scintille.net'
    msg['To'] = 'davide@scintille.net'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

    print("Disk is low")
else:
    print("Disk is ok")
