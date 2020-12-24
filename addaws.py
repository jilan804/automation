import boto3
iam = boto3.resource('iam') #using resource representing IAM
created_user = iam.create_user(
    UserName='user_Praveen31'
)
print(created_user)
