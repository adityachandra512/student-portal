import cv2

# Print OpenCV version
print(cv2.__version__)

# Try to create the LBPHFaceRecognizer
try:
    clf = cv2.face.LBPHFaceRecognizer_create()
    print("LBPHFaceRecognizer created successfully!")
except AttributeError as e:
    print(f"Error: {e}")
