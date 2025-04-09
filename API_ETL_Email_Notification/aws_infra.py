import boto3
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
# print(config.sections())


bucket = config['AWS']["BUCKET_NAME"]
region = config["AWS"]["REGION"]

s3_client = boto3.client('s3', region_name=region)
# location = {'LocationConstraint': region} - location constrint not required when bucket is created in us-east-1 region.
s3_client.create_bucket(Bucket=bucket)

# We are able to connect to AWS because AWS Credentials are stored in the local.
print(f'Bucket "{bucket}" is created.')