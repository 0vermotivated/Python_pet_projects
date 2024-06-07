import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_msg(msg):
    email = ""
    password = ""
    to = ""

    smtp_server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    smtp_server.login(email, password)

    message = MIMEMultipart()
    message['From'] = email
    message['To'] = to
    message['Subject'] = "Сообщение отправлено по кнопке"

    message.attach(MIMEText(msg, 'plain'))
    smtp_server.send_message(message)
    smtp_server.quit()