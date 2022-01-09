import cv2
import csv
import numpy as np

## Import two times the first image using OpenCV
img1_all = cv2.imread('1_l_1.jpg')
img1_high = cv2.imread('1_l_1.jpg')

## Import the minutiae using the csv standard
enroll1_all = []
enroll1_high = []
with open('1_l_1_enrollment.txt', newline='') as inputfile:
    for row in csv.reader(inputfile, delimiter=' '):
        enroll1_all.append(row)
        if row[4]=='1':
            enroll1_high.append(row)
## Convert the enrollment lists into numpy arrays
enroll1_all = np.asarray(enroll1_all)
enroll1_high = np.asarray(enroll1_high)

## Draw all minutiae on top of the palms
for minu in enroll1_all:
    cv2.circle(img1_all,(int(minu[0]),int(minu[1])),5,(0,0,255),5)
cv2.imwrite('1_l_1_minutiaeall.jpg', img1_all)

## Draw the minutiae on top of the palm
for minu in enroll1_high:
    cv2.circle(img1_high,(int(minu[0]),int(minu[1])),5,(255,0,255),5)
cv2.imwrite('1_l_1_minutiaehigh.jpg', img1_high)

## Import two times the second image using OpenCV
img2_all = cv2.imread('1_l_2.jpg')
img2_high = cv2.imread('1_l_2.jpg')

## Load the enrollment of another palm
enroll2_all = []
enroll2_high = []
with open('1_l_2_enrollment.txt', newline='') as inputfile:
    for row in csv.reader(inputfile, delimiter=' '):
        enroll2_all.append(row)
        if row[4]=='1':
            enroll2_high.append(row)
## Convert the enrollment lists into numpy arrays
enroll2_all = np.asarray(enroll2_all)
enroll2_high = np.asarray(enroll2_high)

## Draw all minutiae on top of the palms
for minu in enroll2_all:
    cv2.circle(img2_all,(int(minu[0]),int(minu[1])),5,(0,0,255),5)
cv2.imwrite('1_l_5_minutiaeall.jpg', img2_all)

## Draw the minutiae on top of the palm
for minu in enroll2_high:
    cv2.circle(img2_high,(int(minu[0]),int(minu[1])),5,(255,0,255),5)
cv2.imwrite('1_l_2_minutiaehigh.jpg', img2_high)

## Match the two palmprints
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

tri1 = Delaunay(enroll1_high[:,0:2])
plt.triplot(enroll1_high[:,0], enroll1_high[:,1], tri1.simplices.copy())
plt.plot(enroll1_high[:,0], enroll1_high[:,1], 'o')
plt.show()

tri2 = Delaunay(enroll2_high[:,0:2])
plt.triplot(enroll2_high[:,0], enroll2_high[:,1], tri2.simplices.copy())
plt.plot(enroll2_high[:,0], enroll2_high[:,1], 'o')
plt.show()