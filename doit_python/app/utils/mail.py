import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


class Mail:
    def __init__(self, account: str, password: str):
        self.account = account
        self.password = password

        self._smtp = None

    def __enter__(self):
        print("__enter__")
        self._smtp = self._login()
        return self._smtp

    def __exit__(self):
        print("__exit__")
        self._smtp.quit()

    def send(self, subject: str, content: str, to_email: str, attachment_path: str = None):

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = self.account
        msg["To"] = to_email

        content = MIMEText(content, "html")
        msg.attach(content)

        if not attachment_path:
            base = MIMEBase("application", "octet-stream")
            with open(attachment_path, "rb") as file:
                base.set_payload(file.read())
            encoders.encode_base64(base)
            base.add_header("Content-Disposition", "attachment", filename=os.path.basename(attachment_path))
            msg.attach(base)

        self._smtp.sendmail(self.account, to_email, msg.as_string())

    def _login(self) -> smtplib.SMTP_SSL:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(self.account, self.password)
        return smtp
