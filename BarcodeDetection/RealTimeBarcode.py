#####################################
# This version works on python 3    #
# Install pillow, zbarlight and cv2 #
#####################################

# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time
import sys
import cv2
import zbarlight
from PIL import Image

# Debug mode
DEBUG = False
if len(sys.argv) > 1:
	DEBUG = sys.argv[-1] == 'DEBUG'

# Configuration options
FULLSCREEN = not DEBUG
if not DEBUG:
    RESOLUTION = (640, 480)
else:
	RESOLUTION = (480, 270)

# Initialise Raspberry Pi camera
camera = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
camera.set(RESOLUTION[0],RESOLUTION[1])
#camera.framerate = 10
#camera.vflip = True
#camera.hflip = True
#camera.color_effects = (128, 128)
# set up stream buffer
rawCapture = cv2.resize(camera, dsize=RESOLUTION)
# allow camera to warm up
time.sleep(0.1)
print("Camera ready")

# Initialise OpenCV window
if FULLSCREEN:
	cv2.namedWindow("#iothack15", cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty("#iothack15", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
else:
	cv2.namedWindow("#iothack15")

print("OpenCV version: %s" % (cv2.__version__))
print("Press q to exit ...")

# scanner = zbarlight.ImageScanner()
# scanner.parse_config('enable')

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # as raw NumPy array
    output = frame.array.copy()

    # raw detection code
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)
    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()

    # create a reader
    codes = zbarlight.scan_codes(['qrcode'], pil)
    print('QR codes: %s' % codes)

    # show the frame
    cv2.imshow("#iothack15", output)

    # clear stream for next frame
    rawCapture.truncate(0)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
    	break

# When everything is done, release the capture
camera.close()
cv2.destroyAllWindows()