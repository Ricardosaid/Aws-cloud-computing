import boto3
sqs = boto3.resource('sqs')

#Get the queue

queue = sqs.get_queue_by_name(QueueName = "Test")

#Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames = ["Author"]):
    #Get the custom author message attribute is it was set
    author_text = ""
    if message.message_attributes is not None:
        author_name = message.message_attributes.get("Author").get("StringValue")
        if author_name:
            author_text = "({0})".format(author_name)
    
    #Print the body and author
    print("Hello, {0}! {1}".format(message.body, author_text))
    message.delete()