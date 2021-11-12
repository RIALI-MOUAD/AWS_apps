import statistics
import boto3
import time
from datetime import datetime


#now = str(datetime.now())
def messageResp(message):
    now = str(datetime.now().strftime("%Y-%m-%d-%H%M%S"))
    t=[int(n) for n in (format(message.body)).split()]
    minimum, maximum = min(t),max(t)
    sum1, length = sum(t), len(t)
    average, median = sum1/length, statistics.median(t)
    return now+" : minimum is %d " %(minimum) + " maximum is %d " %(maximum)+  " average is %d  " %(average) + " median is %d " %(median)

def check10(s):
    t=[int(n) for n in s.split()]
    return (len(t)>10) or (any(n < 0 for n in t))

def sendMessage(queue ,message ,file=None):
    print('sending...')
    print(message)
    #file.write(message+'\n')
    print('Sent!!')
    return queue.send_message(MessageBody=message)

'''
        current_date_and_time = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        current_date_and_time_string = str(current_date_and_time)
        extension = ".txt"
        log_file =  "log_"+current_date_and_time_string + extension
        s3 = boto3.resource('s3')
        txt_data = results
        object = s3.Object(bucket_name='partie1', key=log_file)
            result = object.put(Body=txt_data)
'''
def putText(txt_data, bucket="devilman", file="log.txt"):
    #print('creating Object...')
    s3 = boto3.resource('s3')
    object = s3.Object(bucket_name=bucket, key=file)
    result = object.put(Body=txt_data)
    print('Object created!!')
    return result

def createObject(fileSrc, bucket="devilman", file="log.txt"):
    print('creating Object...')
    s3 = boto3.resource('s3')
    result = s3.Bucket(bucket).upload_file(fileSrc,file)
    print('Object created!!')
    return result
