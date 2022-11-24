import boto3

sqs = boto3.resource('sqs')

# Get an SQS.Queue instance

queue = sqs.get_queue_by_name(QueueName = 'Test')

#queue = sqs.create_queue(QueueName = 'Test', Attributes = {'DelaySeconds':'10'})

# Create a new message
response = queue.send_message(
    MessageBody="Hallo wie gehts!",
    MessageAttributes = {
        'Author' : {
            'StringValue':'Saidleben',
            'DataType':'String'
        }
    }
)

#The response is NOT a resource, but gives you a message ID
print(response.get('MessageId'))
print(response.get('MD50fMessageBody'))
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))



