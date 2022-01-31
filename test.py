from moto import mock_s3


@mock_s3
def test_multiple_downloads():
    bucket_name = "bnasdf"
    import boto3
    s3_client = boto3.client('s3', region_name='eu-west-1')
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-west-1'})
    with open('red.jpg', 'rb') as file:
        s3_client.upload_fileobj(file, bucket_name, "red.jpg")
    s3_client.head_object(Bucket=bucket_name, Key="red.jpg")

    r = s3_client.download_file(f"{bucket_name}.s3.amazonaws.com", "red.jpg", "test_file_temp.json")
    print(r)
    # this creates a file with content: <?xml version="1.0" encoding="UTF-8"?><ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>test_bucket.s3.eu-west-1.amazonaws.com</Name><MaxKeys>1000</MaxKeys><IsTruncated>false</IsTruncated><Contents><Key>area_type.json</Key><LastModified>2022-01-29T13:23:04.000Z</LastModified><ETag>&#34;b9e351ad74db70cb713126fd490137e4&#34;</ETag><Size>269601</Size><StorageClass>STANDARD</StorageClass><Owner><ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID><DisplayName>webfile</DisplayName></Owner></Contents></ListBucketResult>

    r = s3_client.download_file(f"{bucket_name}.s3.amazonaws.com", "red.jpg", "test_file_temp2.json")
    print(r)
    # this returns the actual file

    r = s3_client.download_file(f"{bucket_name}.s3.amazonaws.com", "red.jpg", "test_file_temp3.json")
    print(r)
    # this returns the xml meta data again
