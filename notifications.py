import smtplib

def send_email(to, subject):
    server = smtplib.SMTP('smtp.example.com')
    server.sendmail("noreply@example.com", to, subject)
    server.quit()
    return True

def notify_user(user_email):
    send_email(user_email, "Welcome!")
    return f"Notification sent to {user_email}"