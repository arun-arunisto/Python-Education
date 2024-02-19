import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from twilio.rest import Client
import re
from github import Auth, Github



load_dotenv()
class programUtilities:
    def __init__(self):
        #mail
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.context = ssl.create_default_context()
        self.sender_mail = os.getenv("SENDER_MAIL")
        self.password = os.getenv("PASSWORD")
        self.server = smtplib.SMTP(self.smtp_server, self.port)
        self.server.ehlo()
        self.server.starttls(context=self.context)
        self.server.ehlo()
        self.msg = MIMEMultipart()

        #whatsapp
        self.from_ = os.getenv("FROM_")
        self.account_sid = os.getenv("ACCOUNT_SID")
        self.auth_token = os.getenv("AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)



    #sending mail instantly
    def send_mail_instant(self, rec_mail, image_to_send):
        #image_data
        with open(image_to_send, 'rb') as f:
            img_data = f.read()
        self.msg["Subject"] = "Alert!! Stranger Detected!!"
        self.msg["FROM"] = self.sender_mail
        self.msg["TO"] = rec_mail
        text = MIMEText("Alert!! Stranger!!")
        self.msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(image_to_send))
        self.msg.attach(image)
        try:
            self.server.login(self.sender_mail, self.password)
            self.server.sendmail(self.sender_mail, rec_mail, self.msg.as_string())
        except Exception as e:
            print(e)

    #final mail
    def final_mail(self, rec_mail, link):
        self.msg["Subject"] = "Daily Report!"
        self.msg["From"] = self.sender_mail
        self.msg["To"] = rec_mail
        text = MIMEText(f"Click on the link below \n{link}")
        self.msg.attach(text)
        try:
            self.server.login(self.sender_mail, self.password)
            self.server.sendmail(self.sender_mail, rec_mail, self.msg.as_string())
        except Exception as e:
            print(e)

    #Whatsapp msg instant
    def send_whatsapp_msg_instant(self, rec_mobile, img_link):
        try:
            message = self.client.messages.create(
                body=f"Alert! Stranger Detected!",
                media_url="https://raw.githubusercontent.com/arun-arunisto/UploadingImages/todo/"+img_link,
                from_=self.from_,
                to=f"whatsapp:+91{rec_mobile}"
            )
            print("Whatsapp message sid:",message.sid)
        except Exception as e:
            print(e)

    #Whatsapp msg final
    def send_whatsapp_msg_final(self, rec_mobile, link):
        try:
            message = self.client.messages.create(
                body=f"Daily Report!\nClick the below link!\n{link}",
                from_=self.from_,
                to=f"whatsapp:+91{rec_mobile}"
            )
            print("Whatsapp message sid:",message.sid)
        except Exception as e:
            print(e)

    #creating folders to save images
    def images_save_path(self, folder_name):
        folder_name = re.sub(r'[<>:"/\\|?*]', '_', folder_name)
        path = os.path.join("images/", folder_name)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        return path

    #uploading images to github for whatsapp
    def image_to_github(self, path_to_file):
        auth = Auth.Token(os.getenv("GIT_TOKEN"))
        user = Github(auth=auth)
        repo = user.get_repo(os.getenv("GIT_REPO"))
        try:
            with open(path_to_file, "rb") as file:
                data = file.read()

            repo.create_file(path_to_file, "uploading image", data, branch=os.getenv("GIT_BRANCH"))
            print("Git hub repo id:",repo.id)
        except Exception as e:
            print(e)



if __name__ == "__main__":
    print(os.getenv("GIT_TOKEN"))
