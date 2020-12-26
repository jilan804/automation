import boto3
iam = boto3.resource('iam') #using resource representing IAM
client = boto3.client('iam')

response = client.delete_user(
    UserName='user_Praveen31'
)
print(response)