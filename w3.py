import os
import glob
import boto3
from botocore.exceptions import ClientError


def create_s3_bucket(bucket_name):
    print("Creating a bucket..." + bucket_name)

    s3 = boto3.client(
        's3',
        aws_access_key_id="",
        aws_secret_access_key=""
    )
    # print(s3)
    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-northeast-2'
            }
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists. skipping...")
        else:
            print("Unknown error, exit...")
            # print(e)


def dump(video_data, n):
    # os.system(f"ffmpeg -i {video_data} -ss 00:{n}:00 -to 00:{n+1}:00 -c copy output{n}.mp4")

    input_path = "/home/hyoinjeong/baedalgeekW3"
    files = glob.glob(os.path.join(input_path, f'{video_data}{n}.mp4'))
    stored_names = list(map(lambda x: x.split("/")[4], files))
    print(stored_names)

    s3 = boto3.client(
        's3',
        aws_access_key_id="",
        aws_secret_access_key=""
    )

    for file, name in zip(files, stored_names):
        s3.upload_file(file, "baedalgeekw3", name)

def load(n):
    # os.system(f"ffmpeg -i {video_data} -ss 00:{n}:00 -to 00:{n+1}:00 -c copy output{n}.mp4")

    s3 = boto3.client(
        's3',
        aws_access_key_id="",
        aws_secret_access_key=""
    )

    s3.download_file('baedalgeekw3',f'output{n}.mp4',f'/home/hyoinjeong/baedalgeekW3/return{n}.mp4')


# response = create_s3_bucket(bucket_name="baedalgeekw3")
# print("Bucket : " + str(response))
dump("output", 14)


# response = create_s3_bucket(bucket_name="baedalgeekw3")
# print("Bucket : " + str(response))
# dump("output", 13)
load(14)

