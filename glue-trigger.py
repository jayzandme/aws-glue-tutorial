import boto3

def lambda_handler(event, context):

source_key_name = event['Records'][0]['s3']['object']['key']
filename = source_key_name.rsplit('/',1)[1].split('.',1)[0]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('glue_triggers')

dynamodb_response = table.get_item(Key={'filename':filename})
glue_job = dynamodb_response['Item']['glue_job']

glue = boto3.client('glue')
glue_response = glue.start_job_run(JobName = glue_job)