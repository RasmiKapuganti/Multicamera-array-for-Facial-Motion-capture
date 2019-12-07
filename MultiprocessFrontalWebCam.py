import cvlib as cv
import cv2
from multiprocessing import Process
import os
import threading


def f(camID):
    vc = cv2.VideoCapture(camID)

    # counter to store the frames in a folder "frameswiththreading"
    count = 0

    if not vc.isOpened():
        print("Could not open webcam")
        exit()

    # loop through frames
    while vc.isOpened():



        camIDstr = str(camID)
        cv2.namedWindow("preview" + camIDstr)
        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()

        if not rval:
            print("Could not read frame")
            exit()



        # apply face detection
        face, confidence = cv.detect_face(frame)

        print(face)
        print(confidence)

        # save frames in the frames folder
        framespath = "C:/Users/rasmi/Desktop/RasmiCapstone/newframes"


        # loop through detected faces
        for idx, fi in enumerate(face):
            (startX, startY) = fi[0], fi[1]
            (endX, endY) = fi[2], fi[3]

            cv2.imwrite(
                os.path.join(framespath, "frame%dCamera%dConfidence%4.2f.jpg" % (count, camID, confidence[idx] * 100)),
                frame)
            count += 1

            # draw rectangle over face
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

            text = "{:.2f}%".format(confidence[idx] * 100)


            Y = startY - 10 if startY - 10 > 10 else startY + 10

            # write confidence percentage on top of face rectangle
            cv2.putText(frame, text, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 0), 2)

        # display output
        cv2.imshow("Real-time face detection" + camIDstr, frame)



        # press "Q" to stop
        key = cv2.waitKey(2)
        if key == 27:  # exit on ESC
            break
    vc.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
        #f(0)
        '''
        t0 = threading.Thread(target=f, args= (0,))
        t0.start()
        t1 = threading.Thread(target=f, args= (1,))
        t1.start()
        
        '''
        p0 = Process(target=f, args=(0,))
        p0.start()
        p1 = Process(target=f, args=(1,))
        p1.start()
        p2 = Process(target=f, args=(2,))
        p2.start()