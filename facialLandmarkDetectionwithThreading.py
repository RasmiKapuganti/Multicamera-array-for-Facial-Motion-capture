import dlib
import cv2
import threading
import numpy as np
from renderFace import renderFace
import os


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID

    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)


def writeLandmarksToFile(landmarks, landmarksFileName):
    with open(landmarksFileName, 'w') as f:
        for p in landmarks.parts():
            f.write("%s %s\n" % (int(p.x), int(p.y)))

    f.close()


# Landmark model location
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
# Get the face detector
faceDetector = dlib.get_frontal_face_detector()
# the landmark detector is implemented in the shape_predictor class
landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)


def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False

    #counter to store the frames in a folder "frameswiththreading"
    count = 0

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()

        #save frames in the frames folder
        framespath = "C:/Users/rasmi/Desktop/RasmiCapstone/frameswiththreading"
        cv2.imwrite(os.path.join(framespath, "frame%dCamera%d.jpg" % (count,camID)  ), frame)
        count += 1

        #Detect faces in the image
        faceRects = faceDetector(frame, 0)
        print ("Number of faces detected in Camera %d : " % camID,len(faceRects))

        # List to store landmarks of all detected faces
        landmarksAll = []

        # Loop over all detected face rectangles
        for i in range(0, len(faceRects)):
            newRect = dlib.rectangle(int(faceRects[i].left()), int(faceRects[i].top()),
                                     int(faceRects[i].right()), int(faceRects[i].bottom()))

            # for every face rectangle, run landmarkDetector
            landmarks = landmarkDetector(frame, newRect)

        # Print number of landmarks
        if i == 0:
            print ("Number of landmarks", len(landmarks.parts()))

        # store landmarks for current face
        landmarksAll.append(landmarks)

        # Draw landmarks on face
        renderFace(frame, landmarks)

        #cv2.imshow("Facial Landmark detector", frame)

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)


# Create threads as follows
thread1 = camThread("Camera 0", 0)
print ("Thread1 created")
print ()
thread2 = camThread("Camera 1", 1)
print ("Thread2 created")
print ()
thread3 = camThread("Camera 2", 2)


thread1.start()
print ("just checking flow thread 1 start")
thread2.start()
print ("Checking flow thread 2 start")
thread3.start()
print ("Checking thread 3 start")
print()
print("Active threads", threading.activeCount())
