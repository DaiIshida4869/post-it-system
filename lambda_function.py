import json
import os
from email.mime.text import MIMEText

import boto3
from email_lists.list_ses_recipient_email import recipient_emails_list
from jinja2 import Environment, FileSystemLoader
from security_tips.list_of_security_tips import security_tips

from src.content_generators import (JokeGenerator, QuoteGenerator,
                                    SecurityTipGenerator)
from src.holiday_checker import HolidayChecker


def load_template(template_name):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    return env.get_template(template_name)

def lambda_handler(event, context):
    query = "Tell me about today's holiday."
    holiday_checker = HolidayChecker()
    answer = holiday_checker.get_holiday_explanation(query)
    joke = JokeGenerator.get_random_joke()
    quote = QuoteGenerator.get_random_quote()
    security_tip = SecurityTipGenerator.get_random_security_tip(security_tips)
    # Email template
    sender = os.getenv('SES_SENDER')
    recipient = recipient_emails_list
    subject = "[📝 Amazon Post-It] Morning Fuel: Motivate, Secure, Explore & Laugh Today"
    template = load_template('email_template.html')
    body = template.render(
        answer=answer,
        joke=joke,
        quote=quote,
        security_tip=security_tip
    )
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    # AWS SES
    client = boto3.client('ses', region_name='us-east-1')
    response = client.send_email(
        Destination={'ToAddresses': [recipient]},
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': body,
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source=sender,
    )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }
