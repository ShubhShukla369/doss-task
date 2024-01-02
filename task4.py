import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() 
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
subject = "Email"
body = "This is a doss email sent from Python."
to_email = "shuklashubh818@gmail.com"
smtp_server = "smtp.example.com"
smtp_port = 587  # Update the port according to your SMTP server requirements
sender_email = "shuklashubh818@gmail.com"
sender_password = "12345678"

# Send the email
send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password)
