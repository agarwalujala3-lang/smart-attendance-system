# Smart Attendance System (AWS | Python | Face Recognition)

## Overview

The **Smart Attendance System** is a cloud-based, serverless application designed to automate attendance management using **AWS services and facial recognition technology.**
The system eliminates manual attendance processes by securely capturing facial images, verifying identities using AWS Rekognition, and storing attendance records in a scalable cloud database.

This project was developed as part of my **industrial training at CETPA Infotech Pvt. Ltd., Noida**, with a strong focus on **cloud architecture, service integration, and real-world AWS workflows.**

## Problem Statement

Traditional attendance systems rely on manual registers or basic digital sheets, which lead to:

- Human errors and data inconsistency

- Time-consuming manual processing

- Proxy attendance

- Lack of real-time visibility and reporting

- Difficulty in maintaining scalable records

The Smart Attendance System addresses these issues by providing a **secure, automated, and real-time cloud solution.**

## Project Objectives

- Automate attendance marking using facial recognition

- Store attendance records securely on the cloud

- Prevent duplicate and proxy attendance

- Enable real-time access to attendance data

- Design a scalable and cost-effective serverless system

## AWS Services Used

- **Amazon S3** – Storage of facial images

- **AWS Rekognition** – Face detection and matching

- **AWS Lambda (Python)** – Backend logic execution

- **Amazon API Gateway** – Secure REST API endpoints

- **AWS IAM** – Access control and permissions

## System Architecture

The system follows a **cloud-native, serverless architecture** with clearly separated layers:

- **User Interface Layer** – Captures images and displays results

- **API Management Layer** – Handles request routing and security

- **Application Logic Layer** – Processes attendance logic using Lambda

- **Data Storage Layer** – Stores images and attendance records

This design ensures **high availability, scalability, and minimal maintenance overhead.** 

## Architecture Workflow

- User captures an image from the frontend

- Image is uploaded to **Amazon S3**

- S3 event triggers **AWS Lambda**

- Lambda sends image to **AWS Rekognition** for face matching

- Rekognition returns match results

- Attendance is validated and stored in **DynamoDB**

- Confirmation response is returned via **API Gateway**

This event-driven flow ensures **real-time attendance marking.**

## Implementation Summary

### Environment Setup

- AWS account configured with IAM users and roles

- Local development using Python and VS Code

- Secure permissions configured for all AWS services

### Backend Logic

- Python-based AWS Lambda functions handle:

- Student registration

- Face indexing

- Attendance marking

- Data retrieval

- REST APIs exposed via API Gateway

### Storage & Database

- **Amazon S3** stores facial images securely

- **Amazon DynamoDB** stores:

    - Student details

    - Attendance records

    - Timestamps and status

### Frontend

- Simple web-based interface

- Admin panel for student registration

- Student panel for attendance marking

- Focused on functionality rather than UI complexity

## Testing & Verification

- Unit testing of Lambda functions

- Integration testing across AWS services

- Functional testing of:

    - Face recognition accuracy

    - Attendance storage

    - Duplicate entry prevention

- Performance testing under concurrent usage

The system performed reliably and efficiently.

## Project Evidence & Deployment Proof

This project was **fully deployed and tested on AWS.**

- Verified components include:

- Working frontend interface

- DynamoDB tables with real attendance records

- Active Lambda functions

- API Gateway routes

- IAM roles with required permissions

**Additional screenshots are available in the** /screenshots **directory**, including:

- Frontend UI

- DynamoDB tables

- Lambda functions

- API Gateway routes

- IAM permissions

- S3 buckets and Rekognition collections

## What I Learned

- Designing **serverless architectures** on AWS

- Integrating multiple AWS services into a single workflow

- Using **AWS Rekognition** for real-world applications

- Managing access securely with **IAM roles and policies**

- Building scalable systems without managing servers

## Future Enhancements

- Mobile application integration

- Advanced analytics and dashboards

- Multi-organization support

- Authentication using AWS Cognito

## Conclusion

The Smart Attendance System demonstrates a **practical implementation of cloud-based automation** using AWS.
It highlights how serverless services can be combined to build **secure, scalable, and real-time applications** suitable for educational and organizational use.