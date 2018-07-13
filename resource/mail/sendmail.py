# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# page
with open('mail.html', 'r', encoding='utf-8') as fp:
    html_page = fp.read().replace('\n', '')
    fp.close
# Create a text/plain message
msg = MIMEMultipart()
msg['From'] = 'Yuil Tripathee <rt041560@gmail.com>'
msg['To'] = 'Yuil Tripathee <yuiltripathee79@gmail.com>'
# msg['CC'] = 'Bishal Pun <bishalpun13@gmail.com>'
msg['Subject'] = 'Sample email attachment'
print('Mail header initialized')

page = MIMEText(html_page, 'html')
msg.attach(page)
text = """This email is sent from Yuil Tripathee
Software Engineer Intern at Dynamics Softech Computer Solutions.
"""
txt = MIMEText(text, 'plain')
msg.attach(txt)
# Mail engine
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as mail_sys:
        mail_sys.ehlo()
        mail_sys.starttls()
        mail_sys.login('rt041560@gmail.com','rohanforyuil')
        mail_sys.sendmail('rt041560@gmail.com',['yuiltripathee79@gmail.com'], msg.as_string())
        print('Mail sent sucessfully')
        pass
except Exception:
    print('Mail failed to transfer')
    raise
