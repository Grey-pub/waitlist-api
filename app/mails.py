import smtplib
from email.mime.text import MIMEText
from django.conf import settings
import logging

def mailer(to_email, subject, message, is_html=False):
    sender = settings.EMAIL_HOST_USER
    recipients = [to_email]
    password = settings.EMAIL_HOST_PASSWORD

    if is_html:
        msg = MIMEText(message, 'html')  # 'html' is set here for HTML content
    else:
        msg = MIMEText(message, 'plain')  # Fallback to plain text if needed
    
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
            return True

    except Exception as e:
        error_message = f"error: {e}"
        logging.error(msg=error_message)
        return False
    
def send_confirmation_mail(email, first_name, flag):
    subject = "You're on the GreyPub waitlist 🚀"
    if flag:
        message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                <p>Hi {first_name},</p>
                <p>Thanks for joining the GreyPub waitlist! We're excited to have you with us. You'll be one of the first to know when we launch. Stay tuned for updates on how GreyPub can help with your academic projects.</p>
                <p>We've noticed your question and will get back to you shortly with a response. In the meantime, feel free to visit our <a href='https://greypub.vercel.app' style='color: #1a73e8; text-decoration: none;'>website</a> for more information.</p>
                <p>Best,<br>The GreyPub Team</p>
            </body>
        </html>
        """
    else:
        message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                <p>Hi {first_name},</p>
                <p>Thanks for joining the GreyPub waitlist! We're excited to have you with us. You'll be one of the first to know when we launch. Stay tuned for updates on how GreyPub can help with your academic projects.</p>
                <p>Feel free to visit our <a href='https://greypub.vercel.app' style='color: #1a73e8; text-decoration: none;'>website</a> to learn more or reach out if you have any questions.</p>
                <p>Best,<br>The GreyPub Team</p>
            </body>
        </html>
        """


    mailer(to_email=email, subject=subject, message=message, is_html=True)

def send_response_mail(email, first_name, question, response):
    subject = "Got Your Question——Here's What You Need to Know!"
    message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <p>Hey {first_name},</p>
                <p>Thanks for reaching out to us! We loved seeing your question and we're excited to dive right in and get you the info you need.</p>
                
                <div style="border-top: 2px solid #f0f0f0; margin-top: 20px; padding-top: 10px;">
                    <p style="font-weight: bold; color: #4CAF50;">Your Question:</p>
                    <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px; font-style: italic;">
                        {question}
                    </div>
                </div>

                <div style="border-top: 2px solid #f0f0f0; margin-top: 20px; padding-top: 10px;">
                    <p style="font-weight: bold; color: #4CAF50;">Our Response:</p>
                    <div style="background-color: #e7f3fe; padding: 10px; border-radius: 5px;">
                        {response}
                    </div>
                </div>

                <p style="margin-top: 30px;">
                    If anything still isn't clear or if you've got more questions (or just want to chat about GreyPub), feel free to hit us up! We're here for you and can't wait to see where this journey takes us together.
                </p>

                <p>
                    Thanks again for being a part of the GreyPub community——stay awesome and we'll be in touch soon with more updates!
                </p>
                <p style="margin-top: 30px;">
                    <a href="https://greypub.vercel.app" style="color: #4CAF50; text-decoration: none; font-weight: bold;">Visit our website</a>
                </p>
                <p>
                    
                </p>
                <p>Cheers,<br>The GreyPub Team</p>
            </body>
        </html>
    """
    
    mailer(to_email=email, subject=subject, message=message, is_html=True)

