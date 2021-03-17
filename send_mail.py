import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    #port = 2525
    port = 993
    #smtp_server = 'smtp.mailtrap.io'
    smtp_server = 'smtp.gmail.com'
    #login = 'c7b29e2f43d020:055191ab3ad8c2'
    login = 'landry72@gmail.com'
    password = 'landry1348'
   # MAIL_USE_SSL=True
   # MAIL_USERNAME = 'your@gmail.com'
   # MAIL_PASSWORD = 'yourpassword'
    
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'landry72@gmail.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
