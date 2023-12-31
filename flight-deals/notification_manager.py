import smtplib

my_email = "sagarch700@gmail.com"
password = "xhmjgllkimhczqlm"

class NotificationManager:

    def __init__(self):
        pass

    def send_mail(self, destination, message):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=my_email, password=password)
        print(message)
        message = f"Subject:Low Price alert {destination}" + "\n\n" + message
        self.connection.sendmail(from_addr=my_email, to_addrs= "chsagar657@gmail.com", msg= message.encode())
        self.connection.close()
        print("success")

