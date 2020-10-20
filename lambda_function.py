import random
# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('HelloWorldDatabase')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    c=random.randint(0,10)
# extract values from the event object we got from the Lambda service and store in a variable
    name = event['Name'] 
    name1= event['birthday']
    name2= event['school']
    data='Hello '+name2+' student, ' + name
    day = [20,19,21,20,21,22,23,23,23,24,23,22] #按日期順序把每个月的分隔星座的日期列出来，從1月
    star = ['Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius']
    birthday=name1.split("/")
    month=str(birthday[0])
    date=str(birthday[1])
# write name and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        
        Item={
            'ID': name,
            'LatestGreetingTime':now
            })
# return a properly formatted JSON object
    if int(date) < day[int(month)-1]: 
        return {
            'statusCode': 200,
            'body': json.dumps(data+'. Your astrological sign is '+star[int(month)-1]+', luckey number is '+str(c)+'. ')
        }
    elif int(month)==12 and int(date)>21: 
        return {
            'statusCode': 200,
            'body': json.dumps(data+'. Your astrological sign is '+star[0]+', luckey number is '+str(c)+'. ')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(data+'. Your astrological sign is '+star[int(month)]+', luckey number is '+str(c)+'. ')
        }

