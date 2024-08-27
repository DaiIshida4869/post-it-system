import os

import boto3
from botocore.exceptions import ClientError


class BedrockAuth():
    
    def __init__(self):
        self.runtime = "bedrock-runtime"
        self.region_name = os.getenv('REGION_NAME')
        self.aws_access_key_id = os.getenv('ACCESS_KEY')
        self.aws_secret_access_key = os.getenv('SECRET_ACCESS_KEY')

    def load_client(self):
        try:
            client = boto3.client(
                self.runtime,
                region_name=self.region_name,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key
            )
            return client
        except ClientError as e:
            print(e)
