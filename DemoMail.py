import smtplib
sendermail = "ponnurumahesh129@gmail.com"
recievemail = "maheshmaahi129@gmail.com"
password = input(str("please enter your password"))
message = "Hello,This message was sent with the help of Python"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sendermail,password)
print("Login Successfully")
server.sendmail(sendermail,recievemail,message)
print("message has been successfully sent to", recievemail)