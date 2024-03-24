import cv2
import numpy as np

def detect_needle(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    
    # Apply edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Apply morphological closing to enhance edges
    kernel = np.ones((5,5), np.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    
    # Perform Hough Line Transform
    lines = cv2.HoughLinesP(closed, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=10)
    
    if lines is not None:
        # Calculate the angle of the line
        mean_line = np.mean(lines, axis=0, dtype=np.int32)
        x1, y1, x2, y2 = mean_line[0]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        
        # Draw the line on the original frame
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return frame, angle

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect and draw the needle on the frame
    result, angle = detect_needle(frame)
    angle = angle + 90  # Adjust angle if necessary
    if angle < 45:
        angle += 180
    
    # Display the result
    cv2.imshow('Result', result)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()

print("Angle of the detected needle:", angle)
pressure = 0.55556 * (angle - 55)  # Calculate pressure
print("Pressure:", pressure)
