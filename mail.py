import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("testmailtest579@gmail.com", "test123test123")

# message to be sent
message = "Hlo"

# sending the mail
s.sendmail("testmailtest579@gmail.com", "abhishekmadhu9@gmail.com", message)

# terminating the session
s.quit()