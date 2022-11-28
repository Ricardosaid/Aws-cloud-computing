# Aws-cloud-computing
Cloud computing samples

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

## DynamoDB 

### Using DynamoDB locally

If port 8000 is already in use, specify a different port number using the `--port ` option

Specify the parameter `--endpoint-url` to connect to the local database

Update the endpoint in your code when you are ready to connect to the web service

```console
docker pull amazon/dynamodb-local
docker run -p 8000:8000 amazon/dynamodb-local:latest
```

### Create a table

The table's name is `Music` and has the following details:

1. Partition Key - `Artist`
2. Sort Key - `SongTitle`

Code in aws:

```console
aws dynamodb create-table \
--table-name Music \
--attribute-definitions \
AttributeName=Artist,AttributeType=S \
AttributeName=SongTitle,AttributeType=S \
--key-schema \
AttributeName=Artist,KeyType=HASH \
AttributeName=SongTitle,KeyType=RANGE \
--provisioned-throughput \
ReadCapacityUnits=5,WriteCapacityUnits=5 \
--table-class STANDARD
```
To verify the table's status, in CLI:

```console
aws dynamodb describe-table --table-name Music | grep TableStatus
```
You'll see the status as `ACTIVE`

Like best practice, enable `Point-in-time recovery for DynamoDB` by running the following command:
```console
aws dynamodb update-continuous-backups \
--table-name Music \
--point-in-time-recovery-specification \
PointInTimeRecoveryEnabled=true
```
> Note: There are cost implications to enabling continuous backups with point-in-time recovery
