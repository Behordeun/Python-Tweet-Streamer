# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:0045 2022
Updated on Tue Jun 30 12:02pm 2022

@author: Behordeun
"""
###################################################################################
##1. This Script will copy json files in it's direct path to an s3 bucket.
##2. It accepts the name of the file and see if it can find the file in it's immediate path only. 
##3. If it cannot find the file, it suggests attempting to upload all json files in same folder
##4. Check if file is already in the bucket and skips if true
############# Requirements: ###################
# AWS credentials saved as keys.py in same folder
##################################################################################

from datetime import datetime as dt
from time import sleep
import boto3, os
import pandas as pd
from keys import aws_access_key_id, aws_secret_access_key, region_name

year = dt.now().year
month= dt.strftime(dt.now(), '%B')
day = dt.now().day

#Prepare AWS Session with Credentials
session = boto3.session.Session(
    aws_access_key_id = aws_access_key_id, 
    aws_secret_access_key = aws_secret_access_key, 
    region_name = region_name)
s3 = session.client('s3')


def s3_upload(filename_on_disk, year=year, month=month, day=day):
    """
    Put json file into s3 bucket if it is not already there, organizing them by keyword and production date.
    """
    
    filename_aws = f"{year}/{month}/{day}/{filename_on_disk}"
    if filename_aws in [line['Key'] for line in s3.list_objects(Bucket='dgasm-2.0')['Contents']]:
        return False, "File with same name already in the bucket!\n"

    
    print("Uploading file(s) ...")
    try:
        s3.upload_file(filename_on_disk, 'dgasm-2.0', filename_aws)
        print('Done!')
        return True, 'File uploaded!'
    except Exception as e:
        print(f"Error uploading: {e}")
        return False, 'Something went wrong'

def write_all_json():
    """
    Get all json files and see if they are already in the bucket before putting
    """
    total_files = 0
    total_uploaded_files = 0
    for line in [line for line in os.listdir() if line.endswith('.json')]:
        print(f"Attempting upload of {line} to s3 ...")
        try:
            status, message = s3_upload(line)
            if status:
                total_uploaded_files += 1
                sleep(1)
            else:
                print(message)
                sleep(1)
            total_files += 1
        except Exception as e:
            print(f"Error writing file '{line}' to disk. Skipped...")
    return True, f"Wrote {total_uploaded_files} of {total_files} files(s) to s3."


#Da Flow
user_filename = input("Input the filename if you know it, else type 'No'.\n>>>  ")
if user_filename.lower() != 'no':
    #try to find this file on the disk
    if not os.path.exists(user_filename.strip()):
        print(f"We cannot find any file by name '{user_filename}'")
        ans = input("Should we process and search for un-uploaded files?\nYes/No >>> ")
        if ans.lower() == 'no':
            print("Got that. See ya!")
            raise SystemExit
        elif ans.lower() == 'yes':
            _, message = write_all_json()
            print(message)
        else:
            print(f"{ans} is neither 'Yes/No'. See ya!")
            raise SystemExit
    else:
        _, message = s3_upload(user_filename)
        print(message)
elif user_filename.lower() == 'no':
    _, message = write_all_json()
    print(message)