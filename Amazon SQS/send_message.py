import boto3

sqs = boto3.resource('sqs')

# Get an SQS.Queue instance

queue = sqs.get_queue_by_name(QueueName = 'Test')

#queue = sqs.create_queue(QueueName = 'Test', Attributes = {'DelaySeconds':'10'})

responseBatch = queue.send_messages(
    Entries = [
        {
            'Id':'1',
            'MessageBody':'ImageOne'
        },
        {
            'Id':'2',
            'MessageBody':'ImageTwo',
            'MessageAttributes': {
                'Author': {
                    'StringValue':'SaidLeben',
                    'DataType':'String'
                }
            }
        }
    ]
)

# Create a new message
# response = queue.send_message(
#     MessageBody="Hallo wie gehts!",
#     MessageAttributes = {
#         'Author' : {
#             'StringValue':'Saidleben',
#             'DataType':'String'
#         }
#     }
# )

#The response is NOT a resource, but gives you a message ID
print(responseBatch.get('MessageId'))
print(responseBatch.get('MD50fMessageBody'))
print(responseBatch.get('Failed'))
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))



