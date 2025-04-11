import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone
import json
import boto3
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
bucket = config['AWS']["BUCKET_NAME"]
region = config["AWS"]["REGION"]


def create_uri():

    uri = 'http://api.openweathermap.org/data/2.5/air_pollution/history?lat=17.3568&lon=78.4524&start=1712480400&end=1744015728&appid=81bfd28556d8968f573f03093881fd98'
    return uri
 
def fetch_data(uri):

    response = requests.get(uri)
    
    return response.content


def save_data_to_file(data):

    timeStamp_utc = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    filename = f'{timeStamp_utc}.parquet'

    with open(filename, 'w') as f:
        json.dump(data, f, indent = 2)

    return filename


def store_file_in_s3(bucket, api_response, object_name):

    s3_client = boto3.client('s3', region_name=region)
    s3_client.put_object(Body = api_response, Bucket = bucket, 
                         Key = object_name, ContentType="application/json")

    print('File Uploaded Successfully !!!')
    

if __name__ == '__main__':

    uri = create_uri()

    data = fetch_data(uri)

    # file = save_data_to_file(data)

    store_file_in_s3(bucket = bucket, api_response= data, object_name= 'air_pollution_data.parquet')

