import cv2
from multiprocessing import Process

def f(camID):
        vc = cv2.VideoCapture(camID)
        camIDstr = str(camID)
        cv2.namedWindow("preview" + camIDstr)
        if vc.isOpened(): # try to get the first frame
                rval,  frame  = vc.read()
        else:
                rval  = False

        while rval:
                cv2.imshow("preview" + camIDstr, frame)
                rval, frame = vc.read()
                key = cv2.waitKey(2)
                if key == 27: # exit on ESC
                        break
        cv2.destroyWindow("preview" + camIDstr)

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