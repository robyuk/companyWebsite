import smtplib
import ssl
import os


def sendEmail(msg='Subject: Test\n\nTest', receivers=[os.getenv('PYEMAIL')]):
    host = 'smtp.gmail.com'
    port = 465

    sender = os.getenv('PYEMAIL')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, os.getenv('PYPW'))
        server.sendmail(sender, receivers, msg)


if __name__ == '__main__':
    sendEmail()
