# TODO implement rate limit protection

import boto3 
from dotenv import load_dotenv
import os
import requests
load_dotenv()

url_arr = ["URL_STRING_1", "URL_STRING_2"]

# setup S3 destination
session = boto3.Session()
s3 = session.resource('s3')
bucket_name = os.getenv('BUCKET_NAME')
print(bucket_name)
bucket = s3.Bucket(bucket_name)

"""
read contents of each URL then
put object in S3 bucket
"""
for i, url in enumerate(url_arr):
  # print(url)
  r = requests.get(url, stream=True)
  key = f'test-file_{i}.jpeg'
  bucket.upload_fileobj(r.raw, key)
