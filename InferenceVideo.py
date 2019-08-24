import os
import time

from mmdet.apis import init_detector, inference_detector, show_result
from get_dataset.FrameExtraction import Video2Frame


config_file = 'configs/htc/htc_x101_64x4d_fpn_20e_16gpu.py'
checkpoint_file = 'checkpoint/htc_x101_64x4d_fpn_20e_20190408-497f2561.pth'

videoPath = './dataset/1.mp4'
framePath = './frames/1/'
resultPath = './inference_results/1/'
maskPath = './mask/1/'

# # build the model from a config file and a checkpoint file
# model = init_detector(config_file, checkpoint_file, device='cuda:0')
#
# path = './dataset/frames/'
# for i in range(17,18):
# 	video = i
# 	src_path = os.path.join(path, "%03d/" %(video))
# 	imgs = os.listdir(src_path)
# 	imgs.sort()
# 	imgs_path = []
# 	for i, names in enumerate(imgs):
# 		if '.png' in names:
# 			imgs_path.append(src_path+imgs[i])
# 	for i, result in enumerate(inference_detector(model, imgs_path)):
# 	    show_result(imgs_path[i], result, model.CLASSES, out_file='./results/'+"%03d/htc_x101/" %(video)+'result_{}.png'.format(i))


if __name__=='__main__':
	# TODO: Create path list and modify folder creation code
	if not (os.path.isdir(framePath)):
		os.makedirs(os.path.join(framePath))
	if not (os.path.isdir(resultPath)):
		os.makedirs(os.path.join(resultPath))
	if not (os.path.isdir(maskPath)):
		os.makedirs(os.path.join(maskPath))

	Video2Frame(videoPath, framePath)

	imgList = os.listdir(framePath)
	imgList.sort()
	imgPathList = []
	for idx, name in enumerate(imgList):
		if '.png' in name:
			imgPathList.append(framePath+imgList[idx])

	start = time.time()
	# build the model from a config file and a checkpoint file
	model = init_detector(config_file, checkpoint_file, device='cuda:0')
	for idx, result in enumerate(inference_detector(model, imgPathList)):
		filename = os.path.join(resultPath, 'result_{}.png'.format(idx))
		maskname = os.path.join(maskPath, 'result_{}.png'.format(idx))
		show_result(imgPathList[idx], result, model.CLASSES, out_file=filename, out_file_mask=maskname)
	print("Total inference time (for %d frames): %f sec" %(len(imgList), time.time()-start))