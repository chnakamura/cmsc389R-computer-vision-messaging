import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('computer-vision-messaging')

data = open('test.jpg','rb')
bucket.put_object(Key='test.jpg', Body=data)

client = boto3.client('rekognition')
response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'computer-vision-messaging',
            'Name': 'test.jpg'
        }
    }
)

print response['Labels']