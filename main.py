import smtplib, ssl, random, string

allCharacters = list(string.digits)
code = ''

for i in range(6):
    code += allCharacters[random.randint(0, len(allCharacters) - 1)]

receiver_email = input("Please enter your email: ")

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "<SENDERS-EMAIL>"  # Enter your address
password = "<SENDERS-PASSWORD>"
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, code)

userCode = input("Please enter the code: ")
if userCode == code:
    print("Your code is correct!")
else:
    print("Sorry! Wrong code.")
