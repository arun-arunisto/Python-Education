import smtplib

#simple mail sending
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("<mail_id>", "<password>")
message = "message content"
server.sendmail("<from_address>", "<to_address>", message)
server.quit()

#mail sending using user-agent
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart()
message['From'] = "<from_address>"
message["To"] = "<to_address"
message["Subject"] = "<subject>"

body = "<message_content>"

message.attach(MIMEText(body, 'plain'))

user_agent = "<user_agent_string>" #refer link : https://useragentstring.com/
message.add_header("User-Agent", user_agent)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("<mail_id>", "<password>")
    server.sendmail("<from_address>", "<to_address>", message.as_string())
