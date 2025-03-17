import cv2 as cv
import numpy as np

# 기본 변수 설정
recording = False
filter_mode = 0
video_writer = None

camera = cv.VideoCapture(0)
assert camera.isOpened(), 'Cannot capture source'

# 버튼 위치 설정
recording_button = (80, 80)
filter_button = (200, 80)
button_size = 50

def mouse_event_handler(event,x,y,flags,param):
    global recording, filter_mode, video_writer
    
    if event == cv.EVENT_LBUTTONDOWN:
        record_dist = np.sqrt((x - recording_button[0])**2 + (y - recording_button[1])**2)
        filter_dist = np.sqrt((x - filter_button[0])**2 + (y - filter_button[1])**2)

        if record_dist < button_size:
            recording = not recording
            if recording:
                frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
                frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))
                video_writer = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'mp4v'), 20.0, (frame_width, frame_height))
            else:
                video_writer.release()

        if filter_dist < button_size:
            filter_mode = (filter_mode + 1) % 3

cv.namedWindow('Video Recorder')
cv.setMouseCallback('Video Recorder', mouse_event_handler)

while True:
    ret, frame = camera.read()
    assert ret, 'Cannot capture frame'

    clean_frame = frame.copy()

    if filter_mode == 1:
        clean_frame = cv.bitwise_not(clean_frame)
        frame = cv.bitwise_not(frame)
    elif filter_mode == 2:
        clean_frame = cv.flip(clean_frame, 1)
        frame = cv.flip(frame, 1)

    if recording and video_writer:
        video_writer.write(clean_frame)

    record_color = (0, 0, 200) if recording else (0, 0, 255)
    filter_color = (0, 255, 0) if filter_mode == 1 else (255, 0, 0) if filter_mode == 2 else (200, 200, 200)

    cv.circle(frame, recording_button, button_size, record_color, -1)
    cv.circle(frame, filter_button, button_size, filter_color, -1)

    cv.putText(frame, "STOP" if recording else "REC", (60, 85), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3)
    cv.putText(frame, "FILTER", (175, 85), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3)

    cv.imshow('Video Recorder', frame)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
    if key == 32:
        filter_mode = (filter_mode + 1) % 3

camera.release()
cv.destroyAllWindows()