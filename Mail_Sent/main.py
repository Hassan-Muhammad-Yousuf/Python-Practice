import smtplib

# recipient email addresses
recipients = []
n = int(input("Enter number of people you want to send an email to: "))
for i in range(n):
    email_addr = input(f"Enter email address {i+1}: ")
    recipients.append(email_addr)

# Connect to Gmail SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# credentials
your_email = input("Enter your email address: ")
your_password = input("Enter your App Password (not regular password): ")

# Login to Gmail account
try:
    s.login(your_email, your_password)
except smtplib.SMTPAuthenticationError as e:
    print("Login failed! Check your email/password. Use App Password if 2FA is enabled.")
    print(e)
    exit()

# Email content
subject = input("Enter subject of the email: ")
body = input("Enter body of the email: ")
message = f"Subject: {subject}\n\n{body}"

# Send email to each recipient
for recipient in recipients:
    try:
        s.sendmail(your_email, recipient, message)
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

s.quit()
print("All done!")
