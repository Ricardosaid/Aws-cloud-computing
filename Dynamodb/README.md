## DynamoDB 
### Requirements
Install Boto3 :

```console
pip install boto3
```
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

### Write Data to a table

In CLI:
```console
aws dynamodb put-item \
--table-name Music \
--item \
'{"Artist":{"S":"Artista Uno"},"SongTitle":{"S":"Cancion Uno"},"AlbumTitle":{"S":"Album uno"},"Awards":{"N":"1"}}'
```

### Read data from a table

In CLI:
```console
aws dynamodb get-item --consistent-read \
--table-name Music \
--key '{"Artist":{"S":"Artista Uno"},"SongTitle":{"S":"Cancion Uno"}}'
```

### Update data in a tabla 

In CLI:
```console
aws dynamodb update-item \
--table-name Music \
--key '{"Artist":{"S":"Artista Uno"},"SongTitle":{"S":"Cancion uno"}}' \
--update-expression "SET AlbumTitle = :newval" \
--expression-attribute-values '{":newval":{"S":"Updated Album Title"}}' \
--return-values ALL_NEW
```

### Query data in a table
```console
aws dynamodb query \
--table-name Music \
--key-condition-expression "Artist = :name" \
--expression-attribute-values '{":name":{"S":"Coldplay"}}'
```
> Note: --projection-expression "SongTitle" -> filter of SongTitle

### Scan a table

```console
aws dynamodb scan \
--table-name Music
--filter-expression "Artist =:name" \
--expression-attribute-values '{":name":{"S":"Coldplay"}}'
```

