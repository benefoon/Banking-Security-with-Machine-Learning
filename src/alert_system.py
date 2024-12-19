import smtplib
from email.mime.text import MIMEText

def send_alert_email(receiver_email, message):
    """Sends an alert email."""
    sender_email = "your-email@example.com"
    password = "your-password"
    msg = MIMEText(message)
    msg['Subject'] = 'Suspicious Transaction Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_alert_email("admin@example.com", "Suspicious transaction detected!")
