import boto3
import time
from utils import check10

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='requestQueue', Attributes={
                'DelaySeconds': '0'
                })

print(queue.url)


while(1):
    val = input("Enter your value: ")
    while(check10(val)):
        print('10 Element exceeded Or Negative numbers Detected!!')
        val = input("Enter your value: ")
    response = queue.send_message(MessageBody=val)
    #time.sleep(3)
    # Get the queue
    queueResponse = sqs.get_queue_by_name(QueueName='responseQueue')
    # Process messages by printing out body and optional author name
    #print(queueResponse.receive_messages()[0].body)
    time.sleep(15)
    for message in queueResponse.receive_messages():
        print(format(message.body))
        #time.sleep(4)
        message.delete(QueueUrl='https://sqs.us-east-1.amazonaws.com/360548546737/responseQueue', ReceiptHandle=message.receipt_handle)
