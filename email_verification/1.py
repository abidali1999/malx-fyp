import re
import smtplib
from email.message import EmailMessage

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def send_verification_email(email):
    sender_email = '21022@students.riphah.edu.pk'
    sender_password = 'Thenigma'
    verification_code = '123456'  # Generate this securely in a real application
    msg = EmailMessage()
    msg.set_content(f'Your verification code is: {verification_code}')
    msg['Subject'] = 'Email Verification'
    msg['From'] = sender_email
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

def verify_email(email, entered_code):
    # In a real application, retrieve the actual verification code from a database
    actual_code = '123456'

    return entered_code == actual_code

# Example usage
user_email = 'abidali1999063@gmail.com'
send_verification_email(user_email)
# if is_valid_email(user_email):
#     send_verification_email(user_email)
#     print('Verification email sent. Please check your email for the verification code.')

#     entered_code = input('Enter the verification code: ')

#     if verify_email(user_email, entered_code):
#         print('Email verified successfully! You can now proceed with the signup process.')
#     else:
#         print('Invalid verification code. Please try again.')
# else:
#     print('Invalid email address. Please enter a valid email.')
