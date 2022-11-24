import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName = 'Test', Attributes = {'DelaySeconds':'10'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))



