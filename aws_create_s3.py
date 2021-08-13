#!/bin/python3
#Python Program for creating an S3 bucket with the given region & bucket name
import boto3
import sys

#connecting to S3

#myregion = 'eu-west-2'
myregion = sys.argv[1]

s3_client = boto3.client('s3',
	region_name=myregion)

#bucket_name = 'jyothypython123bucket'
bucket_name = sys.argv[2]
location= {'LocationConstraint': myregion}

#Function for create bucket

s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)

