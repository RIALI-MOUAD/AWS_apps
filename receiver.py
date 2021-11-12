import boto3
import statistics
import time
from datetime import datetime
from utils import *

# datetime object containing current date and time
now = str(datetime.now().strftime("%Y-%m-%d-%H%M%S"))
file = "log_"+now+".txt"

#print("now =", now)

# Get the service resource
sqs1 = boto3.resource('sqs')


#Get the queue
queueRequest = sqs1.get_queue_by_name(QueueName="requestQueue")

queue = sqs1.create_queue(QueueName='responseQueue', Attributes={
                'DelaySeconds': '2'
                })
#putText(txt_data, bucket="devilman", file="log.txt"):
while(1):
    try:
        #f = open(file,"a")
        for message in queueRequest.receive_messages():
            message1 = messageResp(message)
            response = sendMessage(queue ,message1)
            #time.sleep(2)
            #_ = createObject(file)
            _ = putText(message1,file=file)
            message.delete(QueueUrl='https://sqs.us-east-1.amazonaws.com/360548546737/requestQueue', ReceiptHandle=message.receipt_handle)
            print("request queue deleted")
    except:
        #f.close()
        print("Exception")
