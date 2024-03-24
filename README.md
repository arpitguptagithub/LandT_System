# Multilingual Automation System README

## Project Overview

This project aims to develop a multilingual automation system for level and pressure control using Google Assistant and Raspberry Pi. The system leverages natural language processing (NLP) techniques using the SpaCy library to interpret user commands. Additionally, basic Python libraries such as Matplotlib and Pandas are utilized for version control of the system's data. To ensure security, the project employs libraries like hashlib and secrets for password storage, safeguarding against cybersecurity threats.

## Features

- Multilingual support for user interaction.
- Automation of level and pressure control systems.
- Integration with Google Assistant for voice commands.
- Raspberry Pi implementation for physical control.
- NLP processing using SpaCy for interpreting user instructions.
- Version control of system data using Matplotlib and Pandas.
- Secure password storage using hashlib and secrets.

## Contributors 
- [Arpit Gupta](https://github.com/arpitguptagithub)
- [Chirag Kotian](https://github.com/ChiragKotian)
- [Sudhakar V](https://github.com/sudhakarv1)

## Presentation 
<iframe src="https://github.com/arpitguptagithub/LandT_System/raw/main/CreaTech Submission Tempelate.pptx" width="100%" height="400px"></iframe>


## Installation Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-repo-url.git
    ```

2. Install required Python libraries:

    ```bash
    pip install spacy matplotlib pandas
    ```

3. Set up SpaCy language models:

    ```bash
    python -m spacy download en
    python -m spacy download fr
    # Add additional languages as needed
    ```

4. Run the system:

    ```bash
    python main.py
    ```

## Usage

1. Ensure the Raspberry Pi is properly connected to the control systems.
2. Activate Google Assistant and initiate communication with the automation system.
3. Issue voice commands in the preferred language for level and pressure control.
4. Monitor system responses and feedback.
5. Utilize version control features to track changes and maintain data integrity.
6. Ensure passwords are securely stored and managed using provided libraries.

## Pressure Control System Details

The pressure control system is designed to regulate pressure using a PID (Proportional-Integral-Derivative) controller. Here's a detailed explanation of its operation:

- **Components Used:**
  - Normal compressor with an analog pressure meter.
  - On-off feature for compressor operation.
  - PWM control scheme for variable speed of the air pump generated using Raspberry Pi 5.
  - Motor driver: Cytron Smart Drive 40 Enhanced MDS40B.
  - Lab bench power supply set to CV mode (12V).

- **PID Control:**
  - The PID controller regulates the duty cycle of the PWM signal.
  - The user sets the setpoint pressure.
  - The algorithm, based on the current pressure (to be measured using a pressure sensor), determines the duty cycle.
  - This ensures that the system maintains the desired pressure level effectively.

- **Implementation Details:**
  - The system operates on threads to ensure a constant PID control loop frequency.
  - Threads enable parallel execution of tasks, ensuring efficient operation and timely response to pressure changes.

## OpenCV Needle Detection Script

This Python script utilizes OpenCV (Open Source Computer Vision Library) to detect and track the position of a needle on a gauge from live video footage captured by a camera. The detected angle of the needle is then used to calculate a corresponding pressure value.

### Code Breakdown

1. **Import Libraries:** The script begins by importing necessary libraries, including OpenCV (cv2) for image processing and NumPy (np) for numerical computations.

2. **detect_needle Function:**
   - This function takes a frame (image) captured from the camera as input.
   - It processes the frame to detect the needle's position using computer vision techniques:
     - Conversion to grayscale: Converts the color image to grayscale for easier processing.
     - Gaussian Blur: Applies Gaussian blurring to reduce noise in the image.
     - Canny Edge Detection: Detects edges in the image using the Canny edge detection algorithm.
     - Morphological Closing: Performs morphological closing to enhance the detected edges.
     - Hough Line Transform: Applies the Hough Line Transform to detect lines in the image, particularly the needle.
   - If lines representing the needle are detected:
     - It calculates the angle of the needle from the horizontal axis using the arctangent function.
     - Draws the detected line on the original frame.
   - Returns the frame with the detected needle and its angle.

3. **Main Loop:**
   - The script initializes the camera capture object (cap) to access the default camera.
   - It enters a while loop to continuously capture frames from the camera.
   - Inside the loop, each frame is processed using the detect_needle function to detect and track the needle.
   - The detected angle of the needle is adjusted as needed and displayed on the frame.
   - Pressing the 'q' key terminates the loop and exits the program.

4. **Release Resources:**
   - After exiting the loop, the script releases the camera capture object and closes all OpenCV windows.

5. **Output:**
   - The angle of the detected needle and the corresponding pressure value are printed to the console.

### Usage

To use this script:
- Ensure that you have Python installed along with the required libraries (opencv-python and numpy).
- Connect a camera to your system.
- Run the script.
- Point the camera towards the gauge you want to monitor.
- The script will continuously display the video feed with the detected needle's angle and pressure value.
- Press 'q' to exit the program.

### Note

- This script assumes that the needle moves in a linear manner and that the gauge has been properly calibrated to provide accurate pressure readings.
- Depending on the environment and lighting conditions, you may need to adjust parameters such as the Gaussian blur kernel size, Canny edge detection thresholds, and Hough Line Transform parameters to achieve optimal needle detection.

