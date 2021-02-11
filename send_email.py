def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hrshsingh00@gmail.com', 'Ramsha@420')
    email = EmailMessage()
    email['From'] = 'hrshsingh00@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.sendmail('hrshsingh00@gmail.com',
                    'gauravtriyar27@gmail.com',
                    'hey, i am creating email bot in python')
