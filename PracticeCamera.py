# import numpy as np
# import cv2
# video_capture0=cv2.VideoCapture(0)
# video_capture1=cv2.VideoCapture(1)

# while True:

#     ret0, frame0=video_capture0.read()
#     ret1, frame1=video_capture1.read()

#     if(ret0):
#         cv2.imshow('Cam0',frame0)

#     if(ret1):
#         cv2.imshow('cam1', frame1)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# video_capture0.release()
# video_capture1.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np

all_camera_idx_available = []

for camera_idx in range(10):
    cap = cv2.VideoCapture(camera_idx)
    if cap.isOpened():
        print(f'Camera index available: {camera_idx}')
        all_camera_idx_available.append(camera_idx)
        cap.release()