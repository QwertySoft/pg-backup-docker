from environs import Env
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys


env = Env()

sender_email = env("EMAIL_FROM")
receiver_email = env("EMAIL_TO")
password = env("EMAIL_PASSWORD")

message = MIMEMultipart("alternative")
message["Subject"] = f"Backup %s %s" % (
    env("EMAIL_PREFIX", default="[BACKUP]"), datetime.now())
message["From"] = sender_email
message["To"] = receiver_email
text = """\
Your backup has been compleated
"""
part1 = MIMEText(text, "plain")
message.attach(part1)

filename = sys.argv[0]
attachment = open(f'./%s' % filename, "rb")
