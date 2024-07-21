import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # 0 for default camera, replace with video file path for video

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    gray = cv2.GaussianBlur(gray, (15, 15), 0)

    # Perform edge detection
    edges = cv2.Canny(gray, 30, 150)

    # Perform a dilation and erosion to close gaps in between object edges
    dilated = cv2.dilate(edges, None, iterations=2)
    eroded = cv2.erode(dilated, None, iterations=1)

    # Find contours in the eroded image
    contours, _ = cv2.findContours(eroded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours and draw them on the original frame
    for contour in contours:
        # We can add condition on contour size to filter out small noise
        if cv2.contourArea(contour) > 100:  
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.circle(frame, (x + w // 2, y + h // 2), max(w // 2, h // 2), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
