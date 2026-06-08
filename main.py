""" 
Application designed for automated email dispatching.

Author: https://github.com/rafael-smoura
License: MIT
"""

from email.message import EmailMessage
import smtplib
import ssl

# Note: Create a file named 'password.txt' and place your 16-digit app password inside it. 
# Do not upload your app password file when deploying or pushing to GitHub.

try:
    with open('password.txt', 'r', encoding='utf-8-sig') as f:
        password = f.read().replace(" ", "").replace("\ufeff", "").strip()
except FileNotFoundError:
    print("[ERROR] The file 'password.txt' was not found in the current directory.")
    print("Please create the 'password.txt' file and paste your 16-digit app password inside it.")
    exit()

# 1 - EMAIL DATA CONFIGURATION
candidate_name = 'user_name'
company_name = 'company'

from_email = 'email_user@gmail.com'
to_email = 'email_destiny@gmail.com'

subject = f'Hiring Process Update — {company_name}'

body = f'''
Hello, {candidate_name},

I hope this email finds you well.

Thank you very much for taking the time to participate in our recruitment process for the Software Engineering position. It was a privilege to learn more about your projects and your background in the field.

We had the opportunity to connect with outstanding professionals and, after a thorough review of the requirements needed for the current stage of this role, we have decided to move forward with another candidate whose skills align more closely with our immediate project scope.

Please note that this decision does not reflect on the high quality of your technical assessment and our conversations. Your profile stood out to us, particularly regarding your code organization.

Because of this, we will keep your resume and portfolio in our priority talent pool. As soon as new opportunities open up in our technology department, you will be among the first people we reach out to.

I wish you great success in your professional journey, and I would like to invite you to connect with me on LinkedIn.

Best regards,

{company_name}
'''

# 2 - STRUCTURING THE EMAIL MESSAGE
print("Structuring the email content...")
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

# TLS/SSL encryption context
ssl_context = ssl.create_default_context()

# 3 - SERVER CONNECTION AND EMAIL DISPATCH
print("Connecting to Gmail and sending the message...")

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl_context) as smtp:
    smtp.login(from_email, password)
    smtp.send_message(message)

print("Process completed! The email was sent successfully.")