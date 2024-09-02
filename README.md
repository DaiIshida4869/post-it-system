# Integration of AWS Bedrock API for Customizable Newsletters

> Use AWS Bedrock to generate information for your business newsletter. 

# Setting Up AWS Bedrock API:

> Access and Authentication: Begin by setting up your AWS account and obtaining API credentials for AWS Bedrock. This involves configuring access roles and permissions to securely interact with the service.

# Generating Newsletter Content:

> Content Creation: Use AWS Bedrock’s natural language generation models to draft initial content for your newsletters. You can provide prompts or themes related to your business’s news, updates, and industry trends.

# Setting Up Email Recipients:
To send the newsletter to multiple recipients, create a CSV file named recipients.csv that contains the email addresses of the recipients. Each email address should be separated by a comma on a single line. This CSV file will be used by the Lambda function to send the emails.  
Example of `recipients.csv`:  
```
recipient1@example.com,
recipient2@example.com,
recipient3@example.com
```

# Documentation 
* Working with .zip file archives for Python Lambda functions - https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
* Getting started with Amazon Bedrock - https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html
* Defining Lambda function permissions with an execution role - https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html
* Create an EventBridge scheduled rule for AWS Lambda functions - https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html

# Architecture
![AWS Diagram](https://github.com/DaiIshida4869/post-it-system/blob/main/AWS%20Diagram.png)
