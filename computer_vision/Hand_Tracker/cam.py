import cv2


class Cam:
    def __init__(self, cam, marker_image):
        self.cam = cam
        self.marker_image = marker_image

    def webcam_on(self, cap):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        return cap

# Check if the webcam is opened correctly


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()