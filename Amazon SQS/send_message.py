import boto3

sqs = boto3.resource('sqs')

# Get an SQS.Queue instance

queue = sqs.get_queue_by_name(QueueName = 'Test')

#queue = sqs.create_queue(QueueName = 'Test', Attributes = {'DelaySeconds':'10'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))



