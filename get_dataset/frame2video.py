import cv2
import numpy as np
import os

from os.path import isfile, join


def convert_frames_to_video(pathIn, pathOut, fps):
	frame_array = []
	files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

	imgs_sorted = []
	for i in files:
		i= i.split('_')[-1]
		i = i.split('.')[0]
		imgs_sorted.append(i)
	imgs_sorted.sort(key=int)
	for id, x in enumerate(imgs_sorted):
		imgs_sorted[id] = "result2__" + imgs_sorted[id] + ".png"
	files = imgs_sorted

	# for sorting the file names properly
	# files.sort(key=lambda x: int(x[5:-4]))

	for i in range(len(files)):
		filename = pathIn + files[i]
		# reading each files
		img = cv2.imread(filename)
		height, width, layers = img.shape
		size = (width, height)
		print(filename)
		# inserting the frames into an image array
		frame_array.append(img)

	out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

	for i in range(len(frame_array)):
		# writing to a image array
		out.write(frame_array[i])
	out.release()


def main():
	pathIn = './119-80+1/'
	pathOut = 'video119-80+1.avi'
	fps = 7.0
	convert_frames_to_video(pathIn, pathOut, fps)


if __name__ == "__main__":
	main()