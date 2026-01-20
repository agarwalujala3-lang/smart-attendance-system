## Implementation Overview

The Smart Attendance System was implemented using AWS serverless services.
The project focuses on service integration rather than heavy frontend or backend coding.

AWS Lambda functions handle registration and attendance logic.
API Gateway exposes REST endpoints used by the web interface.
Amazon Rekognition is used for facial recognition and matching.
DynamoDB stores student and attendance data.
Amazon S3 is used for storing facial images.

The implementation emphasizes scalability, security, and real-time processing.
