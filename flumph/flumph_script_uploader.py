import boto3

client = boto3.client("s3")
client.upload_file("flumph_script.lua", "change_me", "flumph_script.lua")
