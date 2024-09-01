import json
import os
from email.mime.text import MIMEText

import boto3
from jinja2 import Environment, FileSystemLoader

from src.content_generators import JokeGenerator, QuoteGenerator
from src.data_loader import DataLoader
from src.holiday_checker import HolidayChecker
from src.template_loader import TemplateLoader


def lambda_handler(event, context):
    query = "Tell me about today's holiday."
    holiday_checker = HolidayChecker()
    answer = holiday_checker.get_holiday_explanation(query)
    joke = JokeGenerator.get_random_joke()
    quote = QuoteGenerator.get_random_quote()
    # Email template
    sender = os.getenv('SES_SENDER')
    recipient = DataLoader.load_recipients('recipients.txt')
    subject = "[📝 Amazon Post-It] Morning Fuel: Motivate, Secure, Explore & Laugh Today"
    template = TemplateLoader.load_template('email_template.html')
    body = template.render(
        answer=answer,
        joke=joke,
        quote=quote,
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
