import cv2
import numpy as np

class Cam:
    def __enter__(self):
        print("error occurred")
    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            print("hi")
            # return False # uncomment to pass exception through
        return True
    
    def __init__(self) -> None:
        print("Cam created")
        self.turnOnWebCam()
    
    def createColorMask(self, tolerance):
        upper_bound = np.array([179, 255, 255])
        lower_bound = np.array([0,10,200])

        return (upper_bound, lower_bound)

    def turnOnWebCam(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        upperBound, lowerBound = self.createColorMask(10)

        while True:
            _, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            mask = cv2.inRange(frame, lowerBound, upperBound)

            maskedImage = cv2.bitwise_and(frame, frame, mask=mask)

            
            cv2.rectangle(frame, (0, 0), (200, 200), (0, 0, 0), 1)

            frame = cv2.addWeighted(frame, 1, maskedImage, 1,0)

            cv2.imshow('Input', maskedImage)
            c = cv2.waitKey(1)
            if c == ord('q'):
                break
        cv2.destroyAllWindows()

   

    

# Check if the webcam is opened correctly


