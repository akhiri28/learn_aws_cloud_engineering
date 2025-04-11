import json
import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone
import boto3
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
bucket = config['AWS']["BUCKET_NAME"]
region = config["AWS"]["REGION"]

def lambda_handler(event, context):
    # TODO implement
    uri = 'http://api.openweathermap.org/data/2.5/air_pollution/history?lat=17.3568&lon=78.4524&start=1712480400&end=1744015728&appid=81bfd28556d8968f573f03093881fd98'

    response = requests.get(uri)

    s3_client = boto3.client('s3', region_name=region)

    s3_client.put_object(Body = response.content, Bucket = bucket, 
                         Key = 'air_pollution_data_lambda.parquet', 
                         ContentType="application/json")
    return {
        'status': 'Success'
    }


