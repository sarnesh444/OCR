import cv2
import numpy as np

# Load image
im = cv2.imread('cbv_template_contextdict.jpg')

# Make HSV and extract S, i.e. Saturation
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
s=hsv[:,:,1]
# Save saturation just for debug
cv2.imwrite('saturation.png',s)

# Make greyscale version and inverted, thresholded greyscale version
gr = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_,grinv = cv2.threshold(gr,127,255,cv2.THRESH_BINARY_INV)

# Find row numbers of rows with colour in them
meanSatByRow=np.mean(s,axis=1)
rows = np.where(meanSatByRow>50)

# Replace selected rows with those from the inverted, thresholded image
gr[rows]=grinv[rows]

# Save result
cv2.imwrite('result.png',gr)
