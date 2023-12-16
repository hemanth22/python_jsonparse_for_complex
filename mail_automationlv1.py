import smtplib
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
reporterhtml = subprocess.getoutput("cat reporter.html")
sender_email = "hemanthbitraece@gmail.com"
receiver_email = "hemanthbitra@live.com"
message = MIMEMultipart("alternative")

message["Subject"] = "[LV] Report"
message["From"] = sender_email
message["To"] = ",".join(receiver_email)

text = reporterhtml
html = reporterhtml

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    #server.login(login,password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print("Email sent successfully!")
