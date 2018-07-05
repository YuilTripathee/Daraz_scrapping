<<<<<<< HEAD
# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEMultipart()
msg['From'] = 'Yuil Tripathee <ronnietr@gmail.com>'
msg['To'] = 'Yuil Tripathee <yuiltripathee79@gmail.com>'
# msg['CC'] = 'Bishal Pun <bishalpun13@gmail.com>'
msg['Subject'] = 'Sample email attachment'
print('Mail header initialized')

# The mail body also just as attachment
with open('text.txt', 'r') as text:
    body = MIMEText(text.read())
    msg.attach(body)
    pass
print('Body written')

# JPEG attachment
filenames = [
    'img.jpg',
    'text.txt'
]
for filename in filenames:
    # filename='img.jpg'
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="octet-stream")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)
print('File attached sucessfully')

# Mail engine
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as mail_sys:
        mail_sys.ehlo()
        mail_sys.starttls()
        mail_sys.login('ronnietr7@gmail.com','ronnie@15')
        mail_sys.sendmail('ronnietr7@gmail.com',['yuiltripathee79@gmail.com'], msg.as_string())
        print('Mail sent sucessfully')
        pass
except Exception:
    print('Mail failed to transfer')
    raise
=======
# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEMultipart()
msg['From'] = 'Yuil Tripathee <ronnietr@gmail.com>'
msg['To'] = 'Yuil Tripathee <yuiltripathee79@gmail.com>'
# msg['CC'] = 'Bishal Pun <bishalpun13@gmail.com>'
msg['Subject'] = 'Sample email attachment'
print('Mail header initialized')

# The mail body also just as attachment
with open('text.txt', 'r') as text:
    body = MIMEText(text.read())
    msg.attach(body)
    pass
print('Body written')

# JPEG attachment
filenames = [
    'img.jpg',
    'text.txt'
]
for filename in filenames:
    # filename='img.jpg'
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="octet-stream")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)
print('File attached sucessfully')

# Mail engine
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as mail_sys:
        mail_sys.ehlo()
        mail_sys.starttls()
        mail_sys.login('ronnietr7@gmail.com','ronnie@15')
        mail_sys.sendmail('ronnietr7@gmail.com',['yuiltripathee79@gmail.com'], msg.as_string())
        print('Mail sent sucessfully')
        pass
except Exception:
    print('Mail failed to transfer')
    raise
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
