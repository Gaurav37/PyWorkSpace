from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import argparse


def decode(im) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', str(obj.data),'\n')
    # print("objects",decodedObjects)

  return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points;

    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

  # Display results
  cv2.imshow("Results", im);
  cv2.waitKey(0);


#Main
if __name__ == '__main__':

  # Read image
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--image", required = True, help = "path to the image file")
  ap.add_argument("--show", help = "option to show inner images", type=int)

  args = vars(ap.parse_args())
  show = args["show"]

  # load the image and convert it to grayscale
  im = cv2.imread(args["image"])
  # im = cv2.imread('.jpeg')
  print("I am here")

  decodedObjects = decode(im)
  display(im, decodedObjects)