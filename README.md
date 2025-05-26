# Automatic_Number_Plate_Recognition_Based_Restricted_Zone_Access_Control
Automated number plate recognition system with Arduino-based access control for restricted zones using OpenCV and Tesseract OCR.
# Description:

This project implements an Automatic Number Plate Recognition (ANPR) system integrated with restricted zone access control using computer vision and Arduino. The system captures real-time video using a webcam, processes the frames with Tesseract OCR to extract license plate text, and sends the recognized plate number to an Arduino through serial communication.

When a valid license plate (predefined in the Arduino code) is detected, the Arduino activates a response—such as lighting an LED or opening a gate (via a servo motor). This creates an automated, contactless access control system suitable for restricted areas such as parking lots, private buildings, or security zones.

# Key Components:

    OpenCV for video capture and frame processing

    Tesseract OCR for number plate recognition

    Arduino for controlling physical devices (e.g., LED or servo motor)

    Serial Communication between PC and Arduino

    Access validation logic to permit only authorized vehicles

# Use Cases:

    Secure entry to parking lots

    Gated community access

    Office building vehicle access

    Toll booths with whitelist-based entry
