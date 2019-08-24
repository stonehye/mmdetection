import cv2
import os


def Video2Frame(invideofilename, save_path):
	vidcap = cv2.VideoCapture(invideofilename)
	count = 0
	while True:
		success, image = vidcap.read()
		if not success:
			break
		print('Read a new frame: ', success)
		fname = "{}.png".format("{0:05d}".format(count))
		cv2.imwrite(save_path + fname, image)
		count += 1
	print("{} images are extracted in {}.".format(count, save_path))


# Test Code
# if __name__ == "__main__":
# 	path = '../dataset'
# 	for i in range (17,18):
# 		video_path = os.path.join(path, 'video', "%03d" %(i)) + '.mp4'
# 		print(video_path)
# 		dst_path = os.path.join(path, 'frames', "%03d/" %(i))
# 		os.makedirs(dst_path)
# 		print(dst_path)
# 		Video2Frame(video_path, dst_path)