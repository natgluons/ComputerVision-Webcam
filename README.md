# ESP32-CAM Face Detection with OpenCV

This project streams video from an ESP32-CAM and performs face detection using OpenCV in Python.

## Overview

The ESP32-CAM is a cost-effective board with a built-in camera capable of streaming video over Wi-Fi. This project demonstrates how to use OpenCV to detect faces in real-time from the video stream provided by the ESP32-CAM.

## Requirements

### Hardware
- ESP32-CAM (AI Thinker model)
- USB-to-Serial adapter (for flashing the ESP32-CAM)

### Software
- Arduino IDE or PlatformIO for uploading the ESP32-CAM code
- Python 3.x with OpenCV library

## Use Case

This setup can be used for simple home security systems, smart doorbells, or any application requiring face detection on a live video stream.

## Quick Start

1. **Set up the ESP32-CAM**:
   - Upload the provided ESP32-CAM code using Arduino IDE or PlatformIO.
   - Connect the ESP32-CAM to your Wi-Fi network.

2. **Run the Python script**:
   - Use the provided Python script to connect to the ESP32-CAM's video stream.
   - OpenCV will detect and highlight faces in the video feed.

## Result

![computervision_webcam](https://github.com/user-attachments/assets/728f086b-8f61-4e34-9a72-20197c0c2a7e)

