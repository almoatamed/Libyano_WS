from __future__ import print_function 
import jetson.inference
import jetson.utils

import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Classify a live camera stream using an image recognition DNN.")

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument('--headless', action='store_true', default=(), help="run without display")

# is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]
argv = ['', '--input-width=640', '--input-height=480', '/dev/video0', 'rtp://192.168.131.51:1234', '--headless']

try:
	opt = parser.parse_known_args(args =argv[1:])
	print(opt)
	opt = opt[0]
	print(opt)
	print(sys.argv)
except:
	print("")
	parser.print_help()
	sys.exit(0)

output_frames = True

input_vid = jetson.utils.videoSource(opt.input_URI, argv=argv)
output_vid = None
if output_frames:
	output_vid = jetson.utils.videoOutput(opt.output_URI, argv=argv)
print('##################################finished loading models##########################')
 
def interrupt():
	print('interrupted')

valid_detect_count = 0
interrupt_detect_count = 5
while True:
	# print('|',end='')
	img = input_vid.Capture()
	if output_vid:
		output_vid.Render(img)
