import cv2
import os
import numpy as np
file_name = "grab.png"

path = '../mask_results/PNG/background/'
for i in range(17, 18):
	video = i
	#
	# dst_path =  os.path.join(path, "%03d/" % (video))
	# imgs = os.listdir(dst_path)
	# imgs.sort()
	# imgs_path = []
	# for i, names in enumerate(imgs):
	# 	if '.jpg' in names:
	# 		imgs_path.append(dst_path + imgs[i])
	#
	# os.makedirs(path + "grabCut/" + "%03d/" % (video))
	# for j in imgs_path:
	# 	img = cv2.imread(j, 1)
	# 	mask = np.zeros(img.shape[:2], np.uint8)
	# 	bgdModel = np.zeros((1, 65), np.float64)
	# 	fgdModel = np.zeros((1, 65), np.float64)
	# 	rect = (50, 50, 450, 290)
	# 	cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
	# 	save_path = path + "grabCut/" + "%03d/" % (video) + j.split('/')[-1]
	# 	cv2.imwrite(save_path, img)

	# 1. conver to .png
	# from PIL import Image
	# dst_path = os.path.join(path, "%03d/" % (video))
	# imgs = os.listdir(dst_path)
	# imgs.sort()
	# imgs_path = []
	#
	# for i, names in enumerate(imgs):
	# 	if '.jpg' in names:
	# 		imgs_path.append(dst_path + imgs[i])
	# os.makedirs(path + "PNG/"+ "%03d/" % (video))
	# for j in imgs_path:
	# 	save_path = path + "PNG/"+ "%03d/" % (video) + j.split('/')[-1]
	# 	save_path = save_path.split('.jpg')[0]+'.png'
	# 	pic = Image.open(j)
	# 	pic.save(save_path)

	# 2. remove background
	dst_path = path +"%03d_ms/" % (video)
	imgs = os.listdir(dst_path)
	imgs.sort()
	imgs_path = []
	for i, names in enumerate(imgs):
		if '.png' in names:
			imgs_path.append(dst_path + imgs[i])

	result_path = path + "PNG/background/" + "%03d_ms_result/" % (video)
	os.makedirs(result_path)
	for j in imgs_path:
		img = cv2.imread(j, 1)

		tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
		b, g, r = cv2.split(img)
		rgba = [b,g,r, alpha]
		dst = cv2.merge(rgba,4)

		save_path = result_path + j.split('/')[-1]
		cv2.imwrite(save_path, dst)

	# img = cv2.imread("ms_rcnn.png", 1)
	#
	# tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
	# b, g, r = cv2.split(img)
	# rgba = [b, g, r, alpha]
	# dst = cv2.merge(rgba, 4)
	#
	# cv2.imwrite("ms_rcnn_bg.png", dst)