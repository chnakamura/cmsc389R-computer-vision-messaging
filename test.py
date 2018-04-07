import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('computer-vision-messaging')

if s3.Object('vision','test.jpg') is None:

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

passwd = response['Labels'][-1]['Name']
print passwd