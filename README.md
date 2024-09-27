#Smile Detector and Photo Capture
Overview
The Smile Detector and Photo Capture application utilizes OpenCV and Haar cascades for real-time face and smile detection via a webcam. When a smile is detected, the program captures a photo and saves it with a timestamped filename, allowing users to create a collection of smiling photos effortlessly.

Features
Real-Time Face Detection: Uses Haar cascades to detect faces in real time.
Smile Detection: Identifies smiles within detected faces.
Photo Capture: Automatically captures and saves an image when a smile is detected, naming the file with a timestamp.
User-Friendly Interface: Displays the webcam feed with detection rectangles around faces and smiles.
Requirements
Python 3.x
OpenCV library



Download the Haar cascade XML files for face and smile detection:
https://github.com/opencv/opencv/tree/master/data/haarcascades




hen a smile is detected, a photo will be taken and saved in the current directory with a timestamped filename (e.g., self-23-09-27-14-30-00.png).



Code Explanation
Video Capture: Initializes the webcam feed using cv2.VideoCapture(0).
Face and Smile Detection: The program uses Haar cascades to detect faces and smiles in the captured frames.
Photo Capture: When a smile is detected, the program captures the current frame and saves it to the disk with a timestamp.
Acknowledgments
OpenCV for the image processing functionalities.
Contributors of the Haar cascade classifiers.
License
This project is open source and available for anyone to use and modify.

