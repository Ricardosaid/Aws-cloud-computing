## Amazon SQS
### Requirements
Install Boto3 :

```console
pip install boto3
```

### Create a New Python SQS Queue: Standard

Standart = Messages are delivered in the same order as they are sent.

In this example will use the queue name `test`.

First, create a queue:

```console
# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '10'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
```


> Note:Thanks Boto3 Docs 1.26.16 documentation por the information! 