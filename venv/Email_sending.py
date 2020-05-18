from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def main():
    try:
        msg = MIMEMultipart()
        msg['From'] = 'prabalthecoder@gmail.com'
        msg['To'] = 'contact@rdciti.com'
        msg['Subject'] = 'Hello 1..2..3..'

        message = "this is my email from python"
        msg.attach(MIMEText(message))
        S = smtplib.SMTP(host='smtp.gmail.com', port=587)
        S.starttls()
        S.login('prabalthecoder@gmail.com', 'GOOGLEACCOUNTSABKABAAPHOTAHAI')
        S.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print("Sorry:{0}".format(repr(e)))


if __name__ == "__main__":
    main()
