import cv2
import time

class CallBack:

    def __init__(self):
        cv2.namedWindow("Camera", cv2.CV_WINDOW_AUTOSIZE )
        self.capture = cv2.VideoCapture(0)
        self.param = "hola, son las "+time.asctime()

    def on_mouse(self,event, x, y, flag, param):
        if(event == cv2.cv.CV_EVENT_MOUSEMOVE):
           print param
           print x,y
           print flag

    def callback(self):
        while True:
             flag, src = self.capture.read()
             cv2.setMouseCallback("Camera",self.on_mouse, param = self.param)
             cv2.imshow("Camera", src)
             self.param = "hola, son las "+time.asctime()
             if cv2.waitKey(10) == 27:
                  break

if __name__ == '__main__':
    cb = CallBack()
    cb.callback()
