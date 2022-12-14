using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.S3.Util;

class CreateBucket
{
    private const string bucketName = "Name";
    //especificamos la region
    private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USEast1;
    private static IAmazonS3 s3Client;

    public static void Main()
    {
        //Creamos nuestro cliente s3
        s3Client = new AmazonS3Client(bucketRegion);
        CreateBucketAsync().Wait();
    }

    public static async  Task CreateBucketAsync()
    {
        try
        {
            if (!(await AmazonS3Util.DoesS3BucketExistV2Async(s3Client, bucketName)))
            {
                var putBucketRequest = new PutBucketRequest
                {
                    BucketName = bucketName,
                    UseClientRegion = true
                };
                PutBucketResponse putBucketResponse = await s3Client.PutBucketAsync(putBucketRequest);

            }

            string bucketLocation = await FindBucketLocationAsync(s3Client);
        }
        catch (AmazonS3Exception e)
        {
            Console.WriteLine(e);
            throw;
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
    }

    public static async Task<string> FindBucketLocationAsync(IAmazonS3 amazonS3)
    {
        string bucketLocation;
        var request = new GetBucketLocationRequest
        {
            BucketName = bucketName
        };
        GetBucketLocationResponse response = await amazonS3.GetBucketLocationAsync(request);
        bucketLocation = response.Location.ToString();
        return bucketLocation;
    }
}