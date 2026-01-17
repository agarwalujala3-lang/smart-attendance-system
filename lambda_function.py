import json
import uuid
import datetime
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AttendanceTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        student_id = body.get('student_id')
        status = body.get('status')

        if not student_id or not status:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing required fields"})
            }

        attendance_id = str(uuid.uuid4())
        timestamp = datetime.datetime.utcnow().isoformat()

        item = {
            "attendance_id": attendance_id,
            "student_id": student_id,
            "status": status,
            "timestamp": timestamp
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Attendance recorded successfully",
                "attendance_id": attendance_id
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
