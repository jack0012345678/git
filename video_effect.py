import socket
import time
import cv2
from gaze_tracking import GazeTracking
tello_ip = '192.168.10.1'
tello_port = 8889
tello_address = (tello_ip, tello_port)

socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

socket.sendto ('command'.encode (' utf-8 '), tello_address)
socket.sendto ('streamon'.encode (' utf-8 '), tello_address)
print ("Start streaming")
capture = cv2.VideoCapture ('udp:/0.0.0.0:11111',cv2.CAP_FFMPEG)

capture.open('udp:/0.0.0.0:11111')
gaze = GazeTracking()
while True:
    ret, frame =capture.read()
    print(ret)
    if(ret):
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""
    
        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
    
        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    
        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        
        
        img = cv2.resize(frame, dsize=(720, 500), interpolation=cv2.INTER_AREA)      

        cv2.imshow('frame', img)
    if cv2.waitKey (1)&0xFF == ord ('q'):
        break
capture.release ()
cv2.destroyAllWindows ()
socket.sendto ('streamoff'.encode (' utf-8 '), tello_address)