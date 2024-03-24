def detect_needle(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
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
        
        # Draw the line on the original image
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return image, angle

# Load the image
image = cv2.imread('gauge-5.jpg')

# Detect and draw the needle on the image
result, angle = detect_needle(image)
angle = angle+90
if (angle<45):
    angle = 180+angle
# Display the result
plt.imshow(image)

print("Angle of the detected needle:", angle)
#print(angle)
pressure = 0.55556*(angle - 55)
print("Detected pressure is:", pressure, "psi")
