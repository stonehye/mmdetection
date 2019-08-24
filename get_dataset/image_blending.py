import numpy as np
import cv2
import os
from get_dataset.alpha_blending import alpha

from PIL import Image


def imgBlending(imgfile1, imgfile2, idx):
	path = "result_TEST.png"
	mul = 120

	layer1 = Image.open(imgfile1)
	layer2 = Image.open(imgfile2)

	layer1 = layer1.convert("RGBA")
	layer2 = layer2.convert("RGBA")

	# final1 = Image.new("RGBA", layer1.size)
	# final1.paste(layer1, layer1)
	# final1.paste(layer2, layer2)
	#
	# final2 = Image.new("RGBA", layer1.size)
	# final2 = Image.alpha_composite(final2, layer1)
	# final2 = Image.alpha_composite(final2, layer2)

	layer2.paste(layer1,(-500+idx*mul, 0),layer1)
	layer2.save(path)

if __name__ == "__main__":
	path = '../mask_results/PNG/background/017_ms/'
	imgs = os.listdir(path)

	imgs_sorted = []
	for i in imgs:
		if '.png' in i:
			i= i.split('_')[-1]
			i = i.split('.')[0]
			imgs_sorted.append(i)
	imgs_sorted.sort(key=int)
	for id, x in enumerate(imgs_sorted):
		imgs_sorted[id] = "result_" + imgs_sorted[id] + ".png"

	fore = "../mask_results/PNG/background/PNG/background/017_ms_result/"
	a = "../mask_results/PNG/background/017/"
	original_path = '../dataset/frames/017/'

	imgBlending(fore + imgs_sorted[59], 'background.png', 0)
	for idx, i in enumerate(range(60, 85, 3)):
		imgBlending(fore + imgs_sorted[i], 'result_TEST.png', idx+1)

	# -여러이미지 겹치기-
	frame_num = 119-80+1
	# 1: 첫 두 이미지 합성
	# alpha(fore=fore + imgs_sorted[80], back=fore + "result_81.png", al='', num = 0, framenum=frame_num)
	# 2: 나머지 합성
	# for idx, i in enumerate(range(82, 119)):
	# 	alpha(fore = fore + imgs_sorted[i], back = 'result2__'+str(idx)+'.png', al = '', num = idx+1, framenum=frame_num)

	# ms_rcnn 알파 이미지 + 원본이미지 합성
	# print(imgs_sorted)
	# for idx, i in enumerate(imgs_sorted):
	# 	print(original_path+"%05d"%(idx)+".png")
	# 	alpha(fore=original_path+"%05d"%(idx)+".png", back='', al=path+i, num=idx)

