import os
import boto3
from dotenv import load_dotenv
import re
from botocore.exceptions import ClientError
import requests


load_dotenv()

s3_client = boto3.client('s3',
                        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
                        region_name=os.environ.get("AWS_REGION"), 
                        config=boto3.session.Config(signature_version='s3v4'))
s3_bucket_name = os.environ.get("AWS_BUCKET_NAME")
print("Completed")


#sample data
bike_model_id = 328
company = "Suzuki"
model = "Access 125 (BS6)"
img_file_name = "SUZUKI_ACCESS_125_(BS6).png"
bike_image_key = 'bike_models/images/'+ re.sub(r'(?<=\d)(?=(?:\d\d\d)+\b)',
                                                   '/',
                                                   f'{bike_model_id:09d}')+'/medium/'+img_file_name
print(bike_image_key)

#generating presigned URL
def create_presigned_url(bucket_name, object_name):
    try:
        response = s3_client.generate_presigned_url(
                'get_object',
                Params={
                        "Bucket":bucket_name,
                        "Key":object_name,
                    }
            )
        return response
    except ClientError as e:
        return e
"""
url_link = create_presigned_url(s3_bucket_name, bike_image_key)
#print(url_link)
response = requests.get(url_link)
print(response)
"""
#generating a presigned url to upload a file
def create_presigned_post(bucket_name, object_name):
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name)
    except ClientError as e:
        print("Hello")
        return e
    return response

object_name = "rb_logo.svg"
"""
url_link = create_presigned_url(s3_bucket_name, object_name)
print(url_link)
response = requests.get(url_link)
print(response)
"""
"""
response = create_presigned_post(s3_bucket_name, object_name)
print(response)
"""
#access control list
"""
result = s3_client.get_bucket_acl(Bucket=s3_bucket_name)
print(result)
"""

#retrieving the list of buckets
"""
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket["Name"])
"""

#uploading file
def upload_file(filename, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(filename)

    try:
        response = s3_client.upload_file(filename, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True
"""
response = upload_file("rb_logo.svg", s3_bucket_name)
print(response)
"""
"""
print(os.path.basename(object_name))
"""

#downloading a file
def download_file(bucket_name, object_name, file_name):
    try:
        response = s3_client.download_file(bucket_name, object_name, file_name)
    except ClientError as e:
        print(e)
        return False
    return True

response = download_file(s3_bucket_name, "rb_logo.svg", "rb_logo.svg")
print(response)











