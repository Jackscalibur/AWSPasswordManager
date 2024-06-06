import boto3
from botocore.exceptions import ClientError


class SecretsManager:
    def __init__(self):
        self.client = boto3.client('secretsmanager')
