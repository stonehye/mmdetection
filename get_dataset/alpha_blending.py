import cv2
import os

def alpha (fore, back, al, num, framenum = None):
	# # Read the images
	# foreground = cv2.imread(fore)
	# background = cv2.imread(back)
	# #alpha = cv2.imread(al)
	#
	# # Convert uint8 to float
	# foreground = foreground.astype(float)
	# background = background.astype(float)
	#
	# # Normalize the alpha mask to keep intensity between 0 and 1
	# #alpha = alpha.astype(float) / 255
	#
	# # Multiply the foreground with the alpha matte
	# #foreground = cv2.multiply(alpha, foreground)
	#
	# # Multiply the background with ( 1 - alpha )
	# #background = cv2.multiply(1.0 - alpha+0.5, background)
	#
	# # Add the masked foreground and background.
	# #outImage = cv2.add(foreground, background)
	# imgAddWeighted = cv2.addWeighted(foreground, 1/25, background, 1, 0)
	#
	# # cv2.imwrite('./ll2l22/'+ al.split('/')[-1],imgAddWeighted)
	# cv2.imwrite('result2__'+str(num)+'.png', imgAddWeighted)

	# -여러이미지 겹치기-
	# foreground = cv2.imread(fore)
	# background = cv2.imread(back)
	# foreground = foreground.astype(float)
	# background = background.astype(float)
	# imgAddWeighted = cv2.addWeighted(foreground, 1/(framenum-3), background, 1, 0) # 계속 바꿔주기
	# cv2.imwrite('result2__'+str(num)+'.png', imgAddWeighted)

	# ms_rcnn 알파 이미지 + 원본이미지 합성
	foreground = cv2.imread(fore)
	alpha = cv2.imread(al)
	foreground = foreground.astype(float)
	alpha = alpha.astype(float) / 255
	foreground = cv2.multiply(alpha, foreground)
	cv2.imwrite("result_"+str(num)+'.png', foreground)